# Método de Trabalho — INFLUENTZ

> **Por que este documento existe.** O Marco perguntou: *"eu não sei o que você quer de mim nesse que você está me mandando."*
>
> Isso é falha de processo minha. Eu vinha entregando coisas sem dizer **o que aquilo é**, **em que fase está** e **o que eu preciso dele**. Sem isso, ele não tem como avaliar — e acaba apontando como falha algo que ainda nem deveria estar pronto, ou aprovando algo achando que está pronto quando não está.
>
> Este documento resolve isso de forma permanente.
>
> **Versão:** v1.0

---

## 1. O erro que este documento corrige 🔴

Um estudo de produto sério não entrega "telas". Ele entrega **fases**, cada uma com um **portão de aprovação**. O Marco já tinha isso escrito, em `DESENVOLVIMENTO PLATAFORMA COMPLETA INFLUENTZ ESTRUTURA.docx`, no Drive dele — documento que eu **não tinha lido** quando comecei a desenhar.

Resultado: eu pulei da Fase 0 direto para a Fase 4. As fases que eu pulei são exatamente as que garantem que **nada falta**. Por isso o Marco vinha encontrando buracos — não por falta de atenção dele, mas por ausência das fases que existem para fechar buracos.

---

## 2. As 8 fases, e onde nós realmente estamos 🟢

| Fase | O que ela entrega | Estado real |
|---|---|---|
| **0 — Descoberta** | O que o produto é, quem usa, quais módulos, o que ele **não** é | 🟡 parcial (SPEC existe, mas não bate com a Constituição do Drive) |
| **1 — Arquitetura** | Mapa das superfícies: Brand Web, Creator App, Agency Web, Admin Web. Que tela mora onde | 🔴 **não feita** |
| **2 — Feature Matrix** | Inventário **completo** de funções, por papel e por módulo | 🔴 **não feita** |
| **3 — Priorização** | O que entra agora, o que entra depois | 🟡 parcial |
| **4 — Wireframes** | Estrutura das telas, sem visual final | 🟡 10 telas de ~40 |
| **5 — Foundation** | Base visual: shell, sidebar, cards, botões, estados, tokens | 🟡 tokens sim, componentes não |
| **6 — UI final** | Visual premium por tela | 🟡 2 telas |
| **7 — Implementação** | Código | 🔴 não iniciada |
| **8 — QA** | Bugs, estados quebrados, acessibilidade, performance | 🔴 não iniciada |

⚠️ **A Fase 2 é a que responde "não pode faltar nada".** Enquanto ela não existir, qualquer tela que eu desenhar é chute educado — e o Marco vai continuar, com razão, encontrando ausências.

---

## 3. O contrato de entrega 🟢

**Regra permanente: toda entrega minha vem com este cabeçalho, sem exceção.**

```
O QUE É:        [wireframe / UI final / documento / protótipo]
FASE:           [0 a 8]
ESTADO:         [rascunho para reagir / pronto para aprovar]
O QUE OLHAR:    [exatamente onde o Marco deve prestar atenção]
O QUE IGNORAR:  [o que ainda está cru de propósito]
O QUE PRECISO:  [aprovar? escolher entre A e B? só ler?]
SE APROVADO:    [o que eu faço em seguida]
```

**Por que "o que ignorar" é tão importante quanto "o que olhar":** wireframe é feio de propósito. Se eu não avisar, o Marco gasta energia reclamando de cor numa fase em que cor ainda não existe — e eu gasto energia consertando o que não era para estar pronto.

---

## 4. Os três estados de uma entrega 🟢

| Estado | O que significa | O que o Marco faz |
|---|---|---|
| 🔵 **Rascunho para reagir** | Estou pensando alto. Pode estar errado | Reage, aponta, corrige o rumo |
| 🟡 **Pronto para aprovar** | Terminei. Acho que está certo | Aprova ou reprova com motivo |
| 🟢 **Aprovado e travado** | Não reabre sem motivo novo | Nada. Está fechado |

⚠️ **Nada avança de fase sem estar 🟢.** Foi por não ter isso que a Fase 4 começou com a Fase 2 em branco.

