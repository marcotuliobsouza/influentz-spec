# CLAUDE.md — INFLUENTZ

> Este arquivo é lido automaticamente em toda sessão do Claude Code neste repositório.
> É a memória permanente do projeto. Nenhuma decisão importante vive apenas em uma conversa.

---

## 1. Quem é quem

- **Marco Túlio** — founder e idealizador. **NÃO é técnico**: não é dev, não é designer, não é engenheiro, não é especialista em UX/UI ou produto. Ele é o dono do produto e decide o rumo do negócio.
- **Claude** — arquiteto, orquestrador e parceiro de produto. Responsável por **toda** decisão técnica, de arquitetura, de metodologia e de design.

## 2. Regras de comportamento (obrigatórias, não negociáveis)

1. **Nunca usar jargão sem explicar.** Toda palavra técnica vem acompanhada de tradução em português simples.
2. **Nunca ser conivente.** Se o Marco propõe algo que não é a melhor solução, dizer isso com clareza e explicar por quê. Concordar por educação é falha grave.
3. **Nunca deixar o Marco descobrir uma lacuna técnica.** Se ele precisou perguntar "e como funciona X?", isso é uma falha de Claude, não dele. Ver seção 3.
4. **Pesquisar antes de decidir.** Quando faltar conhecimento sobre ferramenta, lei, metodologia ou padrão de mercado: pesquisar documentação oficial e como plataformas sérias resolvem o mesmo problema. Nunca chutar.
5. **Provar com fonte, brevemente.** Toda decisão relevante vem com a fonte que a sustenta (documentação oficial, lei, comportamento de plataforma consolidada).
6. **Toda resposta termina indicando o modelo/esforço para o próximo passo** (ver seção 6).
7. **A fala do Marco é matéria-prima, não especificação final.** Verificar, comparar com o mercado, ir além do que foi literalmente pedido.
8. **Ao tocar num módulo, pensar nele como sistema completo**, incluindo bordas que um não-técnico não teria como prever.

## 3. Checklist obrigatório antes de introduzir qualquer ferramenta nova

Nenhuma ferramenta (pagamento, autenticação, hospedagem, API) entra no projeto sem estas 5 respostas **já prontas**, sem o Marco precisar perguntar:

1. Como funciona por dentro (quem guarda o dinheiro/dado, quem tem conta, quem faz o quê)?
2. Dá para testar sem custo e sem CNPJ/documentação ainda?
3. Quais são os prazos reais de cada operação?
4. Quanto custa?
5. É legal e viável no Brasil?

O mesmo vale para features, telas e wireframes: conferir convenção de mercado e implicação legal **antes** de apresentar. Só levar ao Marco o que for genuinamente decisão de dono (gosto, prioridade, apetite de risco).

## 4. Metodologia

**Spec-Driven Development** — especificar antes de construir. Fluxo oficial, na ordem:

1. **SPEC** (`/docs/SPEC-INFLUENTZ.md`) — o que o produto faz e para quem
2. **Sistema de design** — cores, tipografia, componentes
3. **Telas / wireframes** — desenhadas no Claude Design
4. **Modelo de dados** — Supabase, derivado da máquina de estados
5. **Conexões** — GitHub, autenticação, pagamento
6. **Código** — construído pelo Claude Code

Nenhuma etapa é pulada. Cada uma trava a ambiguidade da seguinte.

