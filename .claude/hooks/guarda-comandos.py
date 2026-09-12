#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Guarda de comandos da INFLUENTZ.

Roda ANTES de todo comando de terminal (PreToolUse sobre Bash) e BLOQUEIA
o comando quando ele é destrutivo ou viola a governança. Ao contrário dos
outros dois guardas, este não avisa: impede.

Mecanismo: código de saída 2. A documentação do Claude Code define exit 2
em PreToolUse como bloqueio incondicional, independente da saída JSON.
Fonte: https://code.claude.com/docs/en/hooks (consultada em 12/09/2026).

DUAS FAIXAS, porque enforcement desproporcional vira enforcement desligado:

  DESTRUTIVO — perde trabalho e não tem desfazer. Não há escape aqui.
    reset --hard · push forçado · rm -rf · git clean -fd · branch -D ·
    checkout -- . · qualquer escrita em docs/marca/ (fonte de marca fechada)

  GOVERNANÇA — reversível, mas é decisão do Founder, não minha.
    merge · push para main · release/tag · deploy
    Escape explícito: prefixar o comando com APROVADO_PELO_FOUNDER=1.

Honestidade sobre o alcance, porque o projeto não promete o que não cumpre:
o escape acima é uma trava contra ACIDENTE e contra o agente agir sozinho —
fica visível na transcrição e no histórico do terminal. Não é controle
criptográfico: quem escreve o comando pode escrever o prefixo. O controle
que não depende de quem executa é a proteção de branch no GitHub, que é
configuração do Founder e está registrada em .claude/guardas/LEIA-ME.md.

Tudo que não está nas listas passa direto. Desenvolvimento normal — ler,
testar, editar, commitar, criar branch, push do branch de trabalho — nunca
é bloqueado.
"""

import json
import re
import sys

ESCAPE = re.compile(r"\bAPROVADO_PELO_FOUNDER=1\b")

# Separadores de comando encadeado: um "git status && git push --force" tem
# que ser lido como dois comandos, senão a trava é contornada por acidente.
SEPARADORES = re.compile(r"&&|\|\||;|\n|\|")

# Corpo de heredoc é DADO sendo escrito, não comando sendo executado. Escrever
# documentação que cita um comando destrutivo não é executá-lo — este guarda
# bloqueou a própria página que o documenta antes desta regra existir.
# Continua valendo o que já estava declarado como falso negativo conhecido:
# comando dentro de script só é pego quando o script é executado.
HEREDOC = re.compile(
    r"<<-?\s*(['\"]?)([A-Za-z_][A-Za-z0-9_]*)\1.*?^\s*\2\s*$",
    re.DOTALL | re.MULTILINE,
)


def sem_heredoc(comando):
    """Remove o conteúdo escrito por heredoc, preservando a linha de comando."""
    return HEREDOC.sub("<<HEREDOC", comando)

DESTRUTIVO = [
    (
        re.compile(r"\bgit\s+reset\b[^\n]*--hard\b"),
        "git reset --hard apaga trabalho não commitado sem desfazer. "
        "Use 'git stash' ou commite antes.",
    ),
    (
        re.compile(r"\bgit\s+push\b[^\n]*(--force(?!-with-lease)\b|\s-f\b)"),
        "push forçado reescreve histórico remoto. "
        "A recuperação dos 54 commits só foi possível porque o histórico estava intacto.",
    ),
    (
        re.compile(r"\bgit\s+push\b[^\n]*\s\+[\w/]"),
        "push com '+' é push forçado disfarçado — mesma regra.",
    ),
    (
        re.compile(r"\brm\s+(-[a-zA-Z]*r[a-zA-Z]*f|-[a-zA-Z]*f[a-zA-Z]*r)\b"),
        "rm -rf não tem desfazer. Se um arquivo precisa sair, "
        "'git rm' mantém o histórico.",
    ),
    (
        re.compile(r"\bgit\s+clean\b[^\n]*-[a-zA-Z]*f"),
        "git clean -f apaga arquivo que nunca foi commitado — some sem rastro.",
    ),
    (
        re.compile(r"\bgit\s+branch\b[^\n]*\s-D\b"),
        "git branch -D apaga branch sem conferir se foi integrado. Use -d.",
    ),
    (
        re.compile(r"\bgit\s+checkout\b[^\n]*\s--\s+\.(\s|$)"),
        "git checkout -- . descarta toda alteração da árvore de uma vez.",
    ),
    (
        re.compile(r"\b(rm|mv|cp|truncate|tee|sed\s+-i)\b[^\n]*docs/marca/"),
        "docs/marca/ é a fonte fechada da identidade da marca (CLAUDE.md §7). "
        "Só o Founder altera, e não por comando de agente.",
    ),
]

GOVERNANCA = [
    (
        re.compile(r"\bgit\s+merge\b"),
        "merge é decisão do Founder (governança: nenhum merge sem aprovação).",
    ),
    (
        re.compile(r"\bgit\s+push\b[^\n]*\borigin\s+(HEAD:)?main\b"),
        "push direto para main é decisão do Founder. "
        "O trabalho vai para o branch designado.",
    ),
    (
        re.compile(r"\bgit\s+push\b[^\n]*--tags\b|\bgit\s+tag\b[^\n]*\s-[^\s]*\s*v\d"),
        "publicar tag/release é decisão do Founder.",
    ),
    (
        re.compile(r"\b(vercel|netlify)\b(?![^\n]*\b(--help|-h)\b)"),
        "deploy é decisão do Founder. Nada sobe sem aprovação.",
    ),
    (
        re.compile(r"\bsupabase\b[^\n]*\b(db\s+push|link|migration\s+up)\b"),
        "alterar banco de fornecedor é decisão do Founder.",
    ),
]


def avalia(comando):
    """Devolve (motivo, faixa) do primeiro bloqueio encontrado, ou (None, None)."""
    comando = sem_heredoc(comando)
    tem_escape = bool(ESCAPE.search(comando))
    for pedaco in SEPARADORES.split(comando):
        pedaco = pedaco.strip()
        if not pedaco:
            continue
        for padrao, motivo in DESTRUTIVO:
            if padrao.search(pedaco):
                return motivo, "DESTRUTIVO"
        if tem_escape:
            continue  # o escape só vale para a faixa de governança
        for padrao, motivo in GOVERNANCA:
            if padrao.search(pedaco):
                return motivo, "GOVERNANÇA"
    return None, None


def main():
    try:
        dados = json.load(sys.stdin)
    except Exception:
        return 0  # sem entrada legível, não há o que julgar — não atrapalha
    if dados.get("tool_name") != "Bash":
        return 0
    comando = (dados.get("tool_input") or {}).get("command") or ""
    motivo, faixa = avalia(comando)
    if not motivo:
        return 0

    if faixa == "DESTRUTIVO":
        saida = (
            "GUARDA DE COMANDOS — BLOQUEADO ({}).\n{}\n"
            "Esta faixa não tem escape. Se o comando é mesmo necessário, "
            "explique ao Founder o que será perdido e peça que ele execute.".format(
                faixa, motivo
            )
        )
    else:
        saida = (
            "GUARDA DE COMANDOS — BLOQUEADO ({}).\n{}\n"
            "Se o Founder já aprovou, refaça com o prefixo APROVADO_PELO_FOUNDER=1 "
            "— o prefixo fica registrado na transcrição.".format(faixa, motivo)
        )
    print(saida, file=sys.stderr)
    return 2


if __name__ == "__main__":
    sys.exit(main())
