# CRITÉRIO DE ACEITE — FATIA 1

> "PRONTO QUANDO…" para cada uma das 68 funções da Fatia 1 (`docs/FEATURE-MATRIX.md` §8:
> ciclo completo, remoto, vitrine, um contrato, Pix). Formato Dado/Quando/Então.
> Nenhum critério aceita "funciona bem" ou "está correto" — só o observável.
>
> Números batem com `FEATURE-MATRIX.md`. Fonte de cada regra: a seção correspondente
> da SPEC/MÁQUINA-DE-ESTADOS, citada entre parênteses.

## Conta (1–7)

**1 — Cadastro por e-mail e senha**
Dado um e-mail não cadastrado e uma senha válida, quando o usuário envia o formulário, então a conta é criada e ele está autenticado.

**2 — Verificação de e-mail**
Dado um cadastro recém-criado, quando o link de verificação é clicado, então o e-mail passa de não-verificado para verificado; até lá, ações que exigem e-mail verificado ficam bloqueadas com essa razão explícita.

**3 — Escolha de papel: criador ou marca**
Dado um cadastro sem papel definido, quando o usuário escolhe "criador" ou "marca", então a conta é permanentemente desse papel e a tela seguinte é a do papel escolhido (não existe troca de papel na mesma conta).

**4 — Recuperação de senha**
Dado um e-mail cadastrado, quando "esqueci a senha" é acionado, então um link de troca de senha, válido por tempo limitado, chega ao e-mail; usá-lo define nova senha e invalida o link.

**5 — Verificação de identidade com prova de vida**
Dado um usuário que inicia a verificação, quando o provedor de pagamento aprova a prova de vida, então o status de identidade muda para verificado; se recusa, o motivo do provedor é mostrado (função 42).

**6 — Verificação de CNPJ**
Dado um CNPJ informado, quando o provedor de pagamento confirma a situação cadastral, então a conta é marcada como empresa verificada; CNPJ inválido ou baixado bloqueia com o motivo.

**7 — Encerrar conta e baixar meus dados**
Dado um pedido de encerramento, quando não há contrato ativo nem disputa aberta, então a conta é encerrada e um arquivo com os dados pessoais é disponibilizado para download; havendo contrato/disputa aberta, o pedido fica em espera e isso é dito na tela (SPEC §14.5.2).

**8 — Aceite dos Termos sempre pelo titular**
Dado qualquer fluxo que exige aceite de Termos, quando o aceite é registrado, então ele grava o CPF/CNPJ do próprio titular autenticado — nunca de um operador agindo em nome de outro; tentar aceitar em nome de terceiro é impossível pela própria estrutura da tela (função 72 registra versão/data/origem).

## Redes sociais (8–12)

**9 — Conta conectada e desde quando**
Dado um criador com rede conectada, quando ele abre a tela de conexões, então vê o @ da conta e a data da primeira conexão.

**10 — Desconectar rede**
Dado uma rede conectada, quando o criador desconecta, então o token é revogado e a rede para de aparecer como fonte de métrica em itens novos; itens de vitrine já publicados com métrica daquela rede continuam mostrando o selo com a última data de leitura (função 11).

**11 — Selo "conectado por API" com data**
Dado qualquer métrica exibida (perfil, vitrine, busca), quando a tela renderiza, então mostra "via API · atualizado em [data]" ao lado do número — nunca um número sem a data.

**12 — Renovação automática de acesso**
Dado um token perto de expirar, quando o sistema tenta renovar automaticamente e falha, então o criador recebe aviso pedindo reconexão, com a métrica marcada como desatualizada até reconectar (nunca some silenciosamente).

## Notificações (13–16)

**13 — Central de notificações**
Dado um evento que gera notificação (proposta recebida, prazo vencendo, pagamento liberado), quando ele ocorre, então aparece na central dentro do produto, ordenado por mais recente.

**14 — E-mail para o crítico**
Dado um evento marcado como crítico (pagamento, prazo, disputa), quando ocorre, então um e-mail é disparado, mesmo que o usuário esteja com notificação no app desativada.

**15 — Notificação no celular**
Dado um usuário com push habilitado, quando um evento gera notificação, então ela chega como push no celular em até 1 minuto do evento.

