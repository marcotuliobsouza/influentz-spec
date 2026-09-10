# INVENTÁRIO DE FUNÇÕES — INFLUENTZ

> **Versão:** v3.1 · 09/09/2026
> **O que é:** tudo o que a plataforma faz, organizado pela ordem em que a pessoa usa.
> **91 funções no v1.** Se algo não está aqui, não existe no lançamento.

**Prioridade:** **E** = sem isso não lança · **P** = entra no v1 se couber · **F** = depois do v1.

**As quatro superfícies:** `CRIADOR` · `MARCA` · `AGÊNCIA` · `ADMIN`.
Todo usuário tem web, iOS e Android com função completa. O que muda é para qual tela cada superfície foi desenhada primeiro, não o que ela pode fazer.

---

## 1. A base — vale para todo mundo

### 1.1 Conta

| # | Função | Prio |
|---|---|---|
| 1 | Cadastro por e-mail e senha | E |
| 2 | Verificação de e-mail | E |
| 3 | Escolha de papel: criador, marca ou agência | E |
| 4 | Recuperação de senha | E |
| 5 | Verificação de identidade com prova de vida, feita pelo provedor de pagamento | E |
| 6 | Verificação de CNPJ | E |
| 7 | Encerrar conta e baixar meus dados | E |

**Telefone é campo de contato, não é verificado por SMS no v1.** A prova de que a pessoa é ela mesma vem da função 5, que é incomparavelmente mais forte que um código por mensagem.

### 1.2 Redes sociais e métricas

| # | Função | Prio |
|---|---|---|
| 8 | Conectar Instagram, YouTube e TikTok | E |
| 9 | Mostrar qual conta está conectada e desde quando | E |
| 10 | Desconectar rede | E |
| 11 | Selo "conectado por API" com a data da última atualização, em toda métrica | E |
| 12 | Renovação automática de acesso, com aviso de reconexão quando falha | E |
| 12.1 | **Série histórica de seguidores**, gravada desde o primeiro dia | E |

**Na INFLUENTZ não existe métrica que não venha da API oficial da rede.** Sem captura de tela, sem número digitado, sem aprovação manual.

**Conta pessoal não tem API.** Quando o criador tem conta pessoal no Instagram ou TikTok, a função 8 mostra o passo a passo de conversão para conta profissional — que é grátis e leva um minuto — e o botão de tentar de novo.

### 1.3 Notificações

| # | Função | Prio |
|---|---|---|
| 13 | Central de notificações dentro do produto | E |
| 14 | E-mail para o que é crítico | E |
| 15 | Notificação no celular | E |
| 16 | Marcador visual de não lido | E |
| 17 | WhatsApp | F |

### 1.4 Suporte

| # | Função | Prio |
|---|---|---|
| 18 | Falar com o suporte — envia junto, automaticamente, quem é o usuário, em que tela estava e de qual contrato | E |

Não existe sistema de chamados no v1. Com 20 contratos por mês, a mensagem cai no e-mail do operador e vira item da caixa de entrada (função 88).

### 1.5 Os seis estados obrigatórios de toda tela

Nenhuma tela é considerada pronta sem os seis: **vazio · carregando · erro · sem internet · sucesso · sem permissão.**

Duas regras que valem em toda tela onde aparece número:

- **Dado que falta nunca vira zero.** Aparece como ausente, com a data da última leitura.
- **Todo número explica de onde veio, de quando é e o que não cobre.**

---

## 2. Criador

### 2.1 Perfil e vitrine

| # | Função | Prio |
|---|---|---|
| 19 | Montar perfil: foto, bio, categorias | E |
| 20 | Modalidade: remoto, presencial ou híbrido | E |
| 21 | Montar item de vitrine | E |
| 22 | Pausar ou arquivar item, **e pausar tudo até uma data** (férias) | E |
| 22.1 | **Limite de trabalhos ao mesmo tempo** — padrão 3. No limite, os itens saem da busca e o perfil continua aberto | E |
| 23 | Portfólio de trabalhos anteriores | P |
| 24 | Nota e histórico no perfil, com número de contratos concluídos | E |

### 2.2 O dia a dia

| # | Função | Prio |
|---|---|---|
| 25 | Resumo do dia: o que precisa da minha ação | E |
| 26 | Calendário do criador | E |
| 27 | Clicar num dia abre o que está em jogo | E |
| 28 | Marcos com data aparecem no calendário automaticamente | E |

### 2.3 Fechar trabalho

| # | Função | Prio |
|---|---|---|
| 29 | Propostas recebidas | E |
| 30 | Aceitar, recusar ou pedir ajuste | E |
| 31 | Candidatar-se a pedido aberto | E |
| 32 | Meus contratos, por estado | E |

### 2.4 Entregar

| # | Função | Prio |
|---|---|---|
| 33 | Enviar a entrega | E |
| 34 | Ver o pedido de ajuste referenciado ao ponto exato do briefing | E |
| 35 | Confirmar identificação publicitária, **e declarar uso de inteligência artificial** (não / parcial / integral) | E |
| 36 | **Confirmar a entrega no formato que o contrato pede** — link do post (P1), arquivo (P2), check-in de comparecimento (P3) ou código de anúncio (P4) | E |

