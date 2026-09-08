# Feature Matrix — INFLUENTZ

> **O que é este documento.** O inventário **completo** de tudo que a plataforma faz, organizado por quem usa e por módulo. É o documento que existe para garantir que **nada falta**.
>
> Ele nasce de uma instrução direta do Marco: *"não faltar nada, absolutamente nada neste produto, que o cliente na hora que usar sinta falta."*
>
> **Como ler a prioridade:**
> **E** = essencial (sem isso não existe produto) · **P** = premium (é o que faz a plataforma valer a comissão) · **F** = futuro (depois de haver volume)
>
> **Versão:** v2.1 — **~81 funções vivas no v1**. Ver §0.2 (o corte) e §5.7 (as quebras do caminho).
> **O que mudou da v1.0:** acesso por plataforma corrigido (§0.1), contrato recorrente reincorporado (§3.5), e **30 funções acrescentadas pela auditoria do especialista de produto** (§5.5), que encontrou 12 lacunas — 8 delas capazes de travar o lançamento.
> **Fonte de marca:** `docs/marca/` — pasta BRANDING do Drive, estudada por inteiro
>
> **Legenda:** 🔵 proposta de Claude além do que foi pedido · ⚠️ decisão com risco ou dependência

---

## 0. As quatro superfícies 🟢

Um erro das telas anteriores foi não deixar claro de quem era cada visão. Corrigido: **a plataforma tem quatro superfícies**, e toda tela declara a qual pertence.

### 0.1 ⚠️ Correção: ninguém fica preso a uma plataforma

**A v1.0 deste documento deu a entender que o criador só teria aplicativo de celular. Isso estava errado, e o Marco corrigiu.**

🟢 **Regra: todo usuário tem acesso completo em toda plataforma.**

| | Web responsivo | iOS | Android |
|---|---|---|---|
| Criador | ✅ completo | ✅ | ✅ |
| Marca | ✅ completo | ✅ | ✅ |
| Agência | ✅ completo | ✅ | ✅ |
| Admin | ✅ completo | — | — |

**Nenhuma função existe em um lugar e falta no outro.** Um criador que só tem computador precisa conseguir fazer tudo; uma marca que precisa aprovar uma entrega no aeroporto precisa conseguir aprovar pelo celular.

**O que muda é para qual contexto cada tela é desenhada primeiro** — e isso é decisão de desenho, não de acesso:

| Superfície | Contexto principal | Por quê | Mas também roda em |
|---|---|---|---|
| **CREATOR** | Celular | O criador grava, publica e acompanha do telefone. Entregar arquivo, ver agenda e conferir saldo acontece na rua | web completo, e web é onde ele monta a vitrine com calma |
| **BRAND** | Computador | Comparar 5 propostas lado a lado, revisar contrato e aprovar pagamento é trabalho de mesa | celular completo, com layout próprio para aprovar e acompanhar |
| **AGENCY** | Computador | Opera várias marcas e criadores ao mesmo tempo | celular completo |
| **ADMIN** | Computador | Mediação, financeiro e Trust & Safety exigem tela grande | — |

⚠️ **Desenhar para o contexto principal não é espremer o outro.** A tela de comparação no celular não é a tabela de computador encolhida — vira cartões que se empilham. Duas telas diferentes, mesma função, nenhuma perda.

🔵 **Uma pessoa pode ter mais de um espaço.** O dono de agência também é criador; o gerente atende três marcas. Sem isso, ele precisa de três logins e a plataforma parece amadora. Um seletor de espaço no topo resolve.

---

## 0.2 🔴 O CORTE DE 08/09/2026 — leia isto antes da lista

> **Revisado por:** especialista `cortador`, com contexto limpo. Ele é a única voz do projeto autorizada a deletar (`CLAUDE.md` §2.2).

**As funções abaixo estão riscadas na lista, com o motivo em cada linha.** Nada foi apagado do arquivo: quem construir precisa saber o que foi cortado e por quê, para não recriar por engano.

### O placar

| | |
|---|---|
| Entraram | **171 numeradas** |
| ❌ **Morrem** | **38** — a capacidade some do v1 |
| 🔗 **Somem da lista sem sumir do produto** | **22** — a mesma coisa contada duas ou três vezes, ou regra escrita como função |
| 🔵 **Adiadas (módulos inteiros)** | **23** |
| ✅ **Sobra** | **≈ 84 — metade do que estava escrito** |

### Três números que descrevem o problema melhor que qualquer parágrafo

1. **122 das 170 estavam marcadas "Essencial". 72%.** Quando quase tudo é essencial, a etiqueta parou de decidir alguma coisa.
2. **O documento dizia 172 e o arquivo tinha 171 numeradas.** O inventário que existe para não deixar faltar nada não conseguia contar a si mesmo.
3. 🔴 **Não existia função de avaliação. Nenhuma.** A avaliação mútua é o passo 9 do fluxo principal da SPEC §5, tem uma máquina de estados inteira e está no fim da própria Fatia 1 — e não tinha número. **A auditoria acrescentou 30 funções e passou por cima do último passo do ciclo enquanto criava um gerador automático de dossiê de chargeback.** A matriz cresceu onde os revisores olharam, não onde o produto precisa. Corrigido em §2.9 e §3.9.

### A leitura honesta, e ela vale mais que a lista

O padrão que matou o bloco de convite estava **em todo lugar onde um especialista foi acionado sem contrapeso.** `produto`, `financeiro` e `juridico-br` foram convocados para achar o que falta, e cada um achou — todos corretos dentro do próprio recorte, e **nenhum deles com autoridade para dizer "isso não vale o que custa"**. Foi assim que uma perda esperada de **R$ 23 por mês** gerou quatro funções: dossiê automático, fundo com painel, teto por transação e saldo negativo. **O raciocínio nunca foi errado. Só nunca foi confrontado com o tamanho do problema.**

**Onde o produto estava mais inchado, em uma frase:** no aparato administrativo e antifraude — Admin, chargeback, saúde de API e coorte-piloto somavam quase 30 funções para socorrer 20 contratos por mês operados por uma pessoa, enquanto o passo final do fluxo, a avaliação, não tinha número nenhum.

### ⚠️ Três contradições encontradas, e duas já corrigidas

1. ✅ **Antecipação de recebíveis (73) × regra de ouro (SPEC §4.2).** O mesmo repositório prometia e proibia adiantar dinheiro. **Função cortada.**
2. ✅ **Nota fiscal como portão bloqueante (150) × decisão travada** *"o criador nunca espera mais que o prazo do meio de pagamento"*. **Portão removido; o anexo fica.**
3. ⚠️ **Pedido aberto está na Fatia 2 (§7) e numa decisão travada do v1.** Duas verdades sobre o mesmo módulo — **em aberto.** O mesmo vale para agência: decisão travada do v1 na SPEC §2, e Fatia 4 aqui.

### O que NÃO foi cortado, e por quê

Para não sobrar dúvida sobre o que ficou de fora da faca: **10** (LGPD — lei não se corta) · **65** (CONAR, é o escudo da plataforma e custa uma caixa de seleção) · **166** (sem Termos versionados a aprovação por silêncio não é oponível a ninguém) · **127** (é por ele existir que deu para cortar o dossiê automático) · **143** e **144** (saídas de beco sem saída: gente com dinheiro aprovado que não sai) · **145** (sem os dados de reembolso, o dinheiro devolvido não tem para onde ir) · **157** (a MAQUINA §8.0 faz o relógio do criador começar aqui; sem ele o criador leva penalidade por atraso dos Correios) · **§1.5**, os seis estados obrigatórios de toda tela · **92** (decisão travada, não reabre).

