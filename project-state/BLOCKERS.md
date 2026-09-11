# BLOCKERS — INFLUENTZ

> Impedimentos reais. Vazio é o estado bom — mantenha assim.

## Bloqueando o próximo passo
Nenhum. As 3 lacunas da `MAQUINA-DE-ESTADOS.md` foram fechadas em 11/09 (§3.2, §9.4, §10.0) — ver `DECISIONS.md`.

## 🔴 DECISÃO DO DONO — bloqueia a função 76 virar tela ou código

**Disputa de permanência: o que ela executa.** Reaberta em 11/09 a pedido do Marco, depois de a perícia documental mostrar que a conclusão anterior não estava comprovada.

**O que está escrito (§8.0.3):** *"Descumprir gera registro, cláusula e direito de disputa da marca; nunca estorno automático."* E o estado `removido_antes_do_prazo`: *"conta no histórico do criador — nunca gera estorno automático."*

**Por que isso não fecha a questão:** a palavra é *automático*. O texto proíbe o estorno que acontece sozinho — **não proíbe estorno decidido por mediação humana**. E a máquina de disputa tem `executada` = *"dinheiro movimentado conforme a decisão"* como desfecho normal; uma disputa que nunca o alcança está usando uma máquina que não foi desenhada para ela.

**Precedente que enfraquece a eliminação anterior:** SPEC §4.3(b) já resolve o caso "dinheiro já saiu e a marca tem direito" — *"a plataforma não debita o criador: paga o fundo de contestação"*. O mecanismo existe e já é usado; dizer que o fundo não serve aqui é argumento para redimensioná-lo, não prova de impossibilidade.

**Furo mecânico na própria proposta de reputação:** a avaliação mútua (funções 74/75) acontece **ao fim do contrato**; a permanência dura 90 dias **depois** disso. Quando o post é removido no dia 40, **a nota já foi dada, publicada e fechada**. "Conta no histórico" existe; "conta na nota" não tem mecânica escrita.

**Quatro alternativas reais** — efeitos completos na resposta ao Marco de 11/09. Nenhuma pode ser escolhida por engenharia.

**Dependência jurídica registrada, sem parecer:** (1) se a relação criador↔plataforma for de consumo (pergunta em aberto, SPEC §15), prometer "direito de disputa" e entregar só registro pode ter leitura diferente de B2B; (2) cobrança do criador depende de parecer (SPEC §4.3 camada 6 e §15); (3) a redação da cláusula de permanência e do que acontece no descumprimento é trabalho de advogado, não nosso.

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
