# BLOCKERS — INFLUENTZ

> Impedimentos reais. Vazio é o estado bom — mantenha assim.

## Bloqueando o próximo passo
Nenhum bloqueio total — mas o `qa-estrategia` encontrou 3 lacunas na `MAQUINA-DE-ESTADOS.md` ao decidir cobertura de teste da Fatia 1 (`QA-FATIA-1.md`). Não são bloqueio de produto (o Marco não decide isso) — são trabalho do `arquiteto-tecnico`, registrado aqui em vez de resolvido sem revisão:

1. **Função 42 (reenvio de documento recusado):** a MÁQUINA não lista um estado de "reenviado, aguardando nova análise" — não dá para saber se reenvio é o mesmo caso de "aprova/recusa" ou um estado novo.
2. **Função 63 (checkout):** não há regra de timeout se o webhook do provedor nunca chegar — falta saber se existe devolução automática para "aguardando pagamento" ou se fica preso até reconciliação manual (função 86).
3. **Função 76 (abrir disputa):** a MÁQUINA cita `em_disputa` a partir de estados diferentes em pontos diferentes do documento, sem uma lista única e fechada de quais estados são elegíveis para abrir disputa.

Nenhuma impede escrever teste — o `qa-estrategia` decidiu cobertura mesmo sem essas respostas (todas automatizado obrigatório, por prudência). Mas ficam sem caso de teste fechado até o `arquiteto-tecnico` fechar a lista de estados.

## Bloqueando código (Fase 7)
- **CNPJ da INFLUENTZ não aberto.** Sem ele, Pagar.me não sai do sandbox. Não bloqueia especificar nem codar contra o sandbox — bloqueia produção.
- **Contador e advogado não contratados.** Lista de perguntas pronta em SPEC §15. Pendência do Marco, não de engenharia.

## Bloqueando lançamento
- **Lista de cold start** (SPEC §14.1) — quantos criadores/marcas o Marco tem hoje. Único item que nem dinheiro nem engenharia resolvem.
