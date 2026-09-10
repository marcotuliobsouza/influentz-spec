# Sistema de Design — INFLUENTZ

> Base: identidade visual desenvolvida por agência em 2020. **O guia original agora vive neste repositório**, em `docs/marca/Guia da Marca - Influentz (2020).pdf` (33 páginas), e não só no Google Drive.
> Este documento traduz aquele guia em regras técnicas prontas para implementação em shadcn/ui.
>
> **Versão:** v0.4
> **O que mudou da v0.3:** as duas divergências que estavam aguardando decisão foram **decididas** — fundo de página em §3.0.1 e terminologia da interface em §10.2. A decisão de fundo **reverte a recomendação que este próprio documento fazia na v0.3**, com o motivo registrado.
>
>
> **Legenda:** 🟢 definido · 🟡 em aberto · 🔵 proposta de Claude além do pedido · ⚠️ correção ou risco

---

## 1. Conceito (herdado do guia original) 🟢

Símbolo = "play" de vídeo, representando o ambiente de trabalho do criador de conteúdo.
Tipografia com letras minúsculas remete à linguagem das redes sociais.

---

## 2. Duas vozes, uma identidade 🟢

| Contexto | Voz | Regra |
|---|---|---|
| Marketing, onboarding, produto (telas do criador, vitrine) | **Voz de marca** | Minúsculo, sem ponto final, tom jovem/informal |
| Contrato, nota fiscal, e-mail financeiro, painel institucional (marca/agência) | **Voz institucional** | Gramática padrão — precisa ser levada a sério pelo jurídico/financeiro de quem recebe |

*Por quê:* a mesma marca pode ter duas vozes — o visual (cor, logo, forma) não muda; só o registro do texto muda conforme quem está lendo.

### 2.1 Onde uma voz vira a outra 🔵

A regra da tabela acima separa por *contexto*, mas telas reais misturam os dois. A tela de proposta (SPEC §3.1) é "produto" — e ao mesmo tempo é juridicamente vinculante, com campos de direito de imagem e exclusividade. Voz informal ali é risco.

**Regra prática, decidida por texto e não por tela:**

> Se este texto pudesse ser impresso e mostrado a um juiz ou a um contador, é **voz institucional**.

| Voz de marca (minúsculo, informal) | Voz institucional (gramática padrão) |
|---|---|
| Navegação, menus, botões de descoberta | Termos comerciais da proposta (prazo, exclusividade, mídias) |
| Estados vazios ("você ainda não tem propostas") | Qualquer valor em dinheiro, data de repasse, prazo contratual |
| Onboarding, vitrine, perfil, busca | Contrato, nota fiscal, recibo, extrato |
| Notificações de atividade | Aprovação de marco, abertura de disputa, cancelamento |
| Marketing e páginas públicas | Termos de Uso, Política de Privacidade, LGPD |
| — | **Toda confirmação de ação irreversível**, sem exceção |

*Por que a última linha:* "tem certeza que quer cancelar?" em tom informal reduz a percepção de gravidade de um ato que move dinheiro. Confirmação de ação irreversível é o único lugar onde queremos que a pessoa desacelere.

### 2.2 ⚠️ O minúsculo é escrito, nunca aplicado por efeito visual

O minúsculo tem que estar **escrito no texto**, não aplicado por CSS (`text-transform: lowercase`, o comando que rebaixa letras automaticamente na tela).

*Por quê, concretamente neste produto:* o efeito automático não sabe distinguir palavra comum de sigla. Ele transformaria **CNPJ → cnpj, CPF → cpf, MEI → mei, Pix → pix, LGPD → lgpd, R$ → r$** — termos que aparecem o tempo todo aqui. Além disso, o texto que a pessoa copia da tela sai diferente do que ela vê, e a busca no navegador deixa de bater.

Consequência prática: siglas, nomes próprios e valores em dinheiro **mantêm a grafia correta mesmo na voz de marca**. Escreve-se "conecte seu CNPJ" e não "conecte seu cnpj".

---

## 3. Cores

### 3.0 A cor de fundo, e o que o guia da marca define

Na página 8 do guia original, uma chamada aponta explicitamente para o rosa mais claro da paleta com o rótulo **"cor do background"**:

| | `#4f2e3c` | `#620073` | `#ff007b` | `#fbc9c9` | `#e1b8b4` | **`#fcd8e3`** |
|---|---|---|---|---|---|---|
| | vinho | roxo | rosa | rosa suave | rosa suave | ← **"cor do background"** |


**Acessibilidade não é o problema:** texto `n-900` sobre `#fcd8e3` mede entre 14,3:1 e 16,1:1 (§3.2) — AAA folgado. O fundo rosa é viável.

