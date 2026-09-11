# COBERTURA DE TESTE — FATIA 1

> Decisão do `qa-estrategia`, sobre os 68 critérios de `ACEITE-FATIA-1.md`.
> O que testar e quanto, antes do código existir. Critério aplicado (definido
> no próprio `.claude/agents/qa-estrategia.md`): dinheiro/dado sensível →
> automatizado sempre; só UI → manual no 1º ciclo; terceiro → contrato de
> sandbox; regra com "cliente bom" documentado → caso nomeado com esse cliente.

## Tabela de cobertura

| # / função | Categoria | Cobertura | Motivo |
|---|---|---|---|
| 1 — Cadastro e-mail/senha | UI/estado de conta | Manual 1º ciclo | Não move dinheiro nem dado sensível |
| 2 — Verificação de e-mail | Dado sensível | Automatizado obrigatório | Gate que bloqueia ação com razão — precisa de prova, não só UI |
| 3 — Escolha de papel (irreversível) | Estado permanente | Automatizado obrigatório | Sem volta; erro vira migração de banco, não correção de tela |
| 4 — Recuperação de senha | Dado sensível | Automatizado obrigatório | Token com validade/invalidação — falha é conta sequestrável |
| 5 — Verificação de identidade | Integração terceiro + dado sensível | Contrato de sandbox | Resposta do Pagar.me muda; mock esconde mudança de contrato KYC |
| 6 — Verificação de CNPJ | Integração terceiro + dinheiro | Contrato de sandbox | Destrava teto de R$ 15.000 — efeito financeiro direto |
| 7 — Encerrar conta / baixar dados | Dado sensível | Automatizado obrigatório | Exceção "contrato/disputa ativa bloqueia" quebra silencioso em refactor |
| 8 — Aceite de Termos do titular | Cliente-bom + jurídico | Automatizado obrigatório | Operador tentando aceitar em nome de terceiro tem que ser estruturalmente impossível |
| 9 — Conta conectada e data | UI | Manual 1º ciclo | Só exibição de dado já validado |
| 10 — Desconectar rede | Dado (token) | Automatizado obrigatório | Revogação é ação de segurança; regra de selo histórico é contraintuitiva |
| 11 — Selo "via API · data" | UI | Manual 1º ciclo → automatiza ao repetir | Vale snapshot na 2ª superfície que usar o componente |
| 12 — Renovação automática de token | Dado sensível | Automatizado obrigatório | Cliente-bom: token cai durante negociação de contrato em andamento |
| 13 — Central de notificações | UI | Manual 1º ciclo | Lista sem dinheiro envolvido |
| 14 — E-mail para evento crítico | Dado sensível | Automatizado obrigatório | Cliente-bom: push desligado + pagamento liberado — e-mail é a única via |
| 15 — Push em até 1 min | Integração terceiro | Contrato de sandbox | Depende do provedor de push; nunca medir latência exata em CI |
| 16 — Marcador de não lido | UI | Manual 1º ciclo | Contador de tela |
| 18 — Suporte com contexto automático | UI/operacional | Manual → automatiza ao repetir | Erro atrasa mediação, mas não move dinheiro direto |
| 19 — Montar perfil | Regra de visibilidade | Automatizado obrigatório | Cliente-bom: falta 1 campo — a tela tem que dizer qual, não "incompleto" |
| 20 — Modalidade (remoto/presencial/híbrido) | Decide qual máquina roda | Automatizado obrigatório | Erro manda presencial pela trilha de API, que não existe fisicamente |
| 21 — Item de vitrine (piso R$ 150) | Dinheiro | Automatizado obrigatório | Cliente-bom: bloqueio na digitação, não editável depois disfarçado |
| 22 — Pausar/arquivar + reativação por data | Job agendado | Automatizado obrigatório | Reativação sem gatilho manual falha silencioso sem teste |
| 24 — Nota e histórico (exclui cancelado/disputa) | Confiança/venda | Automatizado obrigatório | Cliente-bom: disputa perdida não pode contaminar nota nem contagem |
| 25 — Resumo do dia (criador) | UI | Manual 1º ciclo | Priorização de exibição |
| 26 — Calendário do criador | UI | Manual 1º ciclo | Exibição de datas existentes |
| 27 — Clicar no dia abre contratos | UI | Manual 1º ciclo | Navegação |
| 28 — Marcos automáticos no calendário | Criação automática | Automatizado obrigatório | Marco que não aparece = prazo perdido sem culpa do criador |
| 29 — Propostas recebidas | UI/estado | Manual 1º ciclo | Exibição de estado já gravado |
| 30 — Aceitar/recusar/ajustar proposta | Pré-dinheiro | Automatizado obrigatório | Fronteira exata onde proposta vira contrato |
| 31 — Candidatar-se sem duplicar | Integridade | Automatizado obrigatório | Cliente-bom: duplo clique não pode gerar candidatura dupla |
| 32 — Meus contratos por estado | UI | Manual → automatiza ao repetir | Snapshot quando a lista de estados estabilizar |
| 33 — Enviar entrega | Transição + notificação crítica | Automatizado obrigatório | Inicia o relógio de aprovação/liberação (função 59) |
| 34 — Ver ajuste referenciado | UI | Manual 1º ciclo | Exibição vinculada |
| 35 — Identificação publicitária + uso de IA | Cláusula jurídica | Automatizado obrigatório | Bloqueio de compliance — vazar é passivo da plataforma |
| 36 — Confirmar entrega por tipo P1–P4 | Validação por formato | Automatizado obrigatório | Cliente-bom: presencial não pode ser aceito por link colado |
| 38 — Recebimentos: bloqueado→aguardando→disponível | Dinheiro | Automatizado obrigatório | Liberação de escrow, sem exceção |
| 39 — Extrato com origem | Dinheiro/rastreabilidade | Automatizado obrigatório | Erro de rastreio é motivo de disputa e obrigação BCB |
| 40 — Trocar conta bancária | Dinheiro + antifraude | Automatizado obrigatório | Cliente-bom: aviso ao e-mail anterior é a trava contra golpe de conta invadida |
| 42 — Motivo de recusa + reenvio | Integração terceiro | Contrato de sandbox | Texto vem do Pagar.me e muda por versão de doc |
| 44 — Agenda de recebíveis | Dinheiro + lei (BCB) | Automatizado obrigatório | Obrigação vencida — nunca número único sem composição |
| 45 — Contratos que gravam a agenda | Dinheiro/auditoria | Automatizado obrigatório | Sem rastreabilidade não sobrevive a fiscalização |
| 47 — Busca de criadores | UI/listagem | Manual → automatiza ao repetir | Automatiza quando o catálogo crescer |
| 48 — Filtros combinados (E lógico) | Regra de negócio | Automatizado obrigatório | Cliente-bom: "OU" silencioso em vez de "E" é bug clássico |
| 49 — Perfil completo do criador | UI | Manual 1º ciclo | Agregação de dados já testados em 19/24 |
| 50 — Contratar da vitrine | Dinheiro (nasce contrato) | Automatizado obrigatório | Preço/prazo têm que congelar exatamente como no item |
| 51 — Proposta direta (não vira contrato sozinha) | Regra de estado | Automatizado obrigatório | Cliente-bom: proteção do criador contra cobrança sem aceite |
| 55 — Painel do dia da marca | UI | Manual 1º ciclo | Priorização de exibição |
| 58 — Contrato com marcos e estados | Consulta de estado | Automatizado obrigatório | Erro aqui erra decisão de mediação de disputa |
| 59 — Aprovar entrega (+ automática em 7 dias) | Dinheiro | Automatizado obrigatório | Cliente-bom: marca ausente não pode travar pagamento de quem entregou certo |
| 60 — Pedir ajuste referenciado (bloqueia sem referência) | Integridade de disputa | Automatizado obrigatório | É a prova que evita a fatia de disputas por confusão de escopo (MAQUINA §12) |
| 62 — Cancelar dentro da janela | Dinheiro | Automatizado obrigatório | Janela numérica exata (7d/48h) precisa de teste de limite |
| 63 — Checkout Pix/boleto/cartão | Dinheiro + terceiro | Contrato de sandbox + automatizado na regra "nunca manual" | Os dois juntos: sandbox para o formato real, automatizado para a regra de negócio |
| 67 — Notas fiscais e recibos | Dado fiscal | Automatizado obrigatório | Indisponibilidade é passivo tributário dos dois lados |
| 70 — Perfil público da marca | UI | Manual 1º ciclo | Exibição institucional |
| 71 — Chat liberado só após pagamento | Dado sensível/acesso | Automatizado obrigatório | Gate amarrado a dinheiro — vazar antes é "combinei por fora" |
| 72 — Termos versionados | Jurídico | Automatizado obrigatório | Prova de aceite em eventual disputa judicial |
| 73 — Contrato em PDF idêntico | Jurídico | Automatizado obrigatório | Cliente-bom: divergência de valor vira disputa contratual |
| 74 — Avaliar a outra ponta | Regra de estado | Automatizado obrigatório | Mesmo padrão de risco da função 75 |
| 75 — Publicação simultânea às cegas | Integridade | Automatizado obrigatório | Vazamento antes da hora muda o comportamento da 2ª parte |
| 76 — Abrir disputa (congela dinheiro) | Dinheiro | Automatizado obrigatório | Transição mais sensível da máquina — ⚠️ ver lacuna 3 |
| 80 — Mediar com evidências lado a lado | UI operacional | Manual → automatiza ao repetir | Decisão em si é a função 81, não esta |
| 81 — Liberar/reter/estornar | Dinheiro | Automatizado obrigatório | "Exatamente uma ação" tem que estar travado em código |
| 82 — Buscar usuário e histórico | Dado sensível | Automatizado obrigatório | Acesso a CPF/CNPJ só por operador autorizado |
| 83 — Suspender/banir | Dado sensível + dinheiro indireto | Automatizado obrigatório | Cliente-bom: marca banida não pode travar dinheiro do criador em contrato ativo |
| 84 — Registro de auditoria imutável | Jurídico | Automatizado obrigatório | Ausência de editar/apagar só se prova testando que falha |
| 86 — Reconciliação de pagamento | Dinheiro + terceiro | Contrato de sandbox | Depende do comportamento real de webhook perdido do Pagar.me |
| 88 — Caixa de entrada do operador | UI operacional | Manual → automatiza ao repetir | Agrega itens de funções já cobertas |
| 89 — Painel do dono | UI/dado agregado | Manual → automatiza ao repetir | Leitura; fonte de dados já coberta em outras funções |
| 92 — Prazo vencido: cancelar ou disputa | Dinheiro | Automatizado obrigatório | Cliente-bom: desvio para disputa é a proteção do criador que contesta |

