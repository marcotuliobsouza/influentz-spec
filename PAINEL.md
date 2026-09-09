# PAINEL — INFLUENTZ

> ## 👉 https://claude.ai/code/artifact/e70bb45c-0871-4ba9-a235-33284bcf6137
>
> **O Marco lê a versão publicada, não este arquivo.** Ele trabalha pelo navegador e não abre o repositório — insistir em "está no PAINEL.md" é falar com uma parede.
>
> **Obrigação de toda sessão:** ao mudar algo relevante, atualizar **os dois** — este arquivo e a página publicada, republicando o mesmo endereço.
>
> Atualizado em 09/09/2026.

---

## O que a INFLUENTZ é

Uma marca contrata um criador de conteúdo. A INFLUENTZ **segura o dinheiro** até o trabalho ser entregue e publicado, **confere pela API da rede social** que a publicação existe e está no ar, e só então **libera o pagamento sozinha**. Cobra comissão nisso.

Três coisas fazem a plataforma valer o que cobra:

1. **A marca não paga adiantado para desconhecido.** O dinheiro fica retido.
2. **O criador não é calote.** O dinheiro já está lá antes de ele começar a trabalhar.
3. **As métricas são reais.** Vêm da API oficial da rede, nunca de captura de tela.

---

## Onde estamos

**Fase: desenho do produto.** Nada de código ainda, e isso é de propósito — código antes de produto definido é dinheiro jogado fora.

| | |
|---|---|
| ✅ **Pronto** | O que o produto faz, como o dinheiro anda, a identidade visual, e as 97 funções do lançamento |
| ✂️ **Cortado** | O produto pedia coisa demais de quem usa. Tela de contratar de ~25 campos para **6**; direitos de 7 campos para **1**; dez tipos de trabalho para **4** |
| 🔨 **Agora** | **A tela de contratar**, publicada e revisada, esperando o julgamento do Marco antes de autorizar o resto |
| ⏳ **Depois** | Banco de dados → conexões → código → testes |

---

## O que eu preciso de você

**Duas coisas, e nenhuma delas é técnica.**

> ### 1. Olhe a tela de contratar, no painel publicado
> **Se você fosse a marca, você fecharia nessa tela? O que te faria desistir?**
>
> Você não precisa aprovar onze telas para dizer se o produto está de pé — precisa ver uma. Se estiver de pé, sigo para as outras. Se não, refaço agora, que é quando é barato.

> ### 2. A lista de cold start
> Quantos criadores e quantas marcas atenderiam o seu telefone hoje?

Marketplace vazio não tem produto. É o único item que nem dinheiro nem engenharia resolvem.

**O que você não precisa fazer:** ler documento técnico, auditar especificação, procurar o que falta, escolher número. Se eu te mandar uma pergunta que eu conseguiria responder pesquisando, me corrija.

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

## Quanto custa manter a plataforma no ar

**Você perguntou se os valores de armazenamento eram por mês, por ano ou por giga. A pergunta era justa — os números saíam sem unidade, o que é o mesmo que não sair. Refiz a conta inteira. Agora toda linha tem unidade e período.**

| Fase | **Por mês** | Uma vez só |
|---|---|---|
| Enquanto só existe desenvolvimento (nenhuma cobrança real) | **R$ 3,33** — é o domínio, diluído em 12 meses | — |
| Primeiro contrato de verdade (o seu, no teste) | **R$ 296,21** | R$ 137,50 na Google Play |
| **Lançamento** — 20 contratos por mês | **R$ 307,76** | — |
| Operação — 1.000 contratos por mês | **R$ 1.607,13** (sem o fornecedor de métricas) | — |

**Isso é só tecnologia.** Com o contador, o lançamento fica entre **R$ 503 e R$ 908 por mês**. **De 2 a 5 contratos por mês pagam a tecnologia** e de 5 a 13 pagam tudo, dependendo do ticket. A meta de 20 paga o conjunto em qualquer cenário.

**Duas coisas que eu preciso corrigir para você:**

1. 🔴 **Eu te disse que o fornecedor de métricas tem plano gratuito de 250 contas. Isso não está publicado em lugar nenhum.** Fui à página oficial de preços e ela só oferece orçamento sob medida. **A escolha do fornecedor continua certa** — uma integração em vez de três, sem fila de aprovação, sem exigir CNPJ. **O que não está provado é o "R$ 0".** Falta um e-mail pedindo o número por escrito, não uma decisão nova.

2. 🔴 **E a pergunta a fazer antes do preço é maior que o preço:** *a cobrança é por conta conectada ou por consulta?* Conferir que a publicação continua no ar gera cerca de **90 mil consultas por mês** na fase de operação. **Se for por consulta, essa linha sozinha custa mais que toda a infraestrutura junta.** Já cortei 79% dessas consultas mudando a frequência da checagem, sem perder nada.