### 3.0.1 Decisão 🟢

**Fundo padrão de página: `n-50` `#fdf9fa`. Cartões e superfícies de leitura: `#ffffff`. O `#fcd8e3` do guia vira superfície de destaque de marca, não papel de parede.**

| Superfície | Token | Onde |
|---|---|---|
| Fundo de página (padrão do produto inteiro) | `n-50` `#fdf9fa` | Todas as telas |
| Cartão, tabela, formulário, contrato | `#ffffff` | Por cima do fundo |
| **Destaque de marca** | **`#fcd8e3`** | Topo de página pública, faixa de onboarding, estado vazio, bloco promocional, cartão em destaque |
| Destaque institucional | `#620073` roxo / `#4f2e3c` vinho | Rodapé, faixa de credibilidade, painel institucional |

**Por que esta decisão e não a que eu mesmo tinha recomendado antes.** A versão anterior deste documento propunha rosa nas telas de marca e branco nas telas de produto. Está errada por dois motivos que só ficam visíveis quando se pergunta "o que é premium":

1. **Fundo saturado envelhece rápido e lê como categoria, não como qualidade.** Rosa forte de página inteira comunica "aplicativo de beleza, 2020". Produto que precisa parecer infraestrutura financeira — e é isso que a INFLUENTZ é: escrow, split, nota fiscal — usa superfície quase neutra e gasta o orçamento de cor em momentos escolhidos. É o que Stripe, Shopify e o próprio app do Nubank fazem: a cor da marca é intensa na comunicação e contida na interface, onde ela concorre com botão, alerta e selo de estado.
2. **Duas cores de página partem o produto em dois.** A regra das duas vozes (§2.1) é sobre *texto* — a pessoa não percebe que mudou de registro. Mudar o fundo, ela percebe: parece que saiu do site e entrou noutro sistema. Justamente no pulo da vitrine para o contrato, que é o momento em que a plataforma mais precisa parecer uma coisa só.

**O que se ganha mantendo `n-50` em vez de branco puro:** `n-50` é o mesmo rosa da marca, quase apagado (tem a matiz do `#ff007b` em saturação mínima, §3.3). O produto não fica com cara de painel de banco genérico, e o cartão branco por cima ganha separação sem precisar de sombra pesada. É a intenção da agência — "o fundo não é branco" — executada no nível de 2026.

**Contrastes medidos** (fórmula WCAG 2.1, não estimados):

| Combinação | Medido | Veredito |
|---|---|---|
| `n-900` sobre `n-50` | 17,25:1 | AAA |
| `n-600` (texto secundário) sobre `n-50` | 6,13:1 | AA |
| `n-900` sobre `#fcd8e3` | 13,79:1 | AAA |
| `n-600` sobre `#fcd8e3` | 4,90:1 | AA, com folga curta |
| Roxo `#620073` sobre `#fcd8e3` | 9,10:1 | AAA |

⚠️ **Sobre superfície `#fcd8e3`, o texto secundário sobe para `n-700`.** O `n-600` passa em AA por pouco (4,90:1 contra 6,13:1 no fundo padrão). Como `#fcd8e3` só aparece em bloco de destaque, e não em tela densa, isso não custa nada — mas precisa estar escrito, senão alguém reaproveita o token errado.

⚠️ **Reversível a um token.** Se um dia a decisão mudar, muda-se `background` e o produto inteiro acompanha. Nenhum componente sabe qual é a cor do fundo.

### 3.1 Cores de marca (herdadas do guia original) 🟢

| Cor | Hex | Uso |
|---|---|---|
| Rosa vibrante | `#ff007b` | Cor de ação (botão primário, destaque) — **sempre com texto preto em cima**, nunca branco |
| Roxo | `#620073` | Fundo escuro / cor institucional — texto branco em cima, livre |
| Vinho | `#4f2e3c` | Fundo escuro alternativo — texto branco em cima, livre |
| Rosas suaves | `#fbc9c9` `#e1b8b4` `#fcd8e3` | Fundos claros, cartões, estados suaves — texto preto em cima |

**Nunca fazer:** texto roxo em cima do vinho (quase ilegível). Texto branco em cima do rosa vibrante em tamanho pequeno (falha de leitura).

### 3.2 Contrastes medidos 🟢

Calculados pela fórmula oficial da norma WCAG 2.1 (norma internacional de acessibilidade). **AA** = mínimo exigido para texto normal (4,5:1) e é o piso adotado neste projeto. **AAA** = nível mais rigoroso (7:1).

