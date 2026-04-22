(function () {
  "use strict";

  const STORAGE_KEY = "lbm_skills_v1";

  const DEFAULT_SKILLS = [
    {
      name: "Comunicação",
      synonyms: "comunicacao, oratoria, apresentação, apresentacao, public speaking",
      description:
        "Capacidade de se expressar com clareza e adaptar a mensagem ao público.",
    },
    {
      name: "Liderança",
      synonyms: "lideranca, gestão de pessoas, gestao de pessoas, liderar times",
      description: "Conduzir e motivar pessoas em direção a um objetivo comum.",
    },
    {
      name: "Vendas",
      synonyms: "vendas, prospecção, prospeccao, b2b, closer, negociação, negociacao",
      description: "Prospectar, negociar e fechar negócios.",
    },
    {
      name: "Excel",
      synonyms: "excel, planilhas, google sheets, sheets, vba",
      description: "Modelagem de dados, fórmulas e automações em planilhas.",
    },
    {
      name: "Python",
      synonyms: "python, py, pandas, numpy",
      description: "Programação em Python para automação, dados e scripts.",
    },
    {
      name: "Power BI",
      synonyms: "power bi, powerbi, pbi, dax",
      description: "Construção de dashboards e modelagem no Power BI.",
    },
    {
      name: "SQL",
      synonyms: "sql, mysql, postgres, postgresql, bigquery, query, queries",
      description: "Consulta e manipulação de dados em bancos relacionais.",
    },
    {
      name: "Marketing",
      synonyms: "marketing, mkt, trafego pago, tráfego pago, ads, growth",
      description: "Planejamento e execução de estratégias de marketing.",
    },
  ];

  const SAMPLE_CHAT = [
    "21/04/2026 09:12 - João Silva: Bom dia pessoal! Eu trabalho com Excel avançado e também toco vendas B2B há 5 anos.",
    "21/04/2026 09:14 - Maria Souza: Oi João! Eu sou mais do lado técnico, mexo com Python, SQL e venho estudando Power BI.",
    "21/04/2026 09:15 - Maria Souza: Também já liderei um time pequeno de analistas, então pegaria liderança também.",
    "21/04/2026 09:20 - Carlos: Bom dia! Minhas skills principais são comunicação e marketing digital (tráfego pago).",
    "21/04/2026 09:22 - Ana Paula: Eu meio que atuo em tudo rs, mas minha base mesmo é SQL e apresentação para cliente.",
    "21/04/2026 09:25 - João Silva: <Mídia oculta>",
    "21/04/2026 09:26 - João Silva: Esqueci de falar que também dou aula de Excel no YouTube.",
  ].join("\n");

  // ===== Parser do WhatsApp =====

  // Android: "21/04/2026 09:12 - Nome: mensagem"  (pode ter vírgula antes da hora)
  // iOS:     "[21/04/2026, 09:12:45] Nome: mensagem"
  const RE_ANDROID = /^(\d{1,2}\/\d{1,2}\/\d{2,4}),?\s+(\d{1,2}:\d{2}(?::\d{2})?)\s+[-–—]\s+([^:]+?):\s?(.*)$/;
  const RE_IOS = /^\[(\d{1,2}\/\d{1,2}\/\d{2,4}),?\s+(\d{1,2}:\d{2}(?::\d{2})?)\]\s+([^:]+?):\s?(.*)$/;

  function parseWhatsApp(raw) {
    if (!raw) return [];
    // strip BOM
    const text = raw.replace(/^﻿/, "");
    // normaliza NBSP e espaço fino para espaço normal (WhatsApp iOS usa U+202F)
    const normalized = text.replace(/[   ]/g, " ");
    const lines = normalized.split(/\r?\n/);
    const messages = [];
    let current = null;

    for (const line of lines) {
      const mAndroid = line.match(RE_ANDROID);
      const mIos = line.match(RE_IOS);
      const m = mAndroid || mIos;
      if (m) {
        if (current) messages.push(current);
        current = {
          date: m[1],
          time: m[2],
          sender: m[3].trim(),
          message: m[4],
        };
      } else if (current) {
        // continuação da mensagem anterior (multilinha)
        current.message += "\n" + line;
      }
      // linhas antes da primeira mensagem são ignoradas (cabeçalho do export)
    }
    if (current) messages.push(current);
    return messages;
  }

  // ===== Matcher =====

  function normalize(s) {
    return (s || "")
      .normalize("NFD")
      .replace(/[̀-ͯ]/g, "")
      .toLowerCase();
  }

  function escapeRegex(s) {
    return s.replace(/[.*+?^${}()|[\]\\]/g, "\\$&");
  }

  function compileSkill(skill) {
    const terms = [skill.name, ...(skill.synonyms || "").split(",")]
      .map((t) => normalize(t).trim())
      .filter(Boolean);
    const unique = [...new Set(terms)];
    if (!unique.length) return null;
    // word boundaries permissivas: início/fim de string, ou caractere não alfanumérico
    const pattern = unique.map(escapeRegex).join("|");
    return new RegExp("(^|[^a-z0-9])(" + pattern + ")(?=[^a-z0-9]|$)", "i");
  }

  function classify(messages, skills) {
    const compiled = skills
      .map((s) => ({ skill: s, re: compileSkill(s) }))
      .filter((x) => x.re);
    return messages.map((msg) => {
      const text = normalize(msg.message);
      const matches = [];
      const seen = new Set();
      for (const { skill, re } of compiled) {
        if (re.test(text) && !seen.has(skill.name)) {
          seen.add(skill.name);
          matches.push({ name: skill.name, description: skill.description });
        }
      }
      return Object.assign({}, msg, { matches });
    });
  }

  // ===== Persistência =====

  function loadSkills() {
    try {
      const raw = localStorage.getItem(STORAGE_KEY);
      if (!raw) return clone(DEFAULT_SKILLS);
      const parsed = JSON.parse(raw);
      if (!Array.isArray(parsed)) return clone(DEFAULT_SKILLS);
      return parsed
        .map((s) => ({
          name: String(s.name || "").trim(),
          synonyms: String(s.synonyms || "").trim(),
          description: String(s.description || "").trim(),
        }))
        .filter((s) => s.name);
    } catch (_) {
      return clone(DEFAULT_SKILLS);
    }
  }

  function saveSkills(skills) {
    localStorage.setItem(STORAGE_KEY, JSON.stringify(skills));
  }

  function clone(v) {
    return JSON.parse(JSON.stringify(v));
  }

  // ===== State =====

  let skills = loadSkills();
  let lastResults = [];

  // ===== Render: editor de skills =====

  const editor = document.getElementById("skills-editor");
  const skillsStatus = document.getElementById("skills-status");

  function renderSkillsEditor() {
    editor.innerHTML = "";
    skills.forEach((skill, index) => {
      const item = document.createElement("div");
      item.className = "skill-item";

      const name = document.createElement("input");
      name.type = "text";
      name.placeholder = "Nome da skill";
      name.value = skill.name;
      name.addEventListener("input", () => (skills[index].name = name.value));

      const syn = document.createElement("input");
      syn.type = "text";
      syn.placeholder = "sinônimos, separados, por vírgula";
      syn.value = skill.synonyms;
      syn.addEventListener("input", () => (skills[index].synonyms = syn.value));

      const desc = document.createElement("textarea");
      desc.rows = 2;
      desc.placeholder = "Descrição do que é essa skill";
      desc.value = skill.description;
      desc.addEventListener(
        "input",
        () => (skills[index].description = desc.value)
      );

      const remove = document.createElement("button");
      remove.type = "button";
      remove.className = "skill-remove";
      remove.textContent = "Remover";
      remove.addEventListener("click", () => {
        skills.splice(index, 1);
        renderSkillsEditor();
      });

      item.appendChild(name);
      item.appendChild(syn);
      item.appendChild(desc);
      item.appendChild(remove);
      editor.appendChild(item);
    });
    if (!skills.length) {
      const empty = document.createElement("p");
      empty.className = "empty";
      empty.textContent = "Nenhuma skill cadastrada. Clique em + Adicionar skill.";
      editor.appendChild(empty);
    }
  }

  function flashStatus(msg) {
    skillsStatus.textContent = msg;
    setTimeout(() => {
      if (skillsStatus.textContent === msg) skillsStatus.textContent = "";
    }, 2500);
  }

  document.getElementById("skill-add").addEventListener("click", () => {
    skills.push({ name: "", synonyms: "", description: "" });
    renderSkillsEditor();
  });

  document.getElementById("skill-save").addEventListener("click", () => {
    const cleaned = skills
      .map((s) => ({
        name: (s.name || "").trim(),
        synonyms: (s.synonyms || "").trim(),
        description: (s.description || "").trim(),
      }))
      .filter((s) => s.name);
    skills = cleaned;
    saveSkills(skills);
    renderSkillsEditor();
    flashStatus("Salvo no navegador (" + skills.length + " skills).");
  });

  document.getElementById("skill-reset").addEventListener("click", () => {
    if (!confirm("Restaurar a lista padrão? Suas skills atuais serão perdidas."))
      return;
    skills = clone(DEFAULT_SKILLS);
    saveSkills(skills);
    renderSkillsEditor();
    flashStatus("Lista padrão restaurada.");
  });

  document.getElementById("skill-export").addEventListener("click", () => {
    downloadBlob(
      JSON.stringify(skills, null, 2),
      "application/json",
      "skills-lbm-boratti.json"
    );
  });

  document.getElementById("skill-import").addEventListener("change", (e) => {
    const file = e.target.files && e.target.files[0];
    if (!file) return;
    const reader = new FileReader();
    reader.onload = () => {
      try {
        const parsed = JSON.parse(reader.result);
        if (!Array.isArray(parsed)) throw new Error("JSON deve ser uma lista");
        skills = parsed
          .map((s) => ({
            name: String(s.name || "").trim(),
            synonyms: String(s.synonyms || "").trim(),
            description: String(s.description || "").trim(),
          }))
          .filter((s) => s.name);
        saveSkills(skills);
        renderSkillsEditor();
        flashStatus("Importado: " + skills.length + " skills.");
      } catch (err) {
        alert("Não consegui ler o JSON: " + err.message);
      }
    };
    reader.readAsText(file);
    e.target.value = "";
  });

  // ===== Entrada do chat =====

  const chatText = document.getElementById("chat-text");
  const chatFile = document.getElementById("chat-file");

  // WhatsApp Web põe "[HH:MM, DD/MM/AAAA] Remetente: " em data-pre-plain-text
  const RE_PRE_PLAIN =
    /^\[(\d{1,2}:\d{2}(?::\d{2})?),\s*(\d{1,2}\/\d{1,2}\/\d{2,4})\]\s*([^:]+):\s*$/;

  const BLOCK_SELECTOR =
    "address,article,aside,blockquote,div,dd,dl,dt,figcaption,figure,footer,form,h1,h2,h3,h4,h5,h6,header,hr,li,main,nav,ol,p,pre,section,table,tr,ul";

  function extractTextPreservingBr(root) {
    const clone = root.cloneNode(true);
    clone.querySelectorAll("script,style").forEach((el) => el.remove());
    clone.querySelectorAll("br").forEach((br) => br.replaceWith("\n"));
    clone.querySelectorAll(BLOCK_SELECTOR).forEach((el) => {
      el.append("\n");
    });
    return clone.textContent.replace(/[ \t]+\n/g, "\n").replace(/\n{3,}/g, "\n\n").trim();
  }

  function convertPastedHtmlToWhatsapp(html) {
    if (!html) return "";
    const doc = new DOMParser().parseFromString(html, "text/html");
    const bubbles = doc.querySelectorAll("[data-pre-plain-text]");
    if (bubbles.length) {
      const lines = [];
      bubbles.forEach((el) => {
        const prefix = el.getAttribute("data-pre-plain-text") || "";
        const m = prefix.match(RE_PRE_PLAIN);
        const body = extractTextPreservingBr(el);
        if (m) {
          lines.push(m[2] + " " + m[1] + " - " + m[3].trim() + ": " + body);
        } else if (body) {
          lines.push(body);
        }
      });
      return lines.join("\n");
    }
    return extractTextPreservingBr(doc.body || doc.documentElement);
  }

  function insertAtCursor(textarea, value) {
    textarea.focus();
    let inserted = false;
    try {
      inserted = document.execCommand("insertText", false, value);
    } catch (_) {
      inserted = false;
    }
    if (inserted) return;
    const start = textarea.selectionStart;
    const end = textarea.selectionEnd;
    if (typeof textarea.setRangeText === "function") {
      textarea.setRangeText(value, start, end, "end");
    } else {
      const v = textarea.value;
      textarea.value = v.slice(0, start) + value + v.slice(end);
      const pos = start + value.length;
      textarea.selectionStart = textarea.selectionEnd = pos;
    }
    textarea.dispatchEvent(new Event("input", { bubbles: true }));
  }

  chatText.addEventListener("paste", (e) => {
    const dt = e.clipboardData;
    if (!dt) return;
    const html = dt.getData("text/html");
    if (!html) return;
    const converted = convertPastedHtmlToWhatsapp(html);
    const plain = dt.getData("text/plain") || "";
    if (!converted || converted === plain.trim()) return;
    e.preventDefault();
    insertAtCursor(chatText, converted);
  });

  chatFile.addEventListener("change", (e) => {
    const file = e.target.files && e.target.files[0];
    if (!file) return;
    const reader = new FileReader();
    reader.onload = () => {
      chatText.value = String(reader.result || "");
    };
    reader.readAsText(file, "utf-8");
    e.target.value = "";
  });

  document.getElementById("chat-sample").addEventListener("click", () => {
    chatText.value = SAMPLE_CHAT;
  });

  document.getElementById("chat-clear").addEventListener("click", () => {
    chatText.value = "";
    lastResults = [];
    renderResults();
  });

  // ===== Análise =====

  const summaryEl = document.getElementById("summary");
  const tbody = document.querySelector("#results-table tbody");
  const emptyEl = document.getElementById("results-empty");
  const showAll = document.getElementById("show-all");
  const exportCsvBtn = document.getElementById("export-csv");
  const exportJsonBtn = document.getElementById("export-json");

  document.getElementById("analyze").addEventListener("click", () => {
    const messages = parseWhatsApp(chatText.value);
    if (!messages.length) {
      alert(
        "Não encontrei mensagens no formato do WhatsApp. Confira se colou o conteúdo certo."
      );
      lastResults = [];
      renderResults();
      return;
    }
    lastResults = classify(messages, skills);
    renderResults();
  });

  showAll.addEventListener("change", renderResults);

  function renderResults() {
    tbody.innerHTML = "";
    const hasAny = lastResults.length > 0;
    const rows = showAll.checked
      ? lastResults
      : lastResults.filter((r) => r.matches.length > 0);

    if (!rows.length) {
      emptyEl.style.display = "block";
      emptyEl.textContent = hasAny
        ? "Nenhuma mensagem casou com as skills do dicionário. Marque a opção acima para ver todas."
        : "Nenhuma análise ainda. Cole um chat e clique em Analisar conversa.";
      exportCsvBtn.disabled = !hasAny;
      exportJsonBtn.disabled = !hasAny;
      summaryEl.innerHTML = hasAny ? buildSummary() : "";
      return;
    }

    emptyEl.style.display = "none";
    exportCsvBtn.disabled = false;
    exportJsonBtn.disabled = false;

    const frag = document.createDocumentFragment();
    for (const row of rows) {
      const tr = document.createElement("tr");
      tr.appendChild(td(row.date + " " + row.time, "col-datetime"));
      tr.appendChild(td(row.sender, "col-sender"));
      tr.appendChild(td(row.message, "col-message"));

      const skillsTd = document.createElement("td");
      skillsTd.className = "col-skills";
      for (const s of row.matches) {
        const badge = document.createElement("span");
        badge.className = "skill-badge";
        badge.textContent = s.name;
        skillsTd.appendChild(badge);
      }
      tr.appendChild(skillsTd);

      tr.appendChild(
        td(row.matches.map((s) => s.description).join(" • "), "col-desc")
      );
      frag.appendChild(tr);
    }
    tbody.appendChild(frag);
    summaryEl.innerHTML = buildSummary();
  }

  function td(text, cls) {
    const el = document.createElement("td");
    if (cls) el.className = cls;
    el.textContent = text;
    return el;
  }

  function buildSummary() {
    const total = lastResults.length;
    const senders = new Set(lastResults.map((r) => r.sender));
    const detected = lastResults.filter((r) => r.matches.length > 0).length;
    const skillCounts = {};
    for (const r of lastResults) {
      for (const s of r.matches) {
        skillCounts[s.name] = (skillCounts[s.name] || 0) + 1;
      }
    }
    const top = Object.entries(skillCounts)
      .sort((a, b) => b[1] - a[1])
      .slice(0, 5)
      .map(([n, c]) => n + " (" + c + ")")
      .join(", ");
    return [
      "<span><strong>" + total + "</strong> mensagens</span>",
      "<span><strong>" + senders.size + "</strong> participantes</span>",
      "<span><strong>" + detected + "</strong> com skill detectada</span>",
      top ? "<span>Top: " + escapeHtml(top) + "</span>" : "",
    ]
      .filter(Boolean)
      .join("");
  }

  function escapeHtml(s) {
    return String(s)
      .replace(/&/g, "&amp;")
      .replace(/</g, "&lt;")
      .replace(/>/g, "&gt;");
  }

  // ===== Export =====

  exportCsvBtn.addEventListener("click", () => {
    const rows = lastResults.filter((r) => showAll.checked || r.matches.length);
    const header = ["data", "hora", "remetente", "mensagem", "skills", "descricoes"];
    const lines = [header.map(csvCell).join(",")];
    for (const r of rows) {
      lines.push(
        [
          r.date,
          r.time,
          r.sender,
          r.message,
          r.matches.map((s) => s.name).join(" | "),
          r.matches.map((s) => s.description).join(" | "),
        ]
          .map(csvCell)
          .join(",")
      );
    }
    // BOM para Excel reconhecer UTF-8
    downloadBlob("﻿" + lines.join("\n"), "text/csv", "skills-classificadas.csv");
  });

  exportJsonBtn.addEventListener("click", () => {
    const rows = lastResults.filter((r) => showAll.checked || r.matches.length);
    downloadBlob(
      JSON.stringify(rows, null, 2),
      "application/json",
      "skills-classificadas.json"
    );
  });

  function csvCell(v) {
    const s = String(v == null ? "" : v);
    if (/[",\n]/.test(s)) {
      return '"' + s.replace(/"/g, '""') + '"';
    }
    return s;
  }

  function downloadBlob(content, mime, filename) {
    const blob = new Blob([content], { type: mime + ";charset=utf-8" });
    const url = URL.createObjectURL(blob);
    const a = document.createElement("a");
    a.href = url;
    a.download = filename;
    document.body.appendChild(a);
    a.click();
    document.body.removeChild(a);
    URL.revokeObjectURL(url);
  }

  // ===== Init =====

  renderSkillsEditor();
  renderResults();
})();
