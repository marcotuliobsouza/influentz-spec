# PAINEL — INFLUENTZ

> **Esta é a única página que o Marco precisa ler.** Tudo o resto é ferramenta de trabalho minha.
> Se algo importante mudar, muda aqui primeiro.
>
> Atualizado em 08/09/2026 — três decisões suas em aberto, ver abaixo

---

## Onde estamos

**Fase: desenho do produto.** Nada de código ainda, e isso é de propósito — código antes de produto definido é dinheiro jogado fora.

| | |
|---|---|
| ✅ **Pronto** | O que o produto é, como o dinheiro anda, a identidade visual, e o inventário completo de funções |
| 🔨 **Em curso** | Desenhar as telas do primeiro ciclo completo |
| ⏳ **Depois** | Banco de dados → conexões → código → testes |

---

## O que eu preciso de você

**Uma coisa só, e ela não é técnica.**

> ### 🔴 A lista de cold start
> Quantos criadores e quantas marcas atenderiam o seu telefone hoje?

É o único item que nem dinheiro nem engenharia resolvem. Marketplace vazio não tem produto.

**O que eu tirei da sua mesa:** o teto do cartão eu decidi (R$ 2.500, com escadinha — o número foi derivado do risco, não escolhido no chute). Você veta quando quiser.

**O CNPJ é seu, e sua decisão está registrada e é boa:** só no pré-lançamento. O que mudou é a informação, não a decisão — ver o quadro abaixo.

---

## 🎯 A data do CNPJ — informação, não pergunta

Duas coisas que eu descobri e que você precisa saber para escolher a data:

1. **A plataforma não recebe um real sem CNPJ.** O Pagar.me só libera as chaves de produção com empresa aberta. Isso já estava na nossa própria especificação e eu não tinha conectado. **O CNPJ nunca foi sobre Instagram — é sobre o dinheiro existir.**
2. **O Instagram antecipa essa data em cerca de 4 meses**, porque a fila da Meta é mais longa que a do Pagar.me e duas etapas dela não dependem de nenhuma linha de código.

**A conta regressiva, contada para trás a partir do primeiro contrato pago (dia D):**

| Quando | O quê |
|---|---|
| **D − 70 dias** | Abrir a empresa. No mesmo dia: submeter a verificação da Meta e abrir a conta bancária |
| D − 56 | Submeter o credenciamento no Pagar.me |
| D − 42 | **Último dia tolerável.** Depois disso a data D escorrega |
| D − 7 | Um contrato de R$ 50 entre duas contas suas: pago, entregue, aprovado, sacado e estornado. **Ninguém lança sem isso** |

**Formato: SLU, não MEI** — MEI é proibido para intermediação de negócios. Custo: abertura entre R$ 640 e R$ 5.000, contador de R$ 195 a R$ 600 por mês.

⚠️ **A parte que eu preciso dizer mesmo sendo desconfortável:** a economia de adiar não existe de verdade. O contador já era obrigatório antes do código de pagamento por sete motivos que não têm nada a ver com Instagram. Adiar não corta o custo — **empurra ele para o mês do lançamento**, que é o pior momento possível. Quatro semanas de folga custam no máximo R$ 600 e compram uma rodada de correção da Meta.

---

## O que você aprova

Você só decide o que é genuinamente de dono: **gosto, prioridade e apetite de risco.** Sempre que eu te mandar algo, vem com etiqueta dizendo o que é e o que eu preciso.

**Já decidido e travado** (não reabre sem motivo novo):

- Pagamento pelo Pagar.me — Pix, boleto e cartão
- Comissão de 15%, caindo para 8% na recontratação
- Dinheiro fica retido até você aprovar a entrega
- Criador precisa ter 18 anos — exigência legal, não escolha
- Identidade visual: logotipo, símbolo e cores da marca são intocáveis
- Todo usuário tem web, iOS e Android, com função completa

---

## Riscos que eu estou vigiando

| Risco | Situação |
|---|---|
| **Marketplace vazio no lançamento** | 🔴 Depende da sua lista de contatos |
| **Data do CNPJ escorregar** | 🟡 Quadro acima. A conta está feita |
| **Contador** — imposto, retenção, e o regime que muda 15,5% para 6% | 🟡 Precisa de profissional antes do código de pagamento |
| **Advogado** — termos, LGPD, publicidade, cláusula de chargeback | 🟡 Precisa de profissional antes do lançamento |
| **Produto grande demais para ser construído** | 🟢 **Resolvido hoje:** de 170 funções sobraram ~84. Ver abaixo |
| Cartão parcelado pagaria o criador em prestações | 🟢 Travado: 1× sempre, 2× e 3× só com antecipação, 4× nunca |
| Instagram travar por fila da Meta | 🟢 Fornecedor de dados entra no dia 1 como redundância, no plano gratuito |
| Plataforma pagar dinheiro que ainda não recebeu | 🟢 Travado por desenho |

---

## ✂️ O que aconteceu hoje: o produto encolheu pela metade

Você perguntou *"pra que esse trem de convite?"* e cinco funções morreram. Isso me fez procurar o padrão — e o padrão era estrutural: **o time de especialistas que eu montei só sabia acrescentar.** A lista foi de 128 para 177 funções e nunca diminuiu uma vez.

**Criei o especialista que faltava — o cortador** — e mandei ele na lista inteira. Resultado:

| | |
|---|---|
| Estavam escritas | 170 |
| Morreram | 38 |
| Eram a mesma coisa contada duas vezes | 22 |
| Ficaram para depois do lançamento | 23 |
| **Sobrou** | **~84** |

**E ele achou o que ninguém tinha visto: não existia função de avaliação.** O último passo do fluxo — os dois se avaliarem depois do contrato — não tinha número, enquanto tinha sido criado um gerador automático de defesa de contestação para um evento que acontece **uma vez a cada 20 meses**. Também não existia **perfil da marca**: o criador recebia proposta sem tela nenhuma para saber quem estava contratando ele. As duas coisas foram criadas.

---

## O time que trabalha neste projeto

Eu não trabalho sozinho. Existem especialistas com contexto próprio, que eu aciono conforme o caso:

| Especialista | Para quê |
|---|---|
| **Produto** | Caçar o que falta, antes de você ver |
| **Design** | Revisar tela contra a marca, com olhar limpo |
| **Jurídico** | Risco brasileiro: LGPD, publicidade, menor, Banco Central |
| **Financeiro** | Impedir que a plataforma prometa dinheiro que não tem |

*Por que isso importa:* eles revisam meu trabalho **antes** de chegar em você. Quem escreve não pode ser quem corrige a própria prova.

---

## Os documentos, e para que servem

Você não precisa ler nenhum. Estão aqui para eu não perder decisão e para quem entrar depois entender.

| Arquivo | É o quê |
|---|---|
| `docs/SPEC-INFLUENTZ.md` | O que o produto faz |
| `docs/FEATURE-MATRIX.md` | Lista completa de funções — a garantia de que nada falta |
| `docs/MAQUINA-DE-ESTADOS.md` | Como cada coisa muda de situação |
| `docs/PRODUTO-DETALHADO.md` | Campos, métricas e tipos de proposta |
| `docs/DESIGN-SYSTEM.md` | Cor, tipo, componente |
| `docs/METODO-DE-TRABALHO.md` | Como trabalhamos e por quê |
| `docs/marca/` | Os ativos oficiais da marca |

---

## Como pedir qualquer coisa

Fale como você fala. **Não precisa saber o nome técnico de nada.** Se você disser "está feio", "faltou isso", "não entendi esse número" — é informação suficiente. Traduzir isso em trabalho é comigo.