| Combinação | Medido | Veredito |
|---|---|---|
| Rosa + texto preto | 5,54:1 | AA — confirma a regra da agência |
| Rosa + texto branco | 3,79:1 | **Reprova** em texto normal — confirma o "nunca branco" |
| Roxo + texto branco | 11,89:1 | AAA |
| Vinho + texto branco | 11,74:1 | AAA |
| Roxo sobre vinho | 1,01:1 | **Reprova** — confirma o "nunca fazer" |
| Rosa sobre roxo | 3,13:1 | **Reprova** em texto normal — ver §6 (modo escuro) |
| Preto sobre rosas suaves | 14,3:1 a 16,1:1 | AAA |

⚠️ **Limite do rosa:** passa em AA, não em AAA. Serve para botão, rótulo curto e destaque — **não** para blocos longos de texto pequeno.

### 3.3 Neutros 🔵

O guia da agência não define fundo de página, texto comum, borda nem texto secundário. Sem isso não existe tela. Estes neutros não são cinzas puros: têm uma dose mínima da matiz do rosa da marca (4,03° no espaço de cor OKLCH), o que faz o produto parecer coeso em vez de "marca colorida colada em cima de cinza de banco".

| Token | Hex | Uso | Contraste sobre branco |
|---|---|---|---|
| `n-50` | `#fdf9fa` | Fundo de página alternativo | — |
| `n-100` | `#f8f3f4` | Superfície suave, linha alternada de tabela | — |
| `n-200` | `#ece5e6` | Borda decorativa, divisória | — |
| `n-300` | `#dbd2d4` | Borda de cartão | — |
| `n-400` | `#aba0a2` | Ícone desabilitado, placeholder | 2,54:1 |
| `n-500` | `#85787b` | **Borda de campo de formulário** (ver ⚠️ abaixo) | 4,23:1 |
| `n-600` | `#685c5e` | **Texto secundário** — piso permitido | 6,40:1 — AA |
| `n-700` | `#4e4446` | Texto de apoio forte | 9,38:1 — AAA |
| `n-800` | `#2e2628` | — | 14,75:1 |
| `n-900` | `#1b1516` | **Texto principal** | 18,02:1 — AAA |
| `n-950` | `#0e080a` | Preto do produto (não usar `#000` puro) | 19,85:1 |

⚠️ **Duas armadilhas que só apareceriam depois, com o produto pronto:**

1. **Texto secundário não pode ser `n-500`.** É a escolha instintiva de todo sistema de design e mede 4,23:1 — reprova. Todo texto secundário (datas, metadados, legendas) usa **no mínimo `n-600`**.
2. **Borda de campo de formulário não pode ser `n-200` nem `n-300`.** A norma exige 3:1 para a borda que identifica um componente (WCAG 2.1, critério 1.4.11); `n-200` mede 1,24:1 e `n-300` mede 1,48:1. Campo de formulário usa **`n-500`** (4,23:1). Borda decorativa de cartão pode continuar clara.

### 3.4 Cores de estado 🔵

Este produto é uma máquina de estados de dinheiro (SPEC §4.6 e §5). Sem cor definida por estado, cada tela inventa a sua.

Decisão: **6 classes de cor, não uma cor por estado.** A cor comunica a *classe de urgência*; o rótulo escrito carrega a precisão. Sete cores quase iguais seriam indistinguíveis e não ajudariam ninguém.

| Classe | Texto | Fundo do selo | Contraste | Estados que ela cobre |
|---|---|---|---|---|
| **Neutro** | `#4e4446` | `#f8f3f4` | 8,54:1 | Rascunho, cancelado, reembolsado, expirado |
| **Info** | `#1d4ed8` | `#dbeafe` | 5,49:1 | Em execução, marco em andamento |
| **Atenção** | `#92400e` | `#fef3c7` | 6,37:1 | Aguardando pagamento, aguardando aprovação, prazo vencendo |
| **Sucesso** | `#15803d` | `#dcfce7` | 4,57:1 | Aprovado, liberado, pago |
| **Crítico** | `#b91c1c` | `#fee2e2` | 5,30:1 | Disputa, contestação de compra, pagamento recusado |
| **Protegido** | `#620073` | `#f3e3f7` | 9,70:1 | **Retido em escrow** |

🔵 **Por que "Protegido" ganha cor própria — e a cor da marca:** o escrow (dinheiro retido pela plataforma até a entrega ser aprovada) é o mecanismo que sustenta a confiança dos dois lados, segundo a SPEC §4.6. Ele não é "aguardando" nem "sucesso": é um estado positivo e único do produto. Usar o roxo institucional faz o momento de maior confiança do fluxo carregar visualmente a marca.

