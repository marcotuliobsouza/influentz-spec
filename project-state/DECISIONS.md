# DECISIONS — INFLUENTZ

> Só decisões de consequência irreversível ou estrutural, com a evidência.
> Decisões de produto/dinheiro/legal vivem na SPEC — aqui só o que muda como o
> projeto é conduzido.

| Decisão | Evidência | Data |
|---|---|---|
| `main` é a única branch de trabalho real; sem fluxo de PR (dono único, sem revisor) | `git log`: 0 PRs em 59 commits | 11/09 |
| Fast-forward de `main` para o branch de 54 commits — zero conflito, `main` era ancestral puro | `git merge-base --is-ancestor` = true | 11/09 |
| Guarda de documentos estendido para cobrir telas (`.html`/`.dc.html`/`canvas.json`), não só `.md` | Achado da auditoria: violação de §4.9.1 publicada, guarda não via | 11/09 |
| "Cartão de crédito" é exceção nomeada na regra de palavra proibida — é o nome do método de pagamento, não o conceito de saldo/carteira que a SPEC §4.9.1 proíbe | Teste de regressão do guarda; SPEC usa a mesma expressão em prosa | 11/09 |
| Arquivo `influentz-wireframes-v1.html` (payload do skill de design) é gitignored e nunca é fonte — sempre regenerado dos `.dc.html` | `.gitignore` da própria pasta, comentado | 11/09 |
| Critério de aceite passa a ser obrigatório antes de qualquer código, começando pela fatia 1 (não as 91 funções de uma vez) | Instrução da recuperação, Passo 7 | 11/09 |
| `project-state/` criado como memória entre sessões — curto, não duplica SPEC/HISTORICO | Falha observada: continuidade dependia da conversa | 11/09 |
| Guarda de números ganhou exceção de subconjunto — "68 funções da Fatia 1" não é o total do v1; sem ela, o próprio critério de aceite acusaria falso positivo | Achado ao escrever ACEITE-FATIA-1.md; guarda disparou, corrigido e reprovado antes de seguir | 11/09 |
