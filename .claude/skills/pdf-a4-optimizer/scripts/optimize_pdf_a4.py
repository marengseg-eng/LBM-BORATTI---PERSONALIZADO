#!/usr/bin/env python3
"""
Normalize and optimize PDF pages onto ISO A4 sheets.

Primary goals:
- create true A4 pages, portrait/landscape/auto
- prevent page-content overlap during normalization by placing each original page
  onto a fresh blank A4 canvas
- preserve vector/text content by default
- offer a raster/flatten mode for problematic PDFs with broken layers, fonts,
  annotations, or visual rendering defects
- optionally render PNG previews and write a JSON report for verification
"""

from __future__ import annotations

import argparse
import json
import math
import sys
from pathlib import Path
from typing import Dict, List, Tuple

try:
    import fitz  # PyMuPDF
except ImportError as exc:  # pragma: no cover
    raise SystemExit("PyMuPDF is required: pip install pymupdf") from exc

A4_PORTRAIT = (595.275590551, 841.88976378)  # points, ISO 216 A4 at 72 pt/in
A4_LANDSCAPE = (A4_PORTRAIT[1], A4_PORTRAIT[0])


def mm_to_pt(mm: float) -> float:
    return mm * 72.0 / 25.4


def page_orientation(width: float, height: float) -> str:
    return "landscape" if width > height else "portrait"


def output_size_for_page(src_w: float, src_h: float, orientation: str) -> Tuple[float, float, str]:
    if orientation == "auto":
        resolved = page_orientation(src_w, src_h)
    else:
        resolved = orientation
    return (*A4_LANDSCAPE, resolved) if resolved == "landscape" else (*A4_PORTRAIT, resolved)


def rect_with_margin(width: float, height: float, margin_pt: float) -> fitz.Rect:
    margin = max(0.0, margin_pt)
    if margin * 2 >= width or margin * 2 >= height:
        raise ValueError("margin is larger than the available A4 page area")
    return fitz.Rect(margin, margin, width - margin, height - margin)


def placement_rect(src_rect: fitz.Rect, inner: fitz.Rect, mode: str) -> Tuple[fitz.Rect, float, Dict[str, float]]:
    src_w, src_h = src_rect.width, src_rect.height
    inner_w, inner_h = inner.width, inner.height
    if src_w <= 0 or src_h <= 0:
        raise ValueError("source page has invalid dimensions")

    if mode == "stretch":
        return inner, math.nan, {
            "scale_x": inner_w / src_w,
            "scale_y": inner_h / src_h,
            "distorted": True,
        }

    scale = min(inner_w / src_w, inner_h / src_h) if mode == "contain" else max(inner_w / src_w, inner_h / src_h)
    draw_w, draw_h = src_w * scale, src_h * scale
    x0 = inner.x0 + (inner_w - draw_w) / 2.0
    y0 = inner.y0 + (inner_h - draw_h) / 2.0
    rect = fitz.Rect(x0, y0, x0 + draw_w, y0 + draw_h)
    metrics = {
        "scale": scale,
        "unused_x_pt": max(0.0, inner_w - draw_w),
        "unused_y_pt": max(0.0, inner_h - draw_h),
        "cropped_by_mode": mode == "cover",
    }
    return rect, scale, metrics


def render_page_to_jpeg(page: fitz.Page, dpi: int, quality: int) -> bytes:
    try:
        from PIL import Image
    except ImportError as exc:  # pragma: no cover
        raise SystemExit("Pillow is required for --flatten: pip install pillow") from exc

    matrix = fitz.Matrix(dpi / 72.0, dpi / 72.0)
    pix = page.get_pixmap(matrix=matrix, alpha=False, colorspace=fitz.csRGB)
    mode = "RGB"
    img = Image.frombytes(mode, [pix.width, pix.height], pix.samples)
    from io import BytesIO

    buffer = BytesIO()
    img.save(buffer, format="JPEG", quality=quality, optimize=True, progressive=True)
    return buffer.getvalue()


def save_check_renders(doc: fitz.Document, check_dir: Path, dpi: int = 120, max_pages: int = 12) -> List[str]:
    check_dir.mkdir(parents=True, exist_ok=True)
    outputs: List[str] = []
    for idx, page in enumerate(doc):
        if idx >= max_pages:
            break
        pix = page.get_pixmap(matrix=fitz.Matrix(dpi / 72.0, dpi / 72.0), alpha=False, colorspace=fitz.csRGB)
        out_path = check_dir / f"page_{idx + 1:03d}.png"
        pix.save(str(out_path))
        outputs.append(str(out_path))
    return outputs