⚠️ **Rosa de ação × vermelho crítico.** Medidos, os dois estão a apenas 23,5° de matiz um do outro — perto o suficiente para confundir num relance. A separação **não** é feita por cor, e sim por forma:

| | Preenchimento | Texto | Onde aparece |
|---|---|---|---|
| Botão primário | Rosa `#ff007b` | **Preto** (5,54:1) | Livre |
| Botão destrutivo | Vermelho `#b91c1c` | **Branco** (6,47:1) | Só dentro de confirmação de ação irreversível |

O contraste de texto preto contra texto branco torna os dois inconfundíveis mesmo para quem não distingue as matizes. Botão destrutivo nunca fica lado a lado com o primário fora de um diálogo de confirmação.

### 3.5 ⚠️ Cor nunca sozinha

Cerca de 8% dos homens têm alguma deficiência de visão de cores, e a confusão mais comum é justamente verde × vermelho — exatamente o par "aprovado" × "disputa". A norma WCAG 2.1 (critério 1.4.1) proíbe usar cor como único meio de transmitir informação.

**Regra:** todo selo de estado tem sempre **ícone + texto escrito**, nunca só a cor. Vale também para gráfico: toda série precisa de rótulo, não só de legenda colorida.

### 3.6 Paleta de gráfico 🔵

Para os painéis (SPEC §7) e as métricas de audiência (SPEC §9). Todas passam do mínimo de 3:1 sobre branco exigido para elemento gráfico.

| Token | Hex | Contraste |
|---|---|---|
| `chart-1` | `#ff007b` rosa | 3,79:1 |
| `chart-2` | `#620073` roxo | 11,89:1 |
| `chart-3` | `#0e7490` teal | 5,36:1 |
| `chart-4` | `#a16207` âmbar | 4,92:1 |
| `chart-5` | `#685c5e` cinza | 6,40:1 |

Escolhidas com matizes bem distantes entre si porque várias têm luminosidade parecida — por isso a regra do §3.5 (rótulo sempre) vale em dobro aqui.

---

## 4. Tipografia

### 4.0 O peso da Raleway no corpo do texto: o guia pede Raleway **Bold** para o corpo do texto

Página 6 do guia original, na íntegra:

> "Os textos do site e da comunicação visual devem usar majoritariamente a fonte **Raleway Bold**, sempre com todas as palavras em letra minúscula e sem ponto final, sempre que possível, **exceto em textos de contratos legais, termos normativos e ou de cunho jurídico**."

Duas coisas saem daí.

**Primeira, a boa notícia:** a frase depois do "exceto" é a regra das duas vozes do §2 deste documento, escrita pela própria agência em 2020. A separação entre voz de marca e voz institucional **não é invenção de Claude** — ela estava na fonte o tempo todo. O §2 agora tem origem documental.

**Segunda, a divergência:** o guia manda usar Bold no corpo do texto, e a v0.2 escreveu "Raleway Regular — corpo de texto" sem registrar que estava divergindo. Falha de transcrição, corrigida agora.

**A divergência se mantém, pelo mesmo motivo já aceito no §4.2.** A v0.2 já corrigiu *Roboto Slab Bold* para Regular no corpo institucional, com a justificativa de que negrito ao longo de parágrafos reduz a velocidade de leitura e passa impressão de texto gritado. O argumento vale igual para a Raleway — e vale mais ainda aqui, porque um guia de 2020 pensava em peça publicitária e site de apresentação, não em painel financeiro com tabela de repasses e extrato de saldo.

**Regra final:**

| Uso | Fonte |
|---|---|
| Título, botão, rótulo curto, chamada de marketing | Raleway **Bold** (700) — como o guia pede |
| Parágrafo, descrição, texto corrido de produto | Raleway **Regular** (400) — divergência consciente |

⚠️ **O que NÃO diverge:** "todas as palavras em letra minúscula e sem ponto final" continua valendo integralmente na voz de marca, com a ressalva técnica do §2.2 (o minúsculo é escrito, nunca aplicado por efeito visual — senão CNPJ vira cnpj).

### 4.1 Famílias (herdadas do guia original) 🟢

- **Raleway Bold** — títulos e voz de marca
- **Raleway Regular** — corpo de texto, voz de marca
- **Roboto Slab Bold** — voz institucional (contratos, painel corporativo) — mais neutra, mais "documento sério"

**Licença e custo** (checklist do `CLAUDE.md` §3): ambas são Google Fonts sob licença SIL Open Font License — uso comercial livre, custo zero, sem exigência de CNPJ. Podem ser hospedadas junto com o produto, sem depender do servidor do Google (o que também evita uma questão de LGPD sobre envio de IP de visitante a terceiros).

### 4.2 ⚠️ Correção: bold não serve para corpo institucional

