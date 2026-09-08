# SPEC — INFLUENTZ

> **O que é este documento.** A fonte da verdade do produto. Toda tela, toda tabela do banco de dados, todo fluxo de pagamento aponta de volta para aqui. Quando algo mudar na visão do produto, muda aqui primeiro — e só depois no código.
>
> **Versão:** v0.5
> **Status:** as 8 decisões de produto que estavam em aberto foram travadas. Provedor de pagamento corrigido de Stripe Connect para Pagar.me.
>
> **O que mudou da v0.4:** correção jurídica em §8.3.1 — criador menor de idade exige **alvará judicial** (ECA art. 149 + Lei nº 15.211/2025), não só assinatura do responsável. Consequência: **18 anos completos** para criar no v1. Ver também `MAQUINA-DE-ESTADOS.md`, que traduz esta SPEC em regras de funcionamento e corrigiu seis lacunas dela.
>
> **Legenda:** 🟢 direção definida · 🟡 decisão em aberto · 🔵 proposta de Claude além do que foi pedido · 🔴 lacuna crítica · ⚠️ precisa de profissional humano

---

## 0. Como Claude trabalha neste projeto 🟢

- A fala do Marco é matéria-prima, não a especificação final. Verificar, comparar com o mercado, ir além do pedido literal.
- Nunca aceitar uma solução só por ser a mais fácil de implementar.
- Ao tocar num módulo, pensar nele como sistema completo, incluindo as bordas que um não-técnico não teria como prever.
- Nenhuma ferramenta entra sem o checklist de 5 perguntas do `CLAUDE.md` §3 respondido de antemão.
- Toda decisão relevante vem com fonte.

---

## 1. Visão do produto 🟢

**INFLUENTZ** é um marketplace que conecta três tipos de participante:

- **Marcas** (`brand`) — empresas que contratam divulgação, conteúdo ou presença.
- **Criadores** (`creator`) — influenciadores, palestrantes, médicos-influenciadores, especialistas. Qualquer pessoa que gera conteúdo ou presença de marca — remoto, presencial ou híbrido.
- **Agências** (`agency`) — representam e gerenciam marcas **e/ou** criadores, mediante convite aceito pelos dois lados.
- **Equipe INFLUENTZ** (`admin` / `staff`) — detalhado na seção 7.

A plataforma existe para que uma marca encontre o criador certo por categoria/nicho (moda e beleza, tecnologia, saúde, etc.), contrate, pague, acompanhe a entrega e resolva qualquer problema no caminho — tudo dentro da plataforma, com segurança jurídica para as duas pontas.

---

## 2. Papel da agência 🟢

A agência **gerencia**, mas quem assina e quem recebe/paga é sempre a marca ou o criador. **A agência nunca toca no dinheiro.**

Motivo: se a agência recebesse e repassasse valores de terceiros, ela passaria a exercer atividade de instituição de pagamento perante o Banco Central — obrigação regulatória que não faz sentido impor a um cliente da plataforma.

🔵 **Autonegociação:** se o mesmo CPF/CNPJ aparecer do lado da agência **e** do criador/marca representado, o sistema sinaliza para revisão manual antes de liberar qualquer benefício.

**Escopo de agência no lançamento** (decisão 7): a agência já entra no v1 em versão enxuta — espaço próprio para agrupar seus criadores e marcas sob um login. Fica para depois: permissões refinadas por membro da equipe da agência e faturamento consolidado entre várias marcas representadas.

*Justificativa da mudança:* a hipótese anterior era adiar agências inteiras. Foi revertida porque agências são justamente o público que hoje sofre com gestão manual e sem workspace — sem um motivo para entrar no dia 1, elas permanecem com seus grupos próprios de criadores fora da plataforma.

---

## 3. Como a contratação é estruturada 🟢

**Modelo híbrido** (decisão 1):

- **Vitrine com preço fixo** — o criador publica um "cardápio" de entregas padronizadas (ex.: *1 Reels — R$ 800*; *3 Stories — R$ 300*; *1 hora de palestra remota — R$ 1.500*). A marca contrata direto, sem negociar.
- **Pedido aberto com proposta** — para campanhas maiores ou fora do padrão, a marca publica briefing e os criadores enviam proposta.

*Por quê os dois:* vitrine reduz atrito e ajuda criador iniciante a vender sem saber negociar; pedido aberto sustenta contratos grandes, onde preço fixo não cabe. É o padrão usado por marketplaces de serviço consolidados (Workana, 99Freelas operam pedido aberto; Fiverr opera vitrine — cada um perde metade do mercado por não ter o outro).

### 3.1 Proposta como menu, não texto livre 🟢

Os termos comerciais são **campos estruturados**, não texto solto. Isso elimina ambiguidade na hora da disputa e aumenta o ticket médio, porque cada campo tem preço implícito. Ver seção 8.2.

---

## 4. Dinheiro 🟢

### 4.1 Provedor de pagamento: Pagar.me

⚠️ **Correção em relação às versões anteriores.** A SPEC nascera apontando para *Stripe Connect*.

- A Stripe internacional libera **Pix para empresa brasileira apenas por convite** e **não oferece parcelamento de cartão no Brasil**. Fonte: https://docs.stripe.com/payments/pix
- O **Pagar.me** (adquirido pela Stripe/Stone) cobre Pix, boleto, cartão parcelado e divisão automática (split) nativa para o Brasil.

