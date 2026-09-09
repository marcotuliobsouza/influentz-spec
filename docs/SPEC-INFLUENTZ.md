# SPEC — INFLUENTZ

> **O que é este documento.** A fonte da verdade do produto. Toda tela, toda tabela do banco de dados, todo fluxo de pagamento aponta de volta para aqui. Quando algo mudar na visão do produto, muda aqui primeiro — e só depois no código.
>
> **Versão:** v0.5
> **Status:** as 8 decisões de produto que estavam em aberto foram travadas. Provedor de pagamento corrigido de Stripe Connect para Pagar.me.
>
> **O que mudou da v0.4:** correção jurídica em §8.3.1 — criador menor de idade exige **alvará judicial** (ECA art. 149 + Lei nº 15.211/2025), não só assinatura do responsável. Consequência: **18 anos completos** para criar no v1. Ver também `MAQUINA-DE-ESTADOS.md`, que traduz esta SPEC em regras de funcionamento e corrigiu seis lacunas dela.
>
> **Legenda:** 🟢 direção definida · 🟡 decisão em aberto · 🔵 proposta de Claude além do que foi pedido · 🔴 lacuna crítica · ⚠️ precisa de profissional humano

---

## 0. Como Claude trabalha neste projeto 🟢

- A fala do Marco é matéria-prima, não a especificação final. Verificar, comparar com o mercado, ir além do pedido literal.
- Nunca aceitar uma solução só por ser a mais fácil de implementar.
- Ao tocar num módulo, pensar nele como sistema completo, incluindo as bordas que um não-técnico não teria como prever.
- Nenhuma ferramenta entra sem o checklist de 5 perguntas do `CLAUDE.md` §3 respondido de antemão.
- Toda decisão relevante vem com fonte.

---

## 1. Visão do produto 🟢

**INFLUENTZ** é um marketplace que conecta três tipos de participante:

- **Marcas** (`brand`) — empresas que contratam divulgação, conteúdo ou presença.
- **Criadores** (`creator`) — influenciadores, palestrantes, médicos-influenciadores, especialistas. Qualquer pessoa que gera conteúdo ou presença de marca — remoto, presencial ou híbrido.
- **Agências** (`agency`) — representam e gerenciam marcas **e/ou** criadores, mediante convite aceito pelos dois lados.
- **Equipe INFLUENTZ** (`admin` / `staff`) — detalhado na seção 7.

A plataforma existe para que uma marca encontre o criador certo por categoria/nicho (moda e beleza, tecnologia, saúde, etc.), contrate, pague, acompanhe a entrega e resolva qualquer problema no caminho — tudo dentro da plataforma, com segurança jurídica para as duas pontas.

---

## 2. Papel da agência 🟢

A agência **gerencia**, mas quem assina e quem recebe/paga é sempre a marca ou o criador. **A agência nunca toca no dinheiro.**

Motivo: se a agência recebesse e repassasse valores de terceiros, ela passaria a exercer atividade de instituição de pagamento perante o Banco Central — obrigação regulatória que não faz sentido impor a um cliente da plataforma.

🔵 **Autonegociação:** se o mesmo CPF/CNPJ aparecer do lado da agência **e** do criador/marca representado, o sistema sinaliza para revisão manual antes de liberar qualquer benefício.

**Escopo de agência no lançamento** (decisão 7): a agência já entra no v1 em versão enxuta — espaço próprio para agrupar seus criadores e marcas sob um login. Fica para depois: permissões refinadas por membro da equipe da agência e faturamento consolidado entre várias marcas representadas.

*Justificativa da mudança:* a hipótese anterior era adiar agências inteiras. Foi revertida porque agências são justamente o público que hoje sofre com gestão manual e sem workspace — sem um motivo para entrar no dia 1, elas permanecem com seus grupos próprios de criadores fora da plataforma.

---

## 3. Como a contratação é estruturada 🟢

**Modelo híbrido** (decisão 1):

- **Vitrine com preço fixo** — o criador publica um "cardápio" de entregas padronizadas (ex.: *1 Reels — R$ 800*; *3 Stories — R$ 300*; *1 hora de palestra remota — R$ 1.500*). A marca contrata direto, sem negociar.
- **Pedido aberto com proposta** — para campanhas maiores ou fora do padrão, a marca publica briefing e os criadores enviam proposta.

*Por quê os dois:* vitrine reduz atrito e ajuda criador iniciante a vender sem saber negociar; pedido aberto sustenta contratos grandes, onde preço fixo não cabe. É o padrão usado por marketplaces de serviço consolidados (Workana, 99Freelas operam pedido aberto; Fiverr opera vitrine — cada um perde metade do mercado por não ter o outro).

### 3.1 Proposta como menu, não texto livre 🟢

Os termos comerciais são **campos estruturados**, não texto solto. Isso elimina ambiguidade na hora da disputa e aumenta o ticket médio, porque cada campo tem preço implícito. Ver seção 8.2.

---

## 4. Dinheiro 🟢

### 4.1 Provedor de pagamento: Pagar.me

⚠️ **Correção em relação às versões anteriores.** A SPEC nascera apontando para *Stripe Connect*.

- A Stripe internacional libera **Pix para empresa brasileira apenas por convite** e **não oferece parcelamento de cartão no Brasil**. Fonte: https://docs.stripe.com/payments/pix
- O **Pagar.me** (adquirido pela Stripe/Stone) cobre Pix, boleto, cartão parcelado e divisão automática (split) nativa para o Brasil.

**Como funciona por dentro** (checklist do `CLAUDE.md` §3):

1. **Quem guarda o dinheiro:** o Pagar.me. A INFLUENTZ não constrói carteira própria e o dinheiro não passa pela conta da plataforma.
2. **Quem tem conta:** cada criador e cada marca vira um *recebedor* dentro da conta Pagar.me da INFLUENTZ — basta CPF/CNPJ e conta bancária. **O usuário não cria conta no Pagar.me.** Fonte: https://docs.pagar.me/docs/recebedores-2
3. **Testes sem CNPJ:** sim. Conta de teste liberada só com e-mail; chaves de produção exigem CNPJ depois. Fonte: https://docs.pagar.me/v4/docs/getting-started
4. **Split:** o valor já nasce dividido no momento do pagamento — a plataforma não recebe tudo para repassar depois. Isso também evita bitributação sobre o valor que nunca foi receita da plataforma.

### 4.2 Meios de pagamento aceitos

| Meio | Aceito no v1 | Quando o dinheiro fica disponível | Pode voltar? |
|---|---|---|---|
| **Pix** | Sim | Na hora, inclusive dentro do split | ⚠️ **Sim, por fraude — e desde 02/02/2026 é mais severo.** Ver §4.2.2, o MED 2.0. **Não cobre desacordo comercial** — qualidade, atraso e arrependimento ficam de fora |
| **Boleto** | Sim | 1 a 2 dias após confirmação | **Não.** É o único meio realmente irreversível |
| **Cartão de crédito** | Sim, para qualquer marca verificada — **CPF ou CNPJ** | **À vista: D+30.** ⚠️ **Parcelado: uma parcela por mês** — D+30, D+60, D+90… uma para cada parcela que a marca escolher, salvo antecipação | Sim — janela de 75 a 540 dias, conforme a bandeira e o motivo |

*Por que cartão entra:* ambiente corporativo usa cartão intensamente. Excluí-lo eliminaria uma fatia relevante da demanda.

### 4.2.4 Parcelamento — duas regras, e a que vale hoje é a B 🔴