**Sobre a função 33.** A entrega exige um **arquivo de revisão em MP4/H.264** — que é o que o criador exporta para a rede de qualquer jeito. O arquivo original é opcional e só é liberado à marca depois da aprovação. Entrega com várias peças permite **aprovar peça a peça**, para o criador não refazer três Stories por causa de um.

**Sobre a função 36, que é o centro do produto.** O que a marca compra é uma **publicação no ar**, não um arquivo aprovado. O criador cola o link; a plataforma confere pela API que ele já conectou que o post existe, é da conta certa e tem a data — e traz o alcance na mesma chamada. **É neste momento que o dinheiro é liberado.**

### 2.5 Produto físico

| # | Função | Prio |
|---|---|---|
| 37 | Confirmar recebimento: *"recebi"* ou *"não recebi ou veio com problema"*, com observação | E |

O relógio de entrega do criador **só começa a correr quando ele confirma o recebimento**. A segunda opção abre item na caixa de entrada do operador.

### 2.6 Dinheiro

| # | Função | Prio |
|---|---|---|
| 38 | Carteira: protegido · aguardando prazo · disponível | E |
| 39 | Extrato com a origem de cada valor | E |
| 40 | Cadastrar e trocar conta bancária — **aviso vai para o e-mail ANTERIOR**, e o repasse automático tem carência de 24 h | E |
| 41 | Sacar fora do ciclo automático, com a tarifa exibida antes | E |
| 42 | Ver o motivo da recusa do provedor e reenviar documento | E |
| 43 | Cadastro fiscal, com aviso sobre formalização | E |
| 44 | Agenda de recebíveis: valor bruto, deduções discriminadas e recebível constituído | E |
| 45 | Contratos que gravam a agenda: contraparte, valores alcançados, natureza e valor | E |
| 46 | Contestar efeito de contrato sobre a agenda | E |

**O repasse é automático.** Todo dia útil, saldo disponível acima de R$ 50 é transferido sozinho, com a tarifa por conta da plataforma. A função 41 existe para quem quer antes do ciclo.

**As funções 44 a 46 são exigência do Banco Central** (Resolução 264/349) e valem para criador e marca.

---

## 3. Marca

### 3.1 Encontrar

| # | Função | Prio |
|---|---|---|
| 47 | Busca de criadores | E |
| 48 | Filtros: categoria, orçamento, região, modalidade, público | E |
| 49 | Perfil completo do criador | E |

### 3.2 Contratar

| # | Função | Prio |
|---|---|---|
| 50 | Contratar da vitrine, com formulário curto | E |
| 51 | Proposta direta, com formulário completo | E |
| 52 | Publicar pedido aberto | E |
| 53 | Ver candidaturas | E |
| 54 | Contratar vários criadores no mesmo pedido | E |

### 3.3 Acompanhar

| # | Função | Prio |
|---|---|---|
| 55 | O que precisa da minha decisão hoje | E |
| 56 | Campanhas em andamento | E |
| 57 | Alerta de prazo de aprovação vencendo | E |
| 58 | Contrato com marcos e estados | E |
| 59 | Aprovar entrega | E |
| 60 | Pedir ajuste referenciado ao ponto exato do briefing | E |
| 61 | Lançar código de rastreio do produto enviado | E |
| 62 | Cancelar dentro da janela | E |

### 3.4 Pagar

| # | Função | Prio |
|---|---|---|
| 63 | Pix, boleto e cartão | E |
| 64 | Simulador de parcelamento: mostra valor da parcela e total **antes** de escolher | E |
| 65 | Conta empresarial verificada, com envio de documentos da empresa | E |
| 66 | Fatura INFLUENTZ: pró-forma e boleto com vencimento acordado | E |
| 67 | Notas fiscais e recibos | E |
| 68 | Baixar a nota do criador dentro do contrato | E |
| 69 | Dados de reembolso — **só para boleto e para Pix fora de 90 dias** | E |

**Sobre a 65 e a 66 — a rota do cliente grande.** Empresa grande no Brasil paga fornecedor por boleto contra nota fiscal, dentro do contas-a-pagar. **Pix e boleto nunca têm teto.** A conta verificada existe para que uma empresa legítima entre com limite alto no cartão **no primeiro dia, sem precisar construir histórico**.

### 3.5 Identidade da marca

| # | Função | Prio |
|---|---|---|
| 70 | Perfil público da marca: nome, logo, segmento, site, histórico e nota recebida | E |

O criador precisa saber quem está contratando ele antes de aceitar.

---

## 4. Comunicação, contrato e avaliação