**16 — Marcador de não lido**
Dado uma notificação nova, quando o usuário não abriu a central, então um contador visível mostra a quantidade de não lidas; abrir a central zera o contador.

## Suporte (18)

**18 — Falar com o suporte, com contexto automático**
Dado um usuário que aciona "falar com o suporte" de qualquer tela, quando a mensagem é enviada, então ela chega ao operador já com: id do usuário, tela de origem e id do contrato (se houver) — sem o usuário precisar digitar nada disso.

## Vitrine do criador (19–22, 24)

**19 — Montar perfil**
Dado um criador sem perfil completo, quando ele preenche foto, bio e categoria, então o perfil passa a ser exibível na busca; faltando qualquer um dos três, o perfil não aparece na busca e a tela diz o que falta.

**20 — Modalidade: remoto, presencial, híbrido**
Dado um item de vitrine em criação, quando o criador escolhe a modalidade, então o item herda as regras daquela modalidade (SPEC — confirmação por API para remoto, bilateral para presencial, MÁQUINA §8.5).

**21 — Montar item de vitrine**
Dado os campos obrigatórios preenchidos (tipo, quantidade, preço ≥ R$ 150, prazo do criador), quando o criador publica, então o item aparece na busca da marca; preço abaixo de R$ 150 é bloqueado na digitação, não depois de o item estar pronto (SPEC §4.5.1).

**22 — Pausar/arquivar item, pausar tudo até data**
Dado um item ativo, quando o criador pausa, então ele some da busca mas mantém contratos em andamento intactos; "pausar tudo até [data]" reativa sozinho na data informada, sem ação manual.

**24 — Nota e histórico no perfil**
Dado um criador com contratos concluídos, quando o perfil é exibido, então mostra a nota média (double-blind, função 75) e o número de contratos concluídos — nunca conta contrato cancelado ou em disputa como concluído.

## Painel do dia e calendário (25–28)

**25 — Resumo do dia**
Dado um usuário com pendências (proposta a responder, entrega a aprovar, prazo vencendo), quando ele abre o app, então a primeira tela lista o que precisa da ação dele hoje, ordenado por urgência.

**26 — Calendário do criador**
Dado contratos com data de entrega, quando o criador abre o calendário, então cada data com entrega aparece marcada.

**27 — Clicar num dia abre o que está em jogo**
Dado um dia marcado no calendário, quando o criador clica nele, então abre a lista de contratos com marco naquele dia.

**28 — Marcos aparecem automaticamente**
Dado um contrato fechado com data de entrega, quando o contrato é criado, então o marco aparece no calendário sem ação manual do criador.

## Propostas e contratos — lado do criador (29–36, 38–40, 42)

**29 — Propostas recebidas**
Dado uma proposta direta enviada por uma marca, quando o criador abre "propostas", então ela aparece com estado "aguardando resposta".

**30 — Aceitar, recusar ou pedir ajuste**
Dado uma proposta pendente, quando o criador aceita, então ela vira contrato e segue para pagamento; recusar a encerra; pedir ajuste devolve à marca com o comentário do criador anexado.

**31 — Candidatar-se a pedido aberto**
Dado um pedido aberto público, quando o criador se candidata, então a candidatura aparece para a marca na tela de comparação (função 49/comparador), e o criador não pode se candidatar duas vezes ao mesmo pedido.

**32 — Meus contratos por estado**
Dado contratos em qualquer estado da máquina de estados, quando o criador abre "meus contratos", então eles aparecem agrupados por estado (aguardando pagamento, em produção, aguardando aprovação, publicado, concluído, disputa).

**33 — Enviar a entrega**
Dado um contrato em produção, quando o criador anexa o arquivo/link e envia, então o estado muda para "aguardando aprovação" e a marca é notificada (função 14).

**34 — Ver pedido de ajuste referenciado**
Dado uma marca que pede ajuste apontando um trecho do briefing, quando o criador abre o pedido, então vê o comentário vinculado exatamente àquele ponto do briefing, não um texto solto.

**35 — Identificação publicitária e uso de IA**
Dado uma entrega em produção, quando o criador a envia, então precisa ter respondido: identificação publicitária confirmada, e uso de IA (não/parcial/integral) — envio é bloqueado sem essas duas respostas.

