# BLOCKERS — INFLUENTZ

> Impedimentos reais. Vazio é o estado bom — mantenha assim.

## Bloqueando o próximo passo
Nenhum. As 3 lacunas da `MAQUINA-DE-ESTADOS.md` foram fechadas em 11/09 (§3.2, §9.4, §10.0) — ver `DECISIONS.md`.

## ✅ DECISÃO DO FOUNDER (11/09) — disputa de permanência não move dinheiro no v1

**Decisão registrada, categoria C do protocolo (§2.1) — matar/manter comportamento de produto.**

> A INFLUENTZ não promete devolução financeira à marca por descumprimento do período de permanência **enquanto não existir mecanismo financeiro, antifraude, operacional e jurídico comprovadamente sustentável**. A arquitetura permanece aberta para introduzir isso depois, com dado real — não é abandono definitivo, e "disputa reputacional" não vira regra automática enquanto a linguagem de tela não estiver decidida (ver auditoria de terminologia abaixo).

**Por que D e não A, B ou C:** B foi investigada pelo `financeiro` e classificada **NÃO COMPROVADA** (ver histórico abaixo — defeito estrutural com Pix/boleto sem teto, aritmética de conluio lucrativa, 3 dados ausentes). C está fora do v1 por decisão já travada (SPEC §4.3 camada 6, depende de parecer). A não foi aprovada como decisão final — ver auditoria abaixo, ela também tinha furo mecânico (nota já fechada antes da permanência acabar).

**O que fica preservado para reabrir B no futuro** (as 6 condições já ficam registradas como pré-requisito, não como promessa): medir a taxa real de remoção precoce em produção (o estado `removido_antes_do_prazo` já registra, de graça) · separar produção de veiculação no preço do contrato · teto de devolução independente do teto de cartão · trava contra o par sem histórico · não-cumulação com chargeback do mesmo contrato · fonte de custeio própria, fora do fundo de contestação.

---

## 🔴 AUDITORIA DE TERMINOLOGIA — a palavra "disputa" cobre dois mecanismos diferentes (11/09)

**O pedido do Founder:** a SPEC usa "disputa" e "direito de disputa" de um jeito que pode prometer restituição financeira sem ter como cumprir. Auditoria completa, sem inventar definição nova.

**A promessa exata, e onde está.** MÁQUINA §8.0.3: *"Descumprir gera **registro, cláusula e direito de disputa da marca**; nunca estorno automático."* É a **única** ocorrência de "direito de disputa" em todo o projeto — busca em SPEC, MÁQUINA, PRODUTO-DETALHADO e FEATURE-MATRIX confirma isso.

**O que já está provado, com evidência — três categorias existem de verdade, não quatro:**

| Categoria pedida pelo Founder | Provada? | Evidência |
|---|---|---|
| **Registrar descumprimento** | ✅ Provada | §8.0.3 já diz "gera registro"; a verificação é automática por API (§8.0.3), a marca não precisa relatar nada |
| **Contestar/relatar descumprimento** | ❌ **Não provada como categoria própria** | Não existe, em documento nenhum, um passo em que a marca "relata" a remoção antes de haver disputa — a detecção é automática (varredura de API), não por relato. Tratar isso como 3ª categoria seria inventar. **Não invento.** |
| **Mediação** | ✅ Provada, e é o processo único | §12.2 e funções 80/81: mediação humana com prazo, painel de Trust & Safety. Já é usada tanto para casos com dinheiro em jogo (§8.1: *"criador já começou — mediação, liberação proporcional ao trabalho feito"*) quanto, na minha própria arquitetura de 11/09, para o caso sem dinheiro (permanência) |
| **Disputa financeira** | ✅ Provada, mas com **fronteira exata que eu não tinha marcado antes** | O estado `executada` ("dinheiro movimentado conforme a decisão") só é alcançável enquanto o marco está **financiado e ainda não `aprovado`** — dinheiro em escrow. É exatamente o precedente de §8.1: mediação decide proporção **antes** do dinheiro sair. Depois de `aprovado` (§8.2: dinheiro liberado na publicação), **não há escrow para mover** — é outro mecanismo |

**O achado real, e é meu, não do Founder:** `MAQUINA-DE-ESTADOS.md` §10.0 — escrita por mim em 11/09 — **lista `em_permanencia`/`removido_antes_do_prazo` na mesma tabela e com a mesma palavra ("disputa") que os seis estados pré-liberação**, todos alimentando o mesmo `contrato.em_disputa` e a mesma máquina que tem `executada` como desfecho normal. **Isso conflacionou os dois mecanismos**, e é exatamente o que criava a leitura de "direito de disputa = pode virar dinheiro" para a marca. §10.0.1 já estava marcada `DECISÃO PENDENTE` desde a rodada anterior — a auditoria confirma que a pendência é maior do que uma linha: é a palavra "disputa" fazendo dois trabalhos.

**Proposta de distinção, sustentável com o que já existe — não é definição nova, é nomear a fronteira que a máquina já desenha:**

| Nome proposto | Quando | Pode terminar em dinheiro? | Onde já existe |
|---|---|---|---|
| **Disputa** (sem qualificador) | Marco financiado, ainda não `aprovado` — as seis situações de MÁQUINA §10.0 exceto permanência | Sim — `executada` é desfecho normal | §12.2, §8.1, funções 76/80/81 |
| **Registro de descumprimento de permanência** | Marco `aprovado`, dinheiro já liberado, publicação saiu do ar antes do prazo | **Não, até o Founder decidir o contrário** (esta é a decisão de hoje) | §8.0.3, hoje escrita como "disputa" — proposta é deixar de chamar assim |

