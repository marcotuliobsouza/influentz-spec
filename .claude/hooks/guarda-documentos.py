#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Guarda de documentos da INFLUENTZ.

Roda sozinho depois de todo Write/Edit em arquivo .md do projeto.
Não pede licença, não depende de eu lembrar da regra: é código.

Verifica três classes de erro que o Marco já teve que encontrar na mão:

1. NÚMERO DIVERGENTE  — um documento afirmando um número travado diferente
   do que está em .claude/numeros-travados.json (foi assim que "98 funções",
   "97" e "91" conviveram nos documentos).
2. PALAVRA PROIBIDA NA INTERFACE — carteira · saldo · crédito · depositar
   (SPEC §4.9.1: saldo pré-pago joga a plataforma dentro do Banco Central).
3. AUTOCRÍTICA DENTRO DE DOCUMENTO DE PRODUTO — CLAUDE.md §2.4: o documento
   descreve o que o produto É; o rastro de decisão vive em docs/HISTORICO.md.

Avisa, não bloqueia: um falso positivo nunca pode travar o trabalho.
"""

import json
import os
import re
import sys

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
CONFIG = os.path.join(RAIZ, ".claude", "numeros-travados.json")

# HISTORICO.md guarda números velhos de propósito — é o rastro, não o produto.
FORA_DE_TUDO = {"HISTORICO.md"}
# Documentos que descrevem o produto. CLAUDE.md e METODO ficam de fora da
# regra de autocrítica: são processo, e lá o registro de correção é legítimo.
DOCS_DE_PRODUTO = {
    "SPEC-INFLUENTZ.md",
    "FEATURE-MATRIX.md",
    "PRODUTO-DETALHADO.md",
    "MAQUINA-DE-ESTADOS.md",
    "DESIGN-SYSTEM.md",
    "PAINEL.md",
}

# Linha que compara com um cenário que NÃO é o escolhido — "a 7,5% seria 25
# contratos" — está explicando a decisão, não afirmando outro número.
CONTRAFACTUAL = re.compile(
    r"\bseria\b|\bseriam\b|mudou de|em vez de|deixou de|no lugar de|\bantes era\b|\bnão é\b",
    re.IGNORECASE,
)

# A regra de palavra proibida é de INTERFACE. Só vale dentro de rótulo entre
# aspas ou em linha que começa marcada como tela/botão/campo.
CITACAO = re.compile(r"\"[^\"]*\"|“[^”]*”|'[^']*'|«[^»]*»")


def normaliza(valor):
    """'R$ 5.000' e '5000' são o mesmo número. Compara sem ponto de milhar."""
    return valor.replace(".", "").replace(" ", "").strip()


def caminho_do_stdin():
    try:
        dados = json.load(sys.stdin)
    except Exception:
        return None
    entrada = dados.get("tool_input") or {}
    resposta = dados.get("tool_response") or {}
    return (
        resposta.get("filePath")
        or entrada.get("file_path")
        or entrada.get("notebook_path")
    )


def linhas_relevantes(texto):
    """Ignora blocos de código e linhas de citação de conversa."""
    dentro_de_codigo = False
    for n, linha in enumerate(texto.splitlines(), 1):
        if linha.lstrip().startswith("```"):
            dentro_de_codigo = not dentro_de_codigo
            continue
        if dentro_de_codigo:
            continue
        yield n, linha


def confere_numeros(cfg, texto, achados):
    for item in cfg.get("numeros", []):
        padrao = re.compile(item["padrao"])
        esperados = {normaliza(v) for v in item["esperado"]}
        for n, linha in linhas_relevantes(texto):
            if CONTRAFACTUAL.search(linha):
                continue  # "a 7,5% o equilíbrio SERIA 25" é explicação, não afirmação
            for achado in padrao.finditer(linha):
                if normaliza(achado.group(1)) in esperados:
                    continue
                achados.append(
                    "linha {}: {} deveria ser {} ({}) — o documento diz {}".format(
                        n,
                        item["rotulo"],
                        " ou ".join(item["esperado"]),
                        item["fonte"],
                        achado.group(1),
                    )
                )


def confere_palavras(cfg, texto, achados):
    bloco = cfg.get("palavras_proibidas_na_interface", {})
    permitidos = [c.lower() for c in bloco.get("contextos_permitidos", [])]
    interface = re.compile(bloco["marcadores_de_interface"], re.IGNORECASE)
    for palavra in bloco.get("palavras", []):
        padrao = re.compile(r"\b" + re.escape(palavra) + r"\w*", re.IGNORECASE)
        for n, linha in linhas_relevantes(texto):
            achado = padrao.search(linha)
            if not achado:
                continue
            dentro_de_rotulo = any(
                c.start() < achado.start() < c.end() for c in CITACAO.finditer(linha)
            )
            if not (dentro_de_rotulo or interface.match(linha)):
                continue  # só texto de tela — a regra é de interface
            baixa = linha.lower()
            if any(c in baixa for c in permitidos):
                continue
            achados.append(
                'linha {}: palavra proibida na interface — "{}" (SPEC §4.9.1). '
                "Se for para descrever o que NÃO existe, diga isso na mesma linha.".format(
                    n, palavra
                )
            )


def confere_autocritica(cfg, texto, achados):
    bloco = cfg.get("autocritica_proibida_em_documento_de_produto", {})
    for bruto in bloco.get("padroes", []):
        padrao = re.compile(bruto, re.IGNORECASE)
        for n, linha in linhas_relevantes(texto):
            if padrao.search(linha):
                achados.append(
                    'linha {}: autocrítica dentro de documento de produto — "{}" '
                    "(CLAUDE.md §2.4). Isso vai para docs/HISTORICO.md.".format(
                        n, padrao.pattern
                    )
                )


def main():
    caminho = caminho_do_stdin()
    if not caminho or not caminho.endswith(".md"):
        return
    nome = os.path.basename(caminho)
    if nome in FORA_DE_TUDO:
        return
    try:
        with open(caminho, "r", encoding="utf-8") as f:
            texto = f.read()
        with open(CONFIG, "r", encoding="utf-8") as f:
            cfg = json.load(f)
    except Exception:
        return

    achados = []
    confere_numeros(cfg, texto, achados)
    if nome in DOCS_DE_PRODUTO:
        confere_palavras(cfg, texto, achados)
        confere_autocritica(cfg, texto, achados)

    if not achados:
        return

    corpo = "GUARDA DE DOCUMENTOS — {} ({} ponto{})\n{}".format(
        nome,
        len(achados),
        "s" if len(achados) > 1 else "",
        "\n".join("  • " + a for a in achados[:20]),
    )
    print(
        json.dumps(
            {
                "systemMessage": corpo,
                "hookSpecificOutput": {
                    "hookEventName": "PostToolUse",
                    "additionalContext": corpo
                    + "\n\nCorrija agora, antes de seguir. Se o número novo é que está certo, "
                    "atualize .claude/numeros-travados.json na mesma entrega e diga isso ao Marco.",
                },
            },
            ensure_ascii=False,
        )
    )


if __name__ == "__main__":
    main()
