# CURRENT_STATE — INFLUENTZ

> Estado real, verificado no repositório. Não é opinião — é o que existe hoje.
> Atualizado: 12/09/2026, depois da fundação de enforcement.

## Código
**Código de produto não existe.** Zero linhas de programa, zero dependências, zero build. É o esperado nesta fase — código é Fase 7 do método, e o produto ainda não fechou.

**Código de harness existe e é testado:** 3 guardas, 1 verificador, 37 testes de regressão, 1 verificação automática no GitHub. Ver a seção de infraestrutura de processo.

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
- **3 guardas** em `.claude/hooks/`: `guarda-comandos.py` (**bloqueia** comando destrutivo e comando que é decisão do Founder, antes de executar), `guarda-documentos.py` (avisa: números travados + palavra proibida + autocrítica, cobrindo `.md` e telas) e `guarda-painel.py` (avisa: painel sincronizado).
- **Executáveis em um comando:** `python3 .claude/guardas/verificar.py` (repositório inteiro, saída 0/1) e `python3 .claude/guardas/testes.py` (37 testes de regressão).
- **Verificação independente:** `.github/workflows/guardas.yml` roda os dois em todo push e pull request.
- **Permissões declaradas** em `.claude/settings.json`: lista que nega, lista que pergunta, lista que libera.
- `.claude/numeros-travados.json` — fonte dos números que os guardas conferem.
- `.claude/guardas/LEIA-ME.md` — o que é lei, o que é aviso, e **o que ainda não está protegido**.

**Nenhuma skill existe, de propósito.** O único fluxo repetitivo comprovado virou comando e verificação automática.

## Git
🔴 **Nenhum branch tem proteção.** A API do GitHub responde `protected: false` para `main` e para o branch de trabalho (verificado em 12/09). Enquanto isso for verdade, o repositório aceita integração sem verificação e sem aprovação — a trava do agente vale só para o agente. O que configurar está em `.claude/guardas/LEIA-ME.md`; é ação do Founder.

`main` está um commit atrás do branch de trabalho. Sem PRs abertos — todo trabalho vai direto a `main` por decisão do processo atual (repositório de um dono só, sem equipe revisando PR).

## Critério de aceite e cobertura de teste
Fatia 1 completa: 68 critérios em `ACEITE-FATIA-1.md`, cobertura decidida em `QA-FATIA-1.md`. Fatias 2 e 3 ainda não — de propósito, só quando a construção chegar lá.
