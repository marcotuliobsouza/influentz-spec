# Feature Matrix — INFLUENTZ

> **O que é este documento.** O inventário **completo** de tudo que a plataforma faz, organizado por quem usa e por módulo. É o documento que existe para garantir que **nada falta**.
>
> Ele nasce de uma instrução direta do Marco: *"não faltar nada, absolutamente nada neste produto, que o cliente na hora que usar sinta falta."*
>
> **Como ler a prioridade:**
> **E** = essencial (sem isso não existe produto) · **P** = premium (é o que faz a plataforma valer a comissão) · **F** = futuro (depois de haver volume)
>
> **Versão:** v1.1 — **169 funções**
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

## 1. Comum a todos — a base que sustenta tudo

### 1.1 Conta e identidade

| # | Função | Prio | Observação |
|---|---|---|---|
| 1 | Cadastro por e-mail e senha | E | |
| 2 | Entrar com Google / Apple | P | Reduz atrito no cadastro |
| 3 | Verificação de e-mail e telefone | E | |
| 4 | Autenticação em duas etapas | P | Obrigatória para quem movimenta dinheiro |
| 5 | Escolha de papel (criador / marca / agência) | E | |
| 6 | **Seletor de espaço de trabalho** | P | 🔵 A mesma pessoa em vários espaços |
| 7 | Verificação de identidade (documento) | E | Reaproveita a do provedor de pagamento |
| 8 | Verificação de CNPJ | E | Para marca e agência |
| 9 | Recuperação de senha | E | |
| 10 | Encerrar conta e baixar meus dados | E | ⚠️ LGPD |

### 1.2 Conexão com redes sociais ⚠️ módulo crítico

Aqui mora uma das melhores observações do Marco: **API de rede social quebra, e a plataforma não pode fingir que não.**

| # | Função | Prio | Observação |
|---|---|---|---|
| 11 | Conectar Instagram / YouTube / TikTok | E | Ao menos uma é obrigatória |
| 12 | **Logotipo oficial e atualizado de cada rede** | E | Seguindo o guia de marca de cada plataforma |
| 13 | Mostrar qual conta está conectada e desde quando | E | |
| 14 | Desconectar rede | E | |
| 15 | **Monitor de saúde da conexão** | E | 🔵 Verifica periodicamente se o acesso ainda funciona |
| 16 | **Aviso de reconexão necessária** | E | 🔵 "Seu Instagram precisa ser reconectado" — no app, por e-mail e por push |
| 17 | **Selo de atualidade em toda métrica** | E | 🔵 "atualizado há 2 dias" · "desatualizado desde 12/09" |
| 18 | **Dado ausente nunca aparece como zero** | E | 🔵 Mostra "não disponível", nunca "0" |
| 19 | Painel administrativo de saúde das APIs | P | Quando a rede muda a versão, o Admin vê antes do usuário reclamar |
| 20 | Congelar métrica com data de corte quando a conexão cai | P | Melhor mostrar dado velho rotulado do que dado errado |

⚠️ **Por que isso é crítico e não detalhe:** métrica velha mostrada como atual é a forma mais rápida de uma plataforma de criadores perder credibilidade. Se a marca contrata com base num número desatualizado e descobre depois, a culpa é da plataforma.

### 1.3 Notificações

| # | Função | Prio | Observação |
|---|---|---|---|
| 21 | Central de notificações no produto | E | |
| 22 | E-mail para o que é crítico | E | Proposta recebida, prazo vencendo, entrega para aprovar |
| 23 | Push no celular | E | |
| 24 | Marcador visual de não lido | E | |
| 25 | Preferências por tipo de notificação | P | |
| 26 | WhatsApp | F | Tem custo por mensagem e exige aprovação de modelos |
| 27 | ~~Alerta sonoro~~ | ❌ | ⚠️ **Não recomendo.** Navegador bloqueia som automático, e ferramenta de trabalho que apita é ferramenta silenciada na primeira semana. Push resolve melhor. Registro a discordância; se o Marco decidir o contrário, eu faço |

### 1.4 Ajuda dentro da tela