| # | Função | Prio |
|---|---|---|
| 71 | Chat, liberado só depois do pagamento | E |
| 72 | Termos de Uso versionados, com registro de qual versão cada um aceitou, quando e de onde | E |
| 73 | Contrato em PDF para as duas pontas | E |
| 74 | Avaliar a outra ponta ao fim do contrato: nota e comentário, nos dois sentidos | E |
| 75 | Publicação simultânea às cegas: nenhum lado vê a nota do outro antes de enviar a sua | E |

**Sobre a 75.** Sem isso, quem avalia primeiro fica refém de retaliação. É como Airbnb e Upwork fazem.

---

## 5. Quando dá problema

| # | Função | Prio |
|---|---|---|
| 76 | Abrir disputa (criador e marca) | E |
| 77 | Enviar evidência | E |
| 78 | Ver o que a outra parte alegou | E |
| 79 | Acompanhar o andamento e o prazo | E |
| 80 | Mediar disputa com as evidências das duas partes | E |
| 81 | Liberar, reter ou estornar valor | E |

---

## 6. Administração

| # | Função | Prio |
|---|---|---|
| 82 | Buscar usuário e ver histórico completo | E |
| 83 | Suspender ou banir, com motivo registrado | E |
| 84 | Registro de auditoria imutável | E |
| 85 | Consulta a listas restritivas no cadastro e antes de contrato de valor alto. Restrição interna é por **sócio, não por CNPJ**, e por vários atributos — sempre como sinal, nunca como bloqueio automático | E |
| 86 | Reconciliação de pagamento: reconsultar o provedor e destravar o contrato | E |
| 87 | Teto de exposição por cobrança no cartão, com degraus por histórico e por verificação | E |
| 88 | **Caixa de entrada do operador** | E |
| 89 | **Painel do dono** | E |

### A caixa de entrada (88)

É a única tela do administrativo que abre todo dia. Uma lista, com origem, prazo e link para o objeto. Caem nela:

verificação manual de contrato · reembolso que falhou · denúncia · **o prazo de defesa de contestação, que é de 10 dias e é fatal** · cobrança acima do limite pedindo análise · alerta de contrato entre partes relacionadas · resultado de lista restritiva · produto extraviado · publicação removida antes do prazo · chamado de suporte.

Cada item tem duas ações: **resolver** ou **recusar com motivo**.

### O painel do dono (89)

Seis números. Sem gráfico, sem filtro.

1. Faturamento do mês e comissão do mês
2. Contratos por estado, com **quantos estão parados e há quantos dias**
3. **Criadores prontos** — perfil, rede conectada e item publicado — sobre criadores cadastrados
4. Marcas que contrataram ao menos uma vez, sobre marcas cadastradas
5. **Contratos entre par que se repete** — a medida de que a plataforma tem retenção, e não só novidade
6. Travados: cadastro recusado, reembolso com falha, disputa aberta

### Sobre o administrativo, de forma geral

**A equipe é uma pessoa.** Não existem quatro papéis de administrador, cinco filas separadas nem painel de conciliação: existe uma caixa de entrada e uma busca. O papel fica modelado no banco para crescer sem reescrever; a tela nasce quando existir a segunda pessoa.

---

## 7. Regras que valem para o produto inteiro

1. **Uma ação óbvia por contexto.** Tela com cinco botões iguais é tela onde ninguém decide.
2. **Linguagem clara antes de linguagem esperta.**
3. **Dinheiro, direitos e permissão falham fechado.** Na dúvida, o sistema nega e pede revisão humana.
4. **Toda métrica mostra de onde veio, de quando é e o que não cobre.**
5. **Dado que falta nunca vira zero.**
6. **Todo estado tem saída.** Nenhuma tela deixa alguém parado sem botão.
7. **O criador nunca espera mais do que o prazo do meio de pagamento.**
8. **Nenhum valor aparece só no fim.** Preço final, taxa e prazo aparecem antes da decisão.

---

## 8. Ordem de construção

**Fatia 1 — o ciclo completo, remoto, vitrine, um marco, Pix.** É a fatia que prova que a plataforma funciona de ponta a ponta.

> criador se cadastra → conecta rede → monta vitrine → marca busca → contrata → paga → criador entrega → publica → marca aprova → criador recebe → os dois se avaliam

Funções: 1–16, 18–22, 24–36, 38–40, 42, 47–51, 55, 58–60, 63, 67, 70–76, 80–84, 86, 88, 89.

**Fatia 2 — pedido aberto e produto físico.** 31, 37, 52–54, 61, 68, 69.

**Fatia 3 — cartão, conta empresarial e cliente grande.** 41, 43–46, 62, 64–66, 85, 87.

**Depois do v1:** agência, contrato recorrente, trabalho presencial, marcos múltiplos, comparador lado a lado, aditivo de escopo, entrar com Google e Apple, autenticação em duas etapas, seletor de espaço de trabalho.

---

## 9. O que depende de profissional humano

A lista completa e atualizada está na **SPEC §15**. Em resumo: **contador** antes do código de pagamento, **advogado** antes do lançamento.

---

*Inventário de produto. Não é parecer jurídico nem contábil. O histórico de como cada decisão chegou aqui está em `docs/HISTORICO.md`.*
