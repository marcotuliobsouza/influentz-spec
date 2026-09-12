#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Testes de regressão dos guardas da INFLUENTZ.

    python3 .claude/guardas/testes.py
    saída 0 = todos passaram · saída 1 = algum falhou

Regra desta suíte: cada teste protege uma falha REAL já encontrada neste
projeto, registrada em project-state/DECISIONS.md. Não há teste inventado
para engordar número — os guardas já foram calibrados cinco vezes, e o
risco concreto é a sexta calibração reabrir o falso positivo da primeira.

Cada caso diz qual falha ele guarda.
"""

import os
import subprocess
import sys
import tempfile

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
VERIFICAR = os.path.join(RAIZ, ".claude", "guardas", "verificar.py")
COMANDOS = os.path.join(RAIZ, ".claude", "hooks", "guarda-comandos.py")

PASS, FAIL = 0, 1


# ---------------------------------------------------------------- documentos

def roda_verificador(nome_do_arquivo, conteudo):
    """Escreve o conteúdo num arquivo temporário com o nome pedido (o nome
    importa: SPEC-INFLUENTZ.md é documento de produto, um .md qualquer não)
    e devolve (codigo, saida)."""
    with tempfile.TemporaryDirectory() as pasta:
        caminho = os.path.join(pasta, nome_do_arquivo)
        with open(caminho, "w", encoding="utf-8") as f:
            f.write(conteudo)
        r = subprocess.run(
            [sys.executable, VERIFICAR, caminho], capture_output=True, text=True
        )
        return r.returncode, r.stdout + r.stderr


CASOS_DOCUMENTO = [
    (
        "falso positivo real: 'cartão de crédito' é o nome do método de pagamento, "
        "não o 'crédito' de saldo que a SPEC §4.9.1 proíbe",
        "SPEC-INFLUENTZ.md",
        'A marca paga com Pix, boleto ou "cartão de crédito" à vista.',
        PASS,
    ),
    (
        "falso positivo real: subconjunto — '68 funções da Fatia 1' não é o total do v1",
        "ACEITE-FATIA-1.md",
        "São 68 funções da Fatia 1, das 91 funções no v1.",
        PASS,
    ),
    (
        "falso positivo real: '44 funções' solto num resumo de categorias "
        "não afirma o total do v1 (o primeiro conserto por exclusão não pegava este)",
        "QA-FATIA-1.md",
        "Somando as categorias de dinheiro e de conteúdo, são 44 funções cobertas.",
        PASS,
    ),
    (
        "falso positivo real: linha contrafactual explica a decisão, não afirma outro número",
        "SPEC-INFLUENTZ.md",
        "A 7,5% o ponto de equilíbrio seria 25 contratos/mês — por isso a "
        "comissão de lançamento é 9,5%.",
        PASS,
    ),
    (
        "falha real: número travado divergente entre documentos "
        "('98', '97' e '91' já conviveram)",
        "FEATURE-MATRIX.md",
        "O escopo fechou em 97 funções no v1.",
        FAIL,
    ),
    (
        "falha real: comissão de lançamento divergente da decisão travada",
        "SPEC-INFLUENTZ.md",
        "A comissão de lançamento é de 7,5% sobre o contrato.",
        FAIL,
    ),
    (
        "falha real §2.4: autocrítica dentro de documento de produto",
        "SPEC-INFLUENTZ.md",
        "Corrigido em 08/09/2026: a versão anterior estava errada.",
        FAIL,
    ),
    (
        "documento de processo pode registrar correção — §2.4 vale só para produto",
        "METODO-DE-TRABALHO.md",
        "Corrigido em 08/09/2026: a versão anterior estava errada.",
        PASS,
    ),
]

CASOS_TELA = [
    (
        "falha real: a violação de §4.9.1 que foi publicada em Extrato.dc.html "
        "e só apareceu semanas depois, numa auditoria por busca de texto",
        "Extrato.dc.html",
        '<div class="titulo">Saldo disponível para saque</div>',
        FAIL,
    ),
    (
        "falha real: 'carteira' como rótulo de tela",
        "Perfil.dc.html",
        "<h2>Minha carteira</h2>",
        FAIL,
    ),
    (
        "o rótulo corrigido não pode disparar — senão o guarda vira barulho",
        "Extrato.dc.html",
        '<div class="titulo">Meus recebimentos</div>'
        '<span>Disponível para envio</span>',
        PASS,
    ),
    (
        "'cartão de crédito' numa tela é o método de pagamento, não violação",
        "Pagamento.dc.html",
        "<button>Pagar com cartão de crédito</button>",
        PASS,
    ),
]


# ----------------------------------------------------------------- comandos

def roda_guarda_comandos(comando):
    entrada = (
        '{"tool_name":"Bash","tool_input":{"command":' + _json_str(comando) + "}}"
    )
    r = subprocess.run(
        [sys.executable, COMANDOS], input=entrada, capture_output=True, text=True
    )
    return r.returncode, r.stderr


def _json_str(s):
    import json as _j

    return _j.dumps(s)


BLOQUEADO, LIBERADO = 2, 0

CASOS_COMANDO = [
    ("destrutivo: reset --hard apaga trabalho não commitado",
     "git reset --hard HEAD~3", BLOQUEADO),
    ("destrutivo: push forçado reescreve histórico remoto — "
     "a recuperação dos 54 commits dependeu do histórico intacto",
     "git push --force origin main", BLOQUEADO),
    ("destrutivo: push forçado na forma curta",
     "git push -f origin minha-branch", BLOQUEADO),
    ("destrutivo: rm -rf", "rm -rf docs/", BLOQUEADO),
    ("destrutivo: rm -fr (ordem trocada das letras)", "rm -fr build", BLOQUEADO),
    ("destrutivo: git clean -fd apaga arquivo nunca commitado",
     "git clean -fd", BLOQUEADO),
    ("destrutivo: escrita na fonte fechada da marca",
     "rm docs/marca/README.md", BLOQUEADO),
    ("encadeamento não pode contornar a trava",
     "git status && git push --force origin main", BLOQUEADO),
    ("destrutivo não tem escape, nem com o prefixo do Founder",
     "APROVADO_PELO_FOUNDER=1 git reset --hard", BLOQUEADO),
    ("governança: merge é decisão do Founder", "git merge main", BLOQUEADO),
    ("governança: push direto para main", "git push origin main", BLOQUEADO),
    ("governança tem escape explícito e registrado",
     "APROVADO_PELO_FOUNDER=1 git merge main", LIBERADO),
    ("falso positivo real, encontrado em 12/09/2026: o guarda bloqueou a escrita "
     "da própria página que o documenta, porque o texto CITA o comando destrutivo. "
     "Corpo de heredoc é dado escrito, não comando executado",
     "cat > LEIA-ME.md <<'MD'\nNunca use git reset --hard aqui.\nMD",
     LIBERADO),
    ("o conserto acima não pode abrir buraco: comando destrutivo DEPOIS do "
     "heredoc continua bloqueado",
     "cat > a.md <<'MD'\ntexto qualquer\nMD\ngit push --force origin main",
     BLOQUEADO),
    ("nem ANTES do heredoc",
     "git reset --hard && cat > a.md <<'MD'\ntexto\nMD",
     BLOQUEADO),
    # --- desenvolvimento normal nunca pode ser bloqueado ---
    ("normal: ver estado", "git status --porcelain", LIBERADO),
    ("normal: commitar", 'git commit -m "ajuste"', LIBERADO),
    ("normal: push do branch de trabalho",
     "git push -u origin claude/project-status-next-steps-0uchhx", LIBERADO),
    ("normal: criar branch", "git checkout -b nova-frente", LIBERADO),
    ("normal: rodar os próprios guardas",
     "python3 .claude/guardas/verificar.py", LIBERADO),
    ("normal: ler arquivo", "cat docs/SPEC-INFLUENTZ.md | head -20", LIBERADO),
    ("normal: apagar um arquivo temporário sem -rf", "rm /tmp/saida.txt", LIBERADO),
    ("normal: push forçado COM lease não é a mesma coisa que --force",
     "git push --force-with-lease origin minha-branch", LIBERADO),
    ("normal: stash em vez de reset --hard", "git stash", LIBERADO),
]


# ------------------------------------------------------------------ execução

def main():
    falhas = []
    total = 0

    print("GUARDA DE DOCUMENTOS E TELAS")
    for descricao, nome, conteudo, esperado in CASOS_DOCUMENTO + CASOS_TELA:
        total += 1
        codigo, saida = roda_verificador(nome, conteudo)
        ok = codigo == esperado
        print("  {} {} [{}]".format("ok  " if ok else "FALHOU", descricao, nome))
        if not ok:
            falhas.append(
                "{} [{}] — esperado {}, obtido {}\n{}".format(
                    descricao,
                    nome,
                    "PASS" if esperado == PASS else "FAIL",
                    "PASS" if codigo == PASS else "FAIL",
                    saida.strip(),
                )
            )

    print("\nGUARDA DE COMANDOS")
    for descricao, comando, esperado in CASOS_COMANDO:
        total += 1
        codigo, erro = roda_guarda_comandos(comando)
        ok = codigo == esperado
        print("  {} {}\n        $ {}".format("ok  " if ok else "FALHOU", descricao, comando))
        if not ok:
            falhas.append(
                "{}\n  $ {}\n  esperado {}, obtido {}\n  {}".format(
                    descricao,
                    comando,
                    "BLOQUEADO" if esperado == BLOQUEADO else "LIBERADO",
                    "BLOQUEADO" if codigo == BLOQUEADO else "LIBERADO",
                    erro.strip(),
                )
            )

    print("\nREPOSITÓRIO INTEIRO")
    total += 1
    r = subprocess.run([sys.executable, VERIFICAR], capture_output=True, text=True, cwd=RAIZ)
    ok = r.returncode == 0
    print("  {} os documentos corretos não geram nenhum aviso "
          "(critério permanente: guarda barulhento é guarda ignorado)".format(
              "ok  " if ok else "FALHOU"))
    if not ok:
        falhas.append("repositório inteiro devia passar\n" + r.stdout + r.stderr)

    print("\n" + "-" * 60)
    if falhas:
        print("FAIL — {} de {} testes falharam\n".format(len(falhas), total))
        for f in falhas:
            print("  * " + f + "\n")
        return 1
    print("PASS — {} de {} testes".format(total, total))
    return 0


if __name__ == "__main__":
    sys.exit(main())