**36 — Confirmar entrega no formato do contrato**
Dado um contrato do tipo P1 (link), P2 (arquivo), P3 (presencial) ou P4 (código de anúncio), quando o criador confirma a entrega, então o sistema exige exatamente o dado daquele tipo — link para P1, upload para P2, check-in bilateral para P3, código para P4 — e rejeita qualquer outro formato.

**38 — Recebimentos: bloqueado · aguardando prazo · disponível**
Dado um contrato pago, quando a publicação é confirmada por API, então o valor muda de "bloqueado" para "aguardando prazo"; ao vencer o prazo de permanência mínima (90 dias, SPEC §8.2), muda para "disponível" (nomenclatura de interface: nunca "carteira"/"saldo" — SPEC §4.9.1).

**39 — Extrato com origem de cada valor**
Dado qualquer valor no extrato do criador, quando ele clica, então vê de qual contrato aquele valor veio, com data e estado.

**40 — Cadastrar/trocar conta bancária**
Dado uma troca de conta bancária, quando ela é salva, então um aviso é enviado ao e-mail ANTERIOR (não ao novo) e o próximo repasse automático só ocorre 24 h depois da troca.

**42 — Ver motivo da recusa e reenviar**
Dado uma verificação recusada **parcialmente** pelo provedor (`partially_denied` / `additional_documents_required`), quando o usuário abre a pendência, então vê o motivo literal do provedor e pode reenviar o documento sem reiniciar o cadastro inteiro.
E: dado um documento reenviado, quando o provedor devolve `pending` / `answered_waiting_analysis`, então a tela mostra **"Reenviado — em nova análise"**, distinta de "em análise" — o criador nunca reenvia duas vezes por não saber se foi (MÁQUINA §3.2).
E: dado uma recusa **definitiva** (`denied` / `fully_denied`), quando ela chega, então o caso vai direto à caixa de entrada do operador **sem esperar os 30 dias**, porque não existe botão que o criador possa apertar (MÁQUINA §3.2).
E: dado qualquer estado de KYC, quando consultado, então o valor do contrato continua `retido` ou `bloqueado_por_verificacao` — nunca liberado, nunca perdido.

## Dinheiro — agenda de recebíveis (44–45)

**44 — Agenda de recebíveis**
Dado um repasse realizado, quando o criador consulta a agenda, então vê valor bruto, cada dedução discriminada (comissão, imposto, tarifa) e o valor líquido recebível — nunca um número único sem composição (obrigação BCB Res. 264/349, vencida desde 01/04/2024).

**45 — Contratos que gravam a agenda**
Dado um lançamento na agenda de recebíveis, quando auditado, então é rastreável à contraparte, ao valor alcançado e à natureza da transação daquele contrato específico.

## Busca e contratação — lado da marca (47–51)

**47 — Busca de criadores**
Dado criadores com perfil completo (função 19), quando a marca busca por termo, então os resultados retornam ordenados por relevância, mostrando apenas criadores com item de vitrine ativo.

**48 — Filtros**
Dado uma busca ativa, quando a marca aplica filtro de categoria, orçamento, região ou modalidade, então os resultados são restritos a criadores que atendem TODOS os filtros marcados simultaneamente.

**49 — Perfil completo do criador**
Dado um resultado de busca, quando a marca abre o perfil, então vê bio, categorias, itens de vitrine, nota, histórico de contratos e métricas com selo de API — os mesmos dados usados na função 24.

**50 — Contratar da vitrine**
Dado um item de vitrine, quando a marca preenche o formulário curto (briefing, quem publica, uso em anúncio) e confirma, então um contrato nasce em "aguardando pagamento" com preço e prazo herdados do item, sem negociação.

**51 — Proposta direta**
Dado uma marca que quer condições diferentes do item de vitrine, quando ela envia proposta direta com formulário completo, então ela chega ao criador como proposta pendente (função 29), não como contrato.

## Painel do dia da marca (55)

**55 — O que precisa da minha decisão hoje**
Dado uma marca com pendências (aprovar entrega, responder pedido de ajuste, decidir disputa), quando ela abre o app, então a tela inicial lista essas pendências ordenadas por prazo mais próximo de vencer.