🔴 **Isto ainda não está aplicado a nenhum documento.** É proposta, registrada aqui. Aplicar significa reescrever §8.0.3/§10.0/§10.0.1 para parar de usar "disputa"/"direito de disputa" no caso de permanência — e isso é edição de MÁQUINA e SPEC, fora do escopo autorizado nesta rodada ("não alterar telas, não implementar"). Fica para quando o Founder confirmar a distinção.

**Dependências jurídicas identificadas, sem parecer:** (1) se a relação for de consumo (SPEC §15 em aberto), a linguagem "direito de disputa" pode já carregar expectativa de reparação sob o CDC, mesmo sem a palavra "financeira" — é pergunta para o advogado, não decido; (2) a cláusula de permanência em si (o que descumprir "custa" ao criador) é redação jurídica, não nossa; (3) renomear de "disputa" para "registro" no contrato já assinado versus em contratos novos pode ter efeito diferente — não opino.

---

## Histórico — como se chegou à decisão de hoje

**Disputa de permanência: o que ela executa.** Reaberta em 11/09 a pedido do Marco, depois de a perícia documental mostrar que a conclusão anterior não estava comprovada.

**O que está escrito (§8.0.3):** *"Descumprir gera registro, cláusula e direito de disputa da marca; nunca estorno automático."* E o estado `removido_antes_do_prazo`: *"conta no histórico do criador — nunca gera estorno automático."*

**Por que isso não fecha a questão:** a palavra é *automático*. O texto proíbe o estorno que acontece sozinho — **não proíbe estorno decidido por mediação humana**. E a máquina de disputa tem `executada` = *"dinheiro movimentado conforme a decisão"* como desfecho normal; uma disputa que nunca o alcança está usando uma máquina que não foi desenhada para ela.

**Precedente que enfraquece a eliminação anterior:** SPEC §4.3(b) já resolve o caso "dinheiro já saiu e a marca tem direito" — *"a plataforma não debita o criador: paga o fundo de contestação"*. O mecanismo existe e já é usado; dizer que o fundo não serve aqui é argumento para redimensioná-lo, não prova de impossibilidade.

**Furo mecânico na própria proposta de reputação:** a avaliação mútua (funções 74/75) acontece **ao fim do contrato**; a permanência dura 90 dias **depois** disso. Quando o post é removido no dia 40, **a nota já foi dada, publicada e fechada**. "Conta no histórico" existe; "conta na nota" não tem mecânica escrita.

**Hipótese B investigada pelo `financeiro` (11/09) — resultado: NÃO COMPROVADA.** Três motivos, e o terceiro independe de qualquer dado futuro:

1. **Falta o dado que decide.** A taxa de remoção precoce (`r`) não existe em documento nenhum — e é ela que separa "cabe em R$ 91/mês" de "drena o principal em 17 meses". Sem `r` só existe fórmula: `E_mensal = N × p_perm × r × ticket × f̄`. Ponto de equilíbrio no lançamento: `p_perm × r × f̄ ≤ 0,379%`.
2. **Falta a estrutura de preço.** Nenhum documento separa quanto do preço é produção (já entregue, irreversível) e quanto é veiculação. Sem isso, devolução proporcional devolve trabalho feito.
3. 🔴 **Defeito estrutural, verdadeiro para qualquer valor de `r`.** O piso do fundo é `2 × maior teto de cartão`. Pix e boleto não têm teto por decisão travada. **A fórmula do piso não contém variável capaz de enxergar a exposição de B.** Um contrato de R$ 30.000 por Pix — que é a rota que a SPEC §4.3.1 construiu de propósito para o cliente grande — expõe R$ 30.000 contra um fundo de R$ 5.000. Aumentar o aporte não corrige: qualquer aporte finito é superado pelo contrato seguinte.

🔴 **E o achado que sozinho reprova B como está escrita — a aritmética do conluio, conferida nesta sessão:** contrato de R$ 1.200, a marca paga R$ 1.260 (preço + 5%), o criador recebe R$ 1.080 (preço − 10%). Publica, remove no dia 1, B devolve à marca. **O par desembolsou R$ 1.260 e recebeu R$ 2.340 — lucro de R$ 1.080 por ciclo, saído do fundo, em 24 horas.** Com Stories o ciclo dura uma hora. **Não é caso de borda: é o resultado dominante da regra.** O freio natural seria cobrar o criador, e isso está fora do v1 (SPEC §4.3 camada 6).

**Red team: 7 de 12 casos não cobertos.** Dois são perda direta de caixa sem freio escrito: (a) marca recebe devolução do fundo **e depois** abre chargeback do mesmo contrato — a plataforma paga duas vezes, e nada impede; (b) conta do criador suspensa pela rede derruba N posts de uma vez — um evento, N devoluções simultâneas, sem má-fé de ninguém.

**Dano colateral não escrito em lugar nenhum:** o fundo é obrigado a repor saldo negativo **no mesmo dia útil** para não travar saque de criador inocente (§4.3 camada 5). B cria um consumidor concorrente acionável pela vontade de um terceiro. **Fundo drenado por remoção de post = saque de criador inocente travado.**

**As 6 condições objetivas que tirariam B de NÃO COMPROVADA:** medir `r` em produção antes de prometer em tela (o estado `removido_antes_do_prazo` já registra — o instrumento existe e é grátis) · congelar no contrato o percentual que é veiculação · teto de devolução que não dependa do teto de cartão, **visível ao pagar** · trava contra o par conluiado que não seja cobrança do criador (candidata: carência para par sem histórico) · regra de não-cumulação com chargeback do mesmo contrato · fonte de custeio própria, separada do fundo.

⚠️ **Se B avançar, falta ainda o `antifraude`** — o vetor de conluio foi achado pelo `financeiro` de passagem; a revisão dedicada não foi feita.

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