---

## 0.3 🎯 A LISTA MÍNIMA VIÁVEL — o que se constrói primeiro

O menor conjunto que fecha o ciclo inteiro: *criador se cadastra → aparece → marca contrata → paga → criador entrega → marca aprova → criador recebe → os dois se avaliam.* **Caminho remoto, vitrine, um marco, Pix.**

**Anel 1 — o ciclo, e nada além dele:**

| Etapa | Funções |
|---|---|
| Criador se cadastra | 1, 3, 5, 7, 9, 166 |
| Conecta rede e ganha métrica | 11, 13, 14, 142, 142.2 |
| Aparece | 48, 52, 54, 84 |
| Marca entra e contrata | 1, 3, 8, 80, 81, 86, **173** |
| Aceite | 58, 59 |
| Paga (Pix, escrow) | 101, 105 |
| Trabalho | 62, 63, 65, 66, 93 |
| Marca aprova ou pede ajuste | 94, 95 |
| Criador recebe | 143, 68, 69, 70, 71, **175, 176** |
| **Os dois se avaliam** | **170, 171, 172** ← a lacuna que não existia |
| Quando quebra | 32, 67, 100, 161–163, 118, 119, 120, 122, 127 |
| Toda tela | §1.5, os seis estados |

**Anel 2 — entra logo depois, ainda no v1:** 10, 21, 22, 23, 24, 40, 41, 50, 53, 64, 75, 76, 79, 87, 88, 89, 92, 99, 144, 145, 150 (sem portão), 151, 154, 156, 157, 167, 123, 128 (só o botão de denúncia), **174, 177**.

**Fora do v1, por decisão consciente e não por esquecimento:** presencial, marcos múltiplos, recorrência, agência, comparador, aditivo, cartão parcelado.

---

## 1. Comum a todos — a base que sustenta tudo

### 1.1 Conta e identidade

| # | Função | Prio | Observação |
|---|---|---|---|
| 1 | Cadastro por e-mail e senha | E | |
| 2 | ~~Entrar com Google / Apple~~ | P | Reduz atrito no cadastro |<br>🔵 ADIADA — segundo caminho de autenticação = classe inteira de bugs de conta duplicada. E-mail e senha resolve 100% de 50 criadores convidados a dedo
| 3 | Verificação de e-mail e telefone | E | |
| 4 | ~~Autenticação em duas etapas~~ | P | Obrigatória para quem movimenta dinheiro |<br>🔵 ADIADA — ⚠️ **em troca, a reconfirmação por e-mail/SMS na 143 passa a ser obrigatória.** A defesa exata contra desvio de repasse não é 2FA em todo login: é confirmação reforçada na troca de conta bancária. Sem essa contrapartida, o adiamento não vale
| 5 | Escolha de papel (criador / marca / agência) | E | |
| 6 | ~~**Seletor de espaço de trabalho**~~ | P | 🔵 A mesma pessoa em vários espaços |<br>🔵 ADIADA a tela — numa base de 60 pessoas, quantas são dona de agência E criadora? ⚠️ **O modelo de dados aceita vários vínculos desde já**, senão é reescrita
| 7 | Verificação de identidade (documento) | E | Reaproveita a do provedor de pagamento |
| 8 | Verificação de CNPJ | E | Para marca e agência |
| 9 | Recuperação de senha | E | |
| 10 | Encerrar conta e baixar meus dados | E | ⚠️ LGPD |

### 1.2 Conexão com redes sociais ⚠️ módulo crítico

Aqui mora uma das melhores observações do Marco: **API de rede social quebra, e a plataforma não pode fingir que não.**

| # | Função | Prio | Observação |
|---|---|---|---|
| 11 | Conectar Instagram / YouTube / TikTok | E | Ao menos uma é obrigatória |
| 12 | ~~**Logotipo oficial e atualizado de cada rede**~~ | E | Seguindo o guia de marca de cada plataforma |<br>🔗 SAI DA CONTAGEM — é ativo de marca, não função
| 13 | Mostrar qual conta está conectada e desde quando | E | |
| 14 | Desconectar rede | E | |
| 15 | ~~**Monitor de saúde da conexão**~~ | E | 🔵 Verifica periodicamente se o acesso ainda funciona |<br>🔗 FUNDE na 142.2 — uma rotina só
| 16 | ~~**Aviso de reconexão necessária**~~ | E | 🔵 "Seu Instagram precisa ser reconectado" — no app, por e-mail e por push |<br>🔗 FUNDE na 142.2 — uma rotina só
| 17 | ~~**Selo de atualidade em toda métrica**~~ | E | 🔵 "atualizado há 2 dias" · "desatualizado desde 12/09" |<br>🔗 FUNDE na 142 — é o mesmo carimbo
| 18 | ~~**Dado ausente nunca aparece como zero**~~ | E | 🔵 Mostra "não disponível", nunca "0" |<br>🔗 SAI DA CONTAGEM — é regra de exibição, já escrita em §6 e na SPEC §9.1.3
| 19 | ~~Painel administrativo de saúde das APIs~~ | P | Quando a rede muda a versão, o Admin vê antes do usuário reclamar |<br>❌ CORTADA — é a 141 com outro nome
| 20 | ~~Congelar métrica com data de corte quando a conexão cai~~ | P | Melhor mostrar dado velho rotulado do que dado errado |<br>🔗 SAI DA CONTAGEM — mesma regra da 18

⚠️ **Por que isso é crítico e não detalhe:** métrica velha mostrada como atual é a forma mais rápida de uma plataforma de criadores perder credibilidade. Se a marca contrata com base num número desatualizado e descobre depois, a culpa é da plataforma.

### 1.3 Notificações

| # | Função | Prio | Observação |
|---|---|---|---|
| 21 | Central de notificações no produto | E | |
| 22 | E-mail para o que é crítico | E | Proposta recebida, prazo vencendo, entrega para aprovar |
| 23 | Push no celular | E | |
| 24 | Marcador visual de não lido | E | |
| 25 | ~~Preferências por tipo de notificação~~ | P | |<br>❌ CORTADA — configuração que ninguém mexe. No v1 existem as notificações que a pessoa quer receber
| 26 | WhatsApp | F | Tem custo por mensagem e exige aprovação de modelos |
| 27 | ~~Alerta sonoro~~ | ❌ | ⚠️ **Não recomendo.** Navegador bloqueia som automático, e ferramenta de trabalho que apita é ferramenta silenciada na primeira semana. Push resolve melhor. Registro a discordância; se o Marco decidir o contrário, eu faço |

### 1.4 Ajuda dentro da tela

| # | Função | Prio | Observação |
|---|---|---|---|
| 28 | ~~**Dica explicativa em todo número que exige interpretação**~~ | E | 🔵 Toda métrica, taxa e prazo tem uma frase que explica |<br>🔗 SAI DA CONTAGEM — é regra de escrita, já em §1.4 e §6
| 29 | ~~Origem do dado visível~~ | E | De qual rede veio, de que período |<br>🔗 FUNDE na 142 — é o mesmo carimbo
| 30 | ~~Primeiro uso guiado por papel~~ | P | |<br>❌ CORTADA — os 50 primeiros entram pela mão do Marco, por telefone. Tour para quem foi cadastrado no WhatsApp
| 31 | ~~Central de ajuda e busca~~ | P | |<br>❌ CORTADA — busca numa central sem artigos. A ajuda real é a 32, falar com o suporte
| 32 | Falar com o suporte | E | |

