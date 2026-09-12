#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Verificador reproduzível dos guardas da INFLUENTZ.

O guarda de documentos foi escrito como hook: lê UM caminho da entrada
padrão e avisa. Isso só funciona na máquina do agente, no turno do agente.
Este script roda as MESMAS funções sobre o repositório inteiro, em um
comando, com código de saída.

    python3 .claude/guardas/verificar.py            # todo o repositório
    python3 .claude/guardas/verificar.py caminho... # só esses arquivos

    saída 0 = PASS   ·   saída 1 = FAIL   ·   saída 2 = erro de execução

Não reescreve o guarda: importa as funções dele. Se a regra mudar lá, muda
aqui junto — não existe segunda cópia da regra para divergir.

Cobertura: .md (números travados; e mais palavra proibida e autocrítica nos
documentos de produto) e .html/.dc.html/canvas.json (palavra proibida em
rótulo de tela). Fora: docs/HISTORICO.md (guarda número velho de propósito)
e arquivos listados no .gitignore da própria pasta (payload regenerável).
"""

import importlib.util
import json
import os
import sys

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
GUARDA = os.path.join(RAIZ, ".claude", "hooks", "guarda-documentos.py")
CONFIG = os.path.join(RAIZ, ".claude", "numeros-travados.json")

# Pastas que nunca entram: dependência, build, cache, histórico do Git.
PULAR = {".git", "node_modules", "__pycache__", ".next", "out", "build", ".vercel"}


def carrega_guarda():
    """O arquivo tem hífen no nome, então não dá para 'import' normal."""
    spec = importlib.util.spec_from_file_location("guarda_documentos", GUARDA)
    modulo = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(modulo)
    return modulo


def arquivos_do_repo():
    for pasta, subpastas, nomes in os.walk(RAIZ):
        subpastas[:] = [s for s in subpastas if s not in PULAR]
        for nome in sorted(nomes):
            yield os.path.join(pasta, nome)


def classifica(g, caminho):
    """Devolve 'documento', 'tela' ou None — mesma regra do hook."""
    nome = os.path.basename(caminho)
    if caminho.endswith(g.EXT_DOCUMENTO):
        tipo = "documento"
    elif caminho.endswith(g.EXT_TELA) or nome == "canvas.json":
        tipo = "tela"
    else:
        return None
    if nome in g.FORA_DE_TUDO or g.eh_gerado(caminho):
        return None
    return tipo


def confere(g, cfg, caminho, tipo):
    with open(caminho, "r", encoding="utf-8") as f:
        texto = f.read()
    achados = []
    if tipo == "documento":
        g.confere_numeros(cfg, texto, achados)
        if os.path.basename(caminho) in g.DOCS_DE_PRODUTO:
            g.confere_palavras(cfg, texto, achados)
            g.confere_autocritica(cfg, texto, achados)
    else:
        g.confere_palavras_tela(cfg, texto, achados)
    return achados


def main(argv):
    try:
        g = carrega_guarda()
        with open(CONFIG, "r", encoding="utf-8") as f:
            cfg = json.load(f)
    except Exception as erro:
        print("ERRO: não consegui carregar o guarda — {}".format(erro), file=sys.stderr)
        return 2

    alvos = [os.path.abspath(a) for a in argv] if argv else list(arquivos_do_repo())

    conferidos = 0
    problemas = []
    for caminho in alvos:
        tipo = classifica(g, caminho)
        if not tipo:
            continue
        conferidos += 1
        try:
            achados = confere(g, cfg, caminho, tipo)
        except Exception as erro:
            print("ERRO ao ler {} — {}".format(caminho, erro), file=sys.stderr)
            return 2
        for a in achados:
            problemas.append((os.path.relpath(caminho, RAIZ), a))

    if problemas:
        print("FAIL — {} ponto(s) em {} arquivo(s) conferido(s)\n".format(
            len(problemas), conferidos))
        atual = None
        for arquivo, achado in problemas:
            if arquivo != atual:
                print("  {}".format(arquivo))
                atual = arquivo
            print("    - {}".format(achado))
        return 1

    print("PASS — {} arquivo(s) conferido(s), nenhum ponto".format(conferidos))
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
