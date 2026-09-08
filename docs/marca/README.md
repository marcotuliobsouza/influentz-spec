# Ativos de marca — INFLUENTZ

> Espelho completo da pasta `INFLUENTZ / MARKETING / BRANDING` do Google Drive, revisada por inteiro em 08/09/2026.
>
> ⚠️ **Esta pasta é a única fonte do Drive que entra no projeto** (decisão do Marco — ver `docs/CONFLITOS-A-RESOLVER.md`).
>
> **Link da origem:** https://drive.google.com/drive/folders/1dx3ptqJmwkg3BfN3I8HLwNllT9ClPYSu

---

## O que está aqui

| Arquivo | O que é | Uso |
|---|---|---|
| `Guia da Marca - Influentz (2020).pdf` | Guia original da agência, 33 páginas | Fonte de tudo abaixo |
| `Logotipo - Influentz (vetor oficial).pdf` | Logotipo completo em vetor | Cabeçalho, marketing, documentos |
| `Simbolo do Logotipo - Influentz (vetor oficial).pdf` | Só o símbolo "play", em vetor | Ícone de aplicativo, favicon, avatar |
| `simbolo-influentz.svg` | 🔵 Símbolo reconstruído como SVG limpo, com o degradê da marca | Pronto para código |
| `padrao-influentz.svg` | 🔵 Padrão de fundo em ladrilho, feito a partir do símbolo oficial | Fundo de capa, estado vazio, faixa |
| `Padroes de Estilo - Influentz (2020).pdf` | Padrões originais da agência | Referência |
| `Icones - Influentz (2020).pdf` | Os 21 ícones da marca | Referência |
| `icones/*.svg` | Os 21 ícones extraídos como SVG | Interface |
| `avatares/*.svg` | Avatar padrão de criador e de empresa | Perfil sem foto |
| `logotipo-influentz.png` | Logotipo com fundo transparente | Onde SVG não serve |

---

## Os 21 ícones oficiais

`busca` · `local` · `home` · `estrela` · `estrela-cheia` · `salvo` · `salvo-cheio` · `check` · `verificado` · `mensagem` · `chat` · `calendario` · `pagamentos` · `config` · `play` · `fechar` · `fechar-circulo` · `adicionar` · `adicionar-circulo` · `voltar` · `voltar-circulo`

**Características:** traço grosso e arredondado, preenchidos (não contornados), cor vinho `#4f2e3c`. É uma linguagem visual amigável e sólida — muito diferente de ícone fino genérico.

⚠️ **`verificado` é o único em degradê** (rosa → roxo). É o selo de conta verificada e não deve ser recolorido.

---

## O que o produto vai precisar e a marca não tem 🔵

O Marco autorizou criar o que faltar, desde que dentro do contexto da identidade. Levantamento honesto do que falta:

| Falta | Para quê |
|---|---|
| Contrato / documento | Módulo de contratos |
| Carteira / saldo | Módulo financeiro |
| Escudo (proteção) | Estado de valor retido |
| Alerta / atenção | Avisos e estados de erro |
| Filtro | Busca |
| Enviar / anexar | Entrega de material |
| Gráfico / métricas | Painéis |
| Olho fechado | Avaliação double-blind |
| Sino | Notificações |
| Relógio | Prazos |
| Caixa / encomenda | Envio de produto físico |
| Seta cima/baixo | Extrato |

🟢 **Regra para criar ícone novo:** seguir exatamente a gramática dos 21 originais — **preenchido, traço grosso, cantos arredondados, mesma densidade visual, cor `currentColor`**. Um ícone novo tem que passar despercebido ao lado dos oficiais. Se der para notar qual é o novo, está errado.

---

## O que continua travado ⚠️

| Item | Regra |
|---|---|
| **Logotipo** | Inquestionável. Não se redesenha, não se reescreve com fonte, não se altera proporção |
| **Símbolo "play"** | Idem |
| **Cores da marca** | `#ff007b` · `#620073` · `#4f2e3c` · `#fbc9c9` · `#e1b8b4` · `#fcd8e3`. Alteração só com pedido explícito e justificativa |
| **Tipografia** | Raleway e Roboto Slab |
| **Respiro do logotipo** | Metade da altura dele, nos quatro lados (medido no vetor — `DESIGN-SYSTEM.md` §9.1) |

**O que é livre, dentro do contexto:** neutros, cores de estado, ícones novos, padrões derivados do símbolo, degradês entre as cores da marca, e todo o sistema de interface.

---

## Pendências 🟡

| Item | Situação |
|---|---|
| 5 fotos de referência (pasta `Fotos e Imagens`) | Quatro passam de 10 MB, que é o limite do conector do Drive. Só uma é acessível por aqui |
| Logotipo animado (GIF e MP4) | Existe na origem. Entra na etapa de código, para a tela de carregamento |
| Ícones das redes sociais | Não são da marca — vêm do guia oficial de cada rede, e entram na etapa de código |