🔵 **Regra de escrita das dicas:** explicar o que o número significa **para a decisão**, não o que ele é tecnicamente. Errado: *"CPM é custo por mil impressões."* Certo: *"quanto você paga para alcançar mil pessoas — serve para comparar criadores de tamanhos diferentes."*

### 1.5 Estados obrigatórios de toda tela 🔵

Nenhuma função está pronta sem estes seis. É a diferença entre maquete e produto:

**vazio** (ainda não há nada) · **carregando** · **erro** · **sem internet** · **sucesso** · **sem permissão**

---

## 2. CREATOR APP — o criador

### 2.1 Início e inteligência

| # | Função | Prio | Observação |
|---|---|---|---|
| 33 | **Resumo do dia** | E | 🔵 "3 entregas esta semana · 1 vence amanhã · 1 esperando o produto chegar" |
| 34 | ~~**O que fazer agora**~~ | E | 🔵 Uma ação óbvia por vez, em ordem de urgência |<br>🔗 FUNDE na 33 — a home do criador é a lista de pendências
| 35 | ~~Saldo em destaque~~ | E | |<br>🔗 ENTRA NA 68 — é o topo da carteira
| 36 | ~~Oportunidades sugeridas~~ | P | |<br>❌ CORTADA — com 10 marcas, "oportunidades sugeridas" é a lista de pedidos abertos, que já existe
| 37 | ~~**Resumo em linguagem simples de cada contrato**~~ | P | 🔵 "Você está no marco 2 de 3. Falta enviar o vídeo até 12/10" |<br>❌ CORTADA — é o que a tela do contrato já mostra
| 38 | ~~Alerta de risco de atraso~~ | P | 🔵 Cruza prazos com a agenda e avisa antes de estourar |<br>❌ CORTADA — motor de inferência cruzando agenda com prazos é onde v1 morre. O lembrete (22/23) já avisa

⚠️ **Sobre inteligência artificial, com honestidade:** no lançamento a IA **não tem com o que aprender** — não existe histórico. Então o v1 entrega inteligência **determinística**: regras claras que somam prazos, contam marcos e ordenam por urgência. Isso resolve quase todo o valor que o Marco descreveu, sem depender de dado que ainda não existe. IA de linguagem entra quando houver volume, e mesmo aí **nunca** libera dinheiro, suspende conta ou decide disputa — isso é regra determinística e humano.

### 2.2 Calendário e agenda ⚠️ módulo que faltava inteiro

Pedido direto do Marco, e ele está certo: **lista de contratos não é gestão de agenda.**

| # | Função | Prio | Observação |
|---|---|---|---|
| 39 | **Calendário do criador** | E | Mês, semana e lista |
| 40 | **Clicar num dia abre o que está em jogo** | E | Contratos daquele dia, em que marco, o que falta |
| 41 | Marcos com data aparecem automaticamente | E | Entrega, publicação, evento presencial |
| 42 | ~~**Bloquear data / marcar indisponibilidade**~~ | E | 🔵 Férias, viagem, agenda cheia |<br>🔵 ADIADA com o presencial
| 43 | ~~**Data bloqueada some da vitrine**~~ | E | 🔵 Impede a marca de contratar para um dia impossível |<br>🔵 ADIADA com o presencial
| 44 | ~~Vista de carga de trabalho~~ | P | 🔵 Quantas entregas por semana — evita o criador aceitar 15 para a mesma semana |<br>❌ CORTADA — o calendário em visão de semana (39) já mostra isso
| 45 | ~~Exportar para Google Calendar / Apple~~ | P | |<br>❌ CORTADA — segunda superfície de sincronização para manter
| 46 | ~~Lembrete configurável antes do prazo~~ | P | |<br>❌ CORTADA — "configurável" é a denúncia: ninguém mexe. Lembrete fixo em 48 h e 24 h dentro da 22/23
| 47 | ~~Sugerir data realista ao aceitar proposta~~ | P | 🔵 Cruza com o que já está agendado |<br>❌ CORTADA — mesma razão da 38

### 2.3 Perfil e vitrine

| # | Função | Prio | Observação |
|---|---|---|---|
| 48 | Montar perfil (foto, bio, categorias) | E | |
| 49 | ~~Avatar padrão quando não há foto~~ | E | Usa o oficial da marca (`docs/marca/avatares`) |<br>🔗 SAI DA CONTAGEM — é valor padrão, não função
| 50 | Modalidade: remoto / presencial / híbrido | E | |
| 51 | ~~Região de atendimento presencial~~ | E | |<br>🔵 ADIADA com o presencial
| 52 | **Montar item de vitrine** | E | Nome, preço, prazo, revisões, direitos |
| 53 | Pausar / arquivar item | E | |
| 54 | Portfólio de trabalhos anteriores | P | |
| 55 | ~~Prévia de "como a marca me vê"~~ | P | 🔵 |<br>❌ CORTADA — o criador abre o próprio perfil público, é o mesmo endereço
| 56 | ~~Selo de verificado~~ | E | Usa o oficial da marca, em degradê |<br>❌ CORTADA do v1 — se todos que recebem dinheiro passam pela verificação (7), o selo não distingue ninguém
| 57 | ~~**Valor líquido visível antes de ofertar**~~ | E | 🔵 O criador vê quanto recebe de fato, já com a comissão descontada |<br>🔗 VIRA REGRA do componente de preço (SPEC §4.5)

### 2.4 Propostas e trabalho

| # | Função | Prio | Observação |
|---|---|---|---|
| 58 | Propostas recebidas | E | |
| 59 | Aceitar / recusar / pedir ajuste | E | Janela de 48 h |
| 60 | Candidatar-se a pedido aberto | E | Criador define preço e prazo |
| 61 | ~~Enviar proposta por conta própria~~ | P | |<br>❌ CORTADA — duplica a candidatura (60) e abre canal de abordagem não solicitada
| 62 | Meus contratos, por estado | E | |
| 63 | **Enviar a entrega** — ⚠️ **arquivo de revisão em MP4/H.264 obrigatório**; o original é opcional e liberado só após aprovar. Entrega com várias peças permite **aprovar peça a peça** | E | ⚠️ Corrigido em 08/09/2026: um arquivo de câmera (.mov, ProRes, 900 MB) **não toca no navegador** — a "prévia em streaming" que substituiu a marca d'água exigia a mesma transcodificação que o corte disse ser cara. MP4 é o que o criador exporta para o Instagram de qualquer jeito. E sem aprovação peça a peça, o criador refaz três Stories por causa de um |
| 64 | Ver o pedido de ajuste referenciado ao briefing | E | |
| 65 | **Confirmar identificação publicitária** | E | ⚠️ Lembrete na entrega: marcou como parceria paga? Vira prova documental |
| 66 | Chat, liberado só após pagamento | E | |
| 67 | Abrir disputa | E | |

### 2.5 Dinheiro