## Nunca automatizar nesta fatia
- Pixel a pixel de qualquer tela (1, 9, 11, 13, 16, 25–27, 29, 32, 34, 47, 49, 55, 70, 80, 88, 89) — design ainda muda, cobertura visual não prova regra de negócio.
- Cobertura duplicada do selo "via API" (função 11) em cada tela — um snapshot no componente central substitui N testes idênticos.
- Suíte E2E cobrindo os 68 critérios em sequência única — mais lenta que a fatia levou para ser codada. E2E reservado a 2–3 jornadas completas (contratar→pagar→entregar→aprovar→liberar; abrir disputa→mediar→resolver).
- Latência exata do push (função 15) além do contrato de sandbox — isso é observabilidade em produção, não teste automatizado.

## Resumo
- **Automatizado obrigatório:** 44 funções
- **Contrato de sandbox:** 6 funções (5, 6, 15, 42, 63 parcial, 86)
- **Manual no 1º ciclo (parte automatiza ao repetir):** 18 funções

---

## ✅ As três lacunas foram fechadas (11/09)

O `qa-estrategia` identificou três pontos onde a documentação não permitia fechar a cobertura. O `arquiteto-tecnico` fechou os três em `MAQUINA-DE-ESTADOS.md` §3.2, §9.4 e §10.0 — e os critérios de aceite das funções 42, 63, 76, 86 e 88 foram atualizados em `ACEITE-FATIA-1.md`.

**O que isso muda na cobertura acima:** nada de categoria. As três continuam onde estavam (42 e 63 em contrato de sandbox, 76 em automatizado obrigatório) — o que mudou é que agora **existe caso de teste fechado** para cada uma, em vez de uma decisão de cobertura sem alvo. O contrato de sandbox da 42 passa a ter que cobrir os seis pares `status`/`status_reason` do provedor.