| # | Função | Prio | Observação |
|---|---|---|---|
| 28 | **Dica explicativa em todo número que exige interpretação** | E | 🔵 Toda métrica, taxa e prazo tem uma frase que explica |
| 29 | Origem do dado visível | E | De qual rede veio, de que período |
| 30 | Primeiro uso guiado por papel | P | |
| 31 | Central de ajuda e busca | P | |
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
| 34 | **O que fazer agora** | E | 🔵 Uma ação óbvia por vez, em ordem de urgência |
| 35 | Saldo em destaque | E | |
| 36 | Oportunidades sugeridas | P | |
| 37 | **Resumo em linguagem simples de cada contrato** | P | 🔵 "Você está no marco 2 de 3. Falta enviar o vídeo até 12/10" |
| 38 | Alerta de risco de atraso | P | 🔵 Cruza prazos com a agenda e avisa antes de estourar |

⚠️ **Sobre inteligência artificial, com honestidade:** no lançamento a IA **não tem com o que aprender** — não existe histórico. Então o v1 entrega inteligência **determinística**: regras claras que somam prazos, contam marcos e ordenam por urgência. Isso resolve quase todo o valor que o Marco descreveu, sem depender de dado que ainda não existe. IA de linguagem entra quando houver volume, e mesmo aí **nunca** libera dinheiro, suspende conta ou decide disputa — isso é regra determinística e humano.

### 2.2 Calendário e agenda ⚠️ módulo que faltava inteiro

Pedido direto do Marco, e ele está certo: **lista de contratos não é gestão de agenda.**

| # | Função | Prio | Observação |
|---|---|---|---|
| 39 | **Calendário do criador** | E | Mês, semana e lista |
| 40 | **Clicar num dia abre o que está em jogo** | E | Contratos daquele dia, em que marco, o que falta |
| 41 | Marcos com data aparecem automaticamente | E | Entrega, publicação, evento presencial |
| 42 | **Bloquear data / marcar indisponibilidade** | E | 🔵 Férias, viagem, agenda cheia |
| 43 | **Data bloqueada some da vitrine** | E | 🔵 Impede a marca de contratar para um dia impossível |
| 44 | Vista de carga de trabalho | P | 🔵 Quantas entregas por semana — evita o criador aceitar 15 para a mesma semana |
| 45 | Exportar para Google Calendar / Apple | P | |
| 46 | Lembrete configurável antes do prazo | P | |
| 47 | Sugerir data realista ao aceitar proposta | P | 🔵 Cruza com o que já está agendado |

### 2.3 Perfil e vitrine

| # | Função | Prio | Observação |
|---|---|---|---|
| 48 | Montar perfil (foto, bio, categorias) | E | |
| 49 | Avatar padrão quando não há foto | E | Usa o oficial da marca (`docs/marca/avatares`) |
| 50 | Modalidade: remoto / presencial / híbrido | E | |
| 51 | Região de atendimento presencial | E | |
| 52 | **Montar item de vitrine** | E | Nome, preço, prazo, revisões, direitos |
| 53 | Pausar / arquivar item | E | |
| 54 | Portfólio de trabalhos anteriores | P | |
| 55 | Prévia de "como a marca me vê" | P | 🔵 |
| 56 | Selo de verificado | E | Usa o oficial da marca, em degradê |
| 57 | **Valor líquido visível antes de ofertar** | E | 🔵 O criador vê quanto recebe de fato, já com a comissão descontada |

### 2.4 Propostas e trabalho

| # | Função | Prio | Observação |
|---|---|---|---|
| 58 | Propostas recebidas | E | |
| 59 | Aceitar / recusar / pedir ajuste | E | Janela de 48 h |
| 60 | Candidatar-se a pedido aberto | E | Criador define preço e prazo |
| 61 | Enviar proposta por conta própria | P | |
| 62 | Meus contratos, por estado | E | |
| 63 | **Enviar a entrega** | E | Arquivo, link ou confirmação de comparecimento |
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
| 72 | Guia embutido de como abrir MEI | P | Reduz o atrito que trava o criador iniciante |
| 73 | Antecipação de recebíveis | P | Segunda fonte de receita |
| 74 | Previsão de recebimento dos próximos 30 dias | P | 🔵 Cruza contratos em andamento com prazos de liberação |

