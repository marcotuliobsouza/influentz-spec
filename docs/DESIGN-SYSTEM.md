# Sistema de Design — INFLUENTZ

> Base: identidade visual desenvolvida por agência em 2020 (Google Drive, pasta BRANDING).
> Este documento traduz aquele guia em regras técnicas prontas para implementação em shadcn/ui.

---

## 1. Conceito (herdado do guia original)

Símbolo = "play" de vídeo, representando o ambiente de trabalho do criador de conteúdo.
Tipografia com letras minúsculas remete à linguagem das redes sociais.

## 2. Duas vozes, uma identidade 🟢

| Contexto | Voz | Regra |
|---|---|---|
| Marketing, onboarding, produto (telas do criador, vitrine) | **Voz de marca** | Minúsculo, sem ponto final, tom jovem/informal |
| Contrato, nota fiscal, e-mail financeiro, painel institucional (marca/agência) | **Voz institucional** | Gramática padrão — precisa ser levada a sério pelo jurídico/financeiro de quem recebe |

*Por quê:* a mesma marca pode ter duas vozes — o visual (cor, logo, forma) não muda; só o registro do texto muda conforme quem está lendo.

## 3. Cores — regras de uso seguras (checado por contraste, padrão WCAG)

| Cor | Hex | Uso |
|---|---|---|
| Rosa vibrante | `#ff007b` | Cor de ação (botão primário, destaque) — **sempre com texto preto em cima**, nunca branco |
| Roxo | `#620073` | Fundo escuro / cor institucional — texto branco em cima, livre |
| Vinho | `#4f2e3c` | Fundo escuro alternativo — texto branco em cima, livre |
| Rosas suaves | `#fbc9c9` `#e1b8b4` `#fcd8e3` | Fundos claros, cartões, estados suaves — texto preto em cima |

**Nunca fazer:** texto roxo em cima do vinho (quase ilegível). Texto branco em cima do rosa vibrante em tamanho pequeno (falha de leitura).

## 4. Tipografia

- **Raleway Bold** — títulos e voz de marca
- **Raleway Regular** — corpo de texto, voz de marca
- **Roboto Slab Bold** — voz institucional (contratos, painel corporativo) — mais neutra, mais "documento sério"

## 5. Próximo passo

Estes tokens entram no `tailwind.config` do projeto assim que o código começar (etapa 6). Antes disso, usados diretamente no Claude Design para gerar as telas (etapa 3), aplicando as regras de contraste acima.