| # | Função | Prio | Observação |
|---|---|---|---|
| 68 | Carteira: protegido / aguardando prazo / disponível | E | Os três estados nunca se confundem |
| 69 | Extrato com origem de cada valor | E | |
| 70 | Sacar para conta bancária | E | |
| 71 | Cadastro fiscal com escada CPF → MEI | E | ⚠️ Precisa de contador |
| 72 | ~~Guia embutido de como abrir MEI~~ | P | Reduz o atrito que trava o criador iniciante |<br>❌ CORTADA — 🔴 empurrava o criador para irregularidade fiscal. Ver SPEC §4.7
| 73 | ~~Antecipação de recebíveis~~ | P | Segunda fonte de receita |<br>❌ CORTADA — 🔴 contradizia frontalmente a regra de ouro da SPEC §4.2. Antecipação ao criador é produto de crédito, com capital e enquadramento próprios
| 74 | ~~Previsão de recebimento dos próximos 30 dias~~ | P | 🔵 Cruza contratos em andamento com prazos de liberação |<br>❌ CORTADA — a carteira (68) já tem três estados com data. É a mesma tabela ordenada de outro jeito

---

## 3. BRAND WEB — a marca

### 3.1 Painel

| # | Função | Prio | Observação |
|---|---|---|---|
| 75 | **O que precisa da minha decisão hoje** | E | 🔵 Entregas para aprovar, propostas para responder, pagamentos pendentes |
| 76 | Campanhas em andamento | E | |
| 77 | ~~Orçamento comprometido × gasto~~ | P | |<br>❌ CORTADA — marca com dois contratos não gerencia orçamento
| 78 | ~~Calendário de publicações contratadas~~ | P | 🔵 Quando cada conteúdo vai ao ar |<br>❌ CORTADA — mesma razão
| 79 | Alerta de prazo de aprovação vencendo | E | ⚠️ Se ela não aprovar, aprova sozinho em 7 dias — ela precisa saber |

### 3.2 Descobrir e contratar

| # | Função | Prio | Observação |
|---|---|---|---|
| 80 | Busca de criadores | E | |
| 81 | Filtros: categoria, orçamento, região, modalidade, público | E | |
| 82 | ~~**Ordenação explicada**~~ | E | 🔵 Nunca ranking oculto — a marca vê por que aquela ordem |<br>🔗 SAI DA CONTAGEM — é regra de escrita
| 83 | ~~Cota de visibilidade para criador novo~~ | E | Sem isso o marketplace nunca gira |<br>❌ CORTADA — com 50 criadores todos são novos e cabem em duas rolagens. No v1 aparece todo mundo
| 84 | Perfil completo do criador | E | |
| 85 | ~~Favoritos / listas~~ | P | |<br>❌ CORTADA — 50 criadores cabem numa tela
| 86 | **Contratar da vitrine** (formulário curto) | E | |
| 87 | **Proposta direta** (formulário completo) | E | |
| 88 | **Publicar pedido aberto** | E | |
| 89 | Ver candidaturas | E | |
| 90 | ~~**Comparador lado a lado**~~ | P | A tela que mais justifica a comissão |<br>🔵 ADIADA — um pedido aberto no piloto recebe três candidaturas; a lista É a comparação
| 91 | ~~Convidar criador para um pedido~~ | P | |<br>❌ CORTADA — a proposta direta (87) já faz isso, e o chat só abre depois do pagamento
| 92 | Contratar vários criadores no mesmo pedido | E | |

### 3.3 Acompanhar e aprovar

| # | Função | Prio | Observação |
|---|---|---|---|
| 93 | Contrato com marcos e estados | E | |
| 94 | Aprovar entrega | E | |
| 95 | **Pedir ajuste referenciado ao briefing** | E | Reduz disputa |
| 96 | ~~Ver quantas revisões restam~~ | E | |<br>🔗 ENTRA NA 95 — é um contador dentro dela
| 97 | ~~Visão de campanha (vários contratos)~~ | P | |<br>❌ CORTADA — com 20 contratos em 10 marcas, o painel de campanha tem duas linhas
| 98 | ~~Baixar contrato em PDF~~ | E | |<br>🔗 FUNDE na 167 — duas linhas, um botão
| 99 | Cancelar dentro da janela | E | |
| 100 | Abrir disputa | E | |

### 3.4 Pagamento

| # | Função | Prio | Observação |
|---|---|---|---|
| 101 | Pix, boleto e cartão | E | Cartão só com CNPJ verificado |
| 102 | ~~**Valor final tudo incluso**~~ | E | Sem taxa somada depois |<br>🔗 VIRA REGRA do componente de preço (SPEC §4.5)
| 103 | ~~Prazo de disponibilização visível por meio~~ | E | |<br>🔗 VIRA REGRA do componente de preço (SPEC §4.5)
| 104 | ~~Financiar marco a marco~~ | E | |<br>🔵 ADIADA — v1 = um marco por contrato, com a máquina modelada para N. Com ticket de R$ 1.200 quase todo contrato tem um marco só. A proteção do escrow não muda
| 105 | Notas fiscais e recibos | E | ⚠️ Contador |
| 106 | ~~Vários métodos salvos~~ | P | |<br>❌ CORTADA — uma marca faz duas compras no piloto

---

## 3.5 Contrato recorrente ⚠️ módulo reincorporado

⚠️ **Eu tinha tirado a recorrência do escopo, e o motivo estava errado.**

Tirei porque a ideia tinha aparecido num documento cuja origem o Marco não reconhecia — ou seja, descartei pela **fonte**, não pelo **mérito**. Isso contraria a regra do `CLAUDE.md` §2.7: a fala do Marco é matéria-prima e o que importa é verificar, não a procedência. Ele devolveu com um caso de uso concreto que fecha a discussão:

> *"uma marca que contratar creator para provador fixo mensal ou outro período acordado pode ter uma recorrência. Do que terem que ficar contratando toda vez a mesma coisa."*

Está certo. E não é conveniência: **é o modelo de contratação mais valioso da plataforma.** Embaixador de marca, provador mensal, pacote fixo de conteúdo. Para o criador vira renda previsível; para a marca vira relação em vez de transação; para a INFLUENTZ vira receita recorrente — que vale muito mais que comissão avulsa.

### 3.5.1 Como funciona 🟢

| # | Função | Prio | Observação |
|---|---|---|---|
| 129 | ~~**Criar contrato recorrente**~~ | P | Mensal, quinzenal, trimestral ou período combinado |<br>🔵 ADIADA — recorrência é Fatia 3, como o próprio §3.5.5 já dizia. Sai da contagem do v1
| 130 | ~~Definir o que se repete a cada ciclo~~ | P | Ex.: 4 Stories + 1 Reels por mês |<br>🔵 ADIADA — recorrência é Fatia 3, como o próprio §3.5.5 já dizia. Sai da contagem do v1
| 131 | ~~**Cada ciclo é um contrato próprio por dentro**~~ | P | Financiamento, entrega, aprovação e repasse independentes |<br>🔵 ADIADA — recorrência é Fatia 3, como o próprio §3.5.5 já dizia. Sai da contagem do v1
| 132 | ~~Renovação automática~~ | P | Com aviso antes de cada ciclo |<br>🔵 ADIADA — recorrência é Fatia 3, como o próprio §3.5.5 já dizia. Sai da contagem do v1
| 133 | ~~**Encerrar a recorrência** (vale a partir do próximo ciclo)~~ | P | Diferente de cancelar o ciclo atual |<br>🔵 ADIADA — recorrência é Fatia 3, como o próprio §3.5.5 já dizia. Sai da contagem do v1
| 134 | ~~**Cancelar só o ciclo atual**~~ | P | Mês em que a marca não vai usar |<br>🔵 ADIADA — recorrência é Fatia 3, como o próprio §3.5.5 já dizia. Sai da contagem do v1
| 135 | ~~**Pausar**~~ | P | Férias do criador, verba parada da marca |<br>🔵 ADIADA — recorrência é Fatia 3, como o próprio §3.5.5 já dizia. Sai da contagem do v1
| 136 | ~~Reajustar valor entre ciclos~~ | P | Precisa de aceite dos dois lados |<br>🔵 ADIADA — recorrência é Fatia 3, como o próprio §3.5.5 já dizia. Sai da contagem do v1
| 137 | ~~Prazo de aviso prévio para encerrar~~ | P | Protege quem reservou agenda |<br>🔵 ADIADA — recorrência é Fatia 3, como o próprio §3.5.5 já dizia. Sai da contagem do v1
| 138 | ~~Ver o histórico de todos os ciclos~~ | P | |<br>🔵 ADIADA — recorrência é Fatia 3, como o próprio §3.5.5 já dizia. Sai da contagem do v1
| 139 | ~~Calendário mostra os ciclos futuros~~ | P | Liga com o módulo de agenda (§2.2) |<br>🔵 ADIADA — recorrência é Fatia 3, como o próprio §3.5.5 já dizia. Sai da contagem do v1

