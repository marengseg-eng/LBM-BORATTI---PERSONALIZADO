#!/usr/bin/env python3
"""
Calcula os derivados do Parecer Tecnico NR-01/NR-17 a partir dos escores dos fatores.

Uso:
    python3 calcular.py dados.json
    python3 calcular.py --exemplo

Entrada (JSON):
{
  "data_avaliacao": "15/06/2026",
  "fatores": [
    {"nome": "Condicoes Ergonomicas", "escore": 24.4},
    {"nome": "Jornada", "escore": 23.7},
    ...
  ],
  "aep": {"total": 61, "baixa": 61, "media_ou_pior": 0},
  "aet": "concluida"
}

Saida: ranking ordenado, indice global, base visual, geometria do donut, veredicto
e as inconsistencias encontradas.
"""
import json
import sys
from datetime import datetime, timedelta

CORES = ["#2aa8e8", "#3b5bdb", "#7b3fe4", "#ec2f72", "#f4511e", "#f5a623",
         "#12a37a", "#0fc2d6", "#2dd4a7", "#8b5cf6", "#f4306d", "#3b82f6"]

# O texto do badge vai impresso no documento — precisa da acentuacao correta.
FAIXAS = [
    (0,  24,  "Conforme", "CONFORME", "#1e7a4a", "#f0fbf4", "#7fce9f"),
    (25, 44,  "Atenção",  "ATENÇÃO",  "#8a6100", "#fff8e6", "#e8c766"),
    (45, 59,  "Moderado", "MODERADO", "#a55200", "#fff2e4", "#efab6d"),
    (60, 74,  "Elevado",  "ELEVADO",  "#a52626", "#fdeeee", "#e79a9a"),
    (75, 100, "Crítico",  "CRÍTICO",  "#7d1d1d", "#fbe4e4", "#d97070"),
]

RAIO = 54.0
CIRC = 2 * 3.141592653589793 * RAIO
GAP = 1.2  # separacao visual entre fatias, em unidades de arco


def classificar(escore):
    exibido = round(escore)
    for lo, hi, nome, badge, cor, fundo, borda in FAIXAS:
        if lo <= exibido <= hi:
            return {"classificacao": nome, "badge": badge,
                    "cor_badge": cor, "fundo": fundo, "borda": borda}
    raise ValueError(f"escore fora de 0-100: {escore}")


def reavaliacao(data_avaliacao):
    d = datetime.strptime(data_avaliacao, "%d/%m/%Y").date()
    try:
        return (d.replace(year=d.year + 1) - timedelta(days=1)).strftime("%d/%m/%Y")
    except ValueError:            # 29/02 -> ano seguinte nao bissexto
        return d.replace(year=d.year + 1, day=28).strftime("%d/%m/%Y")


def veredicto(ranking, aep, aet):
    """Aplica as regras na ordem do SKILL.md e devolve TODOS os motivos aplicaveis."""
    aet = (aet or "").lower().replace("_", " ")
    graves = [f for f in ranking if f["classificacao"] in ("Elevado", "Crítico")]
    fora = [f for f in ranking
            if f["classificacao"] in ("Atenção", "Moderado")]
    aep_pior = aep.get("media_ou_pior", 0) or 0

    def lista(fs):
        return ", ".join(f"{f['nome']} ({f['escore_exibido']}%)" for f in fs)

    desfavoravel, ressalvas = [], []

    if graves:
        desfavoravel.append("fator(es) em faixa Elevado/Critico: " + lista(graves))
    if aet in ("nao iniciada", "pendente"):
        desfavoravel.append("AET exigida e nao iniciada")

    if fora:
        ressalvas.append("fator(es) fora da faixa Conforme: " + lista(fora))
    if aep_pior > 0:
        ressalvas.append(f"{aep_pior} item(ns) da AEP acima de baixa gravidade")
    if aet == "em elaboracao":
        ressalvas.append("AET ainda em elaboracao")

    if desfavoravel:
        return "DESFAVORAVEL", "#c0392b", "; ".join(desfavoravel + ressalvas)
    if ressalvas:
        return "FAVORAVEL COM RESSALVAS", "#e67e22", "; ".join(ressalvas)
    return "FAVORAVEL", "#12a37a", "todos os fatores conformes e ciclo completo"