---

## 5. Quem faz o quê 🟢

Herdado do documento do Marco, adaptado à realidade de hoje:

| Papel | Quem | Responsabilidade |
|---|---|---|
| Product lead, UX lead, UI lead, arquitetura, benchmark, priorização | **Claude** | Toda decisão técnica, de produto e de design. Pesquisar antes de decidir. Nunca deixar o Marco descobrir uma lacuna |
| Implementação, build, testes | **Claude Code** | Código, quando chegarmos lá |
| Decisão estratégica, visão de negócio, aprovação | **Marco** | Aprovar ou reprovar. Dar rumo. **Não precisa saber como se faz** |

**O que isso significa na prática:** quando o Marco diz *"tem que ter calendário"*, isso é matéria-prima. Meu trabalho não é implementar a frase literal — é pesquisar como plataformas sérias resolvem gestão de agenda, decidir o formato certo, e trazer pronto. Se eu voltar perguntando *"que tipo de calendário você quer?"*, eu falhei.

---

## 5.0 O protocolo de decisão — a correção definitiva 🔴

Adotado em 08/09/2026, depois de o Marco escrever: *"Pq vc toda hora deixa a bomba em minha mao? Eu nao deveria ter q pensar nisso... sua metodologia ta certa mesmo para desenvolver a influentez? Se nao, corrija e de forma defnitiva."*

**Diagnóstico honesto do defeito.** O método dizia "só levar ao Marco o que for decisão de dono: gosto, prioridade e apetite de risco". A expressão **"apetite de risco" virou uma porta dos fundos**: todo parâmetro numérico que eu não queria escolher — teto de cartão, prazo de reserva, percentual de fundo — saía por ela com carimbo de "decisão de dono". Não era. Era trabalho meu não feito, embrulhado como consulta.

**Por que isso é grave e não é detalhe de estilo.** O Marco disse desde o primeiro dia que é leigo. Uma pergunta como *"quanto você aceita perder numa contestação?"* não tem resposta possível para quem não conhece a taxa de chargeback do mercado, o limite das bandeiras nem a margem da comissão. Perguntar assim **não consulta: paralisa**. E o projeto para até ele responder.

🟢 **A regra que substitui, em três categorias.** Ela vive em `CLAUDE.md` §2.1, que é lido em toda sessão:

| | O que é | Como chega nele |
|---|---|---|
| **A** | Técnico e de construção | Não chega. É meu |
| **B** | **Parâmetro com referência de mercado** — teto, percentual, prazo, fornecedor, ordem de construção | Chega **já decidido**, em uma linha, com a fonte. Ele veta quando quiser |
| **C** | **Dinheiro do bolso dele · a lista de contatos dele · gosto de marca · quando lançar · matar uma funcionalidade** | Pergunta curta, com a minha recomendação já escrita |

🔴 **O teste que eu aplico antes de mandar qualquer pergunta:** *"eu conseguiria decidir isso pesquisando?"* Se sim, a pergunta não sai — a decisão sai.

🔴 **Teto de perguntas por entrega: duas.** Se passar disso, o problema é meu.

📌 **O que isso não é.** Não é decidir por cima dele. Todo padrão da categoria B vem com a fonte à vista e pode ser vetado sem justificativa. A diferença é que **a plataforma anda enquanto ele não veta**, em vez de esperar.

---

## 5.1 O portão obrigatório — nenhuma regra chega ao Marco sem revisão 🔴

Adotado em 08/09/2026, depois de uma falha minha: eu criei o time de especialistas e, na entrega seguinte, **decidi duas regras sozinho** — verificação manual de rede social e reserva de 90 dias contra contestação. O Marco recusou as duas. Ele estava certo, e o erro não foi o conteúdo: foi **ter decidido sem passar pelo especialista que existia para isso**.

🟢 **Regra:** antes de qualquer regra virar texto em documento, ela passa pelo especialista da área. Sem exceção, sem "esse caso é simples".

