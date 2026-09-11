# TODO — INFLUENTZ

> Próximas tarefas concretas, em ordem. Itens fora do escopo da recuperação
> atual ficam aqui registrados, não implementados por conta própria.

## Agora
1. ✅ **Critério de aceite da fatia 1** — feito, `ACEITE-FATIA-1.md` (68 critérios).
2. ✅ **Auditar `CLAUDE.md` contra este `project-state/`** — feito na recuperação de 11/09.
3. ✅ **Cobertura de teste da fatia 1** — feito, `QA-FATIA-1.md` (44 automatizado obrigatório · 6 contrato de sandbox · 18 manual no 1º ciclo).
4. ✅ **Fechar as 3 lacunas de `MAQUINA-DE-ESTADOS.md`** — feito em 11/09 (§3.2, §9.4, §10.0).
5. **Derivar os casos de teste das funções 42, 63 e 76** agora que a semântica está fechada — trabalho do `qa-estrategia`, e é o próximo passo natural.
6. **Fechar `em_defesa` (§9.1)** — prazo fatal de 10 dias sem porta de saída no diagrama. Achado na revisão adversarial, fora do escopo daquela rodada.

## Depois do critério de aceite
3. Re-derivar as ~30 telas restantes da máquina de estados, uma jornada por vez.
4. Re-sincronizar as 10 telas existentes com as decisões de dinheiro posteriores a 07/09 (comissão 9,5%, mínimo R$ 150, presencial, extrato do criador).

## Correção pendente na SPEC (não aplicada — instrução de não alterar a SPEC nesta rodada)
- 🔴 **SPEC §4.3 camada 5 (linha 204) diz que o fundo acumula R$ 90/mês (5% de R$ 1.800).** Esse número vem da comissão de lançamento antiga de 7,5%. A comissão travada é 9,5% = R$ 2.280/mês, e 5% disso é **R$ 114** — que é o que §4.3.3 já diz. A linha 204 ficou para trás e distorce a matemática em 21%. Achado pelo `financeiro` em 11/09.

## Registrado, não implementado (fora do escopo desta recuperação)
- **Nota stale em `Pagamento.dc.html`**: "requer CNPJ verificado" no cartão de crédito contradiz a decisão atual (cartão disponível a todos; CNPJ verificado só amplia o teto). Corrigir junto com o item 4, não isoladamente.
- **Chave de funcionalidade (feature flag)** para o parcelamento (já "escrito e desligado" na SPEC §4.2.4) — avaliar formato na Fase 7, não antes.
- **Registro de auditoria (audit log)** para disputas — requisito jurídico, decidir estrutura na Fase 6 (arquiteto-técnico).
- Etapa de pesquisa de skills/plugins/geração de imagem — só depois da recuperação, com sinal explícito do Marco.