🔴 **A descoberta que reorganiza esta seção.** A tabela de 4,19% à vista e 13,63% em 6×, com recebimento em 1 dia, é do plano **Essencial** — **e o Essencial não tem split de pagamento**. A INFLUENTZ é marketplace com recebedores, logo é cliente do plano **Flex**, cujas taxas são **customizadas e não publicadas**. E o próprio site avisa: *"para novos vendedores... pode ser retido por até 15 dias por questões de análise. A opção de receber na hora fica disponível automaticamente assim que você constrói um histórico de vendas."* ([pagar.me/ofertas](https://www.pagar.me/ofertas))

**Traduzindo:** a data única em que a regra de parcelamento se apoiava (a) vinha de um plano que não serve para nós e (b) **não existe para conta nova em plano nenhum**.

⚠️ **E a antecipação também não existe no dia 1.** A antecipação pontual só pode ser pedida *"depois de 60 dias transacionando cartão de crédito"*; os modelos automáticos são liberados *"de acordo com o volume transacional existente"*; e mesmo com modelo aprovado, *"a solicitação pode ser negada"* em caso de desvio ou alto índice de chargeback ([Central de Ajuda](https://pagarme.helpjuice.com/pt_BR/antecipa%C3%A7%C3%A3o-como-funcionam-os-modelos-de-antecipa%C3%A7%C3%A3o)). Valor mínimo, máximo e limites: **não publicados em lugar nenhum.**

---

#### 🟢 REGRA B — sem antecipação. **É a que vale hoje.**

| Meio | Regra do v1 |
|---|---|
| **Pix** | Sem teto. Dinheiro do criador **no mesmo dia** da publicação confirmada |
| **Boleto** | Sem teto. Compensa em 1 a 2 dias úteis |
| **Cartão** | **Somente à vista.** Teto de R$ 2.500 (degrau 0) ou R$ 15.000 (KYB) |
| **Cartão parcelado** | ❌ **Não existe. O botão não aparece** — não é "indisponível", simplesmente não é oferecido |
| **Data do criador no cartão** | **D+30 da cobrança**, exibida em dia e mês, nunca como sigla ⚠️ Premissa até o contrato Flex confirmar. Se vier melhor, o criador recebe antes — **nunca depois do prometido** |
| **Ticket alto** | Marcos + Pix, ou Fatura INFLUENTZ em boleto (§4.3.1.2) |

**O que o criador vê ANTES de aceitar** — e esta tela não existia:

> **Você vai receber R$ 1.080**
> *(R$ 1.200 do seu preço, menos 10% de comissão)*
>
> 🟢 **Esta marca vai pagar por Pix.** Disponível **no mesmo dia** em que sua publicação for confirmada.
> 🟡 *Boleto* — disponível **2 dias úteis** depois. · 🟡 *Cartão* — disponível em **12 de outubro**; o dinheiro do cartão só existe 30 dias depois da compra, e isso é regra do sistema de cartões, não nossa.
>
> `Aceitar` · `Recusar`

🔴 **Duas regras de redação inegociáveis:** a data aparece **antes** do botão de aceitar. E **"aprovado" nunca aparece sozinho** — sempre "aprovado, disponível em 12/10". São dois fatos diferentes e a tela nunca funde os dois.

#### 🟡 REGRA A — com data única. **Escrita, e desligada.**

Liga por **uma chave no painel administrativo, sem uma linha de código nova**, quando chegarem três respostas **por escrito**:

1. Qual é a taxa do **plano Flex com split** para a nossa conta.
2. Se existe **data única** para venda parcelada nessa configuração, e a partir de qual histórico.
3. **Quem é debitado da taxa de antecipação** — o marketplace ou o recebedor. Se a resposta for "o recebedor", **a Regra A morre na origem**: ela violaria a regra de que o criador não paga antecipação.

Quando ligada: cartão 2× a 12×, parcela mínima R$ 200, **juros de 1,99% ao mês pagos pelo comprador**, calculados e **congelados na criação do contrato** junto com a comissão, split do criador em **valor fixo** (nunca percentual — senão o juro contamina a base dele).

⚠️ **E o teto muda junto:** no parcelado, o teto por cobrança é **metade** do teto do degrau (R$ 1.250 no degrau 0, R$ 7.500 no KYB), porque **a contestação de uma venda parcelada atinge a transação inteira, e a janela de risco só começa a contar depois da última parcela**. Parcelar não dilui risco: **alonga**.

**A arquitetura que faz as duas conviverem:** duas chaves no Admin (`parcelamento_habilitado` e `data_unica_confirmada`), ambas nascendo desligadas, e **um único ponto no código** que decide quantas parcelas mostrar. Ligar é um clique, não um lançamento de versão.

🔴 **O que a Regra B quebra para um cliente legítimo, dito sem maquiar:** a marca média — R$ 3.000 a R$ 8.000, agência pequena, e-commerce em crescimento — que queria dividir em 3× **não vai poder**. É cliente bom, e alguns vão embora. **A compensação é real e precisa estar na tela:** marcos com Pix resolvem o mesmo problema de caixa, espaçados pela entrega, com **custo zero** contra 6% a 13% de juros; e o boleto de 30 dias dá o mesmo fôlego. O cliente grande não é afetado — ele já ia por boleto.

⚠️ **Regra de ouro contra risco de falência:** a plataforma **nunca adianta dinheiro que ainda não recebeu do provedor.** Uber e iFood adiantam ao motorista/restaurante com capital de giro próprio — copiar isso sem caixa é emprestar dinheiro inexistente. O criador vê no app a data exata em que cada valor vira saldo disponível.

### 4.2.2 MED 2.0 — o Pix mudou em 02/02/2026 🔴

> **Revisado pelo especialista `antifraude`.** Isto corrige uma frase que estava travada como decisão: *"chargeback só existe no cartão"*.

**A frase correta é:** *reversão por **desacordo comercial** só existe no cartão; o Pix tem reversão por **fraude**, com janela curta e **bloqueio antes da análise**.*

A Resolução BCB 493/2025, obrigatória desde **02/02/2026**, mudou o Pix recebido:

| O que mudou | Consequência para nós |
|---|---|
| **Bloqueio cautelar do saldo do recebedor por até 72 h** a partir da notificação de fraude | O banco **bloqueia primeiro e analisa a boa-fé depois** |
| Rastreio em **até 5 camadas** de contas seguintes | Dinheiro de golpe que passou por outra conta antes **alcança o nosso recebedor** |
| Convertido em devolução, a conta pode ser **monitorada por 90 dias**, retendo créditos novos | O criador pode ficar sem receber por um fato que ele não praticou |
| O recebedor pode ser **marcado como fraudador** mesmo sem devolução | Sujar o nome de um criador inocente |

🔴 **Por que isso é nosso e não do provedor:** no split, **o criador é um recebedor**. Uma marca que pague com Pix de dinheiro sujo pode **congelar o saldo do criador**, e ele não tinha como saber.

⚠️ **O relógio é muito pior que o do cartão:** no cartão são 10 dias para defender; no MED são **72 horas de bloqueio**. Vira item da caixa de entrada do operador com prioridade máxima: *"bloqueio cautelar de Pix — responder hoje"*.

✅ **O que NÃO muda:** o teto continua sendo só do cartão. O MED **exclui expressamente desacordo comercial**, então não é chargeback disfarçado e não justifica limite no Pix.

🟢 **E isto reforça a Fatura INFLUENTZ (§4.3.1.2):** o **boleto é o único meio verdadeiramente irreversível** — uma vantagem que a seção nem reivindicava.

### 4.2.3 Devolução de Pix vai para a conta de origem, e isso encolhe uma função 🔴

**Fato:** a devolução nativa do Pix **só pode ser feita para a mesma conta que originou o pagamento**, dentro de **90 dias**. O Banco Central não permite devolver para outra chave.

🔴 **Isso fecha uma rota de lavagem que o nosso próprio desenho estava abrindo.** A função de "dados de reembolso no checkout" deixava a marca informar **uma conta diferente** da que pagou. O golpe seria: pagar R$ 20.000 por Pix, apontar outra conta para reembolso, cancelar dentro da janela — **e sair dinheiro limpo por outra conta, sem contrato nenhum, com a plataforma bancando o trajeto.**

✅ **Regra corrigida:**

- Para Pix dentro de 90 dias, **não se pede dado nenhum** — o caminho de volta já vem junto com o dinheiro.
- A função sobrevive **só para boleto** (que não tem devolução nativa) **e para Pix fora dos 90 dias**.
- Onde ela existir, **a conta de reembolso tem que ter o mesmo CPF ou CNPJ do pagador**.
- **Reembolso para titularidade diferente nunca é automático** — cai na caixa de entrada.

**O que quebra para um cliente legítimo:** quase nada, e na verdade melhora — **menos campos no checkout do Pix**. O caso real que sofre é a empresa que paga pela matriz e quer receber na filial: vira uma revisão de um dia útil, e é raro.

### 4.2.1 Quem pode usar a plataforma 🟢

🔴 **Nenhum usuário precisa de CNPJ para usar a INFLUENTZ.** Nem criador, nem marca.

| Quem | O que precisa | Por quê |
|---|---|---|
| **Criador** | CPF, identidade verificada e conta bancária | O provedor de pagamento aceita recebedor pessoa física. Exigir empresa do criador cortaria a maior parte do mercado — e a atividade dele nem cabe no MEI (§4.7) |
| **Marca** | CPF **ou** CNPJ, identidade verificada | Quem contrata criador não é só empresa grande: é loja de bairro, profissional autônomo, dentista, personal trainer, restaurante, marca pessoal. **Exigir CNPJ da marca cortaria fora boa parte da demanda que sustenta o lançamento** |
| **Agência** | CNPJ | Ela contrata em nome de terceiros; representar alguém exige pessoa jurídica. Fica para depois do v1 |

**O CNPJ é obrigação da INFLUENTZ, não dos usuários.** A plataforma precisa de empresa aberta porque o provedor de pagamento só libera produção assim, e porque quem intermedia dinheiro de terceiros responde por isso. Isso não se transfere para quem usa.

⚠️ **O que a verificação de CNPJ da marca faz, quando existe:** ela não é porta de entrada — é **degrau de limite**. Empresa com documentação verificada entra em R$ 15.000 no cartão no primeiro dia (§4.3.1.1). Marca pessoa física começa no degrau normal e sobe por histórico, como em qualquer plataforma.

### 4.3 Proteção contra contestação de compra (chargeback)

🔴 **Princípio travado: o criador nunca espera mais do que o prazo do meio de pagamento.** Reter dinheiro do criador para cobrir risco de terceiro transfere a ele um custo que é da plataforma.

**A proteção vem de sete camadas, todas antes do repasse:**

| # | Camada | O que é |
|---|---|---|
| 1 | **3D Secure sempre tentado, nunca obrigatório** | Autenticado, a responsabilidade por fraude passa ao banco emissor. Mas **3DS não pode ser pré-requisito absoluto:** cartão corporativo circula por processos B2B dedicados, cai em isenção de autenticação, e muitos sequer estão inscritos no protocolo — exigir 3DS de todos recusaria o cliente grande. E **isenção não é transferência de responsabilidade:** quando o lojista pede a isenção, o risco continua com ele. Regra: 3DS é tentado sempre; sem autenticação, o cartão só passa **dentro do teto verificado**, e o checkout oferece boleto e Pix **antes**. A trilha (§4.11) grava o desfecho — autenticado, tentado, isento ou falhou — porque a defesa de chargeback depende disso |
| 2 | **Teto por transação — só no cartão** | 🔴 **Pix e boleto não têm teto.** O que se limita é exposição a chargeback, e **chargeback só existe no cartão**. Ver §4.3.1: R$ 2.500 para marca nova e anônima, **R$ 15.000 na hora para empresa verificada (KYB)**, e sem teto por Pix ou boleto em qualquer caso |
| 3 | **Dossiê de defesa — os dados, e o alarme** | O que precisa existir são os **dados**: contrato congelado, aceite bilateral com data, hora e IP, comprovante de que o marco foi financiado antes do início, arquivos de entrega datados, aprovação registrada, log do chat e a nota fiscal do criador. Todos já vivem no registro de auditoria, e o dossiê se monta a partir deles. **Não existe gerador automático de PDF:** com um chargeback a cada ~20 meses, seria um robô para um evento que acontece duas vezes por década. **O que existe é o alarme:** o prazo de defesa é de **10 dias corridos e é fatal** ([Pagar.me](https://pagarme.helpjuice.com/pt_BR/sobre-o-pagarme/faq-chargeback)), então vira tarefa com contagem regressiva na caixa de entrada. Perder por silêncio é o único erro imperdoável aqui |
| 4 | **A INFLUENTZ é a responsável declarada** | No split do Pagar.me, `liable` e `charge_processing_fee` são **`true` no recebedor da plataforma e `false` no recebedor do criador, sempre explícitos**. ⚠️ O padrão do provedor joga a responsabilidade no **primeiro recebedor da lista** — depender de ordem de array é acidente esperando acontecer. Fonte: [docs.pagar.me — Split](https://docs.pagar.me/v3/docs/split-rules) |
| 5 | **Fundo de contestação** | 🔴 **Saldo negativo na conta do provedor pode travar o saque de outros criadores que não têm nada a ver com o caso** — o dano vira coletivo e reputacional. Por isso o fundo repõe o saldo negativo **no mesmo dia útil, automaticamente, com alarme**; não é tarefa de fim de mês. **5% da receita de comissão** em **conta bancária separada do CNPJ** — não linha de planilha; dinheiro que só existe em relatório é dinheiro que já foi gasto. Paga os chargebacks perdidos. É a plataforma retendo o dinheiro **dela**. Invisível para o criador. ⚠️ **No lançamento o fundo acumula R$ 90/mês** (5% de R$ 1.800) e **não cobre um chargeback de R$ 2.500 no primeiro ano.** O fundo não é a proteção do lançamento — **o teto da camada 2 é.** O fundo passa a fazer sentido na operação (5% de R$ 180.000 = R$ 9.000/mês) |
| 6 | **Cobrança do criador só com decisão humana** | Chargeback perdido **não** vira dívida do criador automaticamente. Só há cobrança em conluio comprovado ou entrega inexistente, com motivo, autor e data registrados. Fora disso, é custo da plataforma |
| 7 | **Pix como meio padrão** | Pix em destaque no checkout ("dinheiro liberado na hora para o criador"). Cartão é a segunda opção — reduz o volume exposto sem perder a venda de ticket alto |

📊 **A parte honesta, agora com número.** Premissas declaradas: ticket médio R$ 1.200, 40% do GMV em cartão, taxa de chargeback de 0,6% (referência de mercado brasileiro), e 60% dos chargebacks sendo fraude pura — coberta pelo 3DS.

| | Lançamento (20 contratos/mês) | Operação (1.000 contratos/mês) |
|---|---|---|
| GMV | R$ 24.000 | R$ 1.200.000 |
| Perda esperada após 3DS | R$ 23/mês | R$ 1.152/mês |
| Receita de comissão | R$ 1.800 (7,5%) | R$ 180.000 (15%) |
| **Perda ÷ comissão** | **1,3%** | **0,64%** |

🔴 **A conclusão que muda a medida certa: a perda média sempre coube na comissão. Ela nunca foi o problema.** O problema é **concentração**. Com 20 contratos por mês, um único chargeback de R$ 1.200 consome dois terços da comissão do mês, e um contrato de R$ 20.000 contestado apaga onze meses de receita. Não existe lei dos grandes números com 20 contratos. **Por isso a medida certa é teto de exposição por transação (camada 2), e não retenção no tempo** — segurar 90 dias protegia contra a média, que já cabia, e não protegia contra o caso isolado, que é o que mata.

⚠️ **Nem a Garantia de Chargeback nem o antifraude vêm inclusos** no produto padrão do Pagar.me — os dois são contratados à parte, e a Garantia cobre **apenas fraude**, não desacordo comercial. Entram quando o volume de cartão justificar o custo fixo; até lá, o 3DS é a camada 1. Fontes: [Garantia de Chargeback](https://conteudo.stone.com.br/garantia-de-fraude/), [Antifraude ClearSale](https://pagarme.helpjuice.com/pt_BR/antifraude-clearsale).

⚠️ **Pré-autorização não serve de escrow.** A janela de captura no Pagar.me é de 5 horas (checkout) ou 5 dias (API) — depois disso o emissor libera o valor. A ideia de "só capturo o cartão quando a entrega for aprovada" não funciona: o escrow tem que ser com dinheiro capturado. Fonte: [docs.pagar.me — Autorização e captura](https://docs.pagar.me/v3/docs/autoriza%C3%A7%C3%A3o-e-captura).

📌 **O que as plataformas comparáveis fazem:** a **Fiverr** debita do saldo do freelancer e só o protege "a seu exclusivo critério". A **Upwork** briga com o banco e preserva o pagamento do freelancer, desde que o fluxo dela tenha sido seguido. **Nenhuma das duas retém 90 dias do prestador.** E na Stripe Connect, no modelo que a INFLUENTZ usa, **a plataforma é sempre a responsável final** — isso não é escolha generosa, é como o sistema de cartão funciona. Fontes: [Stripe — Disputes on Connect platforms](https://docs.stripe.com/connect/disputes), [Fiverr](https://help.fiverr.com/hc/en-us/articles/360010978618-Chargebacks-and-freelancer-protection), [Upwork](https://support.upwork.com/hc/en-us/articles/14085353385747-What-happens-if-you-file-a-chargeback-as-a-client-on-Upwork).

### 4.3.1 O teto do cartão, e as duas portas para o cliente grande

> **Pix e boleto não têm teto. O que se limita é exposição a chargeback, e chargeback só existe no cartão.**

> *"se uma empresa como COCA COLA usar nossa plataforma e serviço for 30.000 reais a contratação do creator, ela nao vai poder... se limitar, nao teremos clientes pra creators e vice versa"*

**E a pesquisa mostrou que ele estava ainda mais certo do que parecia: o contrato de R$ 30.000 nunca foi um problema de cartão.** Empresa grande no Brasil paga fornecedor por **boleto, TED ou Pix contra nota fiscal**, dentro do contas-a-pagar. O obstáculo real não era o teto — **era a SPEC não ter rota corporativa nenhuma.**

**O número não foi escolhido, foi derivado.** Duas restrições, das premissas já registradas (ticket médio R$ 1.200; 20 contratos/mês; comissão de lançamento 7,5% = R$ 1.800/mês):

- **Piso:** o teto não pode morder o caso normal. Dois tickets médios = **R$ 2.400**.
- **Teto:** nenhuma perda isolada pode consumir mais de 1,5 mês de comissão = **R$ 2.700**.

A interseção é R$ 2.400–2.700. **R$ 2.500 cai dentro; R$ 3.000 cai fora** (1,67 mês) — a sugestão anterior estava alta.

**Frequência esperada:** com 0,6% de chargeback e 40% do GMV em cartão, é **um chargeback a cada ~20 meses**. Mesmo errando por 5×, um a cada 4 meses. R$ 2.500 a cada 4 meses é absorvível sem capital; **R$ 20.000 não é — e é essa que o teto impede.**

| Degrau | Condição de subida | Por cobrança | 24 h | 30 dias |
|---|---|---|---|---|
| **0 — marca nova** | Identidade verificada (CPF ou CNPJ) + 3DS autenticado | **R$ 2.500** | R$ 5.000 | R$ 10.000 |
| 🟢 **V — Verificada (KYB)** | **Sem histórico, sem espera** — ver §4.3.1.1 | **R$ 15.000** | R$ 30.000 | R$ 60.000 |
| **1** | 2 contratos concluídos sem incidente **e** 30 dias | R$ 6.000 | R$ 12.000 | R$ 24.000 |

🔴 **A escada tem um piso de valor, senão ela é escalada com contratos de fachada.** Dois contratos de R$ 100 não podem subir uma marca de R$ 2.500 para R$ 6.000. **Um contrato só conta para subir de degrau se valer pelo menos 20% do teto do degrau seguinte** — e **contrato entre partes relacionadas não conta nunca**, para nada: nem degrau, nem recontratação de 8%, nem avaliação pública.

| **2** | 5 contratos concluídos sem incidente **e** 90 dias | R$ 15.000 | R$ 30.000 | R$ 60.000 |
| **3** | 10 contratos, 180 dias, **e ≥5 deles já fora da janela de 120 dias de contestação** | sem teto automático | — | — |
| **Sempre** | qualquer cobrança acima de **R$ 30.000** | revisão humana, resposta em 1 dia útil | — | — |

🔴 **Por que a contagem é dupla — contratos E dias.** A MAQUINA §7.2 já achou que contador de contratos sozinho é porta de fraude: dois contratos de R$ 1 destravariam o degrau. **Tempo não se falsifica** — e tempo é a dimensão certa do risco, porque a contestação por serviço não recebido conta 120 dias da data prevista de entrega. **Uma marca só está realmente provada quando os contratos antigos dela passaram da janela de disputa** — por isso o degrau 3, o único sem teto, exige exatamente isso.

**Step-up, independente da escada:**

| Gatilho | Ação |
|---|---|
| Cartão emitido fora do Brasil | Revisão manual sempre, em qualquer degrau |
| Cartão pré-pago | Bloqueado no degrau 0 |
| Mesmo cartão em dois CNPJs | Revisão manual |
| Chargeback **aberto** (ganho ou perdido) | Rebaixa um degrau, congela subida por 90 dias. ⚠️ **Não se aplica automaticamente a conta KYB** — vira revisão humana. Uma contestação de um cartão corporativo entre milhares não pode zerar a conta da Coca-Cola |
| Chargeback **perdido** | Volta ao degrau 0 (conta KYB: revisão humana) |

⚠️ **Duas coisas que, se não estiverem explícitas, o código erra:**

1. **O teto incide sobre o valor cobrado no cartão, já com os juros do parcelamento** — não sobre o valor do contrato.
2. **"Cartão emitido fora do Brasil → revisão manual" tem exceção para conta KYB.** Multinacional paga com cartão emitido fora; tratar isso como suspeita é recusar o cliente que a plataforma mais quer.

### 4.3.1.1 Conta Empresarial verificada (KYB) — a porta que faltava 🟢

O mercado não resolve o cliente grande com **espera**; resolve com **verificação**. Upwork e Fiverr Enterprise só liberam faturamento consolidado para empresa aplicada e verificada.

| Requisito | Por quê |
|---|---|
| CNPJ ativo + contrato social/estatuto + quadro de sócios | prova quem é |
| Signatário com poderes comprovados | prova que quem aceitou podia aceitar |
| E-mail em domínio corporativo próprio, validado | corta conta descartável |
| Contrato-quadro assinado eletronicamente pelo próprio titular | vira prova documental |
| Consulta a listas restritivas, gravada na trilha | é o controle que a §4.11 apontou como faltante |

**Efeito: entra direto em R$ 15.000 por cobrança no cartão, sem histórico e sem esperar 90 dias.** Acima disso, revisão humana com resposta em 1 dia útil — e a revisão é **do valor no cartão, nunca do contrato**: Pix e boleto seguem livres.

- **O que protege:** chargeback de fraude pura pressupõe cartão anônimo. Com CNPJ validado, contrato assinado, aceite datado com IP e nota fiscal, o caso migra de "fraude" para "desacordo comercial" — onde a reversão a favor do lojista **com prova de entrega passa de 70%**, contra 15–45% na média. **O dossiê muda a probabilidade de ganhar, não a de acontecer.**
- **O que quebra para um cliente bom:** cerca de dez minutos de envio de documentos, uma vez. Em troca, ele nunca vê a palavra "recusado".

### 4.3.1.2 Fatura INFLUENTZ — a rota que realmente atende R$ 30.000 🟢

1. Contrato fechado → a plataforma emite **pró-forma** com dados da marca, criadores, escopo e valor final.
2. A marca recebe **boleto** (ou Pix com vencimento) no prazo que o contas-a-pagar dela pede — 7, 14, 21 ou 30 dias. Boleto acima de R$ 2.000 é registrado, **entra no DDA da empresa** e cai no fluxo normal dela.
3. **O contrato só sai de `aguardando_pagamento` quando o boleto compensa.** O criador só é acionado depois.
4. Nota fiscal: do criador pelo serviço, da INFLUENTZ pela comissão.

- **O que protege:** boleto é o único meio verdadeiramente irreversível. **Zero exposição de chargeback num contrato de R$ 30.000** — é a proteção mais forte do inventário inteiro, e é a que o cliente grande naturalmente prefere.
- **O que quebra para um cliente bom:** o prazo de faturamento vira espera do criador. Por isso a tela dele mostra **a data prevista de compensação antes de aceitar**, e o contrato não começa antes de pagar. Ele nunca trabalha de graça.

**O que não copiamos do Upwork: faturar depois da entrega (net 30).** Só funciona com capital de giro — ou a plataforma adianta dinheiro que não recebeu (proibido pela §4.2), ou o criador espera mais que o meio de pagamento (proibido pela §4.3). **Fora do v1, e o motivo é o caixa, não a engenharia.**

❌ **Garantia de chargeback contratada: não.** Ela cobre só fraude, é paga à parte, e comprá-la para a faixa alta é pagar por um risco que a Fatura INFLUENTZ **elimina de graça** — em boleto não existe chargeback.

⚠️ **Limite de horário do Pix, que não é nosso e nos atinge:** o Banco Central não impõe teto diurno, mas **das 20h às 6h o teto por transação é R$ 1.000**, e cada banco define o seu. Consequência de produto: **cobrança Pix de valor alto é agendada para horário comercial, e a tela avisa.** Um R$ 30.000 tentado às 21h falha por um motivo que não é nosso.

**§4.3.2 — as duas telas que faltavam.** O roteiro existia só para o degrau 0. **Regra de redação: o teto do cartão nunca aparece antes de Pix e boleto aparecerem** — o roteiro antigo abria pela restrição em vez de abrir pela solução.

> **Contrato R$ 30.000, marca nova.** O cartão nem é oferecido como principal:
> *"Boleto ou Pix — R$ 30.000, valor integral, sem limite. É como a maioria das empresas paga contratos deste porte."* · `[Preciso de boleto com vencimento em 30 dias →]`
> **A palavra "limite" não aparece.**

> **Contrato R$ 30.000, marca verificada (KYB):**
> *"Cartão até R$ 15.000 por cobrança · Boleto e Pix sem limite"* · `[Dividir em 2 marcos]` · `[Pedir análise para pagar tudo no cartão — resposta em 1 dia útil]`

**Precedentes de mercado:** Banco Central (Res. BCB 142/2021 — dispositivo novo: R$ 200 por operação, R$ 1.000/dia, aumento não automático) · PayPal (conta nova retida até 21 dias, revisão a cada 30 dias) · Upwork (conta bancária só após US$ 1.000 gastos em 12 meses) · Mercado Pago (análise mensal recorrente) · [Stripe Radar](https://docs.stripe.com/radar/rules) (revisar acima de US$ 1.000 em pré-pago; 3DS para cliente novo). **O padrão é unânime: teto duro sem histórico, subida por comportamento provado, revisão periódica e porta manual.**

### 4.3.2 O que a marca vê — e a palavra "recusado" nunca aparece

Contrato de R$ 4.800, marca no degrau 0:

> **Cartão de crédito** — até R$ 2.500 por cobrança nesta conta
> Seu contrato é de R$ 4.800. Dois caminhos:
>
> **[Dividir em 2 marcos de R$ 2.400]** — você paga cada etapa quando ela for entregue. É o formato que a maioria usa.
> **[Pagar por Pix — R$ 4.800]** — sem limite, e o criador recebe na hora.
>
> *Seu limite no cartão sobe sozinho conforme você contrata. Depois de 2 contratos concluídos, ele vai para R$ 6.000.*
>
> `Preciso pagar no cartão hoje →` (abre pedido de análise, resposta em 1 dia útil)

Quatro coisas fazem isso funcionar:

1. **A saída principal já existe.** Marcos são cobranças separadas (§4.6), então dividir não é truque. ⚠️ **O teto é por cobrança, não por contrato** — isso precisa estar explícito no código.
2. **O limite vira barra de progresso, não recusa.** Mostrar o próximo degrau converte negativa em promessa.
3. **Existe porta humana.** MAQUINA §10.1 já fixou: todo estado precisa de saída. Teto sem porta é beco.
4. **O limite aparece antes do checkout** — no painel da marca e na tela do contrato, antes de escolher o criador. Descobrir o teto na hora de pagar é a sensação de recusa que se quer evitar.

### 4.4 Comissão (decisão 8)

| Item | Regra |
|---|---|
| Comissão total | **15%** — 10% do criador + 5% da marca |
| Recontratação | Cai para **8%** a partir da 3ª contratação entre a mesma marca e o mesmo criador |
| Lançamento | **7,5%** nos primeiros 90 dias **ou** nas primeiras 50 transações (o que vier primeiro) |
| Configuração | Ajustável no painel administrativo, **nunca fixa no código** |

*Referência de mercado:* Workana cobra do freelancer comissão escalonada de 20% caindo até 5% conforme recompra, mais 4,5% do contratante; 99Freelas cobra de 5% a 20% do freelancer. Marketplaces brasileiros em geral operam entre 10% e 20%. 15% posiciona a INFLUENTZ no meio da faixa, com desconto por fidelização — que é o mecanismo que a Workana usa e funciona.

### 4.4.1 De quem sai a comissão, e o piso que impede prejuízo 🔴

**A comissão sai dos dois lados, na proporção 2 para 1: 10% do criador, 5% da marca.**

⚠️ Isto resolve uma **contradição** que existia entre duas seções: uma dizia 10% + 5%, a outra dizia que a comissão saía só do criador. Eram duas contas diferentes, e o código escolheria sozinho.

**Por que dividida, e por que nessa proporção:**

| | Criador | Marca |
|---|---|---|
| Sensível a preço? | **Muito** — é renda pessoal | Menos — é verba de marketing |
| Tem alternativa fora? | **Muito mais** — fechar por mensagem direta é grátis | Menos — achar criador confiável, com métrica auditada e contrato, é o trabalho todo |
| O que faz a oferta crescer? | **Ele.** Marketplace vazio de criador não tem produto | Ela chega atrás da oferta |

Isso parece argumentar por cobrar mais da marca — e argumenta, até certo ponto. **Duas coisas travam a divisão em 10/5:** a marca compara com a agência, que cobra 15% a 20% de *fee* sobre a verba, então 5% embutido é imbatível; e **o criador compara com a alternativa real dele, que não é 0%** — é receber por Pix sem contrato, sem escrow e sem prova, cobrando sozinho quando a marca some. **10% é metade do que Fiverr, Workana e 99Freelas cobram do prestador.**

📌 **Nenhuma plataforma consolidada cobra de um lado só.** Fiverr: 20% do vendedor + 5,5% do comprador. Upwork: até 15% do freelancer + 5% do cliente. Workana: 20% regressivo + 4,5%. O único caso de lado único é o Airbnb — que migrou **na direção contrária**, e pôde fazer isso porque já tem demanda de sobra. Marketplace em lançamento não tem.

> 🔴 **PISO DE COMISSÃO EFETIVA.** Nenhum contrato é criado com comissão efetiva menor que **o custo do meio de pagamento mais 3 pontos percentuais.** A verificação é automática, roda **na criação do contrato**, e usa a taxa real do provedor gravada na configuração — nunca um número escrito no código.

**Por que isso existe:** a recontratação de 8% no cartão à vista deixa uma margem de 3,7%, e ela ainda precisa pagar a tarifa de repasse, os 5% do fundo de contestação e a infraestrutura — sobrando perto de **2,9% num contrato de R$ 1.200**, no meio de pagamento que carrega 100% do risco de contestação. **E os 8% viram prejuízo se a taxa do provedor passar de 7,79%** — número que, como o plano Flex não é público, ainda não sabemos.

O piso resolve sem matar o desconto de fidelização, que é o mecanismo que segura o par marca–criador dentro da plataforma. **Regra de honestidade obrigatória: o desconto exibido é sempre o efetivamente aplicado** — a tela mostra o número final, nunca a promessa genérica.

### 4.5 Preço exibido (decisão 4)

**A marca vê e paga o preço final, desde a primeira tela de busca. Nunca existe taxa somada no checkout.**

O criador cadastra o preço que quer receber pelo trabalho — R$ 1.200. **A vitrine mostra R$ 1.260 já no card da busca**, com os 5% dentro. A marca navega, escolhe e paga sempre o mesmo número.

| | Valor |
|---|---|
| Preço do criador | R$ 1.200,00 |
| **A marca paga** | **R$ 1.260,00** |
| **O criador recebe** | **R$ 1.080,00** |
| Comissão bruta da plataforma | R$ 180,00 |

**O que cada um vê:**

> **Marca:** *Ana Souza · 1 Reels + 3 Stories* — **R$ 1.260**. *Valor final. Inclui a taxa da INFLUENTZ, a retenção do pagamento e o contrato. Nada é somado no checkout.*

> **Criador:** **Você recebe R$ 1.080** — R$ 1.200 do seu preço, menos R$ 120 de comissão. *Disponível no mesmo dia da publicação confirmada.*

⚠️ **O criador pode simplesmente precificar o trabalho considerando a comissão, e a tela precisa deixar isso óbvio em vez de escondido.**

### 4.6 Escrow e marcos 🟢

- **Escrow sempre ativo:** o dinheiro fica retido até a entrega ser aprovada. Inegociável — é o que sustenta a confiança dos dois lados.
- **Marcos (entrega em etapas):** contrato simples e de valor baixo = uma entrega, um pagamento. Contrato maior ou mais longo = a plataforma sugere dividir em etapas automaticamente. Proteção sempre ligada; complexidade proporcional ao risco.

### 4.6.1 Liberação do repasse — decidido, não perguntado 🎯

> Pergunta do dono: *"a liberacao de payout dos creators sera manual? Automatico? Semanal? Mensal?"* — **Resposta: automático, sem aprovação humana, com varredura diária.**

| Parâmetro | Decisão | Por quê |
|---|---|---|
| Gatilho | Todo dia útil, saldo disponível **≥ R$ 50** → transferência criada | Dinheiro parado no provedor sem motivo é confundir "aprovado" com "disponível" |
| Abaixo de R$ 50 | Acumula, e **varre obrigatoriamente no último dia útil do mês** | Nada fica preso por regra nossa |
| Tarifa | **A plataforma paga** a do repasse programado | O criador ofertou olhando o líquido; tarifa surpresa é taxa somada no fim |
| Saque fora do ciclo | Botão "receber agora", **com a tarifa exibida antes**, paga pelo criador | Escolha dele, custo dele, informado antes |
| Aprovação manual | **Nunca**, para valor já disponível | Equipe de uma pessoa não pode ser gargalo de pagamento |

**Por que varredura própria e não o saque automático nativo:** o nativo só aceita diário, semanal ou mensal, e **não tem piso de valor**. Diário nativo geraria transferência de R$ 12 pagando tarifa de alguns reais; semanal faria o criador esperar até 7 dias **além** do prazo do meio. A varredura com piso entrega o melhor dos dois. **Custo estimado:** ~R$ 73/mês no lançamento; na operação, cerca de 2% da comissão. Cabe.

📌 **Somos mais rápidos que Upwork (5 dias de segurança), Fiverr (14 dias para vendedor novo) e Mercado Pago (D0/D14/D30) — porque não inventamos período de segurança.**

⚠️ **Nada disso pode virar carteira.** A varredura é instrução ao provedor com retorno por webhook: a invariante da §4.9 continua intacta, e vale teste automatizado.

### 4.6.2 Perguntas ao Relacionamento do provedor — por escrito, no credenciamento ⚠️

Nenhuma é decisão do Marco; todas viram documento em `/docs` quando responderem:

1. O plano com recebimento em 1 dia (4,19% / 13,63%) vale para **conta marketplace com split e recebedores**, ou só para conta simples?
2. Recebedor secundário no mesmo modelo do principal: **quem é debitado da taxa de antecipação** — o recebedor ou o marketplace?
3. Antecipação e split convivem na mesma transação, com `liable: true` no recebedor da plataforma?
4. **Pix parcelado já está exposto na API?**
5. Qual o valor máximo por boleto e por Pix na nossa conta?
6. Tarifa oficial de saque e de Pix de saída.
13. 🔴 **Qual o tempo máximo entre a transação e o repasse no split?** Se houver teto, contrato longo com retenção não cabe — e isso muda o desenho, não o preço.
14. Cobrança recorrente com split existe na nossa configuração, ou cada ciclo é uma transação nova?
15. **O teto do cartão vale por transação ou por contrato?** Três ciclos de R$ 10.000 são três exposições ou uma?
7. 🔴 **Como somos notificados de um bloqueio cautelar ou MED sobre um recebedor do nosso split?** Por qual webhook, e **quem apresenta a defesa — nós ou o titular?** Sem essa resposta, o primeiro MED nos pega sem canal, com 72 h de relógio.
8. 🔴 **Qual é a taxa do plano Flex com split para a nossa conta**, à vista e por faixa de parcelas? *(A tabela publicada é do plano Essencial, que não tem split.)*
9. 🔴 **Existe data única de recebimento para venda parcelada nessa configuração, e a partir de qual histórico?**
10. 🔴 **Quem é debitado da taxa de antecipação — o marketplace ou o recebedor?** *(Se for o recebedor, o parcelamento não liga.)*
11. Valor mínimo, máximo e limites de antecipação — por dia, por transação, por conta.
12. 🔴 **A validação de mesma titularidade da conta bancária vale para recebedores criados por API**, ou só pela dashboard? **Se valer só pela dashboard, o desvio de repasse volta a ser possível e vira a prioridade número um.** Hoje estamos protegidos por uma regra que ainda não confirmamos.

### 4.7 Cadastro fiscal do criador

🔴 **FATO: não existe ocupação de influenciador digital ou produtor de conteúdo na lista do MEI.** Os CNAEs da atividade — 7311-4/00 (agências de publicidade), 7319-0/03 (marketing direto), 7319-0/04 (consultoria em publicidade) — **não são permitidos ao MEI**. Abrir MEI com CNAE alheio expõe o criador a **desenquadramento retroativo, cinco anos de tributos e multa de até 70%**. Fontes: [Tactus](https://tactus.com.br/influencer-pode-ser-mei/), [Contabilidade.com](https://contabilidade.com/blog/influencer-pode-ser-mei-descubra-como-abrir-empresa/).

Três consequências, e nenhuma é pequena:

1. **O "guia embutido de como abrir MEI" empurraria o criador para uma irregularidade fiscal.** Não pode existir nessa forma.
2. **O Pagar.me aceita recebedor pessoa física com CPF.** Logo a exigência de MEI é **política da plataforma, não limitação técnica** — e a justificativa que estava escrita não se sustenta.
3. **O bloqueio de saque por pendência fiscal trava dinheiro que o criador já ganhou**, por uma regra que a plataforma inventou, num patamar (R$ 500) para o qual **não foi encontrada base legal**. Isso é exposição jurídica, não proteção.

✅ **Regra do v1, até o contador responder:** o criador **recebe como pessoa física, com CPF**. A plataforma **avisa** sobre formalização e obrigação fiscal, mas **não bloqueia o saque**. O estado `bloqueado_por_pendencia_fiscal` fica modelado e **não é implementado no v1**.

🔴 **Bloquear dinheiro alheio por regra própria é decisão que precisa de parecer antes de virar código, não depois.**

### 4.8 Cadastro do recebedor no provedor de pagamento

**FATO.** Desde 29/02/2024 o Pagar.me exige, para **todo** recebedor novo: dados cadastrais mínimos (Circular BCB 3.978/20) e **validação de identidade com prova de vida**. Cada recebedor ganha uma **Conta Digital vinculada à Stone Pagamentos, regulada pelo BCB**. Fonte: [Adequação de Marketplace para Mudanças Regulatórias](https://docs.pagar.me/page/adequa%C3%A7%C3%A3o-de-marketplace-para-mudan%C3%A7as-regulat%C3%B3rias).

| Quem | Dados obrigatórios |
|---|---|
| **Pessoa física** | CPF, nome, data de nascimento, endereço, e-mail, telefone, **renda mensal** e **atividade profissional** |
| **Pessoa jurídica** | CNPJ, razão social, **faturamento médio anual**, endereço, dados dos sócios |

⚠️ **Renda mensal e atividade profissional não existem no cadastro desenhado.** Sem eles, **o recebedor não é criado** — ou seja, o criador não recebe.

⚠️ **O link de validação de identidade vale 20 minutos**, com até 3 tentativas por código. Ele **não pode** ser mandado por e-mail para a pessoa clicar quando puder: tem que ser gerado dentro do app, na hora, com contagem regressiva visível e botão de gerar novo. Fonte: [Criar recebedores e validar identidade](https://pagarme.helpjuice.com/pt_BR/p2-manual-da-dashboard/dashboard-%7C-criar-recebedores-e-validar-identidade).

### 4.9 A invariante que mantém a INFLUENTZ fora do Banco Central

**FATO — limiares da Resolução BCB 80/2021:** subcredenciador precisa de autorização a partir de **R$ 500 milhões** em 12 meses. Na fase de operação da §14 (1.000 contratos/mês × R$ 1.200 = **R$ 14,4 milhões/ano**), a INFLUENTZ está em **2,9% do limiar**. **Volume não é o risco.**

🔴 **O risco é arquitetural, e é barato de cometer.** A Resolução BCB 150/2021 e a Circular 3.886/2018 enquadram como subadquirente o marketplace que **repassa valores entre terceiros**. O que mantém a INFLUENTZ fora dessa categoria não é o tamanho — é o desenho.

> **INVARIANTE, que vale teste automatizado permanente:**
> **Não existe carteira da INFLUENTZ.** O "saldo" que o criador vê é leitura da conta dele no Pagar.me, não um livro-razão que a plataforma controla. **Não existe botão no Admin que mova dinheiro de um usuário para outro** — toda movimentação é instrução ao Pagar.me, com retorno por webhook. O painel administrativo **autoriza; não transfere.**

No dia em que a plataforma receber bruto para repassar depois, ela vira instituição de pagamento não autorizada **independentemente do volume**.

⚠️ **PLD-FT e comunicação ao COAF são do Pagar.me**, porque a Circular BCB 3.978/2020 alcança instituições autorizadas pelo BCB — e a INFLUENTZ não é uma. **Ressalva honesta:** o art. 9º da Lei 9.613/98 alcança quem faz *"intermediação... de recursos financeiros de terceiros"*, e a palavra é larga o bastante para que **só um advogado diga sim ou não**. Premissa de trabalho: tratar como **não obrigada**, mas **construir os controles do mesmo jeito** — são baratos e são os mesmos que as regras antifraude já exigem.

### 4.10 Agenda de recebíveis — Resolução BCB 264/349

**FATO.** O manual do próprio Pagar.me diz que **a responsabilidade é do marketplace**: é preciso dar ao recebedor uma **interface eletrônica** com agenda de recebíveis por Unidade de Recebíveis (UR), valor bruto por UR, deduções discriminadas, recebíveis constituídos, **contratos que gravam a agenda** (contraparte, URs alcançadas, natureza e valor) e **mecanismo de contestação** desses efeitos. Fonte: [Res.264/349 — Manual de Integração](https://docs.pagar.me/page/res264346-manual-de-integra%C3%A7%C3%A3o).

**Prazo:** era 06/11/2023, prorrogado para **01/04/2024**. **Já vencido.** Não é item de roadmap: é condição para operar.

⚠️ **Lacuna aberta.** A carteira e o extrato desenhados **não são agenda de recebíveis por UR**, e não existe nada sobre contratos que gravam a agenda nem sobre contestação. Vale para criador **e** marca, porque ambos são recebedores no split.

### 4.11 Trilha de auditoria

**FATO.** Não existe norma brasileira que imponha trilha imutável a um marketplace de serviços. As referências são indiretas: Marco Civil art. 15, Circular BCB 3.978/2020 e as regras de disputa das bandeiras. Por isso os números abaixo são **decisão adotada**, não obrigação copiada.

**O que registrar** — todo evento de dinheiro, sem exceção: criação de cobrança; **regra de split aplicada, com `liable` e `charge_processing_fee` explícitos**; webhook recebido, com payload bruto e assinatura; mudança de estado de repasse; decisão de disputa; liberação, estorno, débito; alteração de comissão ou prazo no Admin; e **acesso de admin a dado de terceiro** (LGPD art. 46).

**Campos** — quem (usuário ou `sistema`/`webhook`), o quê, quando (UTC com fuso), de onde (IP e user-agent), valor antes e depois, motivo, e o identificador da transação no Pagar.me.

🔴 **Três provas que precisam nascer no instante do fato, porque não se remontam depois:**

1. **O log dos avisos do 3º e do 6º dia**, com data, canal e confirmação de entrega — é ele que sustenta a aprovação automática. *"O cliente aprovou"* é prova forte; *"o cliente não respondeu em 7 dias"* é prova fraca, **a menos que exista o registro de que ele foi avisado duas vezes**.
2. **O hash do arquivo entregue**, no ato do envio.
3. **O permalink, a resposta bruta da API que confirmou a publicação, e o id numérico da conta que publicou.** Reconstruir isso 60 dias depois, com o post já removido, é impossível.

**Imutabilidade** — tabela `append-only`, sem `UPDATE` nem `DELETE`, com **encadeamento por hash**: cada registro carrega o hash do anterior, então adulterar um quebra a cadeia e isso é verificável. **Barato no dia 1, impossível de retrofitar depois.**

| O quê | Prazo | Por quê |
|---|---|---|
| Registros de acesso à aplicação | **6 meses** | Mínimo do Marco Civil art. 15 |
| Evidência de defesa de chargeback | **24 meses** da data prevista de entrega | A janela vai a 540 dias (18 meses); 24 dá margem |
| Trilha de eventos de dinheiro e dados de KYC | **10 anos** | Espelha o prazo que a Circular BCB 3.978/2020 impõe ao Pagar.me. **Se o provedor guarda 10 anos e nós 2, nós somos o elo fraco** |

⚠️ **A saída para o conflito com a LGPD**, a ser levada ao advogado: guardar a trilha de dinheiro **pseudonimizada** por 10 anos (identificadores, valores, datas, hashes — sem nome, CPF, e-mail ou conteúdo de mensagem), e o **dado pessoal apenas enquanto a base legal existir**. Preserva a auditabilidade e reduz a superfície.

⚠️ **Falta um controle que ainda não existe em lugar nenhum:** consulta a **listas restritivas** (PEP, CEIS, CNEP, sanções) no cadastro e antes de contrato de valor alto, com o resultado e a data gravados na trilha.

⚠️ Regime tributário, retenção de IR sobre a comissão e obrigações acessórias precisam de **contador especializado em plataforma digital** antes de virarem código.

---

## 5. Fluxo principal 🟢

1. **Criação** — marca (ou agência em nome dela) publica pedido, ou contrata direto da vitrine.
2. **Matching** — IA sugere criadores compatíveis; busca manual também disponível.
3. **Proposta e aceite bilateral** — condições confirmadas pelos dois lados antes de qualquer cobrança.
4. **Pagamento** — valor retido em escrow.
5. **Execução por marcos.**
6. **Revisão** — a marca pode pedir ajuste referenciado ao briefing antes de aprovar ou disputar (seção 12.1).
7. **Aprovação final e liberação** — dinheiro liberado ao criador conforme o prazo do meio de pagamento (§4.2), comissão retida.
8. **Disputa** — caminho alternativo, só depois de esgotada a revisão. Mediada pela equipe INFLUENTZ.
9. **Avaliação mútua** — double-blind (seção 13.1).

---

## 6. IA de matching 🟢

- **Nível 1 (lançamento):** filtro inteligente — categoria, orçamento, localização, tipo de entrega, histórico de avaliação.
- **Nível 2:** cruza métricas reais de audiência via API oficial (seção 9).
- **Nível 3:** IA lê o briefing em texto livre e sugere criadores com justificativa.

Lança no Nível 1, com a interface já preparada para os próximos.

### 6.1 Ordenação da busca 🟢

Decisão de negócio com peso alto: define quem ganha dinheiro na plataforma. Ordenar por avaliação enterra o criador novo — que é a maioria no lançamento.

**No v1:** relevância de categoria + cota garantida de exposição para criadores novos. **Destaque pago fica para depois** de haver demanda real — vender destaque em marketplace vazio não gera receita e destrói confiança.

---

## 7. Painel administrativo e equipe interna 🟢

Estrutura completa de papéis construída desde já: **Super Admin**, **Financeiro**, **Suporte**, **Trust & Safety**. No lançamento o Marco opera sozinho como Super Admin — mas a estrutura já existe, para não precisar refazer quando houver equipe.

### 7.1 Painel de cada usuário final

Cada tipo de usuário (criador, marca, agência) tem painel completo — não uma tela solta de contratos.

---

## 8. Compliance e jurídico (Brasil) 🟢 ⚠️

- **LGPD:** consentimento, política de privacidade, direito de exclusão de conta e dados.
- **Termos de Uso + Contrato de Prestação de Serviço:** gerado automaticamente por transação.
- **Disputas:** mediação humana com prazo máximo de resposta (seção 12).

### 8.1 Cancelamento e reembolso 🟢 ⚠️

O CDC protege relações de **consumo**; a maior parte dos contratos aqui é **B2B**, então o CDC não se aplica automaticamente. Ainda assim, adotamos o espírito protetivo:

| Momento do cancelamento | Regra |
|---|---|
| Até 24h após o aceite, antes do criador começar | Reembolso total |
| Criador já começou (marco em andamento) | Sem reembolso automático — mediação, liberação proporcional ao trabalho feito |
| Após aprovação final de um marco | Sem reembolso — serviço prestado e aceito |
| Comissão da plataforma | Devolvida integralmente dentro da janela de 24h; não reembolsada fora dela |

### 8.2 Direitos sobre o conteúdo (decisão 5) 🟢 ⚠️

**Uma pergunta na tela. O resto é padrão fixo.**

O mercado não pergunta: **fixa**. Ninguém pede sete decisões a quem quer comprar um Reels.

🟢 **O que fica na tela de quem contrata:**

| Campo | Como funciona |
|---|---|
| **"A marca pode usar em anúncio pago?"** | Sim/Não. **Já vem marcado conforme o tipo de trabalho** — desmarcado em publicação no perfil, marcado em material entregue. **Este campo único substitui três antigos** (mídias permitidas, impulsionamento e verba máxima) |
| **Exclusividade** | Só em "opções avançadas". Padrão: **nenhuma** |

🟢 **O que vira padrão fixo e invisível**, resumido numa frase editável em "opções avançadas": prazo de uso **12 meses** · todas as mídias da marca · permanência no ar conforme o tipo (90 dias, ou 24 h em Stories) · e **retirada de conteúdo**, que deixa de ser campo e vira cláusula igual para todos — qualquer lado pode pedir remoção em caso de crise, **sem estorno automático**.

⚠️ **Duas cláusulas fixas sobre o material que a marca envia** (foto do produto, kit de mídia), geradas sozinhas: a marca **declara ter os direitos** sobre o que envia, inclusive de imagem de quem apareça nele; e o criador pode usar esse material **apenas para executar aquele contrato**.

⚠️ **O que não pode ser cortado, porque é lei — e mesmo assim não vira pergunta:**

- **Direito de imagem com finalidade e prazo delimitados.** Autorização genérica e eterna é frágil no Brasil. A cláusula é **gerada automaticamente** a partir da finalidade e do prazo que já estão nos campos acima. Zero decisão a mais, texto continua válido.
- **Identificação publicitária.** O guia do CONAR de 2026 manda usar a ferramenta nativa da rede ("parceria paga com"). Isso **deixa de ser campo escolhível** e vira regra fixa da plataforma, com lembrete na hora da entrega. **Menos um campo, mais proteção.**

🔴 **O que isso quebra para um cliente legítimo:** a agência grande que quer 24 meses e mídia offline não acha isso na primeira tela. **Saída:** um link *"ajustar direitos"* logo abaixo da frase de resumo, que abre os campos completos. **Quem precisa, acha; quem não precisa, nem vê.**

*Por que isso é produto, não só jurídico:* cada campo tem preço implícito, o que aumenta o ticket médio e, portanto, a comissão.

### 8.3 Categorias reguladas e proteção de menores (decisão 6) 🟢 ⚠️

**Proibidas no v1:** apostas, bebida alcoólica, produtos financeiros e investimentos, saúde/medicamentos, e qualquer campanha dirigida ao público infantil. São as áreas de regra mais restrita e maior exposição para a plataforma.

**Conteúdo adulto / sexshop — permitido com trava:** a venda desses produtos é legal no Brasil e o CONAR não proíbe sua divulgação, mas impõe limites — o conteúdo não pode ser ofensivo à moral e **deve evitar exposição a menores de idade**. Portanto:

- Categoria adulta exige **verificação de idade por documento**, não autodeclaração, para ver e para se candidatar.
- **Criador menor de 18 anos é bloqueado pelo sistema** de qualquer campanha de categoria adulta ou sensível. Sem exceção, sem override manual.

### 8.3.1 Criador menor de idade

**O que a v0.4 dizia:** criador menor de idade é permitido, bastando assinatura do responsável legal.

**Isso está juridicamente incompleto.** Pesquisa posterior mostrou que a assinatura do responsável resolve apenas metade do problema:

1. **Capacidade civil** — resolvida pela assinatura. Menor de 16 anos precisa ser *representado*; entre 16 e 18, *assistido*. É o que a v0.4 previa.
2. **Autorização judicial** — **não resolvida, e é a parte pesada.** O ECA, artigo 149, exige **alvará judicial** para participação de criança ou adolescente em atividade artística. A Lei nº 15.211/2025 (o "ECA Digital") trouxe isso explicitamente para o ambiente digital: quando há conteúdo monetizado, impulsionado ou exploração habitual da imagem do menor, a autorização judicial pode ser exigida.

**Por que isso muda o produto, e não só o contrato:** o alvará é obtido **pelos pais, através de advogado, em petição ao juiz da Vara da Infância e Juventude** da comarca onde o menor mora. A petição descreve a atividade, a frequência, a carga horária e o destino dos rendimentos. **Nenhuma plataforma consegue emitir isso** — é decisão de um juiz, caso a caso, por criança.

**Isso já está sendo cobrado na prática:** perfis com crianças e adolescentes como protagonistas de conteúdo monetizado vêm sendo notificados a apresentar o alvará sob pena de bloqueio da conta.

🟢 **Decisão para o v1: criador precisa ter 18 anos completos.**

- A trava é automática e sem exceção, conferida pela data de nascimento que a **verificação de identidade do provedor de pagamento já entrega** (§13). Não pede documento novo, não custa nada a mais.
- Marca e agência não têm essa trava — são pessoa jurídica ou representante dela.

*Por que bloquear e não construir o fluxo:* construir agora significaria criar um caminho para um terceiro que **não tem conta na plataforma** (o responsável) assinar, mais a conferência de que ele é mesmo o responsável, mais o recebimento e a validação de um alvará judicial — e ainda assim a plataforma continuaria exposta se o documento fosse falso ou vencido. É a maior exposição jurídica isolada do produto inteiro, num v1 cuja meta (§14) é provar o ciclo com 20 contratos.

🔵 **Caminho para o v2:** o mercado de criador adolescente é real (moda, games, beleza). Ele entra depois, com o alvará como documento obrigatório anexado ao perfil, prazo de validade controlado pelo sistema, e revisão de advogado antes de abrir. Bloquear no v1 não fecha a porta — adia a porta até ela ser segura.

⚠️ Toda esta seção precisa de validação de advogado antes de virar Termos de Uso.

---

## 9. Redes sociais e métricas 🟢

**Conexão direta com a API oficial de cada rede (Instagram, TikTok, YouTube), sem intermediário pago.** O usuário autoriza com um clique e os dados vêm da fonte.

🔴 **Regra travada, sem exceção: na INFLUENTZ não existe métrica que não venha de API.** Não existe captura de tela, não existe número digitado pelo usuário, não existe fila de aprovação manual de métrica. Se o dado não veio da API da rede, ele não aparece na plataforma.

### 9.1 Métrica real desde o primeiro criador

**O problema real que ele resolvia é verdadeiro:** o App Review do Instagram leva semanas, e o criador convidado pessoalmente (§14.1) não pode ficar travado esperando.

✅ **A solução é que as três plataformas já têm mecanismo oficial de pré-aprovação — e ele devolve dado real de API, não estimativa.** Não é contorno: é o caminho que a própria Meta, o TikTok e o Google desenharam para piloto.

| Rede | Ponte oficial no dia 1 | Capacidade | Fonte |
|---|---|---|---|
| **TikTok** | Sandbox: 5 sandboxes × 10 contas-alvo | **50 criadores** | [Add a Sandbox](https://developers.tiktok.com/docs/en/add-a-sandbox) |
| **Instagram** | *Instagram Tester* + Standard Access — "testers can grant the app any permission while it is in development" | **50** sem empresa verificada · **500** com | [App Roles](https://developers.facebook.com/docs/development/build-and-test/app-roles/), [Access Levels](https://developers.facebook.com/docs/graph-api/overview/access-levels) |
| **YouTube** | 🔴 **Direto para a verificação de escopo sensível** — 3 a 5 dias úteis, grátis, **sem exigir empresa**. Nunca ficar em modo Testing | ilimitado | [Sensitive scope verification](https://developers.google.com/identity/protocols/oauth2/production-readiness/sensitive-scope-verification) |

O criador aceita um convite dentro do app da própria rede e autoriza. **A métrica que chega é da API, igual à do dia 200.** A diferença é só administrativa e invisível para ele.

🔴 **Armadilha corrigida: o modo Testing do YouTube não é ponte, é armadilha.** A documentação do Google é explícita — em projeto com tela de consentimento externa e status "Testing", *"is issued a refresh token expiring in 7 days"*. Traduzindo: **o criador teria que reconectar o YouTube toda semana.** Isso destruiria o carimbo "atualizado há 6 h" da §9.1.3 e transformaria a coorte-piloto em suporte semanal. Como a verificação de produção é grátis, leva 3 a 5 dias úteis e **não exige empresa**, o YouTube vai direto para produção. Fonte: [OAuth 2.0](https://developers.google.com/identity/protocols/oauth2).

📌 **Por que a autorização do usuário não basta — a dúvida do dono, respondida.** São duas fechaduras na mesma porta: o **usuário** autoriza (é o botão "Conectar Instagram"), e a **rede** autoriza o aplicativo. A segunda existe porque o clique do usuário é fácil de arrancar — Cambridge Analytica foi exatamente isso, milhões de pessoas clicando "autorizar" num quiz. Desde então a Meta exige saber **qual empresa está por trás do aplicativo**, com CNPJ e contrato social, para ter alguém a responsabilizar se o dado vazar. Não é burocracia: é a rede transferindo responsabilidade legal para uma pessoa jurídica identificável.

⚠️ **Duas ressalvas honestas, que ficam registradas:**

1. **Sandbox e modo de desenvolvimento existem para testar, não para operar.** Rodar 50 criadores pagantes ali estica a intenção da regra. O risco não é multa — é a Meta ver uso de produção em modo dev na hora do review. Mitigação obrigatória: coorte-piloto **fechada e com prazo**, e o App Review submetido **em paralelo, não depois**.
2. **O relógio do App Review só começa quando o fluxo de conexão existe funcionando**, porque a Meta exige vídeo de tela do fluxo real. Não dá para submeter antes do produto.

### 9.1.1 As fases, e o que trava o quê ⚠️

🔴 **A Meta tem três portões em série**, e cada um é pré-requisito do seguinte:

| Portão | O que prova | Exige CNPJ | Prazo |
|---|---|---|---|
| 1. Verificação de Empresa | Que a empresa existe | **Sim** | 1 a 14 dias úteis |
| 2. **Access Verification (Tech Provider)** | Que você presta serviço a **outras** empresas | **Sim** (depende do portão 1) | ~5 dias, prazo oficial |
| 3. App Review | Cada permissão, uma a uma | Depende dos dois | Sem SLA público |

⚠️ **O portão 2 atinge exatamente as permissões que a INFLUENTZ usa** — `instagram_business_basic` e `instagram_manage_insights` estão na lista oficial que exige Access Verification, e a página diz que *"before access verification can begin, a business admin must complete Business Verification"*. Sem ele, a chamada volta com erro 100. Fonte: [Access Verification](https://developers.facebook.com/docs/development/release/access-verification).

⚠️ **Não existe caminho individual.** A Meta encerrou em 01/02/2023: *"individual verification will no longer be allowed for access once the business verification process is complete"* ([anúncio oficial](https://developers.facebook.com/blog/post/2023/02/01/developer-platform-requiring-business-verification-for-advanced-access/)).

❌ **App sob CNPJ de terceiro (parceiro, agência, desenvolvedor) está descartado.** Quem é dono do app é o controlador do dado perante a LGPD; emprestar CNPJ sem o enquadramento de Tech Provider é declaração falsa na verificação, punida com banimento do portfólio inteiro; e o app — com os tokens de todos os criadores — fica sendo ativo de outra pessoa. **A versão legítima dessa ideia é o agregador**, que é a mesma coisa com contrato e sancionada pela Meta.

**Fase 0 — antes de qualquer código de conexão.** Verificar o domínio no Google e publicar Política de Privacidade e Termos. Não depende de empresa, então começa já.

🔴 **A correção que reorganiza tudo: o que trava primeiro é o dinheiro, não a métrica.** A §4.1 já registra que *"chaves de produção exigem CNPJ"* no Pagar.me. A §15 lista pendências de contador que bloqueiam o código de pagamento. **A INFLUENTZ não recebe um real sem CNPJ. Logo o CNPJ nunca foi negociável — só a data era.** O Instagram não cria essa necessidade: ele apenas **antecipa a data em cerca de quatro meses**, porque as filas da Meta são mais longas que a do Pagar.me.

⚠️ **MEI não serve**, e o motivo não tem nada a ver com a Meta: intermediação de negócios (CNAE 7490-1/04) **não está na lista de ocupações permitidas ao MEI** ([Portal Gov.br](https://www.gov.br/empresas-e-negocios/pt-br/empreendedor/quero-ser-mei/atividades-permitidas)), e o teto de R$ 81 mil/ano quebraria no primeiro mês bom. O formato indicado é **SLU (Sociedade Limitada Unipessoal)**.

**Fase 1 — dia 1 do cold start.** YouTube em Testing (100 testers) · Instagram por convite de Tester · TikTok em sandbox. Em paralelo, submeter YouTube (3–5 dias úteis) e TikTok ("several days to two weeks", [App Review FAQ](https://developers.tiktok.com/doc/getting-started-faq)).

**Fase 2 — quando o fluxo estiver pronto.** Submeter o App Review do Instagram com o vídeo de tela. A Meta não publica SLA; relatos de mercado em 2026 falam em ~20 dias de média e 4 a 6 semanas ponta a ponta com uma rodada de correção — **fonte secundária, não oficial**.

**Fase 3 — aprovado.** Vira Advanced Access / produção. **Os criadores da coorte não refazem nada** — o token deles continua válido, só muda o modo do app. Isso precisa estar previsto na modelagem de dados desde já.

### 9.1.1.1 O agregador é o caminho principal, não a reserva 🟢

🔴 **Decisão invertida, e ela tira três aprovações do caminho crítico do lançamento.**

A versão anterior punha a INFLUENTZ construindo **três integrações próprias** — Meta, TikTok e Google —, cada uma com fila de aprovação, exigência de empresa verificada, prazo fora do nosso controle e risco de reprovação. Isso é três vezes o mesmo trabalho, três vezes o mesmo risco, e **três coisas que podem travar o lançamento por motivo que não é nosso.**

✅ **A regra do v1: uma integração só, com um agregador que já tem as aprovações das três redes.**

| | Três integrações próprias | Um agregador |
|---|---|---|
| Aprovações a obter | 3, em série, com CNPJ | **0** |
| Prazo fora do nosso controle | semanas a meses | **nenhum** |
| Risco de reprovação | 3 pontos de falha | **0** |
| Exige CNPJ para começar | **Sim** (Meta) | **Não** |
| Custo no lançamento | R$ 0 | ⚠️ **Não confirmado** — ver o aviso abaixo |
| Trabalho de engenharia | 3× | **1×** |

**O criador não percebe diferença nenhuma:** ele autentica na tela da própria rede, com o login oficial dela. É dado consentido por OAuth, exatamente como seria na integração própria — **não é raspagem, não é print, não é estimativa.** A regra travada continua valendo ao pé da letra: *métrica só por API oficial.*

🔴 **Correção importante: o "plano gratuito de 250 contas" não foi confirmado.** A página oficial de preços do fornecedor diz apenas *"depending on your exact use case, we offer customized plans"*, com botão de orçamento e **nenhum número publicado**. Isso não prova que o plano gratuito não existe — prova que **ele não está publicado**, e portanto **não é fato: é premissa.**

**A decisão de arquitetura continua certa pelos outros motivos** — uma integração em vez de três, zero fila de aprovação, não exige CNPJ, e nenhum ponto de reprovação. **O que falta é um e-mail ao fornecedor com o número por escrito**, não uma escolha nova.

⚠️ **E a pergunta a fazer antes do preço é outra, e é maior:** *a cobrança é por conta conectada ou por chamada?* A verificação de permanência da publicação gera, na fase de operação, cerca de **90.000 consultas por mês** — noventa vezes o número de criadores conectados. **Se for por chamada, essa linha sozinha pode custar mais que toda a infraestrutura somada.** Mitigação já disponível e de graça: verificar uma vez por dia nos primeiros 7 dias e uma vez por semana depois — **corta 79% das chamadas** sem perder a capacidade de detectar remoção.

📌 **Quando a integração própria passa a valer a pena:** depois de 250 criadores conectados, quando o plano gratuito acaba **e já existe receita**. Aí ela vira **otimização de custo**, feita com calma, com a empresa aberta e sem prazo apertado — e não pré-requisito de lançamento. **A camada de abstração já prevista faz a troca ser um adaptador, não uma reescrita.**

❌ **Raspagem continua fora de cogitação.** Fornecedores que entregam dado raspado de perfil público violam os termos das redes e a regra da §9.

⚠️ **Antes de assinar, duas exigências que vão para o `juridico-br`:** o contrato precisa **declarar por escrito que a aprovação do fornecedor junto às redes cobre o uso pelo cliente final**; e, como o acesso fica com ele, ele é **operador de dado pessoal** — exige contrato de tratamento e menção nominal na Política de Privacidade.

### 9.1.4 Riscos, sem maquiagem

| Risco | Consequência real | O que fazer |
|---|---|---|
| Meta reprova o App Review | Instagram fica preso ao teto do modo piloto — e é a rede principal do mercado brasileiro | Data-gatilho com o agregador. Reprovação quase sempre é vídeo ruim ou justificativa vaga, e cabe recurso — mas cada rodada reinicia o relógio |
| **Sem CNPJ** | ⚠️ **O Pagar.me em produção trava antes do Instagram.** A plataforma não recebe dinheiro nenhum. O CNPJ nunca foi decisão sobre métrica | Ver a data-gatilho em §9.1.5 |
| Token do Instagram expira (60 dias sem uso) | Métrica congela | Rotina de renovação + estado `token_expirado` com botão. **Nunca apagar a métrica anterior** — mostrar com data |
| Criador só tem conta pessoal | Não conecta | §9.1.2 — conversão vira passo do onboarding |
| Coorte-piloto lota (50 no TikTok) | Criador 51 fica sem TikTok | Lista de espera com data, e submeter o review antes de chegar em 40 |
| API da rede cai | Métrica não atualiza | Mostrar a última leitura com data. **Nunca zero, nunca em branco** |

⚠️ **Vai para o `juridico-br` antes de virar tela:** conectar rede social é tratamento de dado pessoal — a base legal do consentimento precisa estar no Termo, e é preciso definir o que acontece com a métrica coletada quando o criador desconecta ou pede exclusão (LGPD).

📌 **O que a concorrência faz:** a Squid (hoje Squid by Wake) integra por API oficial da Meta e do TikTok, com atualização em até 24 h ([central de ajuda](https://meajuda.squid.com.br/docs/como-conectar-o-meu-instagram-a-squid)). Métrica por captura de tela não é padrão de mercado — é gambiarra.

### 9.1.5 A data-gatilho do CNPJ 🎯

**As três filas da Meta correm em série** — cada uma é pré-requisito da seguinte — e duas delas **não dependem de uma linha de código**, só de CNPJ e domínio.

| Etapa | Melhor caso | Pior caso |
|---|---|---|
| Abrir SLU | 1 dia útil | 5 dias úteis |
| Portfólio Empresarial + domínio | 1 dia | 3 dias |
| Verificação de Empresa | 1 dia útil | 14 dias úteis |
| Access Verification | ~5 dias | ~10 dias |
| App Review do Instagram | ~14 dias | ~30 dias |
| Uma reprovação e recurso | 0 | ~20 dias |
| **Total** | **~5 semanas** | **~15 semanas** |

*Verificação de Empresa e App Review não têm SLA publicado pela Meta — são relatos de mercado. Access Verification tem "approximately 5 days" na documentação oficial.*

> 🎯 **GATILHO 1 — CNPJ:** a empresa precisa existir **no mínimo 6 semanas antes** do dia em que a tela de conexão do Instagram funcionar de ponta a ponta. Não seis semanas antes do lançamento — seis semanas antes da **tela**. É o tempo dos portões 1 e 2, que são pura fila.
>
> 🎯 **GATILHO 2 — App Review:** submetido no mesmo dia em que a tela funcionar. Como ele exige vídeo do fluxo real, a tela precisa ficar pronta **10 a 15 semanas antes do lançamento**.

**Em calendário:** para o Instagram estar liberado no dia do lançamento, **o CNPJ precisa existir cerca de 4 meses antes.** Na prática: a empresa abre **no dia em que começar o desenvolvimento da tela de conexão** — não depois.

⚠️ **A economia de adiar o CNPJ não existe.** Manter a empresa parada custa contabilidade mensal; cada semana de lançamento atrasado por fila da Meta custa mais — e o contador já era obrigatório antes do primeiro pagamento por seis motivos da §15. Adiar não elimina o custo: **desloca para o pior momento possível, que é o mês do lançamento.**

### 9.2 Detecção de fraude de engajamento 🟡

Analisar proporção curtida/comentário, padrão e horário dos comentários **não é viável pela via oficial:** as APIs entregam métricas agregadas do perfil autorizado, não o conteúdo de comentários nem a lista de seguidores.

O que dá para fazer com dado oficial: **evolução de seguidores ao longo do tempo** (picos anormais são detectáveis) e **taxa de engajamento agregada versus a mediana da categoria**. Pega os casos grosseiros.

---

## 10. Chat 🟢

**O chat só abre depois da proposta aceita e paga.** Antes disso, a comunicação acontece dentro da própria proposta, em campos estruturados (perguntas e ajustes).

*Por quê:* chat liberado antes do contrato é a porta de saída número um de qualquer marketplace. Fechar essa porta por design é mais eficaz — e menos invasivo — do que vigiar conversa.

---

## 11. Notificações 🟡

Central de notificações dentro do produto **não basta** — no início ninguém entra no produto sozinho. As notificações que importam (proposta recebida, prazo vencendo, entrega para aprovar) precisam sair.

- **v1:** e-mail (barato e imediato)
- **v2:** WhatsApp (tem custo por mensagem e exige aprovação de modelos de mensagem)

---

## 12. Disputa e mediação 🟢

### 12.1 Revisão antes da disputa

A marca pode pedir ajuste **referenciado ao briefing** antes de aprovar ou abrir disputa. Reduz drasticamente o volume de mediação.

### 12.2 Disputa

Mediada pela equipe INFLUENTZ, com prazo máximo de resposta, priorizada por risco em painel próprio de Trust & Safety.

---

## 13. Confiança e antifraude 🟢

- **Identidade verificada:** reaproveita a verificação já exigida pelo provedor de pagamento — sem pedir documento duas vezes.
- **Verificação de empresa:** CNPJ ativo confirmado antes de publicar campanha paga.
- **Fraude e lavagem:** apoiado nas ferramentas do provedor, complementado com regras próprias — limite para contas novas, alerta quando o mesmo CPF/CNPJ aparece como marca *e* criador na mesma transação, revisão manual acima de valor definido.

### 13.1 Avaliação mútua sem retaliação 🔵

As duas avaliações ficam ocultas até ambos enviarem (ou o prazo vencer). Elimina a nota-por-vingança. Mesmo mecanismo do Airbnb.

### 13.2 Tentativa de fechar por fora 🟢 ⚠️

1. **Detecção:** monitoramento **dentro do chat da própria plataforma** (nunca fora dela) de padrões que sugerem fechar por fora.
2. **1ª ocorrência:** lembrete automático no chat mostrando as vantagens objetivas de fechar pela plataforma. Convencer, não ameaçar.
3. **Reincidência:** registro formal visível para Trust & Safety — uma pessoa revisa antes de qualquer ação.
4. **Reincidência após aviso formal:** suspensão temporária e, persistindo, banimento.
5. ⚠️ Monitorar conteúdo de mensagem, mesmo interno, precisa estar explícito nos Termos de Uso e na Política de Privacidade (transparência exigida pela LGPD).

---

## 14. Escopo do lançamento (v1) 🟢

**Meta de validação:** 50 criadores com perfil completo, 10 marcas cadastradas, 20 contratos pagos e concluídos. Números pequenos de propósito — o objetivo é provar que o ciclo inteiro funciona com dinheiro de verdade, não crescer.

### 14.1 Cold start 🔴

Um marketplace vazio não tem produto. Isso não é marketing, é viabilidade.

**Os primeiros criadores e marcas entram por convite pessoal do Marco.** É trabalho manual, não escala — e é exatamente assim que todo marketplace começou.

✅ **O plano de entrada, definido pelo dono, em três degraus e nesta ordem:**

| Degrau | O que acontece | Por que nesta ordem |
|---|---|---|
| **1. Operação real interna** | O Marco roda contratos de verdade, com dinheiro de verdade, entre contas dele. Testa velocidade, armazenamento, pagamento, saque e estorno | **Nenhum usuário externo entra antes disso.** Um erro de dinheiro no primeiro contrato real de um convidado custa a relação e a reputação, que são o ativo do cold start |
| **2. Convite pessoal** | Criadores e marcas do círculo dele, um a um | Volume pequeno, curadoria alta, e canal direto para ouvir o que quebra |
| **3. Divulgação paga com um influenciador** | Contratar um influenciador para divulgar a plataforma | 🟢 **E isso é a própria plataforma sendo usada:** a INFLUENTZ contrata pela INFLUENTZ. O primeiro contrato de verdade é o nosso, e ele prova o produto para quem estiver olhando |

**Consequência de infraestrutura, que vale como regra:** a plataforma nasce no menor custo que funciona e **cresce por degrau, conforme a necessidade aparece** — nunca por antecipação. Palavra do dono: *"nos temos que economizar maximo possivel para sobrevivermos ao inicio e depois investirmos ao longo da jornada."*

---

## 14.2 Custo de operar — com unidade e período em toda linha 💰

📌 **Premissa de câmbio, declarada uma vez e válida para a seção inteira: US$ 1,00 = R$ 5,50.** **Todo valor desta seção é por mês**, salvo quando a linha disser *por ano* ou *uma vez*.

**A resposta curta, em cinco linhas:** **R$ 307,76 por mês no lançamento** · **até R$ 908 com contador** · **20 contratos por mês pagam tudo** · **o preço do agregador de métricas é a única incerteza que importa** · **e o vídeo tem que morar no Cloudflare R2.** O resto da seção é a conta que sustenta esses cinco números.

### 14.2.1 A conta do vídeo — o item que explode em silêncio

**Premissa de tamanho:** arquivo MP4/H.264 vertical 1080×1920, até ~3 minutos → **250 MB por arquivo**. Um Reels de 60 s exportado pelo celular dá 90–130 MB; 250 MB só é atingido em peça longa ou 4K. **Planejar por 250 MB é errar para o lado caro, que é o certo.**

| Tipo de arquivo | Quantos por contrato | Tamanho | Retenção |
|---|---|---|---|
| Arquivo final aprovado | 1 | 250 MB | **24 meses**, contados **da publicação confirmada por API** |
| Brutos e versões recusadas | 2 | 500 MB | **90 dias**, contados **do fechamento do contrato** |
| **Total por contrato** | **3** | **750 MB** | — |

**Acervo acumulado no lançamento (20 contratos/mês).** Preço Cloudflare R2: **US$ 0,015 por GB por mês**, com **10 GB por mês grátis**.

| Mês | Acervo total | **Custo por mês** |
|---|---|---|
| 1 | 15 GB | R$ 0,41 |
| 4 | 50 GB — os brutos param de crescer | R$ 3,30 |
| 12 | 90 GB | R$ 6,60 |
| **25 em diante** | **150 GB — estabiliza de vez** | **R$ 11,55** |

**Na operação (1.000 contratos/mês):** finais 6.000 GB + brutos 1.500 GB = **7,3 TB → R$ 617,92 por mês**. **Sem a regra de retenção** seriam 17,6 TB → **R$ 1.485 por mês**. 🔴 **A regra de retenção vale R$ 867 por mês.** Ela não é higiene: é o segundo maior item da conta.

### 14.2.2 Quanto custa cada visualização — e por que o vídeo mora no R2

| Onde o arquivo está | O que se paga por assistir | 1 visualização de 250 MB | 1.000 visualizações |
|---|---|---|---|
| **Cloudflare R2** | Download é **grátis**; paga-se só a leitura (US$ 0,36 por milhão de operações) | **R$ 0,00002** | **R$ 0,02** |
| Supabase Storage | **US$ 0,09 por GB baixado** | R$ 0,12 | R$ 123,75 |

🔴 **É 6.200 vezes mais caro, e nada na tela muda** — o vídeo toca igual. Aparece só na fatura, 30 dias depois. **Decisão: o vídeo mora no R2 e em nenhum outro lugar, e nunca passa pelo servidor do site** — o celular do criador manda direto para o R2 com endereço temporário assinado.

### 14.2.3 A conta do lançamento — 20 contratos/mês · 50 criadores · 10 marcas · 1 operador

| Serviço | Paga-se por quê | Preço unitário oficial | Quantidade e premissa | **R$ por mês** |
|---|---|---|---|---|
| Supabase Pro | banco + login + trilha de auditoria | US$ 25/mês: 8 GB de banco, 250 GB de download, backup diário por 7 dias | banco < 500 MB; 60 usuários ativos/mês | 137,50 |
| Vercel Pro | hospedar o site | US$ 20/mês, 1 TB de tráfego e 10 M de requisições | ~20 GB/mês | 110,00 |
| R2 — guardar vídeo | US$ 0,015 por GB por mês | acervo em regime: 150 GB (no mês 12 são 90 GB → R$ 6,60) | 11,55 |
| R2 — subir e assistir | Classe A US$ 4,50/M · Classe B US$ 0,36/M | 3.120 e ~2.000 por mês — dentro do gratuito | 0,00 |
| Resend | e-mail transacional | Free: 3.000 por mês **e teto de 100 por dia** | ~350 por mês | 0,00 |
| Expo Push | notificação no celular | **grátis, sem custo por mensagem** | ~600 por mês | 0,00 |
| Sentry Developer | monitorar erro | Free: 5.000 erros/mês, **1 usuário**, 30 dias | < 1.000 por mês | 0,00 |
| Crisp Free | ferramenta de suporte | Free: **2 assentos**, conversas ilimitadas | 3 a 6 chamados/mês | 0,00 |
| Agregador de métricas | ler seguidores e alcance por API oficial | ⚠️ **preço não publicado — só por orçamento** | 50 contas conectadas | **0,00 — premissa, não fato** |
| 17TRACK | rastreio de encomenda | Free: 100 por mês | ~6 objetos/mês | 0,00 |
| Apple Developer | publicar o app iOS | US$ 99 **por ano** | 1 conta | 45,38 |
| Domínio `.com.br` | o endereço | R$ 40 **por ano** | 1 | 3,33 |
| Backblaze B2 | **cópia de segurança do banco, fora do fornecedor principal** | US$ 6,95 por TB por mês, 10 GB grátis | dumps do banco: ~2,4 GB por ano | 0,00 |
| **TOTAL** | | | | **R$ 307,76 por mês** |

**Os outros três estágios, em uma linha cada:**

| Estágio | **R$ por mês** | Pagamento único |
|---|---|---|
| Desenvolvimento puro — nenhuma cobrança real | **R$ 3,33** (é o domínio, diluído em 12 meses) | — |
| Degrau 1 do cold start — o primeiro dinheiro de verdade | **R$ 296,21** (Supabase Pro + Vercel Pro + Apple + domínio) | R$ 137,50 na Google Play |
| Operação — 1.000 contratos/mês | **R$ 1.607,13** sem o agregador · **R$ 4.357,13** com a premissa dele | — |

⚠️ **Isto é só tecnologia.** Não inclui contador (R$ 195 a R$ 600 por mês), advogado, marketing, salário de ninguém, nem a formação do fundo de contestação. **Com o contador, o lançamento fica entre R$ 503 e R$ 908 por mês.**

> ✅ **Em quantos contratos a plataforma paga a própria tecnologia.** Com a comissão efetiva de 15% (§4.4.1) e ticket médio entre R$ 500 e R$ 1.500, **de 2 a 5 contratos por mês pagam a tecnologia e de 5 a 13 pagam tudo, contador incluído. A meta de 20 contratos por mês paga o conjunto em qualquer cenário de preço.**

### 14.2.4 Quando cada plano gratuito estoura — com o número que dispara

| Serviço | Limite do plano gratuito | **Estoura em que número** |
|---|---|---|
| **Vercel Hobby** | uso **não comercial** | 🔴 **No dia da primeira cobrança no site**, inclusive a do fundador. Não é volume, é cláusula |
| **Supabase Free** | 500 MB de banco · **arquivo de no máximo 50 MB** · sem backup · pausa após 1 semana | 🔴 **Antes de qualquer volume:** um vídeo de 250 MB não cabe no teto de 50 MB |
| **Cloudflare R2** | 10 GB por mês | Mês 1 do lançamento (15 GB). Custo de estouro: R$ 0,41 |
| **Resend Free** | 3.000 por mês **e 100 por dia** | 🔴 **O teto diário manda.** O mensal só estoura em ~170 contratos/mês; o diário estoura num único dia de disparo em massa |
| **Sentry Developer** | 5.000 erros/mês, **1 usuário** | **Na segunda pessoa** que precisar ver erro. Volume não é o gatilho |
| **Crisp Free** | **2 assentos** | **No terceiro atendente** |
| **Expo Push** | 600 por segundo | Não estoura neste produto |
| **17TRACK** | 100 por mês | ⚠️ **Depende de uma resposta que não temos:** se a cota for por **consulta** e não por objeto, estoura em **~16 envios por mês** — dentro do lançamento |
| **Agregador de métricas** | ⚠️ não publicado | Ver §9.1.1.1 |

### 14.2.5 As três coisas que podem estourar o custo sem ninguém perceber

1. 🔴 **O agregador de métricas — e o risco não é o preço por conta, é a unidade de cobrança.** A verificação de permanência de 90 dias (§8.2) gera **~90.000 consultas por mês** na operação, noventa vezes o número de criadores conectados. **Se a cobrança for por chamada, essa linha sozinha passa todo o resto somado.** *Mitigação já adotada e de graça:* verificar **1× por dia nos primeiros 7 dias, depois 1× por semana** — cai de 90 para 19 consultas por publicação, **redução de 79%**, sem perder a capacidade de detectar remoção.
2. 🔴 **Um único endereço de vídeo servido do lugar errado** multiplica o custo por 6.200 e não muda nada na tela. *Detecção:* alerta de gasto no Supabase em US$ 5/mês de download.
3. 🔴 **A rotina de exclusão que falha em silêncio.** É ela que mantém o acervo em 7,5 TB em vez de 17,6 TB. Uma rotina que não roda não gera erro: gera silêncio. *Detecção, e ela não custa tela nenhuma:* **a rotina reporta cada execução ao monitoramento que já está pago.** Duas execuções sem reporte é alarme.

### 14.2.6 O que é fato com fonte, e o que ainda é premissa

**Fato, com preço oficial publicado:** Supabase (Free e Pro US$ 25/mês) · Vercel (Hobby não comercial e Pro US$ 20/mês) · Cloudflare R2 (US$ 0,015/GB/mês, download grátis, 11 noves de durabilidade) · Resend (Free 3.000/mês e 100/dia; Pro US$ 20/mês) · Expo Push (sem custo) · Sentry (Developer US$ 0; Team US$ 26/mês) · Crisp (Free 2 assentos; Mini US$ 45/mês) · Backblaze B2 (US$ 6,95/TB/mês) · Apple Developer US$ 99/ano · Google Play US$ 25 uma vez · domínio `.com.br` R$ 40/ano.

**Premissa, não fato — e cada uma move a conta:** dólar a R$ 5,50 (cada R$ 0,50 de variação move a operação em ~R$ 150/mês) · vídeo de 250 MB e 3 arquivos por contrato · **preço do agregador de métricas (a maior)** · preço e unidade de cobrança do 17TRACK · 20 visualizações por entrega na operação.

## 14.2.7 O que o criador sente ao subir um vídeo pelo celular 🔴

**Subir um vídeo de 250 MB pelo 4G brasileiro leva cerca de 5 minutos no mediano e quase 7 no pior caso** (premissa declarada: envio mediano em torno de 7 Mbit/s; por operadora, de 5,42 a 8,83). Isso não é uma barrinha: é tempo suficiente para a pessoa sair do app, atender uma ligação ou a tela bloquear. **As obrigações da tela de envio estão em `PRODUTO-DETALHADO.md` §7.**

✅ **O envio é retomável sem construirmos nada.** O R2 aceita envio em partes no padrão S3 — com partes de 8 MB, um vídeo de 250 MB vira ~32 pedaços, e uma queda aos 70% custa **um pedaço de 8 MB, não os 175 MB já enviados**. Na prática: **perde 9 segundos, não 3 minutos e meio.**

⚠️ **A borda que virou regra:** envio pela metade é apagado pela Cloudflare em **7 dias**. A tela avisa *"envio pausado — retome até dia X"*.

## 14.2.8 A pegadinha do vídeo, e o que a plataforma faz com ela 🟡

Um arquivo MP4 guarda o índice interno (`moov`) **no fim** do arquivo por padrão. Quando isso acontece, **o navegador da marca baixa os 250 MB inteiros antes de mostrar o primeiro quadro**: 60 a 90 segundos, em vez de 1 a 2.

✅ **No v1: a plataforma verifica no recebimento e registra quantos arquivos chegam assim.** Ler os primeiros bytes custa quase nada, e **o caminho principal da marca é baixar o arquivo** — que é o que ela faz de qualquer forma com um vídeo que vai publicar.

🔵 **Corrigir o arquivo automaticamente fica para depois do v1.** Corrigir não é uma opção: é reprocessar 250 MB de vídeo, com fila, worker, um estado novo entre o envio e a disponibilização, e um caminho de falha próprio. **Constrói-se quando a medição disser que é comum — com dado, não com hipótese.** Se for raro, economizamos um serviço inteiro para sempre.

## 14.2.9 Cair e voltar — a régua não é "o site saiu do ar", é "a prova sumiu" 🔴

Contrato, aceite datado e trilha de auditoria não se refazem.

| Peça | O que se perde | Tempo para voltar | **A cópia de segurança de verdade** |
|---|---|---|---|
| **Banco (Supabase)** | 🔴 tudo o que é prova: contrato, aceite com data e IP, trilha de auditoria | horas | ⚠️ **O plano não basta:** o Pro guarda backup diário por **7 dias**, e a janela de contestação chega a **540 dias**. **O de verdade é nosso: cópia diária cifrada para o R2 e cópia mensal para a Backblaze, guardadas 540 dias.** Custo: dentro do gratuito, o banco tem ~2,4 GB por ano de texto |
| **Arquivos (R2)** | a peça que a marca comprou | — | **Versionamento ligado**, que cobre o risco real: apagar por engano. Durabilidade de onze noves cobre o resto. 🔵 Réplica num segundo fornecedor fica para depois do v1 |
| **Site (Vercel)** | ninguém entra; **nada se perde** — o código está no GitHub | **minutos** | Não precisa |
| **Pagar.me** | não se cobra nem se repassa | fora do nosso controle | **O nosso razão é nosso.** Toda chamada gravada antes e depois, com chave de idempotência, para nunca cobrar duas vezes |

**Os dois números da política:** **perda máxima aceitável de dado: 24 horas** · **tempo para voltar: 4 horas** no banco e **15 minutos** no site.

🔴 **24 horas é frouxo para dado de dinheiro, e existe remédio com preço:** recuperação ponto-a-ponto do Supabase por **US$ 100/mês (R$ 550/mês)**, que leva a perda máxima a **segundos**. **Não no lançamento. O gatilho é o dia em que o volume transacionado no mês passar de R$ 55.000** — quando 24 h de perda vale mais que a assinatura.

## 14.4 O que é construído agora, e o que depende de resposta de terceiro 🟢

**A plataforma inteira pode ser construída e testada sem CNPJ, sem resposta do provedor de pagamento e sem aprovação de rede social.** Isso não é otimismo: é consequência de três decisões de arquitetura já tomadas.

| O que ainda não sabemos | Por que não bloqueia | Como entra depois |
|---|---|---|
| **As taxas reais do provedor** | Nenhuma taxa está escrita no código. Elas vivem numa **tabela de configuração**, e as regras leem de lá — inclusive o piso de comissão (§4.4.1) | Digita-se o número na configuração |
| **Se a antecipação vai existir** | O parcelamento já nasce atrás de **duas chaves desligadas** no painel (§4.2.4). O produto funciona inteiro sem elas | Liga a chave |
| **Se a Meta aprova o aplicativo** | O agregador é o caminho principal (§9.1.1.1), e **não depende de aprovação nenhuma** | A integração própria vira otimização de custo, depois |
| **O regime tributário e a nota fiscal** | A emissão da nota é **do usuário**, não da plataforma. O que a plataforma faz é guardar e exibir | Confirma-se com o contador antes do primeiro contrato pago |

🔴 **A regra de arquitetura que sustenta isso — e ela vale como teste automatizado:**

> **Nenhum valor de negócio é escrito dentro do código.** Taxa, prazo, teto, percentual e limite vivem em configuração. **E nenhuma chamada ao provedor de pagamento acontece dentro da regra de negócio** — ela fala com um adaptador. Trocar de provedor, ou descobrir que a taxa é outra, **é trocar um valor ou uma peça, nunca reescrever o dinheiro.**

**O ambiente de teste do provedor é liberado só com e-mail, sem CNPJ.** Dá para construir e rodar o ciclo inteiro — cobrança, split, retenção, aprovação, repasse, estorno — antes de a empresa existir. **A parede é uma só, e é conhecida: nenhuma cobrança real acontece sem CNPJ.**

## 14.5 Arquivos de entrega: por que a plataforma hospeda 🟢

**A ideia de o criador hospedar o arquivo fora e mandar só o link economiza pouco e custa caro.**

**O que ela economiza:** no lançamento, com 20 contratos por mês, o armazenamento custa **cerca de R$ 1 a R$ 11 por mês**. Não é aí que o dinheiro do projeto está.

**O que ela custa, e é o que decide:**

| Risco | Por quê |
|---|---|
| **A prova evapora** | O arquivo num serviço de nuvem pessoal pode ser apagado, trocado depois da aprovação, ou simplesmente expirar. Numa disputa, a plataforma não tem nada — e o que sustenta a defesa de contestação é justamente **o arquivo datado com identificador próprio** |
| **A marca recebe conteúdo trocado** | Aprovar um link não é aprovar um arquivo. O que estava lá na aprovação pode não ser o que está lá depois |
| **O criador entrega e some** | Sem cópia nossa, a marca pagou e ficou sem nada |
| **Vira trabalho para o usuário** | Pedir para o criador hospedar em outro lugar, gerar link e configurar permissão é jogar burocracia nele porque a plataforma quis economizar R$ 11 |

✅ **A economia real está na regra de retenção, e ela já está decidida (§14.2):** **só o arquivo final aprovado fica 24 meses; brutos e versões recusadas ficam 90 dias.** Isso corta dois terços da conta, sem tirar prova nenhuma — porque a defesa se sustenta no **registro** (briefing congelado, log datado, aprovação com horário e IP), que é texto e custa quase nada.

### 14.5.1 De quando cada relógio começa a contar 🔴

**O prazo não conta do envio do arquivo. Conta do marco do contrato — e essa distinção evita apagar prova de um contrato ainda aberto.**

| Arquivo | O relógio começa | Prazo |
|---|---|---|
| Final aprovado | **na publicação confirmada por API** (o mesmo marco que libera o dinheiro, §8.2) | 24 meses |
| Brutos e versões recusadas | **no fechamento do contrato** | 90 dias |

🔴 **O relógio conta do fechamento para que um contrato longo não perca a própria prova.** Num contrato de três meses, prazo contado do envio apagaria os brutos com o contrato ainda aberto — exatamente quando uma disputa sobre *"pedi ajuste e ele atendeu"* pode acontecer.

### 14.5.2 A trava de exclusão 🔴

**Contrato aberto, disputa aberta ou contestação de cartão em andamento congelam a exclusão de qualquer arquivo do contrato, independentemente da idade dele.** Com janela de contestação que chega a 540 dias, é essa trava que impede a plataforma de apagar a própria defesa.

## 14.3 Suporte: comprado, não construído 🟢

**A ferramenta de atendimento é comprada. A fila operacional é construída. Confundir as duas é o erro caro aqui.**

Com 20 contratos/mês, o volume esperado é de **três a seis chamados por mês**. *O que acontece se um sistema de chamados próprio não existir?* **Nada** — uma caixa de e-mail resolve três chamados. Construir fila, tíquete, SLA, macros e relatório para isso consome semanas que deveriam estar na máquina de dinheiro.

✅ **Decisão: ferramenta de chat com plano gratuito de dois lugares, conversas ilimitadas e aplicativo de celular. Custo zero.** ❌ Solução auto-hospedada está descartada: "de graça" ali significa manter servidor, atualizar, fazer backup e ser o responsável quando cair — troca R$ 0 de licença por horas que uma operação de uma pessoa não tem.

🔴 **O que é construído, e não é opcional:** a **caixa de entrada do operador** — aprovar ou recusar contrato em revisão, o prazo fatal de defesa de contestação, reembolso que falhou, publicação removida antes do prazo, cadastro parcialmente recusado, pedido de análise de valor alto. **Isso não é suporte: é operação que mexe em dinheiro e em estado de contrato.** Nenhuma ferramenta comprada aprova um contrato ou defende uma contestação.

**Quando a decisão vira a outra:** ao chegar o terceiro atendente (o plano gratuito tem dois lugares) e, muito depois, em volume alto — mas mesmo lá continua sendo **comprado**. Nem Fiverr nem Upwork construíram o deles.

⚠️ **O gatilho oculto e mais perigoso:** o dia em que o suporte for feito por alguém que não é o fundador. Aí entra controle de quem vê o quê e trilha de acesso a dado de terceiro — **isso é construção nossa, e não vem de ferramenta nenhuma.**

## 15. Pendências que exigem profissional humano ⚠️

| Tema | Profissional | Bloqueia o quê |
|---|---|---|
| 🔴 **A composição documental de uma transação normal, agora com o número exato:** a marca desembolsa R$ 1.260, o criador recebe R$ 1.080, a plataforma fica com R$ 180. **Quantas notas existem, de quem para quem, e de qual valor?** | Contador | **Primeiro contrato pago** |
| **Os 5% da marca são receita de serviço da INFLUENTZ ou desconto no preço do criador?** Muda a base do Simples e muda quem emite o quê | Contador | Primeiro contrato pago |
| **Retenção de 15 dias do provedor em conta nova:** receita reconhecida na venda ou na liquidação? Afeta o primeiro trimestre inteiro | Contador | Código de pagamento |
| **Chargeback de venda parcelada** revertido integralmente: como estornar a comissão e os juros já tributados de uma transação que atravessou dois exercícios | Contador | Código de pagamento |
| 🔴 **A composição documental de uma transação normal.** Com split na origem, a marca desembolsa R$ 1.200 e recebe uma nota do criador de quanto — R$ 1.200 ou R$ 1.080? E a nota da INFLUENTZ pela comissão, existe? **É a pergunta mais urgente da lista: bloqueia o primeiro contrato pago, não o código.** O contador da primeira marca recusa o lançamento da despesa e o contrato nº 1 já vira problema. Até haver resposta, o contrato em PDF declara a composição do valor | Contador | **Primeiro contrato pago** |
| Regime tributário, retenção de IR sobre comissão, obrigações acessórias | Contador especializado em plataforma digital | Código de pagamento |
| Como lançar a perda de chargeback: despesa do período ou provisão? O fundo de contestação é conta contábil ou só segregação de caixa? | Contador | Código de pagamento |
| Comissão já tributada sobre transação depois revertida — dá para recuperar o tributo sobre receita que deixou de existir? | Contador | Código de pagamento |
| Nota fiscal em contrato revertido: o criador emitiu NF, prestou o serviço, e o banco devolveu o dinheiro. Cancela? Emite devolução? | Contador | Lançamento |
| Repasse que a plataforma absorveu — é despesa dedutível? | Contador | Código de pagamento |
| Custo da antecipação de recebíveis embutido no preço: natureza contábil e tributária | Contador | Código de pagamento |
| Devolução parcial do valor do anúncio pago quando a autorização cai antes dos 12 meses: percentual, proporcionalidade e prazo | Contador | Lançamento |
| **Os juros de parcelamento cobrados do comprador são receita da INFLUENTZ?** Entram na base do Simples? São receita de serviço ou financeira? Muda o preço e muda a nota | Contador | Código de pagamento |
| A nota da INFLUENTZ cobre só a comissão, ou comissão + juros? Como o juro aparece no documento fiscal | Contador | Primeiro contrato pago |
| **Pró-forma antes do pagamento:** que documento é emitido no momento do boleto sem gerar obrigação tributária antecipada, já que o serviço ainda não foi prestado? | Contador | Fatura INFLUENTZ |
| **Boleto pago pela marca em nome do criador:** confirmar que o split não configura pagamento de nota de PJ em conta de PF (risco de ISS/INSS/IRPF retroativo) | Contador | Código de pagamento |
| **Retenção na fonte em contrato B2B de valor alto** quando a marca retém por política própria: quem informa o quê, e como o líquido do criador é preservado | Contador | Cliente corporativo |
| Tarifa de saque paga pela plataforma: despesa dedutível, e tratamento do "receber agora" pago pelo criador | Contador | Código de pagamento |
| **Fator R e o Anexo.** Sem folha, a SLU cai no **Anexo V (15,5%)** em vez do Anexo III (6%). Qual pró-labore vira o Fator R, e a partir de que faturamento compensa? | Contador | Abertura da empresa |
| **CNAE principal:** 7490-1/04 (intermediação) ou 6319-4/00 (serviços de informação na internet)? Muda tributação e ISS | Contador | Abertura da empresa |
| **Base de cálculo com split na origem:** a receita é só a comissão, ou o Fisco pode pretender o GMV? Decide se o teto do Simples é atingido com R$ 288 mil ou com R$ 14 milhões de GMV | Contador | Abertura da empresa |
| **Formalização do criador.** Não existe ocupação de influenciador no MEI (§4.7). Qual caminho a plataforma deve recomendar sem induzir a irregularidade, e a partir de que valor? | Contador | Lançamento |
| **Retenções sobre repasse a criador pessoa física.** Com split na origem, quem retém IR e INSS: a marca, a plataforma, ninguém? **É a que mais pode virar passivo** | Contador | Código de pagamento |
| **Nota fiscal do criador como documento de defesa de chargeback.** Se o repasse for revertido, o que acontece com a nota já emitida? | Contador | Lançamento |
| **Reforma tributária (IBS/CBS):** em que janela o split tributário atinge marketplace de serviços? | Contador | Código de pagamento |
| Termos de Uso, Política de Privacidade, direito de imagem, monitoramento de chat | Advogado | Lançamento |
| Categorias reguladas e proteção de menores (§8.3) | Advogado | Lançamento |
| **A relação criador↔plataforma é de consumo ou B2B?** | Advogado | Redação dos Termos, do cancelamento e da comissão |
| Tela e registro de aceite: o que fica gravado e como se prova | Advogado | Lançamento |
| Aprovação automática por silêncio — sobrevive ao CDC art. 51? | Advogado | Lançamento |
| Base legal e ROPA da fase de convite; prazo de retenção do rascunho; aviso de coleta indireta (LGPD art. 9º) | Advogado | Ferramenta de convite |
| O que é compartilhado com a Pagar.me, quando, e como aparece na Política de Privacidade | Advogado | Código de pagamento |
| Regra interna de acesso do Admin a dado de terceiro, com trilha de auditoria (LGPD art. 46) | Advogado | Lançamento |
| Texto da mensagem de convite: identificação do remetente, origem do contato, opt-out | Advogado | Ferramenta de convite |
| Cláusula de responsabilidade por chargeback: a INFLUENTZ absorve, com exceções (conluio, entrega inexistente) que sobrevivam a questionamento | Advogado | Lançamento |
| Validade do clawback — pode a plataforma debitar saldo futuro do criador por decisão administrativa própria? Precisa de anuência prévia, contraditório, prazo? | Advogado | Lançamento |
| Retenção de dados para defesa × LGPD: a janela de chargeback vai a 540 dias e a defesa exige log de chat, IP e horário de aceite. Qual prazo é defensável? | Advogado | Lançamento |
| Exposição ao MED do Pix: obrigações da plataforma quando um Pix recebido é contestado por fraude | Advogado | Código de pagamento |
| Redação da promessa "a INFLUENTZ garante seu pagamento" — mal escrita, vira obrigação incondicional | Advogado | Lançamento |
| Conectar rede social é tratamento de dado pessoal: base legal do consentimento no Termo, e o que acontece com a métrica quando o criador desconecta ou pede exclusão | Advogado | Tela de conexão |
| **Encarregado de dados (DPO): nome e canal publicados na Política de Privacidade.** Exigência da LGPD, custa uma linha, e não estava em lugar nenhum | Advogado | Lançamento |
| **Estorno à marca quando o criador é recusado definitivamente pelo provedor** — devolver um serviço já prestado precisa de cláusula (MAQUINA §3) | Advogado | Lançamento |
| **Cláusula de permanência mínima da publicação** (§8.2) e a consequência de remover antes do prazo | Advogado | Lançamento |
| **Divulgação dos juros de parcelamento** conforme CDC art. 52 — taxa efetiva, número de parcelas e montante total | Advogado | Checkout |
| **Contrato-quadro corporativo** da conta verificada (§4.3.1.1) — peça jurídica nova | Advogado | Cliente corporativo |
| **Cláusula da obrigação de manter a autorização de anúncio por 12 meses**, e a consequência de retirá-la antes. É responsabilização, não garantia — a redação precisa deixar isso claro | Advogado | Lançamento |
| **Cláusula sobre o material que a marca envia** (foto de produto, kit de mídia): a declaração de titularidade e o limite de uso pelo criador. Escrita em §8.2 e **ainda não revisada por advogado** | Advogado | Lançamento |
| **Cláusula da licença de anúncio pago** e da cobrança retroativa por uso sem autorização (PRODUTO §2) — é cobrança sobre fato passado, precisa de redação que sustente | Advogado | Lançamento |
| 🔴 **Quando a plataforma suspende um contrato por suspeita de lavagem, o que ela faz com o dinheiro?** Devolver ao pagador pode ser completar a lavagem; reter sem cláusula é apropriação. **É a única pergunta desta lista que não tem resposta boa improvisada no dia** | Advogado | Lançamento |
| Contrato de operador de dados com o agregador de métricas, e menção nominal na Política de Privacidade | Advogado | Contratar o agregador |
| Declaração escrita do agregador de que a aprovação da Meta dele cobre o uso pelo cliente final | Advogado | Contratar o agregador |

📌 **A pergunta mais estruturante da lista é a primeira.** Enquanto não houver resposta de advogado, **tratamos a relação como de consumo** — é o cenário mais caro, e preparar-se para ele não custa nada se a resposta vier ao contrário. O STJ aplica o finalismo mitigado, e criador pessoa física costuma ser reconhecido como vulnerável, mesmo prestando serviço profissional.

---

## 16. Nota de reconstrução

Esta v0.4 foi reconstruída a partir do histórico de conversas do projeto, porque o arquivo original da v0.3 vivia apenas em uma conversa avulsa — falha estrutural corrigida com a adoção deste repositório e do `CLAUDE.md`.

Se ao ler alguma seção o Marco reconhecer algo que ficou de fora da v0.3, basta apontar: o Git preserva o histórico e a correção entra como uma nova versão, sem retrabalho.

---

*As referências a legislação e a comportamento de plataformas de pagamento são levantamento de arquitetura, não parecer jurídico ou contábil.*