def optimize_pdf(
    input_pdf: Path,
    output_pdf: Path,
    *,
    mode: str,
    orientation: str,
    margin_mm: float,
    flatten: bool,
    raster_dpi: int,
    jpeg_quality: int,
    check_dir: Path | None,
    report_path: Path | None,
) -> Dict[str, object]:
    if not input_pdf.exists():
        raise FileNotFoundError(f"input PDF not found: {input_pdf}")

    source = fitz.open(str(input_pdf))
    if source.page_count == 0:
        raise ValueError("input PDF has no pages")

    out = fitz.open()
    margin_pt = mm_to_pt(margin_mm)
    report_pages: List[Dict[str, object]] = []
    warnings: List[str] = []

    for index in range(source.page_count):
        page = source[index]
        src_rect = page.rect
        out_w, out_h, resolved_orientation = output_size_for_page(src_rect.width, src_rect.height, orientation)
        inner = rect_with_margin(out_w, out_h, margin_pt)
        target, scale, metrics = placement_rect(src_rect, inner, mode)

        new_page = out.new_page(width=out_w, height=out_h)
        if flatten:
            image_bytes = render_page_to_jpeg(page, raster_dpi, jpeg_quality)
            new_page.insert_image(target, stream=image_bytes, keep_proportion=False)
        else:
            # Place the source page onto a blank A4 page. This prevents accidental
            # cross-page accumulation/overlap and keeps vector/text content intact.
            new_page.show_pdf_page(target, source, index, clip=src_rect)

        if mode == "cover":
            warnings.append(f"page {index + 1}: cover mode may crop content outside the A4 sheet")
        if mode == "stretch":
            warnings.append(f"page {index + 1}: stretch mode fills all A4 space but distorts proportions")
        if mode == "contain" and (metrics.get("unused_x_pt", 0) > 1 or metrics.get("unused_y_pt", 0) > 1):
            warnings.append(
                f"page {index + 1}: aspect ratio differs from A4; contain mode preserves content with small blank bands"
            )

        report_pages.append(
            {
                "page": index + 1,
                "source_size_pt": [round(src_rect.width, 3), round(src_rect.height, 3)],
                "source_orientation": page_orientation(src_rect.width, src_rect.height),
                "output_size_pt": [round(out_w, 3), round(out_h, 3)],
                "output_orientation": resolved_orientation,
                "target_rect_pt": [round(target.x0, 3), round(target.y0, 3), round(target.x1, 3), round(target.y1, 3)],
                "mode": mode,
                "flattened": flatten,
                "margin_mm": margin_mm,
                "metrics": {k: (round(v, 6) if isinstance(v, float) and not math.isnan(v) else v) for k, v in metrics.items()},
            }
        )

    output_pdf.parent.mkdir(parents=True, exist_ok=True)
    # Deflate and garbage collection optimize structure without changing visible layout.
    out.save(str(output_pdf), garbage=4, deflate=True, clean=True)

    check_renders: List[str] = []
    if check_dir is not None:
        # Re-open the saved file to verify what was actually written.
        saved = fitz.open(str(output_pdf))
        check_renders = save_check_renders(saved, check_dir)
        saved.close()

    result: Dict[str, object] = {
        "input_pdf": str(input_pdf),
        "output_pdf": str(output_pdf),
        "page_count": source.page_count,
        "mode": mode,
        "orientation": orientation,
        "flattened": flatten,
        "a4_portrait_pt": [round(A4_PORTRAIT[0], 3), round(A4_PORTRAIT[1], 3)],
        "pages": report_pages,
        "warnings": warnings,
        "check_renders": check_renders,
    }

    if report_path is not None:
        report_path.parent.mkdir(parents=True, exist_ok=True)
        report_path.write_text(json.dumps(result, ensure_ascii=False, indent=2), encoding="utf-8")

    source.close()
    out.close()
    return result


def parse_args(argv: List[str]) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Normalize a PDF to professional A4 output.")
    parser.add_argument("input_pdf", type=Path, help="source PDF")
    parser.add_argument("output_pdf", type=Path, help="optimized A4 PDF")
    parser.add_argument(
        "--mode",
        choices=["contain", "stretch", "cover"],
        default="contain",
        help="contain preserves all content; stretch fills A4 but distorts; cover fills A4 but may crop",
    )
    parser.add_argument(
        "--orientation",
        choices=["auto", "portrait", "landscape"],
        default="auto",
        help="A4 orientation for output pages",
    )
    parser.add_argument("--margin-mm", type=float, default=0.0, help="safe margin inside A4 sheet; default 0 for maximum occupation")
    parser.add_argument("--flatten", action="store_true", help="rasterize each page before placing it on A4")
    parser.add_argument("--raster-dpi", type=int, default=220, help="DPI used by --flatten")
    parser.add_argument("--jpeg-quality", type=int, default=92, help="JPEG quality used by --flatten, 1-100")
    parser.add_argument("--check-dir", type=Path, default=None, help="directory for PNG verification renders")
    parser.add_argument("--report", type=Path, default=None, help="write JSON layout report")
    return parser.parse_args(argv)


def main(argv: List[str] | None = None) -> int:
    args = parse_args(sys.argv[1:] if argv is None else argv)
    if args.jpeg_quality < 1 or args.jpeg_quality > 100:
        raise SystemExit("--jpeg-quality must be between 1 and 100")
    if args.raster_dpi < 72 or args.raster_dpi > 600:
        raise SystemExit("--raster-dpi must be between 72 and 600")

    result = optimize_pdf(
        args.input_pdf,
        args.output_pdf,
        mode=args.mode,
        orientation=args.orientation,
        margin_mm=args.margin_mm,
        flatten=args.flatten,
        raster_dpi=args.raster_dpi,
        jpeg_quality=args.jpeg_quality,
        check_dir=args.check_dir,
        report_path=args.report,
    )
    print(json.dumps({"output_pdf": result["output_pdf"], "page_count": result["page_count"], "warnings": result["warnings"]}, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