O guia especifica *Roboto Slab **Bold*** para a voz institucional. Aplicado a um contrato inteiro, texto em negrito ao longo de parágrafos reduz a velocidade de leitura e passa impressão de texto gritado — o oposto do que se quer num documento que precisa ser levado a sério.

**Decisão:** a intenção da agência (institucional = slab serif) é mantida; só o peso muda conforme a função.

| Uso | Fonte |
|---|---|
| Título de documento institucional, cabeçalho de contrato, rótulo de campo legal | Roboto Slab **Bold** (700) |
| Corpo de contrato, termos, cláusulas, texto longo institucional | Roboto Slab **Regular** (400) |

⚠️ **Roboto Slab não tem itálico verdadeiro.** Se um texto pedir itálico, o navegador inventa uma inclinação artificial, que fica visivelmente torta. Em documento institucional, ênfase se faz com **negrito** ou com aspas — nunca com itálico.

### 4.3 Escala tipográfica 🔵

Base 16px. Formato: tamanho / entrelinha.

| Nome | Tamanho | Uso |
|---|---|---|
| `xs` | 12 / 16px | Metadado, legenda de gráfico. Nunca para texto que precise ser lido com atenção |
| `sm` | 14 / 20px | Texto de apoio, tabela densa |
| `base` | 16 / 24px | **Corpo padrão** |
| `lg` | 18 / 28px | Corpo destacado, introdução |
| `xl` | 20 / 28px | Título de cartão |
| `2xl` | 24 / 32px | Título de seção |
| `3xl` | 30 / 36px | Título de página |
| `4xl` | 36 / 40px | Marketing |
| `5xl` | 48 / 52px | Topo de página pública |

Pesos: Raleway 400 (corpo), 600 (subtítulo), 700 (título). Roboto Slab 400 e 700.

⚠️ **Campo de formulário nunca abaixo de 16px.** O Safari no iPhone dá zoom automático ao tocar num campo com texto menor que 16px, e a tela "pula". É a causa mais comum de formulário que parece quebrado no celular. Vale para todo campo de digitação, inclusive os de valor em dinheiro.

### 4.4 ⚠️ Números: a Raleway precisa de ajuste para valores em dinheiro

**Descoberta que afeta todas as telas de dinheiro.** A Raleway traz dois conjuntos de números e usa por padrão o *old-style*: dígitos de alturas diferentes, alguns descendo abaixo da linha de base (como o 3, o 4, o 7 e o 9). Além disso, os dígitos têm larguras diferentes entre si.

Resultado sem ajuste: em qualquer coluna de valores — extrato do criador, tabela de repasses, painel financeiro — os números saem desalinhados e "dançando", com aparência amadora justamente na tela em que a plataforma precisa parecer confiável.

**Regra obrigatória:** todo número em contexto financeiro, de data ou de tabela usa a propriedade CSS `font-variant-numeric: lining-nums tabular-nums`.

- `lining-nums` → todos os dígitos com a mesma altura, alinhados no topo
- `tabular-nums` → todos os dígitos com a mesma largura, para as colunas alinharem verticalmente

Onde aplicar: valores em reais, percentual de comissão, datas de liberação, contadores, métricas de audiência, identificadores de transação, CPF/CNPJ.

