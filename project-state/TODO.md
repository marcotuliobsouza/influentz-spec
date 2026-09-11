# TODO — INFLUENTZ

> Próximas tarefas concretas, em ordem. Itens fora do escopo da recuperação
> atual ficam aqui registrados, não implementados por conta própria.

## Agora
1. ✅ **Critério de aceite da fatia 1** — feito, `ACEITE-FATIA-1.md` (68 critérios).
2. ✅ **Auditar `CLAUDE.md` contra este `project-state/`** — feito na recuperação de 11/09.
3. ✅ **Cobertura de teste da fatia 1** — feito, `QA-FATIA-1.md` (44 automatizado obrigatório · 6 contrato de sandbox · 18 manual no 1º ciclo).
4. **Fechar as 3 lacunas de `MAQUINA-DE-ESTADOS.md`** listadas em `BLOCKERS.md` — trabalho do `arquiteto-tecnico`, antes de escrever os testes das funções 42, 63 e 76.

## Depois do critério de aceite
3. Re-derivar as ~30 telas restantes da máquina de estados, uma jornada por vez.
4. Re-sincronizar as 10 telas existentes com as decisões de dinheiro posteriores a 07/09 (comissão 9,5%, mínimo R$ 150, presencial, extrato do criador).

## Registrado, não implementado (fora do escopo desta recuperação)
- **Nota stale em `Pagamento.dc.html`**: "requer CNPJ verificado" no cartão de crédito contradiz a decisão atual (cartão disponível a todos; CNPJ verificado só amplia o teto). Corrigir junto com o item 4, não isoladamente.
- **Chave de funcionalidade (feature flag)** para o parcelamento (já "escrito e desligado" na SPEC §4.2.4) — avaliar formato na Fase 7, não antes.
- **Registro de auditoria (audit log)** para disputas — requisito jurídico, decidir estrutura na Fase 6 (arquiteto-técnico).
- Etapa de pesquisa de skills/plugins/geração de imagem — só depois da recuperação, com sinal explícito do Marco.
