# PAINEL — INFLUENTZ

> ## 👉 https://claude.ai/code/artifact/e70bb45c-0871-4ba9-a235-33284bcf6137
>
> **O Marco lê a versão publicada, não este arquivo.** Ele trabalha pelo navegador e não abre o repositório — insistir em "está no PAINEL.md" é falar com uma parede.
>
> **Obrigação de toda sessão:** ao mudar algo relevante, atualizar **os dois** — este arquivo e a página publicada, republicando o mesmo endereço.
>
> Atualizado em 10/09/2026.

---

## O que a INFLUENTZ é

Uma marca contrata um criador de conteúdo. A INFLUENTZ **segura o dinheiro** até o trabalho ser entregue e publicado, **confere pela API da rede social** que a publicação existe e está no ar, e só então **libera o pagamento sozinha**. Cobra comissão nisso.

Três coisas fazem a plataforma valer o que cobra:

1. **A marca não paga adiantado para desconhecido.** O dinheiro fica retido.
2. **O criador não é calote.** O dinheiro já está lá antes de ele começar a trabalhar.
3. **As métricas são reais.** Vêm da API oficial da rede, nunca de captura de tela.

---

## 🧭 Onde estamos agora

**Esta seção muda a cada entrega, e é sempre a primeira coisa a olhar.** As outras seções do painel são a explicação completa por trás; esta aqui é o resumo de "para onde meu olho vai primeiro".

### 🔴 Precisa de você agora — só duas coisas, nada mais

> **1. Olhe a tela de contratar, no painel publicado.** Se você fosse a marca, fecharia nessa tela? O que te faria desistir?
>
> **2. A lista de cold start.** Quantos criadores e quantas marcas atenderiam seu telefone hoje? É o único item que nem dinheiro nem engenharia resolvem.

**E um aviso, não pergunta:** separe **R$ 6.800** antes de abrir o CNPJ — R$ 5.000 do fundo de contestação + R$ 1.800 de capital de giro. Está detalhado mais abaixo, em "O dinheiro".

### 🟡 O que mudou nesta rodada — antes → depois