| Se a regra envolve… | Passa por | Antes de |
|---|---|---|
| Cobrança, retenção, repasse, prazo, estorno, contestação, comissão | `financeiro` | Escrever na SPEC §4 ou na máquina de dinheiro |
| Campo, estado, fluxo, caminho de exceção, o que falta | `produto` | Desenhar tela e antes de pedir aprovação |
| O que vira cláusula, termo, consentimento, dado pessoal, publicidade, menor | `juridico-br` | Escrever a regra |
| Tela, cor, ícone, contraste, coerência visual | `design` | Mostrar ao Marco |

**E toda entrega passa a declarar quem revisou.** No cabeçalho da entrega, uma linha:

> *Revisado por: `financeiro` (pesquisa de provedor) · `juridico-br` (aceite de termos)*

Se essa linha estiver vazia, a entrega não está pronta — e o Marco pode devolver sem ler.

**Por que isso resolve o que ele reclamou:** a queixa dele foi *"sempre preciso te guiar"*. Guiar é apontar o que falta. Se o especialista aponta antes, ele não precisa apontar depois. O portão existe para transferir o trabalho de achar erro de volta para mim.

---

## 6. A regra que eu assumo como permanente 🔵

Adotada do próprio documento do Marco (§8 de `DESENVOLVIMENTO PLATAFORMA...`), porque ela está certa:

1. Fazer benchmark por conta própria.
2. Pensar features por conta própria.
3. Propor diferenciais sem ser pedido.
4. Elevar o produto ao nível mais alto que eu conseguir.
5. **Não depender do Marco repetir isso toda vez.**

E uma sexta, que eu acrescento por causa do que aconteceu:

6. **Antes de produzir, verificar o que já existe** — no repositório e no Drive. Duas fontes de verdade que se contradizem custam mais caro que qualquer tela feia.

---

## 7. Sobre marcar o que é de quem 🔴

Pergunta do Marco: *"não sei se essa visão é da marca, do criador ou da agência."*

Isso é um defeito real das telas atuais. Num produto com quatro superfícies, **toda tela precisa declarar de quem ela é** — no próprio desenho, não só no meu texto.

🟢 **Regra adotada:** todo artboard leva um selo de superfície no canto: `BRAND WEB` · `CREATOR APP` · `AGENCY WEB` · `ADMIN WEB`. E o canvas passa a ser organizado por superfície, não por ordem de jornada misturada.

---

## 7.1 A metodologia está certa? — pergunta do Marco, com pesquisa 🟢

> *"preciso saber a metodologia para que não percamos meses e milhares de reais, se sua metodologia já está certa diante de devs profissionais que usam IA para fazer apps e plataformas de sucesso."*

Pergunta justa. Fui pesquisar em vez de me defender.

### A metodologia que usamos tem nome, e é o padrão de 2026

Chama-se **Spec-Driven Development** (desenvolvimento guiado por especificação). A definição: **a especificação versionada é a única fonte de verdade — não o código.** A spec é o produto; o código é o resultado dela, como um arquivo-fonte que vira programa.

Não é teoria. O GitHub abriu o **Spec Kit**, uma ferramenta que força agentes de IA a escrever a especificação antes do código, em **quatro fases com portão** — não se avança sem validar a anterior. Passou de 80 mil estrelas desde o lançamento e funciona com mais de 24 agentes, incluindo o Claude Code.

**O número que responde a preocupação do Marco:** o GitHub relata que times usando esse método refazem trabalho do zero **cerca de dez vezes menos** que quem trabalha por conversa solta. Relatos da comunidade apontam **60% a 80% menos retrabalho**.

**Por que o método existe:** ele nasceu em 2025 como resposta direta ao fracasso do "vibe coding" — pedir código conversando com a IA. O padrão de falha é sempre o mesmo: o agente produz código plausível que **desvia da intenção**, inventa funções que não existem, e apodrece conforme o projeto cresce.

✅ **Nosso `CLAUDE.md` §4 já dizia "Spec-Driven Development" desde o primeiro dia.** Estamos no método certo. E o `docs/` deste repositório é exatamente a spec versionada que o método exige.

