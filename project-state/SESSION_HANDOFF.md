# SESSION_HANDOFF — INFLUENTZ

> O que uma sessão nova precisa saber para continuar sem perguntar.
> Leia isto + `CURRENT_STATE.md` antes de assumir qualquer coisa da conversa anterior.

## O que acabou de acontecer (11/09/2026)
Auditoria completa do projeto, seguida de recuperação controlada:
1. 54 commits que só existiam num branch de trabalho foram integrados a `main` (fast-forward, zero conflito).
2. Duas telas (`Extrato.dc.html`, `Busca.dc.html`) violavam SPEC §4.9.1 (palavra "carteira"/"saldo" na interface) — corrigidas, e o canvas publicado foi atualizado.
3. `guarda-documentos.py` só cobria `.md` — estendido para cobrir telas também.
4. Este `project-state/` foi criado porque a continuidade dependia inteiramente da memória da conversa.

## Onde ler o estado real
`CURRENT_STATE.md` (o que existe) → `ROADMAP.md` (onde estamos na sequência) → `TODO.md` (próxima tarefa concreta) → `BLOCKERS.md` (o que está travado).

## Regra de ouro desta sessão
**Não redesenhe as telas ainda.** A próxima tarefa é o critério de aceite da fatia 1 (`TODO.md` #1), não uma tela nova. Redesenhar antes disso é repetir o erro que gerou 69% de retrabalho no inventário de funções (ver `docs/HISTORICO.md`).

## Postura esperada
O Marco não é técnico e pediu explicitamente para não virar o gerente técnico do projeto: decisões de arquitetura, biblioteca e estrutura são minhas, sem perguntar (CLAUDE.md §2.1, categoria A). Só pergunto quando é dinheiro do bolso dele, gosto de marca, ou matar/manter uma função inteira.