## Contrato e ciclo (58–60, 62–63)

**58 — Contrato com marcos e estados**
Dado um contrato criado, quando consultado a qualquer momento, então mostra o estado atual da máquina de estados e a data de cada marco já ocorrido.

**59 — Aprovar entrega**
Dado uma entrega em "aguardando aprovação", quando a marca aprova, então o criador é liberado para publicar (ou, se já publicado por API, o dinheiro segue para liberação — MÁQUINA §8.0.1); se o prazo de aprovação vence sem ação, aprova automaticamente em 7 dias.

**60 — Pedir ajuste referenciado**
Dado uma entrega em avaliação, quando a marca pede ajuste, então precisa apontar o trecho exato do briefing referenciado — pedido de ajuste sem referência é bloqueado pela tela.

**62 — Cancelar dentro da janela**
Dado um contrato ainda não iniciado ou dentro da janela de cancelamento (remoto/presencial conforme MÁQUINA §13.2), quando qualquer parte cancela dentro do prazo, então o dinheiro retorna pela regra de estorno do meio de pagamento usado (SPEC §4.3.4), sem necessidade de disputa.

**63 — Pix, boleto e cartão**
Dado um contrato em "aguardando pagamento", quando a marca escolhe o meio de pagamento, então o checkout processa exatamente as regras daquele meio (Pix sem teto, boleto sem teto, cartão com teto conforme verificação — SPEC §4.3.1) e o contrato só avança para "pago" com confirmação do provedor, nunca por marcação manual.
E: dado um pagamento confirmado pelo provedor cujo aviso **nunca chegou**, quando o prazo de expiração vence, então o sistema consulta o provedor antes de expirar e **aplica o pagamento atrasado** — jamais marca `expirado_sem_pagamento` com dinheiro dentro do provedor (MÁQUINA §9.4).
E: dado que o provedor confirma que não houve pagamento, quando o contrato vai expirar, então a cobrança é **cancelada no provedor antes** da expiração — senão um boleto pago depois entra sem contrato para recebê-lo.
E: dado que o provedor não responde, quando o prazo vence, então a cobrança vai a `conciliacao_pendente`, o contrato **não se move**, e o caso entra na caixa de entrada.
E: dado o mesmo aviso recebido duas vezes (mesmo `id`), quando processado, então a transição acontece **uma vez só**; dado um aviso pedindo transição impossível no estado atual, então ele é registrado e não força nada.

## Institucional e confiança (67, 70–75)

**67 — Notas fiscais e recibos**
Dado um pagamento confirmado, quando o documento fiscal correspondente é gerado pelo provedor/plataforma, então fica disponível para download por ambas as partes do contrato.

**70 — Perfil público da marca**
Dado uma marca com histórico, quando um criador visualiza o perfil dela, então vê nome, logo, segmento, site e a nota média recebida de criadores anteriores.

**71 — Chat liberado só após pagamento**
Dado um contrato ainda não pago, quando qualquer parte tenta abrir o chat, então o acesso é bloqueado com a razão explícita; pagamento confirmado libera o chat imediatamente.

**72 — Termos versionados**
Dado um aceite de Termos, quando registrado, então grava qual versão do documento, a data/hora e a origem (IP ou dispositivo) — consultável depois, por auditoria (função 84).

**73 — Contrato em PDF**
Dado um contrato pago, quando qualquer parte solicita o PDF, então recebe um documento idêntico para ambos os lados, com todos os termos e valores daquele contrato específico.

**74 — Avaliar a outra ponta**
Dado um contrato concluído, quando qualquer parte avalia, então grava nota e comentário; a avaliação só é publicada quando ambos avaliaram ou o prazo de avaliação vence (função 75).

**75 — Publicação simultânea às cegas**
Dado duas avaliações pendentes do mesmo contrato, quando uma parte envia a sua, então ela fica oculta até a outra parte também enviar (ou o prazo vencer) — nenhuma parte consegue ver a nota do outro antes de dar a sua.

## Disputa (76, 80–84, 86)