### 3.5.2 As três regras que fazem a recorrência não quebrar ⚠️

**1. Um ciclo com problema não contamina os outros.** Se a entrega de março virar disputa, os ciclos de janeiro e fevereiro continuam concluídos e pagos, e o de abril segue. Cada ciclo é uma caixa fechada. Sem isso, uma discussão em um mês trava a relação inteira.

**2. Encerrar a recorrência ≠ cancelar o ciclo atual.** São dois botões diferentes, com consequências diferentes. Confundir os dois é o erro clássico de assinatura — a pessoa clica em "cancelar" achando que está pulando um mês e perde o contrato inteiro.

**3. O criador precisa poder sair.** Recorrência não pode virar armadilha. Ele encerra com o mesmo aviso prévio que a marca tem. ⚠️ O prazo exato precisa de advogado.

### 3.5.3 🔵 A recorrência já nasce com a comissão menor

A SPEC §4.4 dá 8% a partir da terceira contratação entre a mesma marca e o mesmo criador. **Contrato recorrente é exatamente isso, por definição** — então ele entra direto na faixa de 8%, sem esperar três ciclos.

*Por quê:* alinha o incentivo. A plataforma ganha menos por ciclo e muito mais no total, porque troca uma venda por uma relação. É o que faz o criador e a marca preferirem fechar recorrente dentro da plataforma em vez de combinarem por fora.

### 3.5.4 🔵 Como se cobra recorrência no Brasil — e por que isso é uma vantagem agora

Contrato que se repete precisa de cobrança que se repete. Levantamento dos três meios:

| Meio | Serve para recorrência? | Observação |
|---|---|---|
| **Pix Automático** | ✅ **Sim, e é a melhor opção** | O cliente autoriza **uma vez** no app do banco; as cobranças seguintes são debitadas sozinhas |
| Cartão de crédito | ✅ Sim | Cobrança recorrente com cartão salvo. Mas continua com o D+30 e o risco de contestação |
| Boleto | ⚠️ Ruim | Cada ciclo é um boleto novo que alguém precisa lembrar de pagar. Taxa de inadimplência alta |

⚠️ **O Pix Automático é uma janela aberta agora.** É funcionalidade do Banco Central para pagamento recorrente, que entrou em vigor em **14 de maio de 2026** — ou seja, é novidade no mercado. Ele dispensa convênio bancário complexo, o que antes travava empresa pequena, e uma transação Pix custa em média **até 14 vezes menos** que processar cartão. O cliente ainda define limite máximo por cobrança e pode cancelar a autorização quando quiser.

**O que isso significa para a INFLUENTZ:** dá para lançar recorrência com custo de processamento muito menor que o de qualquer concorrente que só use cartão — e sem o D+30. ⚠️ Confirmar com o Pagar.me se o Pix Automático já está disponível na API deles antes de prometer na tela.

