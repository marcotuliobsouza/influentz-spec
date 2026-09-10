#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Guarda do painel.

CLAUDE.md §7: o Marco lê o painel publicado, não arquivo do repositório.
"Documento que ele não consegue abrir é documento que não existe."

Roda quando a sessão para. Se documento de produto mudou e PAINEL.md não
mudou junto, avisa — em voz alta, porque essa é exatamente a falha que fez
o Marco dizer que não sabia de que painel eu estava falando.
"""

import json
import os
import subprocess
import sys

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


def mudou():
    try:
        saida = subprocess.run(
            ["git", "status", "--porcelain"],
            cwd=RAIZ,
            capture_output=True,
            text=True,
            timeout=15,
        ).stdout
    except Exception:
        return set()
    arquivos = set()
    for linha in saida.splitlines():
        if len(linha) > 3:
            arquivos.add(linha[3:].strip().strip('"').split(" -> ")[-1])
    return arquivos


def main():
    try:
        json.load(sys.stdin)
    except Exception:
        pass

    arquivos = mudou()
    if not arquivos:
        return

    produto = sorted(
        a
        for a in arquivos
        if (a.startswith("docs/") or a == "CLAUDE.md")
        and a.endswith(".md")
        and not a.endswith("HISTORICO.md")
    )
    if not produto:
        return
    if "PAINEL.md" in arquivos:
        print(
            json.dumps(
                {
                    "systemMessage": "PAINEL.md foi atualizado. Falta republicar o artefato "
                    "no MESMO endereço (CLAUDE.md §7) — o Marco só lê o painel publicado.",
                },
                ensure_ascii=False,
            )
        )
        return

    print(
        json.dumps(
            {
                "systemMessage": "GUARDA DO PAINEL — mudou {} e o PAINEL.md não mudou junto. "
                "O Marco lê o painel publicado, não o repositório (CLAUDE.md §7).".format(
                    ", ".join(produto[:6])
                ),
            },
            ensure_ascii=False,
        )
    )


if __name__ == "__main__":
    main()
