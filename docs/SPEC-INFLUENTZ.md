# SPEC — INFLUENTZ

> **O que é este documento.** A fonte da verdade do produto. Toda tela, toda tabela do banco de dados, todo fluxo de pagamento aponta de volta para aqui. Quando algo mudar na visão do produto, muda aqui primeiro — e só depois no código.
>
> **Versão:** v0.4
> **Status:** as 8 decisões de produto que estavam em aberto foram travadas. Provedor de pagamento corrigido de Stripe Connect para Pagar.me.
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

### 4.2 Meios de pagamento aceitos (decisão 3)

| Meio | Aceito no v1 | Quando o dinheiro fica disponível |
|---|---|---|
| **Pix** | Sim | Na hora, inclusive dentro do split |
| **Boleto** | Sim | 1 a 2 dias após confirmação |
| **Cartão de crédito** | Sim, **só para marca com CNPJ verificado** | **D+30** — padrão do sistema de cartão brasileiro, não regra da INFLUENTZ |

*Por que cartão entra:* ambiente corporativo usa cartão intensamente. Excluí-lo eliminaria uma fatia relevante da demanda.

⚠️ **Regra de ouro contra risco de falência:** a plataforma **nunca adianta dinheiro que ainda não recebeu do provedor.** Uber e iFood adiantam valores ao motorista/restaurante com capital de giro próprio — copiar isso sem caixa é como emprestar dinheiro inexistente. O criador vê no app a data exata em que cada valor vira saldo disponível.

🔵 **Antecipação de recebíveis:** quem não quiser esperar o D+30 do cartão pode antecipar mediante taxa — serviço já pronto no Pagar.me. Vira segunda fonte de receita, não risco.

### 4.3 Proteção contra contestação de compra (chargeback)

A proteção **não** vem de segurar o dinheiro de todos preventivamente — isso puniria os casos normais para cobrir os raros. Vem de:

1. **Prova documental:** todo contrato passa pelo fluxo oficial (marco combinado antes de começar, entrega enviada pelo sistema, aprovação registrada). É o que sustenta a defesa junto ao banco. É exatamente o mecanismo de proteção de pagamento do Upwork — que condiciona a cobertura a o marco ter sido financiado antes do início e a entrega ter sido submetida pelo fluxo da plataforma. Fonte: https://support.upwork.com/hc/en-us/articles/211063748
2. **3D Secure** e análise automática de fraude em toda cobrança por cartão — reduz a chance de a contestação existir.
3. **Reserva temporária apenas para conta nova**, durante um período de teste curto — não permanente.
4. Se a contestação chegar após a liberação, o valor é descontado do saldo futuro do criador. Nunca do caixa da INFLUENTZ.

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

**Criador menor de idade (fora das categorias sensíveis):** permitido, mas o contrato exige **assinatura do responsável legal**. Menor não assina contrato sozinho no Brasil — sem isso, o contrato é inválido e a plataforma fica exposta.

⚠️ Toda esta seção precisa de validação de advogado antes de virar Termos de Uso.

---

## 9. Redes sociais, métricas e verificação 🟢

**Conexão direta com a API oficial de cada rede (Instagram, TikTok, YouTube), sem intermediário pago.** O usuário autoriza com um clique e os dados vêm da fonte — sem assinatura mensal.

**Trade-off honesto:** cada rede tem processo próprio de aprovação. YouTube é o mais rápido; Instagram e TikTok exigem verificação de empresa e revisão do aplicativo — semanas a meses, fora do nosso controle.

**Como não travar o lançamento:** vai ao ar com **YouTube conectado no dia 1**; Instagram e TikTok entram conforme cada aprovação sai. A arquitetura já nasce pronta para os três.

### 9.1 Pelo menos uma rede conectada é obrigatória 🟢

Vale para criador, marca **e** agência — para publicar serviço, propor contrato ou aparecer na busca.

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
| Termos de Uso, Política de Privacidade, direito de imagem, monitoramento de chat | Advogado | Lançamento |
| Categorias reguladas e proteção de menores (§8.3) | Advogado | Lançamento |

---

## 16. Nota de reconstrução

Esta v0.4 foi reconstruída a partir do histórico de conversas do projeto, porque o arquivo original da v0.3 vivia apenas em uma conversa avulsa — falha estrutural corrigida com a adoção deste repositório e do `CLAUDE.md`.

Se ao ler alguma seção o Marco reconhecer algo que ficou de fora da v0.3, basta apontar: o Git preserva o histórico e a correção entra como uma nova versão, sem retrabalho.

---

*As referências a legislação e a comportamento de plataformas de pagamento são levantamento de arquitetura, não parecer jurídico ou contábil.*