---

## 3. BRAND WEB — a marca

### 3.1 Painel

| # | Função | Prio | Observação |
|---|---|---|---|
| 75 | **O que precisa da minha decisão hoje** | E | 🔵 Entregas para aprovar, propostas para responder, pagamentos pendentes |
| 76 | Campanhas em andamento | E | |
| 77 | Orçamento comprometido × gasto | P | |
| 78 | Calendário de publicações contratadas | P | 🔵 Quando cada conteúdo vai ao ar |
| 79 | Alerta de prazo de aprovação vencendo | E | ⚠️ Se ela não aprovar, aprova sozinho em 7 dias — ela precisa saber |

### 3.2 Descobrir e contratar

| # | Função | Prio | Observação |
|---|---|---|---|
| 80 | Busca de criadores | E | |
| 81 | Filtros: categoria, orçamento, região, modalidade, público | E | |
| 82 | **Ordenação explicada** | E | 🔵 Nunca ranking oculto — a marca vê por que aquela ordem |
| 83 | Cota de visibilidade para criador novo | E | Sem isso o marketplace nunca gira |
| 84 | Perfil completo do criador | E | |
| 85 | Favoritos / listas | P | |
| 86 | **Contratar da vitrine** (formulário curto) | E | |
| 87 | **Proposta direta** (formulário completo) | E | |
| 88 | **Publicar pedido aberto** | E | |
| 89 | Ver candidaturas | E | |
| 90 | **Comparador lado a lado** | P | A tela que mais justifica a comissão |
| 91 | Convidar criador para um pedido | P | |
| 92 | Contratar vários criadores no mesmo pedido | E | |

### 3.3 Acompanhar e aprovar

| # | Função | Prio | Observação |
|---|---|---|---|
| 93 | Contrato com marcos e estados | E | |
| 94 | Aprovar entrega | E | |
| 95 | **Pedir ajuste referenciado ao briefing** | E | Reduz disputa |
| 96 | Ver quantas revisões restam | E | |
| 97 | Visão de campanha (vários contratos) | P | |
| 98 | Baixar contrato em PDF | E | |
| 99 | Cancelar dentro da janela | E | |
| 100 | Abrir disputa | E | |

### 3.4 Pagamento

| # | Função | Prio | Observação |
|---|---|---|---|
| 101 | Pix, boleto e cartão | E | Cartão só com CNPJ verificado |
| 102 | **Valor final tudo incluso** | E | Sem taxa somada depois |
| 103 | Prazo de disponibilização visível por meio | E | |
| 104 | Financiar marco a marco | E | |
| 105 | Notas fiscais e recibos | E | ⚠️ Contador |
| 106 | Vários métodos salvos | P | |

---

## 3.5 Contrato recorrente ⚠️ módulo reincorporado

⚠️ **Eu tinha tirado a recorrência do escopo, e o motivo estava errado.**

Tirei porque a ideia tinha aparecido num documento cuja origem o Marco não reconhecia — ou seja, descartei pela **fonte**, não pelo **mérito**. Isso contraria a regra do `CLAUDE.md` §2.7: a fala do Marco é matéria-prima e o que importa é verificar, não a procedência. Ele devolveu com um caso de uso concreto que fecha a discussão:

> *"uma marca que contratar creator para provador fixo mensal ou outro período acordado pode ter uma recorrência. Do que terem que ficar contratando toda vez a mesma coisa."*

Está certo. E não é conveniência: **é o modelo de contratação mais valioso da plataforma.** Embaixador de marca, provador mensal, pacote fixo de conteúdo. Para o criador vira renda previsível; para a marca vira relação em vez de transação; para a INFLUENTZ vira receita recorrente — que vale muito mais que comissão avulsa.

### 3.5.1 Como funciona 🟢