**O que eu descobri e não estava na conta:** conta de desenvolvedor da Apple (US$ 99 por ano), Google Play (US$ 25, uma vez), e **cópia de segurança de verdade do banco de dados** — o plano guarda backup por 7 dias, e a janela em que uma marca pode contestar uma compra chega a **540 dias**. Aqui a régua não é "o site saiu do ar", é **"a prova sumiu"**. Cópia própria, diária e cifrada, cabe no plano gratuito e passa a ser obrigatória.

**E o plano gratuito da Vercel proíbe uso comercial** — a definição inclui "qualquer método de solicitar ou processar pagamento". **O seu primeiro Pix de teste já dispara isso.** Não é volume, é cláusula.

**Uma coisa que o criador vai sentir:** subir um vídeo de 250 MB pelo 4G leva **quase 5 minutos**. A tela de envio tem quatro obrigações: mostrar MB de MB, deixar sair da tela sem cancelar, **retomar de onde parou** em vez de recomeçar do zero, e confirmar no fim com data, hora e identificador — que é o que vira prova.

---

## O que está decidido

Você pode derrubar qualquer uma destas a qualquer momento, sem justificar.

**Dinheiro**
- Pagamento por Pix, boleto e cartão, pelo Pagar.me
- **Comissão sai dos dois lados: 10% do criador + 5% da marca.** A marca vê o preço final desde a busca, com os 5% dentro — nunca taxa somada no checkout
- O dinheiro fica retido até a entrega ser confirmada
- **Pix e boleto nunca têm limite.** Só o cartão tem, e empresa verificada entra em R$ 15.000 no primeiro dia
- 🟡 **Cartão só à vista no v1.** O parcelamento existe escrito e desligado — liga por uma chave quando o Pagar.me responder três perguntas por escrito
- **O repasse é automático**, todo dia útil, com a tarifa por nossa conta
- **Nenhum usuário precisa de CNPJ.** Criador recebe com CPF; marca contrata com CPF ou CNPJ

**Produto**
- Métricas só por API oficial. Sem captura de tela, em lugar nenhum
- **Um fornecedor único de métricas**, que já tem as aprovações das três redes — em vez de três integrações nossas com três filas de aprovação
- **Quatro tipos de trabalho**, e uma pergunta resolve todos: *quem vai publicar?*
- **Seis campos na tela de contratar.** Direitos são uma frase, não um formulário
- **Duas revisões incluídas, para todo mundo.** Fixo
- **A foto do produto entra no briefing** — o criador precisa ver a embalagem, e é daí que nasce quase todo pedido de ajuste
- **A caixinha de anúncio pago entrega a chave, não só cobra:** conceder a autorização no Instagram e no TikTok vira condição para o criador receber
- Criador precisa ter 18 anos — exigência legal, não escolha
- Todo usuário tem web, iOS e Android, com função completa
- Agência e contrato recorrente ficam para depois do lançamento

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
| Instagram travar em fila da Meta | 🟢 Fornecedor de dados entra no dia 1 e não depende de aprovação nenhuma |
| **Preço do fornecedor de métricas** | 🟡 Não publicado. É a maior incerteza da conta na operação — falta o número por escrito, e a unidade de cobrança |
| Plataforma pagar dinheiro que ainda não recebeu | 🟢 Impossível por desenho |
| Produto grande demais para ser construído | 🟢 97 funções, em três fatias |
| Produto complicado demais para um cliente leigo usar | 🟢 Cortado. Seis campos na tela de contratar |
| Depender de resposta do Pagar.me ou da Meta para construir | 🟢 Não depende. Nenhuma taxa está no código, e as métricas vêm de fornecedor único |

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

Eles revisam meu trabalho **antes** de chegar em você. Quem escreve não corrige a própria prova — e o cortador existe porque os outros quatro só sabiam acrescentar.

---

## Os documentos

Você não precisa ler nenhum. Estão aqui para eu não perder decisão.

| Arquivo | É o quê |
|---|---|
| `docs/SPEC-INFLUENTZ.md` | O que o produto faz |
| `docs/FEATURE-MATRIX.md` | As 97 funções do lançamento |
| `docs/MAQUINA-DE-ESTADOS.md` | Como cada coisa muda de situação |
| `docs/PRODUTO-DETALHADO.md` | Campos, métricas e tipos de proposta |
| `docs/DESIGN-SYSTEM.md` | Cor, tipo, componente |
| `docs/METODO-DE-TRABALHO.md` | Como trabalhamos |
| `docs/HISTORICO.md` | O rastro das decisões. Existe para o registro, não para leitura |
| `docs/marca/` | Os ativos oficiais da marca |

---

## Como pedir qualquer coisa

Fale como você fala. **Não precisa saber o nome técnico de nada.** "Está feio", "faltou isso", "não entendi esse número", "isso me deixou inseguro" — é informação suficiente. Traduzir em trabalho é comigo.