**Como funciona por dentro** (checklist do `CLAUDE.md` §3):

1. **Quem guarda o dinheiro:** o Pagar.me. A INFLUENTZ não constrói carteira própria e o dinheiro não passa pela conta da plataforma.
2. **Quem tem conta:** cada criador e cada marca vira um *recebedor* dentro da conta Pagar.me da INFLUENTZ — basta CPF/CNPJ e conta bancária. **O usuário não cria conta no Pagar.me.** Fonte: https://docs.pagar.me/docs/recebedores-2
3. **Testes sem CNPJ:** sim. Conta de teste liberada só com e-mail; chaves de produção exigem CNPJ depois. Fonte: https://docs.pagar.me/v4/docs/getting-started
4. **Split:** o valor já nasce dividido no momento do pagamento — a plataforma não recebe tudo para repassar depois. Isso também evita bitributação sobre o valor que nunca foi receita da plataforma.

### 4.2 Meios de pagamento aceitos (decisão 3) ⚠️ corrigido em 08/09/2026

| Meio | Aceito no v1 | Quando o dinheiro fica disponível | Pode voltar? |
|---|---|---|---|
| **Pix** | Sim | Na hora, inclusive dentro do split | ⚠️ **Sim, em parte** — o MED (Mecanismo Especial de Devolução) do Banco Central tem janela de **até 80 dias**, só para fraude, golpe ou falha operacional. Não cobre arrependimento |
| **Boleto** | Sim | 1 a 2 dias após confirmação | **Não.** É o único meio realmente irreversível |
| **Cartão de crédito** | Sim, **só para marca com CNPJ verificado** | **À vista: D+30.** ⚠️ **Parcelado: uma parcela por mês** — D+30, D+60, D+90… uma para cada parcela que a marca escolher, salvo antecipação | Sim — janela de 75 a 540 dias, conforme a bandeira e o motivo |

*Por que cartão entra:* ambiente corporativo usa cartão intensamente. Excluí-lo eliminaria uma fatia relevante da demanda.