| # | Função | Prio | Observação |
|---|---|---|---|
| 129 | **Criar contrato recorrente** | P | Mensal, quinzenal, trimestral ou período combinado |
| 130 | Definir o que se repete a cada ciclo | P | Ex.: 4 Stories + 1 Reels por mês |
| 131 | **Cada ciclo é um contrato próprio por dentro** | P | Financiamento, entrega, aprovação e repasse independentes |
| 132 | Renovação automática | P | Com aviso antes de cada ciclo |
| 133 | **Encerrar a recorrência** (vale a partir do próximo ciclo) | P | Diferente de cancelar o ciclo atual |
| 134 | **Cancelar só o ciclo atual** | P | Mês em que a marca não vai usar |
| 135 | **Pausar** | P | Férias do criador, verba parada da marca |
| 136 | Reajustar valor entre ciclos | P | Precisa de aceite dos dois lados |
| 137 | Prazo de aviso prévio para encerrar | P | Protege quem reservou agenda |
| 138 | Ver o histórico de todos os ciclos | P | |
| 139 | Calendário mostra os ciclos futuros | P | Liga com o módulo de agenda (§2.2) |

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
| 107 | Espaço da agência | E | |
| 108 | Convidar marca representada (aceite dos dois lados) | E | |
| 109 | Convidar criador representado (aceite dos dois lados) | E | |
| 110 | Agir em nome de, com autoria registrada | E | Toda ação mostra quem realmente fez |
| 111 | Ver campanhas de todas as marcas num lugar | E | |
| 112 | Calendário consolidado | P | 🔵 Todos os criadores, todas as datas |
| 113 | **Alerta de autonegociação** | E | Mesmo CPF/CNPJ nos dois lados → revisão manual |
| 114 | Permissões por membro da equipe | F | |
| 115 | Faturamento consolidado | F | |
| 116 | Relatório por marca | P | |

---

## 5. ADMIN WEB — equipe INFLUENTZ

| # | Função | Prio | Observação |
|---|---|---|---|
| 117 | Papéis: Super Admin, Financeiro, Suporte, Trust & Safety | E | |
| 118 | Fila de disputas por risco | E | |
| 119 | Mediar disputa com evidências das duas partes | E | |
| 120 | Liberar, reter ou estornar valor | E | ⚠️ Sempre com motivo, autor e registro |
| 121 | Fila de verificação manual | E | Autonegociação, valor alto, conta nova |
| 122 | Buscar usuário e ver histórico completo | E | |
| 123 | Suspender / banir, com motivo | E | |
| 124 | **Configurar comissão e prazos** | E | Nunca fixo no código |
| 125 | Painel financeiro e conciliação | E | |
| 126 | **Painel de saúde das APIs sociais** | P | 🔵 |
| 127 | Registro de auditoria imutável | E | Toda ação sensível fica gravada |
| 128 | Moderação de conteúdo e denúncias | E | |

---

## 5.5 Funções acrescentadas pela auditoria 🔴

Auditoria feita pelo especialista de produto em 08/09/2026, com contexto limpo. Encontrou **12 lacunas, 8 delas capazes de travar o lançamento**. Todas conferidas e todas procedentes. As funções que faltavam:

### Cadastro e identidade

| # | Função | Prio | Resolve |
|---|---|---|---|
| 140 | **Comprovar rede por envio manual** (captura do painel, vídeo de tela) | E | O criador de Instagram entrando no dia 1, com a API ainda na fila |
| 141 | **Fila de aprovação de rede declarada** no Admin | E | Idem |
| 142 | **Rótulo "declarada · não verificada"** ao lado da métrica | E | Nunca misturar dado declarado com dado de API |
| 143 | **Cadastrar e trocar conta bancária** | E | Não existia. Só havia "sacar" |
| 144 | **Ver motivo da recusa do provedor e reenviar documento** | E | O beco sem saída de quem tem dinheiro aprovado que não sai |

### Dinheiro