*Fontes:* [PagBrasil — Pix Automático](https://www.pagbrasil.com/pt-br/metodos-de-pagamento/pix-automatico/) · [Banco Central — cronograma 2026](https://www.socialhub.pro/blog/pix-automatico-2026-decreto-bacen-atualizacao/)

### 3.5.5 Quando isso entra 🟢

**Não no v1.** Não porque seja pouco importante — é o contrário — mas porque recorrência é ciclo simples repetido. Se o ciclo simples não funcionar com dinheiro de verdade, recorrência multiplica o problema por doze.

**Entra na Fatia 3**, logo depois do ciclo simples estar provado. E a máquina de estados já nasce preparada: um contrato avulso é uma recorrência de um ciclo só.

---

## 4. AGENCY WEB — a agência

A agência **gerencia, mas nunca toca no dinheiro** — se recebesse e repassasse valores de terceiros, viraria instituição de pagamento perante o Banco Central.

| # | Função | Prio | Observação |
|---|---|---|---|
| 107 | ~~Espaço da agência~~ | E | |<br>🔵 ADIADA — **agência sai do v1.** Com 50 criadores recrutados pessoalmente, o valor da agência (gerir volume) ainda não existe. O argumento de multi-criador sobrevive sem ela, porque a marca faz igual
| 108 | ~~Convidar marca representada (aceite dos dois lados)~~ | E | |<br>🔵 ADIADA — **agência sai do v1.** Com 50 criadores recrutados pessoalmente, o valor da agência (gerir volume) ainda não existe. O argumento de multi-criador sobrevive sem ela, porque a marca faz igual
| 109 | ~~Convidar criador representado (aceite dos dois lados)~~ | E | |<br>🔵 ADIADA — **agência sai do v1.** Com 50 criadores recrutados pessoalmente, o valor da agência (gerir volume) ainda não existe. O argumento de multi-criador sobrevive sem ela, porque a marca faz igual
| 110 | ~~Agir em nome de, com autoria registrada~~ | E | Toda ação mostra quem realmente fez |<br>🔵 ADIADA — **agência sai do v1.** Com 50 criadores recrutados pessoalmente, o valor da agência (gerir volume) ainda não existe. O argumento de multi-criador sobrevive sem ela, porque a marca faz igual
| 111 | ~~Ver campanhas de todas as marcas num lugar~~ | E | |<br>🔵 ADIADA — **agência sai do v1.** Com 50 criadores recrutados pessoalmente, o valor da agência (gerir volume) ainda não existe. O argumento de multi-criador sobrevive sem ela, porque a marca faz igual
| 112 | ~~Calendário consolidado~~ | P | 🔵 Todos os criadores, todas as datas |<br>❌ CORTADA — a agência tem volume perto de zero no lançamento
| 113 | ~~**Alerta de autonegociação**~~ | E | Mesmo CPF/CNPJ nos dois lados → revisão manual |<br>🔵 ADIADA — **agência sai do v1.** Com 50 criadores recrutados pessoalmente, o valor da agência (gerir volume) ainda não existe. O argumento de multi-criador sobrevive sem ela, porque a marca faz igual
| 114 | Permissões por membro da equipe | F | |
| 115 | Faturamento consolidado | F | |
| 116 | ~~Relatório por marca~~ | P | |<br>❌ CORTADA — mesma razão

---

## 5. ADMIN WEB — equipe INFLUENTZ

| # | Função | Prio | Observação |
|---|---|---|---|
| 117 | ~~Papéis: Super Admin, Financeiro, Suporte, Trust & Safety~~ | E | |<br>❌ CORTADA a matriz de papéis — a equipe tem uma pessoa. v1 = um papel; o campo no banco fica modelado para crescer
| 118 | ~~Fila de disputas por risco~~ | E | |<br>⚠️ REDUZIDA a lista simples — some o "por risco": priorizar uma fila de 1 item é enfeite
| 119 | Mediar disputa com evidências das duas partes | E | |
| 120 | Liberar, reter ou estornar valor | E | ⚠️ Sempre com motivo, autor e registro |
| 121 | ~~Fila de verificação manual~~ | E | Autonegociação, valor alto, conta nova |<br>❌ CORTADA — vira item da caixa de entrada única
| 122 | Buscar usuário e ver histórico completo | E | |
| 123 | Suspender / banir, com motivo | E | |
| 124 | ~~**Configurar comissão e prazos**~~ | E | Nunca fixo no código |<br>❌ CORTADA a tela — "não fixo no código" ≠ "tela de configuração". Tabela de parâmetros no Supabase cumpre a regra inteira para um operador
| 125 | ~~Painel financeiro e conciliação~~ | E | |<br>❌ CORTADA do v1 — com 20 transações/mês a conciliação é o painel do Pagar.me mais um CSV
| 126 | ~~**Painel de saúde das APIs sociais**~~ | P | 🔵 |<br>❌ CORTADA — é a 141 e a 19 com um terceiro nome
| 127 | Registro de auditoria imutável | E | Toda ação sensível fica gravada |
| 128 | ~~Moderação de conteúdo e denúncias~~ | E | |<br>⚠️ REDUZIDA ao botão de denunciar + uma linha na caixa de entrada. O "sistema de moderação" é uma pessoa olhando

---

## 5.5 Funções acrescentadas pela auditoria 🔴

Auditoria feita pelo especialista de produto em 08/09/2026, com contexto limpo. Encontrou **12 lacunas, 8 delas capazes de travar o lançamento**. Todas conferidas e todas procedentes. As funções que faltavam:

### Cadastro e identidade

| # | Função | Prio | Resolve |
|---|---|---|---|
| 140 | ~~**Coorte-piloto de conexão** — convite de tester (Instagram) e contas-alvo de sandbox (TikTok), com vagas contadas~~ | E | O criador de Instagram entrando no dia 1 **com métrica de API real**, sem esperar o App Review ❌ substitui o envio manual |<br>❌ CORTADA — convite de tester/sandbox se configura no console de cada rede, à mão. Nada a construir
| 141 | ~~**Painel de saúde das conexões** no Admin — expiradas, revogadas, status de cada App Review, vagas restantes na coorte~~ | E | ❌ Substitui a fila de aprovação manual, que deixou de existir |<br>❌ CORTADA — o status do App Review se lê no painel da Meta. Espelhar isso aqui é reimplementar o dashboard de outra empresa
| 142 | **Selo "conectado por API" com data da última atualização**, em toda métrica | E | Não existe mais métrica sem selo, porque não existe mais métrica sem API ❌ substitui o rótulo "declarada" |
| 142.1 | ~~**Conversão para conta profissional** — tela com passo a passo e botão "já converti, tentar de novo"~~ | E | Conta pessoal não tem API; isso é passo de onboarding, não recusa |<br>🔗 ENTRA NA 11 — é o estado de erro dela
| 142.2 | **Renovação automática de token e aviso de reconexão** | E | Token do Instagram morre com 60 dias sem uso; métrica congela com data, nunca vira zero |
| 143 | **Cadastrar e trocar conta bancária** | E | Não existia. Só havia "sacar" |
| 144 | **Ver motivo da recusa do provedor e reenviar documento** | E | O beco sem saída de quem tem dinheiro aprovado que não sai |

### Dinheiro

| # | Função | Prio | Resolve |
|---|---|---|---|
| 145 | **Dados de reembolso da marca no checkout** de Pix e boleto | E | Não havia por onde devolver dinheiro fora do cartão |
| 146 | ~~**Acompanhar reembolso** nas duas pontas~~ | E | |<br>🔗 ENTRA NA 93 — é uma linha de status na tela do contrato
| 147 | ~~**Fila de reembolso com falha** no Admin~~ | E | Reembolso que não completa não pode sumir em silêncio |<br>❌ CORTADA — vira item da caixa de entrada única
| 148 | ~~**Dossiê de defesa automático** — PDF único de até 1,9 MB com contrato congelado, aceite datado, comprovante de financiamento anterior ao início, entrega e aprovação~~ | E | ❌ Substitui a "reserva de contestação", eliminada. **Prazo de defesa de 10 dias, fatal** — vira tarefa com contagem regressiva no Trust & Safety |<br>⚠️ REDUZIDA — o gerador de PDF morre (um chargeback a cada ~20 meses). Ficam **os dados** (já no registro 127) e **o alarme de 10 dias**, que é fatal
| 148.1 | ~~**Fundo de contestação** no painel administrativo — 5% da comissão, saldo e histórico de perdas absorvidas~~ | E | A plataforma retém o dinheiro **dela**, não o do criador. Invisível para o criador |<br>❌ CORTADA — o fundo acumula R$ 90/mês no lançamento. É uma conta bancária e uma linha de planilha, não uma tela
| 148.2 | **Teto de exposição por cobrança no cartão**, com escadinha por histórico da marca | E | O risco não é a média, é o caso isolado: um chargeback de R$ 1.200 come dois terços da comissão de um mês de lançamento |
| 149 | ~~**Saldo negativo** com saque e novos contratos bloqueados~~ | E | Idem |<br>❌ CORTADA — a camada 6 da SPEC §4.3 diz que chargeback perdido não vira dívida do criador, e a §15 pergunta ao advogado se o clawback é válido. Máquina de estados para uma cobrança de legalidade aberta
| 150 | ~~**Anexar nota fiscal do criador** antes da liberação do repasse~~ | E | A marca com CNPJ precisa da nota para lançar a despesa |<br>⚠️ CORRIGIDA — 🔴 o portão bloqueante morre: travar o repasse até a NF quebraria a decisão travada *"o criador nunca espera mais que o prazo do meio"*. Fica o anexo **não bloqueante**
| 151 | **Marca baixa a nota do criador** dentro do contrato | E | Idem |

### Entrega

| # | Função | Prio | Resolve |
|---|---|---|---|
| 152 | ~~**Envio retomável**, com tamanho e formato declarados e estado de falha~~ | E | Reels de 900 MB no 4G que cai aos 80% |<br>🔗 SAI DA CONTAGEM — é decisão técnica. O Supabase Storage já implementa TUS nativamente
| 153 | ~~**Prévia com marca d'água antes da aprovação**~~ | E | ⚠️ Ver abaixo |<br>❌ CORTADA — marca d'água em vídeo é pipeline de transcodificação. **A mesma proteção por 5% do custo:** prévia em streaming, sem botão de baixar, por link assinado de vida curta; o original só é liberado depois da aprovação (154)
| 154 | **Original liberado só após aprovar** (ou vencer a aprovação automática) | E | Idem |
| 155 | ~~Prazo de guarda do arquivo após o contrato~~ | P | |<br>🔵 VIRA CLÁUSULA de Termos — com 20 contratos, custo de armazenamento zero
| 156 | **Lançar código de rastreio** (marca) | E | Envio de produto físico |
| 157 | **Confirmar recebimento do produto** — ⚠️ **duas opções, não um botão:** *"recebi"* / *"não recebi ou veio com problema"*, com observação. A segunda abre item na caixa de entrada | E | O relógio do criador só começa aqui. ❌ **A 158 foi cortada por engano** junto com o presencial — extravio é dos Correios, não de evento. Sem esta opção, o criador que recebe a caixa quebrada só pode esperar o prazo estourar segurando o produto |
| 158 | ~~**Declarar extravio** (função separada)~~ | E | ✅ **Absorvida pela 157** — vira a segunda opção dela, não uma tela própria
| 159 | ~~**Check-in presencial** com data, hora e local~~ | E | ⚠️ Ver abaixo |<br>🔵 ADIADA com o presencial
| 160 | ~~**Confirmação de comparecimento pela marca**, com prazo~~ | E | Idem |<br>🔵 ADIADA com o presencial

⚠️ **Por que a prévia com marca d'água (153) é essencial:** o dinheiro fica retido, mas **o conteúdo não**. Sem isso, nada impede a marca de baixar o vídeo final, publicar e nunca aprovar. O escrow protege uma ponta só. Marca d'água antes, original depois da aprovação, protege as duas.

⚠️ **Por que o check-in (159) é essencial:** a regra de cancelamento presencial dá 100% ou 0% conforme quem faltou — mas sem registro, isso vira palavra contra palavra decidindo dinheiro. Check-in com carimbo de hora e local é a prova que faltava.

### Disputa

| # | Função | Prio | Resolve |
|---|---|---|---|
| 161 | **Enviar evidência** | E | A disputa tinha estados e nenhuma função |
| 162 | **Ver o que a outra parte alegou** | E | |
| 163 | **Acompanhar o andamento e o prazo** | E | |
| 164 | ~~**Aceitar acordo** antes da decisão~~ | P | |<br>❌ CORTADA — acordo é o mediador liberando valor parcial, que é a 120. Com uma disputa por mês, o mediador faz na mão

### Contrato

| # | Função | Prio | Resolve |
|---|---|---|---|
| 165 | ~~**Aditivo de escopo** com aceite dos dois lados~~ | P | ⚠️ Ver abaixo |<br>🔵 ADIADA — aditivo é reprecificar, reassinar e refinanciar contrato vivo. No v1 ele existe com outro nome: a marca compra outro item da vitrine
| 166 | **Termos de Uso versionados**, com registro de qual versão cada um aceitou, quando e de onde | E | A aprovação automática por silêncio só é oponível se estiver nos termos aceitos |
| 167 | **Contrato em PDF para as duas pontas e para a agência** | E | Só a marca tinha |

⚠️ **Por que o aditivo (165) importa comercialmente:** hoje, se a marca quer antecipar a publicação ou acrescentar um Story pagando mais, só existem três saídas — pedir ajuste (que consome revisão e não muda preço), cancelar, ou **combinar por fora**. A terceira é exatamente o que a SPEC §13.2 tenta impedir. Sem aditivo, a plataforma empurra volume para fora dela mesma.

### Operação de lançamento — ❌ **cortada inteira em 08/09/2026**

**As funções 168, 169, 169.1, 169.2 e 169.3 foram eliminadas.** Não substituídas: **eliminadas.**

Pergunta do Marco que derrubou o bloco inteiro:

> *"pra que esse trem de convite pros usuarios? So mandar baixa ou acessar via web e ele mesmo cadastrar, pra que complicar isso"*

**Ele está certo, e a resposta honesta é que esse bloco nunca deveria ter nascido.** A SPEC §14.1 diz que o Marco chama pessoalmente os 50 primeiros criadores. Disso eu concluí, sozinho, que a plataforma precisava de "ferramenta de convite" — link nominal, rascunho de perfil, funil, descarte automático. **Cinco funções para resolver um problema que o link da App Store e o endereço do site já resolvem.**

O criador convidado por WhatsApp baixa o app, ou abre o site, e se cadastra — igual a todo mundo. É isso.

⚠️ **O que eu inventei e o que o Marco pediu:**

| | |
|---|---|
| Ele pediu | Nada. §14.1 descreve como ele vai conseguir os primeiros usuários, não uma funcionalidade |
| Eu entreguei | Cinco funções, uma auditoria jurídica e três revisões |

📌 **A atribuição — saber que aquele criador veio do Marco — não justifica funcionalidade nenhuma no v1.** Se um dia importar, é **um campo opcional no cadastro** ("como você conheceu a INFLUENTZ?"), não um subsistema.

🔴 **A lição, registrada porque ela vale para o produto inteiro:** antes de qualquer função nova, a pergunta obrigatória é **"o que acontece se ela não existir?"**. Se a resposta for "quase nada", ela não existe. Ver `CLAUDE.md` §2.2.

---

## 5.6 🔴 As funções que faltavam — encontradas pelo `cortador` em 08/09/2026

Não são acréscimos de auditor procurando o que falta. São **buracos no caminho principal** e **obrigação regulatória vencida**.

### Avaliação — o passo 9 do fluxo, que não tinha número

| # | Função | Prio | Resolve |
|---|---|---|---|
| 170 | **Avaliar a outra ponta** ao fim do contrato — nota e comentário, criador→marca e marca→criador | E | 🔴 O último passo do fluxo principal da SPEC §5 **não existia na matriz** |
| 171 | **Publicação simultânea às cegas** — nenhum lado vê a nota do outro antes de enviar a sua, e ambas aparecem juntas no prazo | E | Sem isso, quem avalia primeiro é refém de retaliação. É como Airbnb e Upwork fazem |
| 172 | **Nota e histórico no perfil**, com número de contratos concluídos | E | A reputação é o que substitui a confiança que um marketplace novo não tem |

### Perfil da marca — o criador não sabia quem estava contratando ele

| # | Função | Prio | Resolve |
|---|---|---|---|
| 173 | **Perfil público da marca** — nome, logo, segmento, site, histórico na plataforma e nota recebida | E | 🔴 O criador recebia uma proposta **sem nenhuma tela para saber quem é a marca.** Decidir sem saber com quem se está fechando é o oposto de um marketplace confiável |

### Agenda de recebíveis — Resolução BCB 264/349, prazo vencido em 01/04/2024

Obrigação **do marketplace**, não do Pagar.me. Ver SPEC §4.10. Vale para criador **e** marca, porque os dois são recebedores no split.

| # | Função | Prio | Resolve |
|---|---|---|---|
| 174 | **Agenda de recebíveis por UR** — valor bruto, deduções discriminadas e recebível constituído | E | A carteira (68) e o extrato (69) **não são isso.** Sem a agenda, a plataforma opera fora de norma em vigor |
| 175 | **Contratos que gravam a agenda** — contraparte, URs alcançadas, natureza e valor do efeito | E | Idem |
| 176 | **Contestar efeito de contrato sobre a agenda**, encaminhado ao sistema de registro | E | Idem |

### Antifraude que não existia

| # | Função | Prio | Resolve |
|---|---|---|---|
| 177 | **Consulta a listas restritivas** (PEP, CEIS, CNEP, sanções) no cadastro e antes de contrato de valor alto, com resultado e data gravados na trilha de auditoria | E | Não existia nenhum controle desse tipo. Barato, e é o mesmo que as regras antifraude já pedem |

### Campos de cadastro que faltavam, e sem os quais o criador não recebe

Não viram função nova — **corrigem a 7 e a 143** (ver SPEC §4.8):

- **Pessoa física:** renda mensal e atividade profissional
- **Pessoa jurídica:** faturamento médio anual e dados dos sócios
- ⚠️ **O link de validação de identidade vale 20 minutos.** Tem que ser gerado dentro do app, na hora, com contagem regressiva visível e botão de gerar novo — nunca mandado por e-mail para a pessoa clicar quando puder

---

## 5.7 🔴 As quebras do caminho — caminhada end-to-end de 08/09/2026

> **Revisado por:** especialista `produto`. **Não é lista do que falta — é onde o caminho quebra.** Placar: **+4 funções novas, −7 mortas na mesma entrega. Saldo: −3.**

### O que a marca compra é uma publicação, não um arquivo

| # | Função | Prio | Resolve |
|---|---|---|---|
| 178 | **Prova de publicação** — o criador cola o permalink; a plataforma **confere pela API já conectada** que o post existe, é da conta certa, tem a data, e traz alcance na mesma chamada. **O repasse é liberado aqui, não na aprovação do arquivo** | E | 🔴 A maior lacuna do produto. O dinheiro saía contra um arquivo aprovado — o criador podia receber sem publicar, publicar e apagar, ou publicar sem marcar parceria paga. **Na disputa a plataforma não tinha prova de nada.** Ver MAQUINA §8.0.1 |
| 178.1 | **Conferência diária de permanência** — o post sumiu antes do prazo? Entra na caixa de entrada e conta no histórico do criador | E | O campo *permanência mínima* (SPEC §8.2, padrão 90 dias) não existia |

⚠️ **A função 65** (confirmar identificação publicitária) era **caixa de seleção de autodeclaração** — exatamente o que a SPEC §9 proíbe para métrica, e que tinha sido aceito como prova. Com a 178, a marcação de parceria paga passa a ser **conferida na mesma leitura da API**.

### A caixa de entrada do operador — seis coisas apontavam para uma tela que não existia

| # | Função | Prio | Resolve |
|---|---|---|---|
| 179 | **Caixa de entrada do operador** — uma lista, com origem, prazo e link para o objeto. É a única tela do Admin que abre todo dia | E | 🔴 O corte dizia *"vira item da caixa de entrada única"* três vezes, e ela **não tinha número, tela nem dono**. Recebem nela: verificação manual, reembolso com falha, denúncia, **o prazo fatal de 10 dias da contestação**, revisão de cobrança alta, alerta de autonegociação, resultado de lista restritiva, extravio, permanência quebrada e chamado de suporte |

⚠️ **Ela também resolve o beco do `aguardando_revisao_manual`:** as ações *aprovar* / *recusar com motivo* vivem aqui, e nasce o estado `recusado_na_revisao`. Antes, o contrato entrava nesse estado e **ninguém tinha como empurrá-lo**.

### Quando o aviso do provedor se perde

| # | Função | Prio | Resolve |
|---|---|---|---|
| 180 | **Reconciliação de pagamento** — toda cobrança em `aguardando_pagamento` é **reconsultada ativamente** no provedor, e o Admin tem o botão *"reconsultar e reconciliar"* | E | 🔴 A máquina do dinheiro obedece ao provedor "via webhook", e **webhook perdido é rotina**. A marca pagou o Pix, o contrato ficou parado, o criador não pôde começar e **ninguém tinha ação possível.** ✅ Não fere a invariante da SPEC §4.9: **reler o estado do provedor não é mover dinheiro** |

### A tela do dono

| # | Função | Prio | Resolve |
|---|---|---|---|
| 181 | **Painel do dono — seis números, sem gráfico e sem filtro** | E | Não existia **nenhuma tela onde o Marco visse se a plataforma está viva.** Ele tinha a busca de usuário e o painel do provedor: os dois respondem sobre *um caso*, nenhum sobre *a plataforma* |

1. GMV do mês e comissão do mês
2. Contratos por estado, com **quantos estão parados e há quantos dias** — é o número que mais importa e o único que ninguém olha
3. **Criadores prontos** (perfil + rede conectada + item publicado) sobre criadores cadastrados — o funil de oferta é o que mata marketplace novo
4. Marcas que contrataram ao menos uma vez, sobre marcas cadastradas
5. **Contratos entre par que se repete** — a única medida de retenção, e não só de novidade
6. Travados: cadastro recusado, reembolso com falha, disputa aberta

### As duas contradições, resolvidas

🟢 **Pedido aberto entra no v1** (Anel 2), como a lista mínima já dizia — corrigido o §7, que o punha na Fatia 2.
🟢 **Agência sai do v1.** Funções 107 a 113 adiadas. Veto do Marco encerra a discussão em qualquer direção.

### O que NÃO virou função, e por quê

- **Sistema de chamados: não se constrói.** *"O que acontece se não existir?"* — com 20 contratos/mês, quase nada: o Marco responde do e-mail dele. **O que falta é uma linha:** a função 32 passa a enviar automaticamente quem é o usuário, em que tela estava e de qual contrato — senão o operador recebe *"não consigo"* sem saber de quem. E o chamado vira item da 179.
- **Histórico, registros, administração de usuário: já existem** — 122, 127, 69, 123 e 10. Nada novo.
- **Comparação de métrica no cold start:** com 50 criadores em oito categorias, a mediana interna sai de três pessoas — é ruído, e às vezes identifica o concorrente. **Regra:** referência externa de mercado no v1, mediana interna só a partir de 30 criadores na categoria; abaixo disso a comparação **não aparece**.

---

## 6. Regras que valem para o produto inteiro 🔵

Levantadas ao longo do trabalho e adotadas como padrão:

1. **Uma ação óbvia por contexto.** Tela com cinco botões iguais é tela onde ninguém decide.
2. **Linguagem clara antes de linguagem esperta.** O Marco é a régua: se ele não entende sozinho, está mal escrito.
3. **Dinheiro, direitos e permissão falham fechado.** Na dúvida, o sistema nega e pede revisão humana.
4. **Toda métrica mostra de onde veio, de quando é e o que ela não cobre.**
5. **Dado que falta nunca vira zero.**
6. **Nenhuma ordenação sem explicação.**
7. **IA assiste; regra determinística e humano decidem o que é sensível.**
8. **Toda ação irreversível confirma em voz institucional**, nunca informal.

---

## 7. O que eu recomendo construir primeiro 🟢

Uma fatia vertical completa vale mais que dez telas soltas. A ordem:

**Fatia 1 — provar o ciclo do dinheiro.** Cadastro do criador → conectar rede → montar vitrine → marca busca → contrata da vitrine → paga com Pix → criador entrega → marca aprova → dinheiro vira saldo → avaliação. É o menor caminho que prova que a plataforma funciona com dinheiro de verdade.

**Fatia 2 — pedido aberto e comparador.** É onde mora a diferenciação.

**Fatia 3 — calendário e painéis.** O que transforma "consegui um trabalho" em "consigo tocar quinze".

**Fatia 4 — agência.** Multiplica volume por cliente.

Admin é construído **junto com cada fatia**, nunca depois — sem ele, ninguém consegue socorrer um usuário travado.

---

## 8. Pendências que exigem profissional humano ⚠️

| Tema | Profissional |
|---|---|
| Escada CPF → MEI, retenção, permuta como renda em espécie | Contador |
| Termos de Uso, LGPD, direito de imagem | Advogado |
| Identificação publicitária conforme guia do CONAR | Advogado |
| Aprovação automática por silêncio | Advogado |
| Cancelamento de trabalho presencial | Advogado |

---

*Inventário de produto. Não é parecer jurídico nem contábil.*