def calcular(dados):
    fatores = dados["fatores"]
    n = len(fatores)
    alertas = []

    if n != 12:
        alertas.append(f"ATENCAO: {n} fatores informados (o modelo padrao usa 12). "
                       "Ajustar o cabecalho e o card de conformes.")

    soma = sum(round(f["escore"]) for f in fatores)   # soma dos valores EXIBIDOS
    indice = round(soma / n)
    soma_bruta = sum(f["escore"] for f in fatores)          # usada so na geometria do donut

    ranking = sorted(fatores, key=lambda f: -f["escore"])
    offset = 0.0
    for i, f in enumerate(ranking):
        f["pos"] = i + 1
        f["rotulo_pos"] = f"#{i + 1:02d}"
        f["cor"] = CORES[i % len(CORES)]
        f["escore_exibido"] = round(f["escore"])
        f.update(classificar(f["escore"]))
        arco = f["escore"] / soma_bruta * CIRC
        f["dash"] = f"{max(arco - GAP, 0.5):.2f} {CIRC - max(arco - GAP, 0.5):.2f}"
        f["dashoffset"] = f"{-offset:.2f}"
        f["angulo"] = round(f["escore"] / soma_bruta * 360, 1)
        offset += arco

    empatados = {}
    for f in ranking:
        empatados.setdefault(f["escore_exibido"], []).append(f["nome"])
    for valor, nomes in empatados.items():
        if len(nomes) > 1 and len({fa["escore"] for fa in ranking
                                   if round(fa["escore"]) == valor}) == 1:
            alertas.append(
                f"Empate real em {valor}% entre {', '.join(nomes)} — o laudo nao permite "
                "desempatar. Confirmar a ordem com o responsavel tecnico.")

    aep = dados.get("aep", {})
    if aep:
        if aep.get("baixa", 0) + aep.get("media_ou_pior", 0) != aep.get("total", 0):
            alertas.append(
                f"INCONSISTENCIA na AEP: {aep.get('baixa')} + {aep.get('media_ou_pior')} "
                f"!= {aep.get('total')}. Nao gerar o documento ate corrigir.")

    conformes = sum(1 for f in ranking if f["classificacao"] == "Conforme")
    par, cor_par, motivo = veredicto(ranking, aep, dados.get("aet"))

    if "indice_informado" in dados and dados["indice_informado"] != indice:
        alertas.append(
            f"DIVERGENCIA: indice informado {dados['indice_informado']}% x calculado {indice}%. "
            "Nao sobrescrever nenhum dos dois — perguntar qual prevalece.")

    return {
        "n_fatores": n,
        "base_visual": soma,
        "indice_global": indice,
        "conformes": f"{conformes}/{n}",
        "ranking": ranking,
        "veredicto": par,
        "cor_veredicto": cor_par,
        "motivo_veredicto": motivo,
        "data_reavaliacao": reavaliacao(dados["data_avaliacao"]) if dados.get("data_avaliacao") else None,
        "alertas": alertas,
    }


EXEMPLO = {
    "data_avaliacao": "15/06/2026",
    "indice_informado": 21,
    "fatores": [
        {"nome": "Condicoes Ergonomicas", "escore": 24.4},
        {"nome": "Jornada", "escore": 23.7},
        {"nome": "Controle", "escore": 22.0},
        {"nome": "Assedio Moral", "escore": 21.0},
        {"nome": "Demanda", "escore": 20.4},
        {"nome": "Apoio Social", "escore": 20.3},
        {"nome": "Assedio Verbal", "escore": 20.2},
        {"nome": "Assedio Fisico / Violencia", "escore": 20.1},
        {"nome": "Papel", "escore": 19.9},
        {"nome": "Relacionamentos", "escore": 19.4},
        {"nome": "Assedio Sexual", "escore": 19.0},
        {"nome": "Mudanca", "escore": 18.0},
    ],
    "aep": {"total": 61, "baixa": 61, "media_ou_pior": 0},
    "aet": "concluida",
}


def main():
    if len(sys.argv) > 1 and sys.argv[1] == "--exemplo":
        dados = EXEMPLO
    elif len(sys.argv) > 1:
        with open(sys.argv[1], encoding="utf-8") as fh:
            dados = json.load(fh)
    else:
        dados = json.load(sys.stdin)

    r = calcular(dados)

    print(f"Base visual .......... {r['base_visual']} pontos de escore")
    print(f"Indice global ........ {r['indice_global']}%")
    print(f"Fatores conformes .... {r['conformes']}")
    print(f"Reavaliacao ate ...... {r['data_reavaliacao']}")
    print(f"Veredicto ............ {r['veredicto']}  ({r['motivo_veredicto']})")
    print()
    print(f"{'Pos':<5}{'Fator':<30}{'%':>5}  {'Classe':<10}{'Angulo':>8}")
    print("-" * 62)
    for f in r["ranking"]:
        print(f"{f['rotulo_pos']:<5}{f['nome']:<30}{f['escore_exibido']:>4}%  "
              f"{f['classificacao']:<10}{f['angulo']:>7}°")
    if r["alertas"]:
        print("\nALERTAS:")
        for a in r["alertas"]:
            print(f"  - {a}")
    else:
        print("\nSem inconsistencias.")


if __name__ == "__main__":
    main()