| Assunto | Era | Passou a ser | Por quê |
|---|---|---|---|
| **Fornecedor de métricas** | Agregador pago (Phyllo/Ayrshare), R$ 4.207 a R$ 34.339/mês | **Integração direta e gratuita** com Meta, TikTok e YouTube | O agregador resolvia um problema de tempo de engenharia gastando um dinheiro que você não tem. As três APIs são gratuitas em modo de teste, cobrindo os 50 criadores sem CNPJ |
| **Tarifa de saque do criador** | "A plataforma paga a tarifa" | **O provedor sempre cobra do criador; a plataforma absorve embutindo o valor no próprio pagamento**, não por uma configuração que não existe | Confirmado na documentação oficial: taxa de saque não é configurável, só a comissão é |
| **Trabalho presencial** | Fora do v1 | **De volta ao v1**, liberado por confirmação bilateral dos dois lados — sua solução | "Não tem API" não é o mesmo que "não tem como confirmar". Confirmação bilateral já é o padrão usado em produto físico |
| **Tela do criador** | Não existia | **Nova: extrato por contrato** — bloqueado, aguardando prazo, disponível, enviado | Você pediu para saber exatamente quanto e quando; hoje é a mesma informação que só existia para nós, agora com tela |
| **Quem confere os documentos** | Você, no olho, achando número errado e texto fora de lugar | **Dois conferentes automáticos**, que rodam sozinhos a cada alteração e travam antes de a coisa chegar em você | Detalhe na seção [Os conferentes automáticos](#conferentes) — e eles já pegaram **cinco defeitos reais** na primeira varredura |

### 🟢 Decidido — histórico, não precisa reler

Tudo isso já está fechado e não muda sem motivo novo. A lista completa está na seção "O que está decidido", mais abaixo — aqui só o resumo por assunto: **dinheiro** (comissão, piso, repasse, carteira, estorno) · **produto** (tipos de trabalho, revisões, direitos) · **infraestrutura** (armazenamento, backup) · **cronograma da empresa**.

<a id="conferentes"></a>

## 🛡️ Os conferentes automáticos — para você parar de ser o revisor

**O problema, dito sem enfeite:** as regras do projeto viviam num arquivo de instruções que eu leio no começo de cada sessão. A própria documentação da Anthropic diz que esse arquivo é **conselho, não garantia** — o modelo lê e tenta seguir, e a aderência cai conforme o arquivo cresce. O nosso cresceu muito. **Era por isso que você encontrava o mesmo tipo de erro dez dias seguidos: número que não batia entre um documento e outro, palavra proibida numa tela, texto de desculpa dentro de documento de produto.**

**O que passou a existir:** dois programas curtos que rodam sozinhos, sem depender de eu lembrar.

| Conferente | Quando age | O que trava |
|---|---|---|
| **Conferente de documento** | toda vez que qualquer documento é alterado | Número que não bate com o número travado do projeto · palavra proibida na tela (carteira, saldo, crédito, depositar — as que jogariam a plataforma dentro do Banco Central) · texto de autocrítica dentro de documento de produto |
| **Conferente do painel** | quando a sessão termina | Documento mudar e este painel não acompanhar |

**Prova de que funciona, não promessa:** na primeira varredura eles encontraram **cinco defeitos reais que já estavam publicados** — um deles aqui mesmo neste painel, um parágrafo de desculpa no meio da explicação de dinheiro. Todos corrigidos nesta entrega.

**E a calibragem, que é a parte que costuma ser pulada:** a primeira versão dos conferentes deu **30 alarmes falsos** só na especificação. Alarme falso demais e ninguém olha mais para o alarme. Foram apertados até o critério que vale daqui em diante: **zero aviso em documento correto.** Se algum dia um deles reclamar de algo legítimo, o conserto é o conferente — nunca desligá-lo.

**O que isso muda para você:** você deixa de ser a última linha de defesa. Continua podendo vetar qualquer decisão — mas achar erro de conferência deixou de ser trabalho seu.

---

## Uma data que você precisa saber

**A plataforma não recebe um real sem CNPJ.** Não é sobre Instagram — o provedor de pagamento só libera produção com empresa aberta. A sua decisão de abrir no pré-lançamento continua valendo; o que muda é quando é o pré-lançamento.

Contando para trás a partir do primeiro contrato pago:

| Quando | O quê |
|---|---|
| **70 dias antes** | Abrir a empresa. No mesmo dia: pedir a verificação junto à Meta e abrir a conta bancária |
| **42 dias antes** | Último dia tolerável. Depois disso a data de lançamento escorrega |
| **7 dias antes** | Um contrato de R$ 50 entre duas contas suas — pago, entregue, aprovado, sacado e estornado de verdade |

**Formato: SLU** (empresa de sócio único). MEI é proibido para esta atividade. Abertura entre R$ 640 e R$ 5.000; contador entre R$ 195 e R$ 600 por mês.

**A parte que eu preciso dizer mesmo sendo desconfortável:** a economia de adiar é menor do que parece. O contador já era obrigatório antes do código de pagamento, por sete motivos que não têm nada a ver com Instagram. Adiar não corta o custo — empurra para o mês do lançamento, que é o pior momento.

---

## O dinheiro: quanto custa, quanto precisa entrar, e a partir de que valor vale a pena

**Você estava certo: a conta não estava completa.** Eu tinha te dado o custo de manter a plataforma no ar sem te dar o outro lado — quanto precisa entrar. Refeito inteiro.

### Quanto custa

| Fase | **Por mês** | Uma vez só |
|---|---|---|
| Enquanto só existe desenvolvimento | **R$ 3,33** | — |
| Primeiro contrato de verdade (o seu, no teste) | **R$ 296,21** | R$ 137,50 na Google Play |
| **Lançamento** — 20 contratos/mês | **R$ 307,76** de tecnologia · **até R$ 908 com contador** | — |
| Operação — 1.000 contratos/mês | **R$ 1.607,13** (sem o fornecedor de métricas) | — |

### Quantos contratos por mês pagam a operação

O número do zero a zero conta **tudo**: comissão real, imposto, a tarifa de cada repasse, a taxa do meio de pagamento e o fundo de contestação. Com tudo somado:

| Fase | Comissão | **Contratos/mês para o zero a zero** |
|---|---|---|
| **Lançamento** (primeiros 90 dias) | 9,5% | **17** |
| Em regime | 15% | **9** |

🔴 **E foi por isso que a comissão de lançamento mudou de 7,5% para 9,5%.** A 7,5%, o ponto de equilíbrio seria **25 contratos por mês — acima da sua própria meta de 20**. Você estaria trabalhando no vermelho durante os 90 dias em que tem menos caixa. No cartão, a plataforma ganharia R$ 11 por contrato.

**O que isso custa ao criador fundador:** num contrato de R$ 1.200, ele recebe R$ 1.086 em vez de R$ 1.110. **R$ 24.** E continua sendo quase metade do que Fiverr, Workana e 99Freelas cobram. **Ninguém vai embora por R$ 24; a plataforma quebra por R$ 163 por mês.**

### De cada R$ 180 de comissão, quanto sobra

| A marca paga por | Custo do contrato | **Sobra** |
|---|---|---|
| Boleto | R$ 90,15 | **R$ 89,85** |
| Pix | R$ 99,13 | **R$ 80,87** |
| Cartão | R$ 142,77 | **R$ 37,23** |

**Não é a mesma venda.** É isso que justifica colocar o Pix em destaque no checkout.

### Valor mínimo de proposta: **R$ 150**

Você perguntou se pode alguém oferecer R$ 1,00. Não pode, e o motivo tem número: **cada contrato tem um custo fixo de R$ 4,37** — a tarifa do repasse ao criador e o armazenamento dos arquivos — que não encolhe. Num contrato de R$ 20, a plataforma paga R$ 4,37 para ganhar R$ 3,00.

**R$ 150** é onde o mercado brasileiro já começa (é o piso publicado para 3 Stories de nano influenciador) e cobre o custo em qualquer meio de pagamento.

**E o criador iniciante que quer cobrar R$ 50 por um Story?** Ele não fica de fora: publica **3 Stories por R$ 150** — mesmo preço por peça, contrato viável. A tela avisa isso no momento em que ele digita o valor, não depois.

### Repasse: quem paga a tarifa

**A plataforma.** Cada repasse custa cerca de **R$ 3,67** — R$ 73 por mês no lançamento. Fiverr, Upwork, Hotmart e Kiwify **todas cobram isso do prestador**; nós absorvemos, porque o criador ofertou olhando o líquido e tarifa surpresa é taxa somada no fim.

**Um ajuste:** a varredura junta por criador, não por contrato. Três entregas no mesmo dia = **uma** transferência, não três.

### Carteira: **não existe, para ninguém**

Nem criador, nem marca. O criador tem uma **conta digital regulada pelo Banco Central**, que é dele — o aplicativo só lê. Ele vê **"Meus recebimentos"**; a marca vê **"Meus pagamentos"**, sem nenhuma linha de saldo.

🔴 **E marca com saldo pré-pago — "deposite R$ 5.000 e contrate depois" — nunca vai existir.** Isso é guardar dinheiro de terceiro, e joga a INFLUENTZ dentro da regulação do Banco Central **independentemente do tamanho**. As palavras *carteira*, *saldo*, *crédito* e *depositar* ficam proibidas na interface.

### Estorno: onde o dinheiro cai

| Como a marca pagou | Por onde volta | Prazo |
|---|---|---|
| Pix | **A conta de origem, obrigatoriamente** — o Banco Central não deixa ser outra | minutos |
| Boleto | Conta informada, com o mesmo CPF/CNPJ do pagador | 1 a 2 dias úteis |
| Cartão | O próprio cartão | 🔴 **até 60 dias — prazo do banco, não nosso** |

**Se o repasse já saiu**, a plataforma **não cobra do criador**: paga o fundo de contestação. **Saldo negativo é sempre nosso, nunca dele.**

### O fundo de contestação, e a regra que mais protege você

O fundo junta 5% da comissão — **R$ 114 por mês no lançamento**. Para acumular um único chargeback de R$ 2.500, levaria **dois anos**. Fundo que começa em zero não é proteção, é intenção.

**Decidido:** o fundo **nasce com R$ 5.000** em conta separada, antes da primeira cobrança real — é o dobro do teto de cartão do primeiro degrau. A R$ 3.000 ele nasceria abaixo do próprio piso, e o cartão não poderia existir no dia 1. E — a regra mais importante desta entrega — **o teto de R$ 15.000 no cartão para empresa verificada só liga quando o fundo cobrir R$ 30.000.** Até lá, ela paga por boleto e Pix, sem limite nenhum, que é a rota que empresa grande já usa naturalmente.

**Por quê:** hoje um único chargeback de R$ 15.000 contra um fundo de R$ 114 apagaria treze meses de receita e travaria o saque de todos os criadores. **É o único cenário do produto inteiro capaz de matar a plataforma num evento só.**

### O número que você precisa saber antes de abrir a empresa

> ## Aporte mínimo para abrir a operação: **R$ 6.800**
>
> **R$ 5.000 do fundo de contestação** — que é exatamente o dobro do teto de cartão do primeiro degrau — mais cerca de **R$ 1.800 de capital de giro**, porque **o provedor retém o repasse de conta nova por até 15 dias**: no primeiro mês e meio a plataforma paga custo fixo sem receber comissão.
>
> Não é opinião sobre risco. **É a soma de duas linhas que já estavam nos documentos e que eu nunca tinha somado.**

---

## Métricas: revertido de agregador pago para integração gratuita 🔴

Semana passada eu te disse: *"tem nome: Phyllo/InsightIQ, com Ayrshare de plano B"* — e o preço ficava entre **R$ 4.207 e R$ 34.339 por mês.** Você respondeu, com razão: **isso é surreal para uma startup micro, sem CNPJ, com orçamento escasso.** Eu estava resolvendo o problema errado — evitar três filas de aprovação, que é um custo de *tempo*, gastando um dinheiro que você não tem.

**Corrigido: o v1 conecta direto em cada rede, de graça.**

| Rede | O que confirma | Custo |
|---|---|---|
| Instagram/Facebook | Post existe e está no ar | **R$ 0** — a revisão do app da Meta é processo, não produto pago |
| TikTok | Vídeo existe | **R$ 0** — sem plano pago publicado em lugar nenhum |
| YouTube | Vídeo existe | **R$ 0**, dentro de 10 mil consultas grátis por dia — dá para mais de 300 criadores checados todo santo dia |

🔴 **Você perguntou: "não precisa de CNPJ, infra e código pra integrar, fora a aprovação que pode demorar ou ser recusada?" — você está certo que isso existe, e eu não deixei claro quando.**

| Fase | Precisa de aprovação? | Precisa de CNPJ? |
|---|---|---|
| **Lançamento — até 50 criadores** (seus fundadores) | **Não.** Modo de teste de cada rede, sem revisão nenhuma | **Não** |
| Crescer além de 50 criadores | Sim — Meta (Advanced Access) e TikTok (auditoria, 1 a 2 semanas) | Não — CNPJ é sobre dinheiro, não sobre métrica |

**Fonte:** [Meta for Developers — App Review](https://developers.facebook.com/docs/development/release/) confirma que testar em modo de desenvolvimento não passa por revisão — só quando quiser abrir ao público. [TikTok for Developers](https://developers.tiktok.com/docs/en/getting-started-faq) confirma sandbox de até 50 contas sem auditoria, e auditoria (quando precisar) libera em 1 a 2 semanas.

**Tradução:** hoje, com você e os criadores que topem testar, isso já funciona de graça, sem esperar ninguém aprovar nada. O "preço em tempo" só aparece quando crescer além de 50 criadores — aí sim entram as três aprovações, uma por rede, e cabe recurso se alguma for recusada.

**O agregador não sumiu, só foi guardado.** Quando houver receita e a dor de manter três integrações separadas custar mais que a assinatura, ele volta — trocar é trocar um adaptador, não reescrever o produto.

## O armazenamento aguenta? Testei contra o pior caso

Você perguntou se não vai ser alto "com tanto upload pesado". **Refiz a conta com o dobro do tamanho de arquivo e quase o dobro da quantidade** — 500 MB por arquivo, 5 arquivos por contrato:

| | Lançamento (20 contratos/mês) | Operação (1.000/mês) |
|---|---|---|
| Custo por mês | **R$ 28** | **R$ 1.134** |

**A premissa triplicou e o número saiu de R$ 9 para R$ 28 por mês.** É por isso que eu não me preocupo com essa linha.

**A conta que você pode fazer sozinho, sem me perguntar:**
> contratos por mês × 18 = o acervo em gigas · acervo × 0,081 = o custo em reais por mês

**E o motivo pelo qual isso nunca vira problema:** armazenar um contrato pela vida inteira custa **R$ 1,46**. Aquele contrato rende **R$ 120**. O custo cresce **82 vezes mais devagar** que a receita.

**O que pode explodir é outra coisa, e já está travado:** arquivo sem contrato. **Só existe envio de arquivo dentro de um contrato pago** — sem contrato, não há para onde enviar.

**Uma coisa que eu recusei, e você precisa saber por quê:** comprimir o vídeo entregue economizaria R$ 1.021 por mês na operação — **e entregaria à marca um arquivo pior do que ela comprou.** Em vez disso, a plataforma gera uma **cópia leve só para revisão**: a marca revisa a entrega em segundos gastando 5 MB, e baixa o original só se quiser.

---

## O que está decidido

Você pode derrubar qualquer uma destas a qualquer momento, sem justificar.

**Dinheiro**
- Pagamento por Pix, boleto e cartão, pelo Pagar.me
- **Comissão sai dos dois lados: 10% do criador + 5% da marca.** A marca vê o preço final desde a busca, com os 5% dentro — nunca taxa somada no checkout
- **Comissão de lançamento: 9,5%** nos primeiros 90 dias. Nenhum contrato existe abaixo de **R$ 150**
- **O fundo de contestação nasce com R$ 5.000.** Aporte total para abrir a operação: **R$ 6.800**
- O dinheiro fica retido até a entrega ser confirmada
- **Pix e boleto nunca têm limite.** Só o cartão tem — e o teto de R$ 15.000 da empresa verificada só liga quando o fundo de contestação cobrir R$ 30.000
- 🟡 **Cartão só à vista no v1.** O parcelamento existe escrito e desligado — liga por uma chave quando o Pagar.me responder três perguntas por escrito
- **O repasse é automático**, todo dia útil, junta por criador (não por contrato). **O provedor sempre cobra a tarifa de saque do criador** — a plataforma absorve embutindo o valor no pagamento dele, não por configuração
- **Não existe carteira para ninguém.** O criador vê "Meus recebimentos"; a marca vê "Meus pagamentos", sem saldo
- **Nenhum usuário precisa de CNPJ.** Criador recebe com CPF; marca contrata com CPF ou CNPJ

**Produto**
- Métricas só por API oficial. Sem captura de tela, em lugar nenhum
- **Integração direta e gratuita com Meta, TikTok e YouTube** — não um agregador pago. Custa tempo de engenharia (três aprovações em vez de uma), não dinheiro que você não tem
- **Quatro tipos de trabalho**, e uma pergunta resolve todos: *quem vai publicar?* Três vão para o lançamento
- **Seis campos na tela de contratar.** Direitos são uma frase, não um formulário
- **Duas revisões incluídas, para todo mundo.** Fixo
- **A foto do produto entra no briefing** — o criador precisa ver a embalagem, e é daí que nasce quase todo pedido de ajuste
- **A caixinha de anúncio pago entrega a chave, não só cobra:** conceder a autorização no Instagram e no TikTok vira condição para o criador receber
- Criador precisa ter 18 anos — exigência legal, não escolha
- Todo usuário tem web, iOS e Android, com função completa
- **Agência fica para depois do lançamento — inteira.** No v1 ela não assinaria, não pagaria, não receberia e não aceitaria termos: sobraria olhar
- **Trabalho presencial entra no v1**, liberado por confirmação bilateral (os dois lados confirmam no app que o serviço aconteceu)
- **Entrega em etapas fica para depois.** Ninguém fica sem saída: Pix e boleto não têm teto, e um contrato de R$ 4.800 é um Pix só
- Contrato recorrente fica para depois do lançamento

**Marca**
- Logotipo, símbolo e cores são intocáveis
- Fundo de página claro; o rosa é destaque, não papel de parede

---

## Riscos que eu estou vigiando

| Risco | Situação |
|---|---|
| **Marketplace vazio no lançamento** | 🔴 Depende da sua lista de contatos |
| **A data do CNPJ escorregar** | 🟡 A conta regressiva está acima |
| **Contador** — imposto, retenção, e o regime que muda 15,5% para 6% | 🟡 Antes do código de pagamento |
| **Advogado** — termos, LGPD, publicidade, chargeback | 🟡 Antes do lançamento |
| **Meta/TikTok recusarem a revisão do app** | 🟡 É por isso que usamos o modo de teste (50 criadores) enquanto isso não é aprovado. Cabe recurso, mas cada rodada reinicia o relógio |
| Preço do fornecedor de métricas | 🟢 Deixou de existir como risco — a rota do v1 agora é gratuita |
| Plataforma pagar dinheiro que ainda não recebeu | 🟢 Impossível por desenho |
| Produto grande demais para ser construído | 🟢 91 funções, em três fatias |
| Produto complicado demais para um cliente leigo usar | 🟢 Cortado. Seis campos na tela de contratar |
| Depender de resposta do Pagar.me ou da Meta para construir | 🟢 Não depende. Nenhuma taxa está no código, e a integração de métrica é nossa, direta com cada rede |

---

## Quem trabalha neste projeto

| Especialista | Para quê |
|---|---|
| **Produto** | Caminhar o produto inteiro e achar onde ele quebra |
| **Financeiro** | Impedir que a plataforma prometa dinheiro que não tem |
| **Jurídico** | Risco brasileiro: LGPD, publicidade, Banco Central |
| **Design** | Revisar tela contra a marca, com olhar limpo |
| **Cortador** | Matar o que não deveria existir. É o único que pode deletar |
| **Antifraude** | Pensar como o golpista antes dele. Achou uma rota de lavagem que o nosso próprio desenho estava abrindo |
| **Arquiteto de produto** | **Coordena o time.** Resolve briga entre especialistas e responde se o produto está de pé como um todo |
| **Infraestrutura** | Quanto custa, quanto aguenta, o que acontece quando cai. Todo número dele tem unidade e período |

Eles revisam meu trabalho **antes** de chegar em você. Quem escreve não corrige a própria prova — e o cortador existe porque os outros só sabiam acrescentar.

**O time acima cuida do produto. Faltava o time de código — e esse eu criei agora, antes de precisar dele:**

| Especialista novo | Para quê | Quando entra |
|---|---|---|
| **Arquiteto técnico** | Estrutura de pastas, modelo de dados, como trocar de fornecedor sem reescrever tudo | Antes da primeira linha de código |
| **QA — estratégia** | Decide o que precisa de teste automatizado (tudo que mexe em dinheiro) e o que não precisa | Antes de cada fatia ser construída |
| **DevOps** | Ambiente de teste, ambiente de produção, e quando trocar um pelo outro em cada fornecedor | Antes do primeiro deploy |
| **Desenvolvedor fullstack** | Implementa o que os anteriores já decidiram | Fase de código |

**Nenhum desses exigiu você instalar nada.** São arquivos de texto no repositório — pesquisados na documentação oficial da Anthropic e em dois repositórios públicos de referência para saber o padrão certo, não inventados por mim sozinho.

🟡 **A resposta sobre "mais especialista" mudou de figura.** Para o produto, a resposta continua sendo não — faltava processo, não gente. Para o código, que ainda nem começou, **sim, faltava**, e agora está pronto antes de precisar. Continua valendo o portão de entrega: nove perguntas antes de qualquer coisa chegar em você, começando por *"o assunto está inteiro, ou é uma fatia?"*. Se eu falhar, **você devolve sem ler**.

---

## Os documentos

Você não precisa ler nenhum. Estão aqui para eu não perder decisão.

| Arquivo | É o quê |
|---|---|
| `docs/SPEC-INFLUENTZ.md` | O que o produto faz |
| `docs/FEATURE-MATRIX.md` | As 91 funções do lançamento |
| `docs/MAQUINA-DE-ESTADOS.md` | Como cada coisa muda de situação |
| `docs/PRODUTO-DETALHADO.md` | Campos, métricas e tipos de proposta |
| `docs/DESIGN-SYSTEM.md` | Cor, tipo, componente |
| `docs/METODO-DE-TRABALHO.md` | Como trabalhamos |
| `docs/HISTORICO.md` | O rastro das decisões. Existe para o registro, não para leitura |
| `docs/marca/` | Os ativos oficiais da marca |

---

## Como pedir qualquer coisa

Fale como você fala. **Não precisa saber o nome técnico de nada.** "Está feio", "faltou isso", "não entendi esse número", "isso me deixou inseguro" — é informação suficiente. Traduzir em trabalho é comigo.
