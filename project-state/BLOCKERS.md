# BLOCKERS — INFLUENTZ

> Impedimentos reais. Vazio é o estado bom — mantenha assim.

## Bloqueando o próximo passo
Nenhum. As 3 lacunas da `MAQUINA-DE-ESTADOS.md` foram fechadas em 11/09 (§3.2, §9.4, §10.0) — ver `DECISIONS.md`.

## Aguardando resposta do provedor (não bloqueia construir)
Perguntas 20 a 24 da SPEC §4.6.2, criadas ao fechar as lacunas. Nenhuma impede escrever código contra o sandbox; todas viram documento quando o Relacionamento responder:
- **20/21/22** — reenvio, autenticação e ordem do webhook. Enquanto não respondem, **a consulta ao provedor é a única fonte confiável**, e é isso que §9.4 já assume.
- **23** — se `denied`/`fully_denied` é recuperável com recebedor novo. Decide se a recusa definitiva encerra o contrato ou a presença do criador.
- **24** — se cancelar cobrança impede pagamento posterior de boleto. É a trava contra dinheiro órfão.

## Sem número com fonte (não invento)
- **Prazo visível do item de conciliação e da recusa definitiva de KYC na caixa de entrada (função 88).** Todo item da 88 promete prazo; esses dois não têm SLA em documento nenhum. É decisão de operação (`infra`), não do Marco.

## Fora de escopo, para a próxima rodada de arquitetura
- **`em_defesa` (§9.1) tem prazo fatal de 10 dias e nenhuma porta de saída por vencimento no diagrama.** A tabela descreve o prazo; a máquina não o executa. Achado na revisão adversarial, não relacionado às 3 lacunas.

## Bloqueando código (Fase 7)
- **CNPJ da INFLUENTZ não aberto.** Sem ele, Pagar.me não sai do sandbox. Não bloqueia especificar nem codar contra o sandbox — bloqueia produção.
- **Contador e advogado não contratados.** Lista de perguntas pronta em SPEC §15. Pendência do Marco, não de engenharia.

## Bloqueando lançamento
- **Lista de cold start** (SPEC §14.1) — quantos criadores/marcas o Marco tem hoje. Único item que nem dinheiro nem engenharia resolvem.
