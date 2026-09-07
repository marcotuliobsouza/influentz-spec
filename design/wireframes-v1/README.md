# Wireframes INFLUENTZ v1

Etapa 3 do fluxo (CLAUDE.md §4) — fluxo principal de ponta a ponta, mobile-first, para marca e criador (SPEC §5).

**Canvas publicado:** https://claude.ai/code/artifact/e4656b12-ab12-47f4-a1d9-1a909af39ccc

## O que tem aqui

Cada `.dc.html` é uma tela (artboard) do canvas de design. `canvas.json` define a posição de cada uma e as anotações que explicam o fluxo.

| Arquivo | Tela |
|---|---|
| `Main.dc.html` | Onboarding — escolha de papel (entrada pública) |
| `Busca.dc.html` | Busca / vitrine de criadores |
| `Perfil.dc.html` | Perfil público do criador, com cardápio |
| `Proposta.dc.html` | Proposta com campos estruturados (SPEC §3.1, §8.2) |
| `Contrato.dc.html` | Acompanhamento do contrato e marcos (ponto de encontro marca/criador) |
| `Pagamento.dc.html` | Checkout — Pix, boleto, cartão |
| `Extrato.dc.html` | Carteira do criador — protegido / aguardando prazo / disponível (SPEC §4.2) |
| `Chat.dc.html` | Chat vinculado ao contrato (SPEC §10) |
| `Avaliacao.dc.html` | Avaliação mútua double-blind (SPEC §13.1) |

Wireframes estáticos (não é protótipo clicável). Nomes e valores são fictícios.

## Como atualizar

Editar o `.dc.html` correspondente (ou `canvas.json`), depois gerar de novo o arquivo publicável com o helper do skill `design`:

```
node <base-dir-do-skill-design>/seed-canvas.mjs \
  --template <base-dir-do-skill-design>/payload.template.html \
  --out influentz-wireframes-v1.html \
  --title "Wireframes INFLUENTZ v1" \
  --artboard Main.dc.html --artboard Busca.dc.html --artboard Perfil.dc.html \
  --artboard Proposta.dc.html --artboard Contrato.dc.html --artboard Pagamento.dc.html \
  --artboard Extrato.dc.html --artboard Chat.dc.html --artboard Avaliacao.dc.html \
  --canvas canvas.json
```

O arquivo gerado (`influentz-wireframes-v1.html`, ~2,5 MB, contém o editor embutido) não é versionado — está no `.gitignore` deste diretório. Ele é regenerado a qualquer momento a partir dos arquivos-fonte acima. A versão viva do design está no canvas publicado, editável diretamente pelo botão "Salvar".
