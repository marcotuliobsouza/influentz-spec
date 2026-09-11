# CURRENT_STATE — INFLUENTZ

> Estado real, verificado no repositório. Não é opinião — é o que existe hoje.
> Atualizado: 11/09/2026, depois da recuperação controlada.

## Código
**Não existe.** Zero linhas de programa, zero dependências, zero build, zero testes. É o esperado nesta fase — código é Fase 7 do método, e o produto ainda não fechou.

## Documentos (fonte de verdade do produto)
| Documento | Versão | Cobre |
|---|---|---|
| `docs/SPEC-INFLUENTZ.md` | v0.5 | Regras de negócio, dinheiro, legal |
| `docs/MAQUINA-DE-ESTADOS.md` | v0.4 | Todo estado e transição do sistema. **§3.2 (KYC), §9.4 (aviso do provedor) e §10.0 (lista única de disputa) fechadas em 11/09** |
| `docs/FEATURE-MATRIX.md` | v3.2 | 91 funções do v1, por jornada |
| `docs/PRODUTO-DETALHADO.md` | v1.0 | Campos, métricas, formulários |
| `docs/DESIGN-SYSTEM.md` | v0.4 | Cor, tipografia, tokens |
| `docs/METODO-DE-TRABALHO.md` | v1.0 | As 8 fases oficiais |

## Telas
10 wireframes em `design/wireframes-v1/*.dc.html`, canvas publicado em
https://claude.ai/code/artifact/e4656b12-ab12-47f4-a1d9-1a909af39ccc

**Datam de 07/09.** Decisões de dinheiro posteriores (comissão 9,5%, mínimo R$ 150, presencial, extrato do criador) ainda não estão refletidas nas telas — são fluxo, não regulatório, por isso não bloqueiam, mas precisam de re-derivação antes da Fase 7.

## Infraestrutura de processo
- 12 especialistas em `.claude/agents/*.md` — todos customizados deste projeto (nenhum nativo do Claude Code). `code-review` e `security-review` são nativos (skills, não agents/).
- 2 guardas automáticos em `.claude/hooks/`: `guarda-documentos.py` (números travados + palavra proibida + autocrítica, cobrindo `.md` e telas `.html`/`.dc.html`/`canvas.json`) e `guarda-painel.py` (painel sincronizado).
- `.claude/numeros-travados.json` — fonte dos números que os guardas conferem.

## Git
`main` e o branch de trabalho estão em paridade (mesmo commit). Sem PRs abertos — todo trabalho vai direto a `main` por decisão do processo atual (repositório de um dono só, sem equipe revisando PR).

## Critério de aceite e cobertura de teste
Fatia 1 completa: 68 critérios em `ACEITE-FATIA-1.md`, cobertura decidida em `QA-FATIA-1.md`. Fatias 2 e 3 ainda não — de propósito, só quando a construção chegar lá.
