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