*Fontes:* [GitHub — Spec Kit](https://github.com/github/spec-kit) · [Spec-Driven Development: guia 2026](https://www.thebcms.com/blog/spec-driven-development/)

### O Marco precisa de um orquestrador separado, como ChatGPT + Codex? 🔴 Não. E o motivo importa

Ele descreveu o arranjo anterior: ChatGPT como orquestrador e arquiteto, Codex como executor. É um padrão real. Mas a pesquisa mostra o custo dele, e nós vivemos esse custo esta semana.

⚠️ **Toda passagem de bastão entre ferramentas perde informação.** Em raciocínio de várias etapas, com o mesmo orçamento de pensamento, **um agente único empatou ou superou o arranjo multiagente** — porque cada transferência perde o que um contexto único teria mantido. Resumo é sempre incompleto, e as decisões implícitas dentro do trabalho de outro **não sobrevivem à passagem**.

**A prova disso está neste projeto.** Existia um corpo inteiro de decisões de produto que eu só descobri semanas depois, por acaso, varrendo o Drive. Não foi falta de capacidade de ninguém — foi a passagem de bastão perdendo informação, exatamente como a pesquisa descreve.

**O padrão que a pesquisa aponta como certo para 2026:**

> **um agente principal é dono do plano e da integração; subagentes especializados cuidam de tarefas fechadas, cada um com seu próprio contexto.**

É literalmente o que já fazemos: eu sou dono do plano, e quando precisei revisar os wireframes contra o sistema de design, abri um subagente com contexto limpo para não corrigir a minha própria prova. Subagentes nativos cobrem cerca de 80% da necessidade de orquestração; ferramenta externa só se justifica quando a complexidade não cabe num prompt de orquestração.

*Fontes:* [Multi-Agent Orchestration: padrões que funcionam em 2026](https://www.digitalapplied.com/blog/multi-agent-orchestration-5-patterns-that-work) · [Claude Code Agent Teams e Subagents — playbook 2026](https://www.developersdigest.tech/blog/claude-code-agent-teams-subagents-2026)

### 🔴 O que realmente faz um projeto perder meses e milhares de reais

Não é a escolha de ferramenta. É esta, e nós já tropeçamos nela:

> **A fonte de verdade viver numa conversa ou num Drive, em vez de viver no repositório.**

Conversa acaba. Contexto de chat se perde. Pasta de Drive não tem histórico de decisão. Repositório tem versão, tem histórico e é lido automaticamente no começo de toda sessão.

🟢 **Regra permanente, e é a que mais economiza dinheiro deste projeto:**

**Nenhuma decisão importante existe até estar num arquivo deste repositório.** Se foi decidido numa conversa e não entrou em `/docs`, não foi decidido.

### Resumo honesto da resposta

| Pergunta do Marco | Resposta |
|---|---|
| A metodologia está certa? | **Sim.** Spec-Driven Development, o padrão de 2026, já declarado no nosso `CLAUDE.md` desde o início |
| Precisa de orquestrador separado? | **Não.** Um agente dono do plano + subagentes para tarefas fechadas é o padrão. Ferramenta a mais adiciona perda na passagem de bastão |
| O que fazia perder tempo? | Fonte de verdade fora do repositório. Corrigido |
| O que ainda falta no método? | Os portões de aprovação por fase, que este documento acabou de instituir |

---

## 8. Onde cada coisa vive 🟢

| Fonte | O que é |
|---|---|
| **Este repositório** (`/docs`) | Fonte de verdade viva. Tudo que decidimos entra aqui |
| **Drive — `00_CLEAN_ROOM_PRODUCT_ENGINEERING`** | Corpo de trabalho anterior (agosto/2026): Constituição, Registro de Decisões, jornadas, papéis. **Tem decisões APROVADAS que o repositório ainda não reflete** |
| **Drive — `MARKETING/BRANDING`** | Ativos de marca. Já espelhado em `/docs/marca` |
| **Canvas do Claude Design** | Telas. Não é fonte de verdade — é reflexo do que está nos documentos |

⚠️ **Enquanto as duas primeiras não forem reconciliadas, nenhuma tela nova deve ser desenhada.** Ver `CONFLITOS-A-RESOLVER.md`.

---

*Documento de processo. Vale a partir de hoje e não expira.*