Fontes: [The League of Moveable Type — Raleway](https://www.theleagueofmoveabletype.com/raleway) (a família traz numerais old-style e lining), [Codesmite — Fixing Raleway's numerals](https://www.codesmite.com/article/fixing-raleway-and-similar-fonts-numerals) (o padrão da fonte é o não-alinhado).

### 4.5 Alinhamento de texto (herdado do guia original) 🟢

Página 22 do guia marca **texto justificado como uso incorreto**. Correto é alinhado à esquerda ou centralizado, sempre respeitando as margens laterais.

A regra é tecnicamente sólida e vale a pena manter: justificar texto na web abre "rios" de espaço branco entre palavras, porque o navegador não hifeniza bem em português. Fica pior ainda em tela de celular, onde a linha é curta.

**Regra:** `text-align: left` como padrão em todo o produto. Centralizado só em chamada curta de marketing. **Justificado em lugar nenhum**, nem em contrato — a legibilidade de um contrato é mais importante que a aparência de bloco.

---

## 5. Espaçamento, raio e elevação 🔵

### 5.1 Espaçamento

Escala de base 4px (padrão do Tailwind, adotado sem alteração para não inventar problema onde não há).

Ritmo de página: 8px (dentro de um componente) · 16px (entre componentes relacionados) · 24px (entre blocos) · 32px e 48px (entre seções) · 64px (respiro de página pública).

Regra única: **só múltiplos de 4.** Valor fora da escala é bug, não escolha.

### 5.2 Raio de canto

`--radius: 0.75rem` (12px) como base; o shadcn/ui deriva os tamanhos menores e maiores a partir dela.

*Por quê 12px e não o padrão 10px do shadcn:* canto mais arredondado lê como mais amigável, coerente com a "linguagem de redes sociais" do §1. As telas institucionais ganham a sobriedade necessária pela tipografia (slab serif) e pela cor (roxo/vinho), não por cantos retos — assim o produto não se parte visualmente em dois produtos.

### 5.3 Elevação (sombra)

⚠️ Sombra praticamente não aparece sobre as superfícies escuras da marca (roxo e vinho). Por isso a regra depende do fundo:

| Fundo | Como separar as camadas |
|---|---|
| Claro (branco, `n-50`, `n-100`) | Sombra suave |
| Escuro (roxo, vinho, `n-900`) | **Sem sombra** — usar fundo um passo mais claro + borda de 1px |

As sombras são pretas tingidas com a matiz da marca (nunca preto puro), o que as faz parecer parte do produto e não uma caixa flutuando.

---

## 6. Modo escuro — decisão 🟢

**O v1 sai só em modo claro.** As telas escuras da marca (roxo, vinho) continuam existindo como *superfícies de destaque* — topo de página pública, painel institucional, faixas — e não como um tema escuro do produto inteiro.

**Duas razões, uma técnica e uma de escopo:**

1. ⚠️ **Técnica, e medida:** um modo escuro ingênuo usaria o roxo `#620073` como fundo de página com o rosa `#ff007b` nas ações. Essa combinação mede **3,13:1 — reprova** para texto normal. Ou seja: um tema escuro aqui não é "usar as cores escuras da marca", exige construir uma escala neutra escura própria e reposicionar o rosa. É trabalho de verdade, não um interruptor.
2. **De escopo:** modo escuro dobra o desenho e a conferência de *cada* tela. A meta de lançamento da SPEC §14 é provar o ciclo completo com dinheiro real em escala pequena (50 criadores, 10 marcas, 20 contratos) — não maximizar acabamento.

**Custo de adiar: zero.** Os tokens já nascem escritos no formato que o shadcn/ui usa para tema (`:root` para claro, bloco `.dark` para escuro). O bloco `.dark` fica declarado e vazio; quando o modo escuro entrar, preenche-se um arquivo, sem tocar em componente nenhum.

---

## 7. Mapa de tokens do shadcn/ui 🔵

*Token = nome fixo para um valor (ex.: "cor de ação" = `#ff007b`). Trocar o valor em um lugar só muda o produto inteiro.*

O shadcn/ui espera esta lista exata de nomes. Preenchê-la é o que torna o sistema implementável. Valores em hexadecimal porque é o formato que o Claude Design usa na etapa 3; na etapa 6 eles são convertidos para OKLCH, que é o formato que o shadcn/ui usa hoje. Fonte: [shadcn/ui — Theming](https://ui.shadcn.com/docs/theming).

| Token shadcn | Valor | Papel |
|---|---|---|
| `background` | `#fdf9fa` (n-50) | **Fundo de página** — ver §3.0.1 |
| `foreground` | `#1b1516` (n-900) | Texto principal |
| `card` | `#ffffff` | Fundo de cartão |
| `card-foreground` | `#1b1516` | Texto no cartão |
| `popover` | `#ffffff` | Menu e balão flutuante |
| `popover-foreground` | `#1b1516` | Texto neles |
| `primary` | `#ff007b` | **Cor de ação** |
| `primary-foreground` | `#0e080a` | **Texto sobre a ação — preto** |
| `secondary` | `#f8f3f4` (n-100) | Botão secundário |
| `secondary-foreground` | `#2e2628` (n-800) | Texto dele |
| `muted` | `#f8f3f4` (n-100) | Superfície apagada |
| `muted-foreground` | `#685c5e` (n-600) | **Texto secundário — piso de acessibilidade** |
| `accent` | `#fcd8e3` | Superfície de passagem do mouse / item selecionado |
| `accent-foreground` | `#620073` | Texto sobre ela (9,10:1) |
| `destructive` | `#b91c1c` | **Ação destrutiva — nunca o rosa** |
| `border` | `#ece5e6` (n-200) | Divisória e borda decorativa |
| `input` | `#85787b` (n-500) | **Borda de campo — exige 3:1** |
| `ring` | `#ff007b` | Anel de foco do teclado (3,79:1 — passa) |
| `chart-1` … `chart-5` | ver §3.6 | Gráficos |
| `radius` | `0.75rem` | Raio base |

⚠️ **`accent` é rosa claro e `primary` é rosa.** Botão primário não vai em cima de superfície `accent` — o botão perde destaque. Superfície `accent` serve para item de menu sob o mouse e linha selecionada, não para hospedar a ação principal.

Os tokens de `sidebar-*` que o shadcn/ui também define ficam iguais aos equivalentes principais até existirem telas com barra lateral (etapa 3).

---

## 8. Ícones 🔵

Conjunto: **Lucide** — o padrão que já vem com o shadcn/ui, sem biblioteca extra. Traço de 1,5px a 2px, tamanho acompanhando o texto ao lado (16px junto de `sm`, 20px junto de `base`).

Todo selo de estado (§3.4) leva ícone, por causa da regra do §3.5.

---

## 9. Aplicação do logotipo 🟢

Transcrito da página 17 do guia original. **As medidas abaixo não foram estimadas a olho:** foram extraídas das coordenadas vetoriais do PDF.

### 9.1 Área de não interferência (respiro)

O guia desenha em amarelo, em volta do logotipo, uma faixa que nenhum outro elemento pode invadir. Medida do vetor:

| Medida | Valor no arquivo |
|---|---|
| Faixa de respiro | **31,4 pt, igual nos quatro lados** |
| Altura total do logotipo (símbolo "play" + palavra) | 59,8 pt |
| Proporção | 0,53 × a altura do logotipo |

🔵 **Regra prática adotada: o respiro é metade da altura do logotipo, nos quatro lados.** Isso arredonda o valor medido em 5% para um número que uma pessoa consegue aplicar sem calculadora e que continua valendo em qualquer tamanho.

Exemplo: logotipo com 40px de altura na tela → **20px livres** em cima, embaixo, à esquerda e à direita.

### 9.2 Uso dentro do aplicativo 🟢

O guia mostra lado a lado o uso incorreto (logotipo ocupando quase toda a largura, colado no texto) e o correto (logotipo pequeno, centralizado, com respiro). A regra escrita é:

> "nas peças publicitárias e redes sociais haverá liberdade criativa no seu uso e aplicações"

Ou seja: **dentro do produto a regra é rígida; fora dele, é livre.** Faz sentido — dentro do app o logotipo é elemento de interface e concorre com botões; fora, é peça de comunicação.

### 9.3 ⚠️ O logotipo não pode ser reproduzido com a Raleway

Página 5 do guia: *"Desenvolvemos uma tipografia exclusiva para a influentz. (...) Os caracteres invadem o espaço uns dos outros como se gerassem influência a partir de onde estão."*

**O logotipo é letra desenhada à mão, não texto digitado.** As letras se sobrepõem de propósito, e nenhuma fonte instalada reproduz isso.

Consequência prática: o logotipo **é sempre um arquivo de imagem vetorial (SVG)**, nunca texto escrito com a fonte. Escrever "influentz" com Raleway em cima de um fundo e chamar de logo produz algo parecido e errado.

🟡 **Pendência que continua aberta:** o arquivo vetorial (`.ai` / `.svg`) está no Drive, em `INFLUENTZ / MARKETING / BRANDING / Arquivos de Marca - Influentz / Logotipo`. Entra na etapa 6 (código), por decisão do Marco. Até lá, as telas da etapa 3 usam um retângulo marcador com as proporções corretas.

### 9.4 Tamanho mínimo 🟡

O guia **não define** tamanho mínimo de aplicação — foi procurado nas 33 páginas e não existe.

🔵 **Proposta, a ser confirmada quando o vetor chegar:** 24px de altura na tela para a versão completa (símbolo + palavra). Abaixo disso, as letras sobrepostas viram borrão e o "play" some. Menor que isso, usa-se só o símbolo "play", que é o que o guia já trata como ícone de aplicativo (página 11).

---

## 10. Terminologia na interface ⚠️

Página 26 do guia é a única do documento que marca palavras como **certas e erradas**:

| ❌ Terminologia incorreta | ✅ Terminologia correta |
|---|---|
| cliente | **sou cliente** |
| blogueiro | **sou influencer** |

E a página 12 mostra os dois caminhos de entrada da marca: **"seja um influentz"** e **"busque um influentz"**.

### 10.1 As palavras que a plataforma usa para as pessoas

| Papel | Guia da marca (2020) | SPEC v0.5 (2026) |
|---|---|---|
| Quem contrata | cliente | **marca** |
| Quem executa | influencer / influentz | **criador** |

Isto não é detalhe de texto: é a palavra que aparece em botão, menu, contrato e notificação. Precisa ser decidido antes da etapa 3, senão cada tela escolhe a sua.

**Recomendação técnica: manter a SPEC (marca / criador) nos rótulos funcionais, e o vocabulário do guia nas chamadas de marca.**

Três razões concretas:

1. **"Influencer" ficou pequeno para o produto.** A SPEC §1 inclui palestrante, médico-influenciador e especialista, com entrega remota, presencial ou híbrida. Um médico contratado para uma palestra não se reconhece como "influencer" — e essa é justamente a ponta de ticket alto.
2. **"Cliente" é ambíguo dentro da plataforma.** Marca e criador são os dois clientes da INFLUENTZ. Num painel de suporte ou financeiro, "cliente" não identifica ninguém.
3. **O guia está certo naquilo que ele realmente decidiu:** proibir "blogueiro". A palavra envelheceu mal e soa depreciativa. Isso se mantém — "blogueiro" não aparece em lugar nenhum.

**Como fica na prática:**

| Contexto | Palavra |
|---|---|
| Menu, rótulo de campo, contrato, painel, e-mail financeiro | marca · criador |
| Onboarding, marketing, página pública | **"seja um influentz"** · **"busque um influentz"** — herdado do guia, e é o melhor ativo verbal da marca |

*Por que "influentz" como substantivo é bom e vale preservar:* a marca vira o nome da coisa, que é o que toda plataforma persegue e quase nenhuma consegue. Mas funciona como chamada, não como rótulo de campo de formulário.

### 10.2 Decisão 🟢

**Rótulo funcional: `marca` e `criador`. Chamada de marca: "seja um influentz" e "busque um influentz". "Blogueiro" e "influencer" não aparecem como rótulo em lugar nenhum.**

Além dos três motivos acima, dois argumentos que só aparecem quando se pensa em expansão:

**1. O mercado mundial já trocou a palavra, e a troca foi na direção de "criador".** "Creator economy" é hoje o termo guarda-chuva — um mercado de US$ 33 bilhões em 2025, contra menos de US$ 10 bilhões em 2020 — e **"influencer marketing" é tratado como uma tática dentro dele**, não como o todo. "Criador" engloba influenciador, produtor de vídeo, podcaster e especialista; "influenciador" engloba só um pedaço. Nomear o produto pelo pedaço menor é escolher o teto mais baixo.

**2. `marca / criador` atravessa a fronteira sem tradução; `cliente / influencer` não.** Traduzidos: `brand` e `creator` são exatamente os termos padrão do mercado global. Já `client` em inglês, num marketplace, é ambíguo — quem é cliente de quem? E o dia em que a INFLUENTZ atender uma marca fora do Brasil, o vocabulário do produto já está no idioma certo, sem refazer tela, contrato e e-mail.

⚠️ **O que fica do guia, e é o mais valioso:** "seja um influentz" / "busque um influentz". A marca virando o nome da coisa é o ativo verbal que uma plataforma leva uma década para construir. Ele fica no marketing, no onboarding e na página pública — onde funciona. Não vira rótulo de campo de formulário, onde precisão vale mais que personalidade.

*Fonte da virada de terminologia:* [eMarketer — FAQ on the creator economy](https://www.emarketer.com/insights/definition-creator-economy) e [Influencer Marketing Factory — Creator Economy 2026](https://theinfluencermarketingfactory.com/creator-economy/).

---

## 11. Pendências 🟡

| Item | Por que ainda não decidido |
|---|---|
| Grade e pontos de quebra (celular/tablet/computador) | Depende das telas da etapa 3 |
| Tokens de `sidebar-*` | Idem |
| Arquivo vetorial do logotipo (SVG) | No Drive; entra na etapa 6 por decisão do Marco (§9.3) |
| Tamanho mínimo do logotipo | Proposta em §9.4, a confirmar com o vetor em mãos |

**Decididas na v0.4:** fundo de página (§3.0.1) e terminologia da interface (§10.2).

**Fechadas na v0.3 pela leitura do guia original:** aplicação do logotipo e área de respiro (§9), alinhamento de texto (§4.5), origem documental da regra das duas vozes (§4.0), inventário de ícones do produto (página 14 do guia).

**Sobre animação e transição:** o guia traz duas animações prontas de tela de carregamento, em vídeo — [abertura](https://vimeo.com/459339279) e [carregando](https://vimeo.com/459339659). Não muda a etapa 3; entra na etapa 6.

---

## 12. Próximo passo

Estes tokens entram no `tailwind.config` do projeto assim que o código começar (etapa 6). Antes disso, usados diretamente no Claude Design para gerar as telas (etapa 3), aplicando as regras de contraste acima.

Todos os contrastes citados neste documento foram calculados pela fórmula da WCAG 2.1, não estimados a olho. O piso do projeto é o nível AA.