🔴 **Correção grave, encontrada pelo especialista `financeiro` em 08/09/2026.** A versão anterior escrevia "cartão → D+30" como se fosse uma linha só. **Não é.** Em venda parcelada, o Pagar.me libera **uma parcela por mês**. Se a marca parcelar em 6× um contrato de R$ 6.000, o criador entrega tudo hoje e recebe R$ 1.000 por mês durante seis meses. Isso é muito pior do que a reserva de 90 dias que foi recusada — e estava na SPEC como se não existisse. Fonte: [Pagar.me — cálculo da antecipação](https://pagarme.helpjuice.com/pt_BR/antecipa%C3%A7%C3%A3o-%7C-como-%C3%A9-feito-o-c%C3%A1lculo-da-antecipa%C3%A7%C3%A3o).

✅ **Regra do v1:** cartão parcelado **só com antecipação automática ligada**, com o custo da antecipação embutido no preço que a marca vê (§4.5 já manda mostrar preço final). Se a antecipação não estiver liberada pelo Pagar.me no lançamento, **cartão só à vista no v1**.

⚠️ **Regra de ouro contra risco de falência:** a plataforma **nunca adianta dinheiro que ainda não recebeu do provedor.** Uber e iFood adiantam ao motorista/restaurante com capital de giro próprio — copiar isso sem caixa é emprestar dinheiro inexistente. O criador vê no app a data exata em que cada valor vira saldo disponível.

### 4.3 Proteção contra contestação de compra (chargeback) ⚠️ reescrito em 08/09/2026

> **Revisado por:** especialista `financeiro`, com pesquisa na documentação do Pagar.me, nas regras de disputa das bandeiras e no desenho de Stripe Connect, Upwork e Fiverr.

⚠️ **O que foi eliminado: a reserva de 90 dias.** Recusada pelo dono do produto — *"quem usará nossa plataforma esperando esse tempo para liberar dinheiro? E só uma parte não garantiria 100% do prejuízo"*. **Ele estava certo nos dois pontos, e a pesquisa achou um terceiro que ninguém tinha visto: a reserva de 90 dias era o pior dos mundos, porque nem protegia.** A contestação por "serviço não recebido" (Visa 13.1) conta **120 dias a partir da data prevista de entrega**, não da compra, com teto de 540 dias. Uma reserva de 90 dias a partir do pagamento **fecharia antes de a janela de risco acabar**. Pagava-se a proposta de valor e não se comprava proteção nenhuma.

🔴 **Princípio travado: o criador nunca espera mais do que o prazo do meio de pagamento.** Reter dinheiro do criador para cobrir risco de terceiro transfere a ele um custo que é da plataforma.

**A proteção vem de sete camadas, todas antes do repasse:**

| # | Camada | O que é |
|---|---|---|
| 1 | **3D Secure obrigatório** | Em 100% das cobranças de cartão. Autenticado, a responsabilidade por chargeback **de fraude** passa ao banco emissor (*liability shift*). Não autenticou, não passa no cartão: o checkout oferece Pix ou boleto. Fonte: [docs.pagar.me — Autenticação via 3DS](https://docs.pagar.me/docs/autentica%C3%A7%C3%A3o-via-3ds) |
| 2 | **Teto por transação no cartão** | Cartão tem valor máximo por cobrança. Acima disso: Pix, boleto, ou divisão em marcos que respeitem o teto. O teto sobe conforme o **histórico da marca** — nunca pela espera do criador. ⚠️ **O valor do teto é decisão do Marco** (apetite de risco). Sugestão de partida: R$ 3.000 por cobrança |
| 3 | **Dossiê de defesa automático** | O sistema gera em um clique o PDF único de até 1,9 MB com contrato congelado, briefing, aceite bilateral com data/hora/IP, comprovante de que o marco foi financiado antes do início, arquivos de entrega datados, aprovação registrada e log do chat. ⚠️ **O prazo de defesa é de 10 dias e é fatal** — vira tarefa com contagem regressiva no painel Trust & Safety. É o mecanismo com que a Upwork efetivamente ganha disputas |
| 4 | **A INFLUENTZ é a responsável declarada** | No split do Pagar.me, `liable` e `charge_processing_fee` são **`true` no recebedor da plataforma e `false` no recebedor do criador, sempre explícitos**. ⚠️ O padrão do provedor joga a responsabilidade no **primeiro recebedor da lista** — depender de ordem de array é acidente esperando acontecer. Fonte: [docs.pagar.me — Split](https://docs.pagar.me/v3/docs/split-rules) |
| 5 | **Fundo de contestação** | **5% da receita de comissão** fica em conta separada e paga os chargebacks perdidos. É a plataforma retendo o dinheiro **dela**, não o do criador. Não aparece em nenhuma tela do criador, porque não é problema dele |
| 6 | **Cobrança do criador só com decisão humana** | Chargeback perdido **não** vira dívida do criador automaticamente. Só há cobrança em conluio comprovado ou entrega inexistente, com motivo, autor e data registrados. Fora disso, é custo da plataforma |
| 7 | **Pix como meio padrão** | Pix em destaque no checkout ("dinheiro liberado na hora para o criador"). Cartão é a segunda opção — reduz o volume exposto sem perder a venda de ticket alto |

📊 **A parte honesta, agora com número.** Premissas declaradas: ticket médio R$ 1.200, 40% do GMV em cartão, taxa de chargeback de 0,6% (referência de mercado brasileiro), e 60% dos chargebacks sendo fraude pura — coberta pelo 3DS.

| | Lançamento (20 contratos/mês) | Operação (1.000 contratos/mês) |
|---|---|---|
| GMV | R$ 24.000 | R$ 1.200.000 |
| Perda esperada após 3DS | R$ 23/mês | R$ 1.152/mês |
| Receita de comissão | R$ 1.800 (7,5%) | R$ 180.000 (15%) |
| **Perda ÷ comissão** | **1,3%** | **0,64%** |

🔴 **A conclusão que muda a medida certa: a perda média sempre coube na comissão. Ela nunca foi o problema.** O problema é **concentração**. Com 20 contratos por mês, um único chargeback de R$ 1.200 consome dois terços da comissão do mês, e um contrato de R$ 20.000 contestado apaga onze meses de receita. Não existe lei dos grandes números com 20 contratos. **Por isso a medida certa é teto de exposição por transação (camada 2), e não retenção no tempo** — segurar 90 dias protegia contra a média, que já cabia, e não protegia contra o caso isolado, que é o que mata.

⚠️ **Nem a Garantia de Chargeback nem o antifraude vêm inclusos** no produto padrão do Pagar.me — os dois são contratados à parte, e a Garantia cobre **apenas fraude**, não desacordo comercial. Entram quando o volume de cartão justificar o custo fixo; até lá, o 3DS é a camada 1. Fontes: [Garantia de Chargeback](https://conteudo.stone.com.br/garantia-de-fraude/), [Antifraude ClearSale](https://pagarme.helpjuice.com/pt_BR/antifraude-clearsale).

⚠️ **Pré-autorização não serve de escrow.** A janela de captura no Pagar.me é de 5 horas (checkout) ou 5 dias (API) — depois disso o emissor libera o valor. A ideia de "só capturo o cartão quando a entrega for aprovada" não funciona: o escrow tem que ser com dinheiro capturado. Fonte: [docs.pagar.me — Autorização e captura](https://docs.pagar.me/v3/docs/autoriza%C3%A7%C3%A3o-e-captura).

📌 **O que as plataformas comparáveis fazem:** a **Fiverr** debita do saldo do freelancer e só o protege "a seu exclusivo critério". A **Upwork** briga com o banco e preserva o pagamento do freelancer, desde que o fluxo dela tenha sido seguido. **Nenhuma das duas retém 90 dias do prestador.** E na Stripe Connect, no modelo que a INFLUENTZ usa, **a plataforma é sempre a responsável final** — isso não é escolha generosa, é como o sistema de cartão funciona. Fontes: [Stripe — Disputes on Connect platforms](https://docs.stripe.com/connect/disputes), [Fiverr](https://help.fiverr.com/hc/en-us/articles/360010978618-Chargebacks-and-freelancer-protection), [Upwork](https://support.upwork.com/hc/en-us/articles/14085353385747-What-happens-if-you-file-a-chargeback-as-a-client-on-Upwork).

### 4.4 Comissão (decisão 8)

| Item | Regra |
|---|---|
| Comissão total | **15%** — 10% do criador + 5% da marca |
| Recontratação | Cai para **8%** a partir da 3ª contratação entre a mesma marca e o mesmo criador |
| Lançamento | **7,5%** nos primeiros 90 dias **ou** nas primeiras 50 transações (o que vier primeiro) |
| Configuração | Ajustável no painel administrativo, **nunca fixa no código** |

*Referência de mercado:* Workana cobra do freelancer comissão escalonada de 20% caindo até 5% conforme recompra, mais 4,5% do contratante; 99Freelas cobra de 5% a 20% do freelancer. Marketplaces brasileiros em geral operam entre 10% e 20%. 15% posiciona a INFLUENTZ no meio da faixa, com desconto por fidelização — que é o mecanismo que a Workana usa e funciona.

### 4.5 Preço exibido (decisão 4)

**A marca vê e paga o preço final, tudo incluso.** A comissão é descontada do lado do criador antes do repasse. Sem surpresa no checkout, que é o principal ponto de atrito relatado por clientes de plataformas que somam taxa no final.

### 4.6 Escrow e marcos 🟢

- **Escrow sempre ativo:** o dinheiro fica retido até a entrega ser aprovada. Inegociável — é o que sustenta a confiança dos dois lados.
- **Marcos (entrega em etapas):** contrato simples e de valor baixo = uma entrega, um pagamento. Contrato maior ou mais longo = a plataforma sugere dividir em etapas automaticamente. Proteção sempre ligada; complexidade proporcional ao risco.

### 4.7 Cadastro fiscal do criador (decisão 2) ⚠️

**MEI ou CNPJ obrigatório** para receber acima de um valor acumulado baixo (referência: R$ 500).

Resolve de uma vez: retenção previdenciária, emissão de nota fiscal, crédito fiscal da marca e boa parte da exposição da plataforma. Abrir MEI é gratuito; a plataforma oferece um guia embutido para reduzir o atrito.

⚠️ Regime tributário, retenção de IR sobre a comissão e obrigações acessórias precisam de **contador especializado em plataforma digital** antes de virarem código.

---

## 5. Fluxo principal 🟢

1. **Criação** — marca (ou agência em nome dela) publica pedido, ou contrata direto da vitrine.
2. **Matching** — IA sugere criadores compatíveis; busca manual também disponível.
3. **Proposta e aceite bilateral** — condições confirmadas pelos dois lados antes de qualquer cobrança.
4. **Pagamento** — valor retido em escrow.
5. **Execução por marcos.**
6. **Revisão** — a marca pode pedir ajuste referenciado ao briefing antes de aprovar ou disputar (seção 12.1).
7. **Aprovação final e liberação** — dinheiro liberado ao criador conforme o prazo do meio de pagamento (§4.2), comissão retida.
8. **Disputa** — caminho alternativo, só depois de esgotada a revisão. Mediada pela equipe INFLUENTZ.
9. **Avaliação mútua** — double-blind (seção 13.1).

---

## 6. IA de matching 🟢

- **Nível 1 (lançamento):** filtro inteligente — categoria, orçamento, localização, tipo de entrega, histórico de avaliação.
- **Nível 2:** cruza métricas reais de audiência via API oficial (seção 9).
- **Nível 3:** IA lê o briefing em texto livre e sugere criadores com justificativa.

Lança no Nível 1, com a interface já preparada para os próximos.

### 6.1 Ordenação da busca 🟢

Decisão de negócio com peso alto: define quem ganha dinheiro na plataforma. Ordenar por avaliação enterra o criador novo — que é a maioria no lançamento.

**No v1:** relevância de categoria + cota garantida de exposição para criadores novos. **Destaque pago fica para depois** de haver demanda real — vender destaque em marketplace vazio não gera receita e destrói confiança.

---

## 7. Painel administrativo e equipe interna 🟢

Estrutura completa de papéis construída desde já: **Super Admin**, **Financeiro**, **Suporte**, **Trust & Safety**. No lançamento o Marco opera sozinho como Super Admin — mas a estrutura já existe, para não precisar refazer quando houver equipe.

### 7.1 Painel de cada usuário final

Cada tipo de usuário (criador, marca, agência) tem painel completo — não uma tela solta de contratos.

---

## 8. Compliance e jurídico (Brasil) 🟢 ⚠️

- **LGPD:** consentimento, política de privacidade, direito de exclusão de conta e dados.
- **Termos de Uso + Contrato de Prestação de Serviço:** gerado automaticamente por transação.
- **Disputas:** mediação humana com prazo máximo de resposta (seção 12).

### 8.1 Cancelamento e reembolso 🟢 ⚠️

O CDC protege relações de **consumo**; a maior parte dos contratos aqui é **B2B**, então o CDC não se aplica automaticamente. Ainda assim, adotamos o espírito protetivo:

| Momento do cancelamento | Regra |
|---|---|
| Até 24h após o aceite, antes do criador começar | Reembolso total |
| Criador já começou (marco em andamento) | Sem reembolso automático — mediação, liberação proporcional ao trabalho feito |
| Após aprovação final de um marco | Sem reembolso — serviço prestado e aceito |
| Comissão da plataforma | Devolvida integralmente dentro da janela de 24h; não reembolsada fora dela |

### 8.2 Direitos sobre o conteúdo (decisão 5) 🟢 ⚠️

**Padrão: uso limitado, com upgrade pago para uso ampliado.** Cada item é campo estruturado da proposta:

| Campo | Opções |
|---|---|
| Prazo de uso | 3 / 6 / 12 meses / perpétuo |
| Mídias permitidas | Redes sociais / site da marca / mídia paga / mídia offline (múltipla escolha) |
| Impulsionamento pago | Sim/não + verba máxima |
| Exclusividade | Nenhuma / 30 / 60 / 90 dias |
| Direito de imagem | Finalidade e prazo delimitados (autorização genérica e eterna é frágil no Brasil) |
| Retirada | Condições para exigir remoção em caso de polêmica de qualquer um dos lados |

*Por que isso é produto, não só jurídico:* cada campo tem preço implícito, o que aumenta o ticket médio e, portanto, a comissão.

### 8.3 Categorias reguladas e proteção de menores (decisão 6) 🟢 ⚠️

**Proibidas no v1:** apostas, bebida alcoólica, produtos financeiros e investimentos, saúde/medicamentos, e qualquer campanha dirigida ao público infantil. São as áreas de regra mais restrita e maior exposição para a plataforma.

**Conteúdo adulto / sexshop — permitido com trava:** a venda desses produtos é legal no Brasil e o CONAR não proíbe sua divulgação, mas impõe limites — o conteúdo não pode ser ofensivo à moral e **deve evitar exposição a menores de idade**. Portanto:

- Categoria adulta exige **verificação de idade por documento**, não autodeclaração, para ver e para se candidatar.
- **Criador menor de 18 anos é bloqueado pelo sistema** de qualquer campanha de categoria adulta ou sensível. Sem exceção, sem override manual.

### 8.3.1 ⚠️ Correção: assinatura do responsável **não basta** para criador menor de idade 🔴

**O que a v0.4 dizia:** criador menor de idade é permitido, bastando assinatura do responsável legal.

**Isso está juridicamente incompleto.** Pesquisa posterior mostrou que a assinatura do responsável resolve apenas metade do problema:

1. **Capacidade civil** — resolvida pela assinatura. Menor de 16 anos precisa ser *representado*; entre 16 e 18, *assistido*. É o que a v0.4 previa.
2. **Autorização judicial** — **não resolvida, e é a parte pesada.** O ECA, artigo 149, exige **alvará judicial** para participação de criança ou adolescente em atividade artística. A Lei nº 15.211/2025 (o "ECA Digital") trouxe isso explicitamente para o ambiente digital: quando há conteúdo monetizado, impulsionado ou exploração habitual da imagem do menor, a autorização judicial pode ser exigida.

**Por que isso muda o produto, e não só o contrato:** o alvará é obtido **pelos pais, através de advogado, em petição ao juiz da Vara da Infância e Juventude** da comarca onde o menor mora. A petição descreve a atividade, a frequência, a carga horária e o destino dos rendimentos. **Nenhuma plataforma consegue emitir isso** — é decisão de um juiz, caso a caso, por criança.

**Isso já está sendo cobrado na prática:** perfis com crianças e adolescentes como protagonistas de conteúdo monetizado vêm sendo notificados a apresentar o alvará sob pena de bloqueio da conta.

🟢 **Decisão para o v1: criador precisa ter 18 anos completos.**

- A trava é automática e sem exceção, conferida pela data de nascimento que a **verificação de identidade do provedor de pagamento já entrega** (§13). Não pede documento novo, não custa nada a mais.
- Marca e agência não têm essa trava — são pessoa jurídica ou representante dela.

*Por que bloquear e não construir o fluxo:* construir agora significaria criar um caminho para um terceiro que **não tem conta na plataforma** (o responsável) assinar, mais a conferência de que ele é mesmo o responsável, mais o recebimento e a validação de um alvará judicial — e ainda assim a plataforma continuaria exposta se o documento fosse falso ou vencido. É a maior exposição jurídica isolada do produto inteiro, num v1 cuja meta (§14) é provar o ciclo com 20 contratos.

🔵 **Caminho para o v2:** o mercado de criador adolescente é real (moda, games, beleza). Ele entra depois, com o alvará como documento obrigatório anexado ao perfil, prazo de validade controlado pelo sistema, e revisão de advogado antes de abrir. Bloquear no v1 não fecha a porta — adia a porta até ela ser segura.

⚠️ Toda esta seção precisa de validação de advogado antes de virar Termos de Uso.

---

## 9. Redes sociais, métricas e verificação 🟢 ⚠️ reescrito em 08/09/2026

> **Revisado por:** especialista `produto`, com pesquisa na documentação oficial da Meta, do TikTok e do Google.

**Conexão direta com a API oficial de cada rede (Instagram, TikTok, YouTube), sem intermediário pago.** O usuário autoriza com um clique e os dados vêm da fonte.

🔴 **Regra travada, sem exceção: na INFLUENTZ não existe métrica que não venha de API.** Não existe captura de tela, não existe número digitado pelo usuário, não existe fila de aprovação manual de métrica. Se o dado não veio da API da rede, ele não aparece na plataforma.

### 9.1 Como isso é possível no dia 1, sem esperar aprovação 🟢 ⚠️ corrigido

⚠️ **O que foi eliminado.** A versão anterior criava um nível "Declarada": o criador mandava captura de tela, o Trust & Safety aprovava à mão, e a métrica aparecia rotulada como não verificada. **Foi recusado pelo dono do produto**, e com razão — é trabalho manual empurrado para o usuário porque a integração é difícil, exatamente o que `CLAUDE.md` §2.9 proíbe.

**O problema real que ele resolvia é verdadeiro:** o App Review do Instagram leva semanas, e o criador convidado pessoalmente (§14.1) não pode ficar travado esperando.

✅ **A solução é que as três plataformas já têm mecanismo oficial de pré-aprovação — e ele devolve dado real de API, não estimativa.** Não é contorno: é o caminho que a própria Meta, o TikTok e o Google desenharam para piloto.

| Rede | Ponte oficial no dia 1 | Capacidade | Fonte |
|---|---|---|---|
| **TikTok** | Sandbox: 5 sandboxes × 10 contas-alvo | **50 criadores** | [Add a Sandbox](https://developers.tiktok.com/docs/en/add-a-sandbox) |
| **Instagram** | *Instagram Tester* + Standard Access — "permissions with Standard Access can only be requested from app users who have a role on the requesting app", e todo app Business já nasce com Standard Access | dezenas (a Meta não publica teto) | [Access Levels](https://developers.facebook.com/docs/graph-api/overview/access-levels) |
| **YouTube** | Modo Testing: 100 testers; depois, verificação de escopo sensível em **3 a 5 dias úteis** | 100 | [Sensitive scope verification](https://developers.google.com/identity/protocols/oauth2/production-readiness/sensitive-scope-verification), [Manage App Audience](https://support.google.com/cloud/answer/15549945?hl=en) |

O criador aceita um convite dentro do app da própria rede e autoriza. **A métrica que chega é da API, igual à do dia 200.** A diferença é só administrativa e invisível para ele.

⚠️ **Duas ressalvas honestas, que ficam registradas:**

1. **Sandbox e modo de desenvolvimento existem para testar, não para operar.** Rodar 50 criadores pagantes ali estica a intenção da regra. O risco não é multa — é a Meta ver uso de produção em modo dev na hora do review. Mitigação obrigatória: coorte-piloto **fechada e com prazo**, e o App Review submetido **em paralelo, não depois**.
2. **O relógio do App Review só começa quando o fluxo de conexão existe funcionando**, porque a Meta exige vídeo de tela do fluxo real. Não dá para submeter antes do produto.

### 9.1.1 As fases, e o que trava o quê ⚠️

**Fase 0 — antes de qualquer código de conexão.** Abrir a **Verificação de Empresa da Meta** (prazo divulgado: até 14 dias úteis) e verificar o domínio no Google. É o único item de prazo que não depende do produto — por isso começa já.

🔴 **CNPJ é caminho crítico do projeto inteiro.** Desde 01/02/2023 a Verificação de Empresa é **obrigatória** para Advanced Access ([Business Verification](https://developers.facebook.com/docs/development/release/business-verification)), e ela exige CNPJ, contrato social, comprovante de endereço e domínio verificado. Sem CNPJ, o Instagram nunca sai do teto do modo piloto. **Isto é decisão de dono, e é a mais urgente do projeto.**

**Fase 1 — dia 1 do cold start.** YouTube em Testing (100 testers) · Instagram por convite de Tester · TikTok em sandbox. Em paralelo, submeter YouTube (3–5 dias úteis) e TikTok ("several days to two weeks", [App Review FAQ](https://developers.tiktok.com/doc/getting-started-faq)).

**Fase 2 — quando o fluxo estiver pronto.** Submeter o App Review do Instagram com o vídeo de tela. A Meta não publica SLA; relatos de mercado em 2026 falam em ~20 dias de média e 4 a 6 semanas ponta a ponta com uma rodada de correção — **fonte secundária, não oficial**.

**Fase 3 — aprovado.** Vira Advanced Access / produção. **Os criadores da coorte não refazem nada** — o token deles continua válido, só muda o modo do app. Isso precisa estar previsto na modelagem de dados desde já.

**Rede de segurança contratada, não improvisada:** negociar com um agregador de dados (Phyllo/InsightIQ) **com data-gatilho**. Se o App Review da Meta não sair até a data X, liga o agregador e ninguém fica sem métrica. Não é o plano principal: preço não é público, e custo recorrente por criador não combina com receita de comissão. ⚠️ Antes de assinar, passa pelo `financeiro` — precisa de teto e gatilho de saída.

### 9.1.2 Conta pessoal não tem API — e isso vira passo de onboarding, não recusa 🟡

A API do Instagram atende apenas contas **profissionais** (Business ou Creator), e não exige mais Página do Facebook vinculada ([doc oficial](https://developers.facebook.com/docs/instagram-platform/instagram-api-with-instagram-login)). Conta pessoal não tem API nenhuma — não existe rota pública.

✅ **Converter para conta profissional é grátis e leva cerca de um minuto, dentro do app da rede.** Então isso não é motivo de recusa: é uma tela com o passo a passo e um botão de "já converti, tentar de novo".

### 9.1.3 O que o usuário vê

- **Criador:** "Conecte sua rede para aparecer na busca" → autorização. Se for conta pessoal, o passo a passo de conversão. Se estiver na coorte-piloto, um passo a mais: aceitar o convite dentro do app da rede, com a imagem do caminho exato. **Nenhuma tela pede captura de tela. Nenhuma.**
- **Métrica, sempre com carimbo:** *"seguidores 82.400 · da API do Instagram · atualizado há 6 h"*. Se o token expirou, faixa de aviso com "métrica congelada em 12/09 — reconecte" e botão. O contrato em andamento **não** para (MAQUINA §3).
- **Marca:** um selo só — **"conectado por API"** — com a data da última atualização. Não existe mais métrica sem selo, porque não existe mais métrica sem API.
- **Admin:** some a fila de aprovação manual. Nasce o **painel de saúde das conexões**: quantas expiraram, quantas foram revogadas, status de cada App Review, e quantas vagas restam na coorte-piloto.

### 9.1.4 Riscos, sem maquiagem

| Risco | Consequência real | O que fazer |
|---|---|---|
| Meta reprova o App Review | Instagram fica preso ao teto do modo piloto — e é a rede principal do mercado brasileiro | Data-gatilho com o agregador. Reprovação quase sempre é vídeo ruim ou justificativa vaga, e cabe recurso — mas cada rodada reinicia o relógio |
| **Sem CNPJ** | Advanced Access é impossível. Trava o produto, não só a métrica | Decisão do Marco, na Fase 0 |
| Token do Instagram expira (60 dias sem uso) | Métrica congela | Rotina de renovação + estado `token_expirado` com botão. **Nunca apagar a métrica anterior** — mostrar com data |
| Criador só tem conta pessoal | Não conecta | §9.1.2 — conversão vira passo do onboarding |
| Coorte-piloto lota (50 no TikTok) | Criador 51 fica sem TikTok | Lista de espera com data, e submeter o review antes de chegar em 40 |
| API da rede cai | Métrica não atualiza | Mostrar a última leitura com data. **Nunca zero, nunca em branco** |

⚠️ **Vai para o `juridico-br` antes de virar tela:** conectar rede social é tratamento de dado pessoal — a base legal do consentimento precisa estar no Termo, e é preciso definir o que acontece com a métrica coletada quando o criador desconecta ou pede exclusão (LGPD).

📌 **O que a concorrência faz:** a Squid (hoje Squid by Wake) integra por API oficial da Meta e do TikTok, com atualização em até 24 h ([central de ajuda](https://meajuda.squid.com.br/docs/como-conectar-o-meu-instagram-a-squid)). Métrica por captura de tela não é padrão de mercado — é gambiarra.

### 9.2 Detecção de fraude de engajamento — escopo corrigido 🟡

A versão anterior propunha analisar proporção curtida/comentário, padrão e horário dos comentários. **Isso não é viável pela via oficial:** as APIs entregam métricas agregadas do perfil autorizado, não o conteúdo de comentários nem a lista de seguidores.

O que dá para fazer com dado oficial: **evolução de seguidores ao longo do tempo** (picos anormais são detectáveis) e **taxa de engajamento agregada versus a mediana da categoria**. Pega os casos grosseiros.

---

## 10. Chat 🟢

**O chat só abre depois da proposta aceita e paga.** Antes disso, a comunicação acontece dentro da própria proposta, em campos estruturados (perguntas e ajustes).

*Por quê:* chat liberado antes do contrato é a porta de saída número um de qualquer marketplace. Fechar essa porta por design é mais eficaz — e menos invasivo — do que vigiar conversa.

---

## 11. Notificações 🟡

Central de notificações dentro do produto **não basta** — no início ninguém entra no produto sozinho. As notificações que importam (proposta recebida, prazo vencendo, entrega para aprovar) precisam sair.

- **v1:** e-mail (barato e imediato)
- **v2:** WhatsApp (tem custo por mensagem e exige aprovação de modelos de mensagem)

---

## 12. Disputa e mediação 🟢

### 12.1 Revisão antes da disputa

A marca pode pedir ajuste **referenciado ao briefing** antes de aprovar ou abrir disputa. Reduz drasticamente o volume de mediação.

### 12.2 Disputa

Mediada pela equipe INFLUENTZ, com prazo máximo de resposta, priorizada por risco em painel próprio de Trust & Safety.

---

## 13. Confiança e antifraude 🟢

- **Identidade verificada:** reaproveita a verificação já exigida pelo provedor de pagamento — sem pedir documento duas vezes.
- **Verificação de empresa:** CNPJ ativo confirmado antes de publicar campanha paga.
- **Fraude e lavagem:** apoiado nas ferramentas do provedor, complementado com regras próprias — limite para contas novas, alerta quando o mesmo CPF/CNPJ aparece como marca *e* criador na mesma transação, revisão manual acima de valor definido.

### 13.1 Avaliação mútua sem retaliação 🔵

As duas avaliações ficam ocultas até ambos enviarem (ou o prazo vencer). Elimina a nota-por-vingança. Mesmo mecanismo do Airbnb.

### 13.2 Tentativa de fechar por fora 🟢 ⚠️

1. **Detecção:** monitoramento **dentro do chat da própria plataforma** (nunca fora dela) de padrões que sugerem fechar por fora.
2. **1ª ocorrência:** lembrete automático no chat mostrando as vantagens objetivas de fechar pela plataforma. Convencer, não ameaçar.
3. **Reincidência:** registro formal visível para Trust & Safety — uma pessoa revisa antes de qualquer ação.
4. **Reincidência após aviso formal:** suspensão temporária e, persistindo, banimento.
5. ⚠️ Monitorar conteúdo de mensagem, mesmo interno, precisa estar explícito nos Termos de Uso e na Política de Privacidade (transparência exigida pela LGPD).

---

## 14. Escopo do lançamento (v1) 🟢

**Meta de validação:** 50 criadores com perfil completo, 10 marcas cadastradas, 20 contratos pagos e concluídos. Números pequenos de propósito — o objetivo é provar que o ciclo inteiro funciona com dinheiro de verdade, não crescer.

### 14.1 Cold start 🔴

Um marketplace vazio não tem produto. Isso não é marketing, é viabilidade.

**Os primeiros 50 criadores e as primeiras 10 marcas entram por convite pessoal do Marco**, com cadastro feito junto com eles. É trabalho manual, não escala — e é exatamente assim que todo marketplace começou.

> **Pergunta em aberto para o Marco:** quantos criadores e quantas marcas atenderiam seu telefone hoje? Essa lista é o ativo mais valioso do projeto neste momento.

---

## 15. Pendências que exigem profissional humano ⚠️

| Tema | Profissional | Bloqueia o quê |
|---|---|---|
| Regime tributário, retenção de IR sobre comissão, obrigações acessórias | Contador especializado em plataforma digital | Código de pagamento |
| Como lançar a perda de chargeback: despesa do período ou provisão? O fundo de contestação é conta contábil ou só segregação de caixa? | Contador | Código de pagamento |
| Comissão já tributada sobre transação depois revertida — dá para recuperar o tributo sobre receita que deixou de existir? | Contador | Código de pagamento |
| Nota fiscal em contrato revertido: o criador emitiu NF, prestou o serviço, e o banco devolveu o dinheiro. Cancela? Emite devolução? | Contador | Lançamento |
| Repasse que a plataforma absorveu — é despesa dedutível? | Contador | Código de pagamento |
| Custo da antecipação de recebíveis embutido no preço: natureza contábil e tributária | Contador | Código de pagamento |
| Termos de Uso, Política de Privacidade, direito de imagem, monitoramento de chat | Advogado | Lançamento |
| Categorias reguladas e proteção de menores (§8.3) | Advogado | Lançamento |
| **A relação criador↔plataforma é de consumo ou B2B?** | Advogado | Redação dos Termos, do cancelamento e da comissão |
| Tela e registro de aceite: o que fica gravado e como se prova | Advogado | Lançamento |
| Aprovação automática por silêncio — sobrevive ao CDC art. 51? | Advogado | Lançamento |
| Base legal e ROPA da fase de convite; prazo de retenção do rascunho; aviso de coleta indireta (LGPD art. 9º) | Advogado | Ferramenta de convite |
| O que é compartilhado com a Pagar.me, quando, e como aparece na Política de Privacidade | Advogado | Código de pagamento |
| Regra interna de acesso do Admin a dado de terceiro, com trilha de auditoria (LGPD art. 46) | Advogado | Lançamento |
| Texto da mensagem de convite: identificação do remetente, origem do contato, opt-out | Advogado | Ferramenta de convite |
| Cláusula de responsabilidade por chargeback: a INFLUENTZ absorve, com exceções (conluio, entrega inexistente) que sobrevivam a questionamento | Advogado | Lançamento |
| Validade do clawback — pode a plataforma debitar saldo futuro do criador por decisão administrativa própria? Precisa de anuência prévia, contraditório, prazo? | Advogado | Lançamento |
| Retenção de dados para defesa × LGPD: a janela de chargeback vai a 540 dias e a defesa exige log de chat, IP e horário de aceite. Qual prazo é defensável? | Advogado | Lançamento |
| Exposição ao MED do Pix: obrigações da plataforma quando um Pix recebido é contestado por fraude | Advogado | Código de pagamento |
| Redação da promessa "a INFLUENTZ garante seu pagamento" — mal escrita, vira obrigação incondicional | Advogado | Lançamento |
| Conectar rede social é tratamento de dado pessoal: base legal do consentimento no Termo, e o que acontece com a métrica quando o criador desconecta ou pede exclusão | Advogado | Tela de conexão |

📌 **A pergunta mais estruturante da lista é a primeira.** Enquanto não houver resposta de advogado, **tratamos a relação como de consumo** — é o cenário mais caro, e preparar-se para ele não custa nada se a resposta vier ao contrário. O STJ aplica o finalismo mitigado, e criador pessoa física costuma ser reconhecido como vulnerável, mesmo prestando serviço profissional.

---

## 16. Nota de reconstrução

Esta v0.4 foi reconstruída a partir do histórico de conversas do projeto, porque o arquivo original da v0.3 vivia apenas em uma conversa avulsa — falha estrutural corrigida com a adoção deste repositório e do `CLAUDE.md`.

Se ao ler alguma seção o Marco reconhecer algo que ficou de fora da v0.3, basta apontar: o Git preserva o histórico e a correção entra como uma nova versão, sem retrabalho.

---

*As referências a legislação e a comportamento de plataformas de pagamento são levantamento de arquitetura, não parecer jurídico ou contábil.*