| # | Função | Prio | Resolve |
|---|---|---|---|
| 145 | **Dados de reembolso da marca no checkout** de Pix e boleto | E | Não havia por onde devolver dinheiro fora do cartão |
| 146 | **Acompanhar reembolso** nas duas pontas | E | |
| 147 | **Fila de reembolso com falha** no Admin | E | Reembolso que não completa não pode sumir em silêncio |
| 148 | **Reserva de contestação** visível ao criador, com data de liberação | E | Contestação que chega depois do saque |
| 149 | **Saldo negativo** com saque e novos contratos bloqueados | E | Idem |
| 150 | **Anexar nota fiscal do criador** antes da liberação do repasse | E | A marca com CNPJ precisa da nota para lançar a despesa |
| 151 | **Marca baixa a nota do criador** dentro do contrato | E | Idem |

### Entrega

| # | Função | Prio | Resolve |
|---|---|---|---|
| 152 | **Envio retomável**, com tamanho e formato declarados e estado de falha | E | Reels de 900 MB no 4G que cai aos 80% |
| 153 | **Prévia com marca d'água antes da aprovação** | E | ⚠️ Ver abaixo |
| 154 | **Original liberado só após aprovar** (ou vencer a aprovação automática) | E | Idem |
| 155 | Prazo de guarda do arquivo após o contrato | P | |
| 156 | **Lançar código de rastreio** (marca) | E | Envio de produto físico |
| 157 | **Confirmar recebimento do produto** (criador) | E | O relógio do criador só começa aqui |
| 158 | **Declarar extravio** | E | |
| 159 | **Check-in presencial** com data, hora e local | E | ⚠️ Ver abaixo |
| 160 | **Confirmação de comparecimento pela marca**, com prazo | E | Idem |

⚠️ **Por que a prévia com marca d'água (153) é essencial:** o dinheiro fica retido, mas **o conteúdo não**. Sem isso, nada impede a marca de baixar o vídeo final, publicar e nunca aprovar. O escrow protege uma ponta só. Marca d'água antes, original depois da aprovação, protege as duas.

⚠️ **Por que o check-in (159) é essencial:** a regra de cancelamento presencial dá 100% ou 0% conforme quem faltou — mas sem registro, isso vira palavra contra palavra decidindo dinheiro. Check-in com carimbo de hora e local é a prova que faltava.

### Disputa

| # | Função | Prio | Resolve |
|---|---|---|---|
| 161 | **Enviar evidência** | E | A disputa tinha estados e nenhuma função |
| 162 | **Ver o que a outra parte alegou** | E | |
| 163 | **Acompanhar o andamento e o prazo** | E | |
| 164 | **Aceitar acordo** antes da decisão | P | |

### Contrato

| # | Função | Prio | Resolve |
|---|---|---|---|
| 165 | **Aditivo de escopo** com aceite dos dois lados | P | ⚠️ Ver abaixo |
| 166 | **Termos de Uso versionados**, com registro de qual versão cada um aceitou, quando e de onde | E | A aprovação automática por silêncio só é oponível se estiver nos termos aceitos |
| 167 | **Contrato em PDF para as duas pontas e para a agência** | E | Só a marca tinha |

⚠️ **Por que o aditivo (165) importa comercialmente:** hoje, se a marca quer antecipar a publicação ou acrescentar um Story pagando mais, só existem três saídas — pedir ajuste (que consome revisão e não muda preço), cancelar, ou **combinar por fora**. A terceira é exatamente o que a SPEC §13.2 tenta impedir. Sem aditivo, a plataforma empurra volume para fora dela mesma.

### Operação de lançamento

| # | Função | Prio | Resolve |
|---|---|---|---|
| 168 | **Convite por link** com papel pré-definido | E | ⚠️ Ver abaixo |
| 169 | **Cadastro assistido** no Admin, com autoria registrada | E | Idem |

⚠️ **Por que 168 e 169 travariam o lançamento:** a SPEC §14.1 diz que os 50 primeiros criadores entram por convite pessoal do Marco, com cadastro feito junto com eles. **Não existia nenhuma ferramenta para isso.** Ele faria por WhatsApp e planilha, fora da plataforma — e a operação que sustenta o lançamento inteiro ficaria sem registro nenhum.

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