**76 — Abrir disputa**
Dado um **marco financiado** em um dos seis estados elegíveis (`em_execucao`, `agendado`, `em_comprovacao`, `ajuste_solicitado`, `reenviado`, `em_permanencia`/`removido_antes_do_prazo` — lista única em MÁQUINA §10.0), quando a parte autorizada abre disputa, então o dinheiro daquele marco é congelado até a resolução e a outra parte é notificada para apresentar evidência.
E: dado um marco em qualquer dos seis estados **não** elegíveis (`planejado`, `aguardando_pagamento`, `financiado`, `aguardando_insumo`, `aprovado`, `concluido`/`cancelado`), quando se tenta abrir disputa, então a ação é recusada com o motivo.
E: dado um marco que entra em disputa, quando o contrato é consultado, então ele aparece em disputa **por derivação** — não existe botão que leve o contrato a `em_disputa` direto.
E: dado um marco já em disputa, quando se tenta abrir uma segunda, então é recusada — no máximo uma disputa aberta por marco.
E: dado uma disputa de permanência, quando decidida, então ela **não move dinheiro** — registra no histórico do criador ou o inocenta (MÁQUINA §10.0.1).

**80 — Mediar disputa com evidências**
Dado uma disputa aberta com evidência de ambas as partes, quando o operador abre o caso, então vê as evidências de criador e marca lado a lado, com timestamp de cada uma.

**81 — Liberar, reter ou estornar**
Dado uma disputa julgada, quando o operador decide, então o sistema executa exatamente uma das três ações (liberar ao criador, reter, estornar à marca) e a move para "resolvida" — não existe estado intermediário sem ação.

**82 — Buscar usuário e ver histórico**
Dado um id, e-mail ou CPF/CNPJ, quando o operador busca, então vê o histórico completo de contratos, disputas e avaliações daquele usuário.

**83 — Suspender ou banir**
Dado uma decisão de suspensão/banimento, quando o operador aplica, então o motivo é registrado de forma imutável (função 84) e a conta perde acesso a criar contrato novo; contratos em andamento seguem a regra de disputa/cancelamento, nunca somem.

**84 — Registro de auditoria imutável**
Dado qualquer ação administrativa (suspender, liberar dinheiro, editar dado sensível), quando ela ocorre, então fica gravada com quem, quando e o quê — sem função de edição ou exclusão desse registro em lugar nenhum do produto.

**86 — Reconciliação de pagamento**
Dado um contrato travado por divergência com o provedor, quando o operador aciona "reconsultar provedor", então o sistema busca o estado real no provedor e destrava o contrato automaticamente se a divergência se resolve.
E: dado que a reconsulta **automática** (varredura diária, SPEC §4.6.1, e todo vencimento de prazo) já roda antes disso, quando ela resolve a divergência, então nenhum item chega ao operador — a ação manual é a exceção, não a regra (MÁQUINA §9.4).

## Operação (88–89, 92)

**88 — Caixa de entrada do operador**
Dado qualquer item que precisa de ação humana (disputa, verificação recusada, reconciliação pendente), quando gerado, então aparece nessa caixa única, com prazo visível — nunca espalhado em múltiplas telas.
E: dado uma recusa definitiva de KYC ou uma cobrança em `conciliacao_pendente`, quando ocorre, então um item é criado aqui — são os dois casos novos que MÁQUINA §3.2 e §9.4 despejam nesta caixa.
⚠️ **O prazo visível desses dois itens novos ainda não tem número com fonte** — ver `BLOCKERS.md`.

**89 — Painel do dono**
Dado o Marco (ou quem ele designar) acessando o painel administrativo, quando aberto, então mostra os números vivos do negócio (contratos/mês, receita de comissão, fundo de contestação) — não uma cópia estática do painel de produto.

**92 — Prazo vencido: cancelar e receber de volta**
Dado um contrato cujo prazo de entrega venceu há mais de 3 dias sem entrega, quando a marca aciona o botão único de cancelamento, então o dinheiro retorna pela regra de estorno (SPEC §4.3.4); se o criador contesta alegando ter entregado, a ação abre disputa (função 76) em vez de executar o cancelamento direto.

---

## O que fica de fora desta lista, de propósito
Funções de fatia 2 e 3 (produto físico, cliente grande, cartão parcelado) não têm critério aqui — ganham o deles quando a construção chegar lá, não antes (regra do Passo 7: não gerar trabalho para o que ainda não vai ser codado).