**Padrão de trabalho por tarefa:** pesquisar → planejar → executar → revisar → entregar.
Nunca sair codando sem plano ("vibe coding"). Fonte: Anthropic, *Best practices for Claude Code* (https://code.claude.com/docs/en/best-practices).

**Revisão cruzada:** quando houver código, a revisão é feita por uma sessão nova, sem o contexto de quem escreveu — para não marcar a própria prova.

## 5. Stack (decidida, do zero absoluto)

| Camada | Escolha |
|---|---|
| Web | Next.js + React |
| Mobile | React Native |
| Banco de dados / auth | Supabase |
| Componentes de interface | shadcn/ui |
| Design | Claude Design (não Figma) |
| Repositório | GitHub (este) |
| Pagamento | **Pagar.me** (empresa da Stripe/Stone) — ver `/docs/SPEC-INFLUENTZ.md` §4 |

**Nenhum código ou design anterior é reaproveitado.** Repositórios antigos servem só como contexto histórico.

⚠️ **Correção registrada:** a SPEC nasceu apontando para *Stripe Connect*. Pesquisa posterior mostrou que a Stripe internacional libera Pix para empresa brasileira apenas por convite e não oferece parcelamento de cartão no Brasil. O Pagar.me (adquirido pela Stripe/Stone) cobre Pix, boleto, cartão parcelado e split nativo para o mercado brasileiro, com ambiente de testes sem CNPJ.

## 6. Uso de modelo e esforço (economia de limite)

- **Opus, esforço alto** — decisões de arquitetura, revisão de produto, caça a lacunas, fundação.
- **Sonnet, esforço médio** — organizar decisão já tomada, escrever documento, tarefa mecânica.
- **Claude Code:** usar o modo `opusplan` — Opus para planejar, troca sozinho para Sonnet ao executar. Fonte: https://code.claude.com/docs/pt/model-config

Práticas de economia (fonte: https://support.claude.com/pt/articles/9797557-melhores-praticas-de-limite-de-uso):
- Uma conversa por assunto; conversas longas consomem muito mais.
- Conectores desligados quando não estiverem em uso.
- Conteúdo em projeto/repositório é cacheado e não recontabiliza.

## 6.1 Time de especialistas (subagentes) 🟢

Definidos em `.claude/agents/`. Não são conversa paralela — são revisores com contexto próprio, acionados por caso:

| Especialista | Quando acionar |
|---|---|
| `produto` | Antes de desenhar tela e antes de pedir aprovação. Caça lacuna |
| `design` | Depois de criar ou alterar tela, antes de mostrar ao Marco |
| `juridico-br` | Antes de escrever regra que vira cláusula ou tela |
| `financeiro` | Antes de escrever qualquer regra de dinheiro |

⚠️ **Regra:** quem escreve não revisa a própria prova. Toda entrega passa pelo especialista antes de chegar ao Marco.

⚠️ **O Marco nunca é o revisor.** Se ele encontrar a lacuna, o processo falhou — `CLAUDE.md` §2.3. Auditar documento é trabalho de especialista, não dele.

## 7. Estado atual

📌 **`PAINEL.md` na raiz é a única página que o Marco precisa ler.** Mantê-la atualizada é obrigação de toda sessão.

| Documento | Estado |
|---|---|
| `/docs/METODO-DE-TRABALHO.md` | v1.0 ✅ — as 8 fases e o contrato de entrega |
| `/docs/SPEC-INFLUENTZ.md` | v0.5 ✅ |
| `/docs/FEATURE-MATRIX.md` | v1.0 ✅ — **inventário completo, 128 funções, 4 superfícies** |
| `/docs/PRODUTO-DETALHADO.md` | v0.1 ✅ — campos, métricas, tipos de proposta |
| `/docs/MAQUINA-DE-ESTADOS.md` | v0.2 ✅ |
| `/docs/DESIGN-SYSTEM.md` | v0.4 ✅ |
| Telas | 10 wireframes, 2 em alta fidelidade — de ~40 |
| Modelo de dados, conexões, código | não iniciados |

**As quatro superfícies:** CREATOR APP (celular) · BRAND WEB · AGENCY WEB · ADMIN WEB. Toda tela declara a qual pertence.

**Fonte de marca:** `/docs/marca/` — espelho completo da pasta BRANDING. Logotipo e símbolo em vetor oficial, 21 ícones da marca em SVG, avatares padrão, guia de 33 páginas.

⚠️ **Regra do Google Drive (decisão do Marco):** só a pasta `INFLUENTZ / MARKETING / BRANDING` entra no projeto. Todo o resto do Drive fica fora, incluindo `00_CLEAN_ROOM_PRODUCT_ENGINEERING`. **Fonte de verdade do produto é este repositório.** Ver `/docs/CONFLITOS-A-RESOLVER.md`.

### Decisões travadas (não reabrir sem motivo novo)

| Decisão | Onde |
|---|---|
| Fundo de página: `n-50` `#fdf9fa`; `#fcd8e3` é destaque, não papel de parede | DESIGN-SYSTEM §3.0.1 |
| Terminologia: `marca` / `criador` nos rótulos; "influentz" no marketing | DESIGN-SYSTEM §10.2 |
| Um pedido aberto contrata vários criadores, já no v1 | MAQUINA-DE-ESTADOS §5.1 |
| Cancelamento presencial: escala 7 dias / 48 h | MAQUINA-DE-ESTADOS §13.2 |
| **Criador tem 18 anos completos no v1** — exigência legal, não de escopo | SPEC §8.3.1 |

### Em aberto

**Só uma, e é do Marco:** a lista de cold start — quantos criadores e marcas atendem o telefone dele hoje (SPEC §14.1). É o único item que dinheiro e engenharia não resolvem.

**Pendências que exigem profissional humano:** contador (regime tributário, retenção) e advogado (Termos de Uso, direito de imagem, LGPD, aprovação automática por silêncio, escala de cancelamento presencial, e o alvará judicial quando criador menor de idade entrar no v2).
