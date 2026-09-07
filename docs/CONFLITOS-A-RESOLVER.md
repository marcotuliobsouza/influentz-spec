# Conflitos a resolver — repositório × Drive

> **O que aconteceu.** Ao varrer o Google Drive por inteiro, encontrei um corpo de trabalho de produto criado em **agosto de 2026** que eu nunca tinha lido: `INFLUENTZ / 00_CLEAN_ROOM_PRODUCT_ENGINEERING`. Ele contém uma **Constituição do Produto v0.2** e um **Registro de Decisões Aprovadas v1.0**, com decisões formalmente marcadas como APROVADAS.
>
> **O problema.** Existem hoje **duas fontes de verdade** que se contradizem: os documentos deste repositório (que eu escrevi) e os documentos do Drive (aprovados antes). Em pelo menos oito pontos elas dizem coisas diferentes.
>
> **A consequência.** Parte do que eu produzi nas últimas sessões contraria decisões que o Marco já tinha aprovado. Isso explica por que ele continuava encontrando ausências: eu estava construindo com metade da informação.
>
> ⚠️ **Nenhuma tela nova deve ser desenhada antes de resolver esta lista.**
>
> **Versão:** v1.0 · **Fonte no Drive:** `INFLUENTZ_Product_Constitution_v0.2.md`, `INFLUENTZ_Approved_Product_Decision_Register_v1.0.md`, `CURRENT_STATUS_v0.3.md`

---

## Como ler esta lista

Cada conflito traz: o que o Drive diz (aprovado), o que o nosso repositório diz, e **minha recomendação técnica**. O Marco decide.

---

## 1. 🔴 Conteúdo adulto — as duas fontes dizem o oposto

| Fonte | O que diz |
|---|---|
| **Drive** (Constituição §17, decisões TS-009/010/011) | INFLUENTZ **não é** um marketplace de conteúdo adulto. Pornografia e serviços sexuais **proibidos**. Só é permitido, com controle de idade e moderação: lingerie, moda praia, beleza, saúde sexual educativa, temas maduros editoriais |
| **Nosso repositório** (SPEC §8.3) | "Conteúdo adulto / sexshop — **permitido** com trava" |

**Recomendação: adotar a versão do Drive.** Não é só posição de marca — é viabilidade operacional. Regras de loja de aplicativos (Apple e Google) e de provedores de pagamento restringem categorias adultas, e uma plataforma que se posiciona ali arrisca ter o app removido e o processamento de pagamento cortado. A versão do Drive protege o negócio; a nossa expunha.

---

## 2. 🔴 Serviços recorrentes — não existem no nosso trabalho

| Fonte | O que diz |
|---|---|
| **Drive** (PF-004, APROVADO) | Serviços recorrentes nativos, com **ciclos financeiros independentes** |
| **Nosso repositório** | Não existe. Nem na SPEC, nem na máquina de estados, nem nas telas |

**Isto é grande.** Recorrência muda a máquina de estados inteira: cada ciclo tem financiamento, entrega, aprovação e repasse próprios; um ciclo com problema não pode travar o seguinte; e cancelamento passa a ter "cancelar o ciclo" e "cancelar o contrato" como coisas diferentes.

**Recomendação: adotar.** É o que transforma contrato pontual em receita previsível — para o criador e para a plataforma. Mas entra depois do ciclo simples funcionar.

---

## 3. 🔴 Criadores virtuais e de IA — não existem no nosso trabalho

| Fonte | O que diz |
|---|---|
| **Drive** (Constituição §16, aprovado) | Criadores virtuais/IA **permitidos**, com rótulo visível (`creator virtual`), operador humano verificado, e proibição de imitar pessoa real |
| **Nosso repositório** | Silêncio total |

**Recomendação: adotar, e tratar como diferencial.** Criador virtual é uma categoria em crescimento, e ser a plataforma que a regula com transparência — em vez de fingir que não existe — é posicionamento defensável. Exige: campo de tipo de perfil, selo visual, e a regra do §15 do Drive (dinheiro só vai para pessoa física ou jurídica verificada, nunca para uma persona sintética anônima).

---

## 4. 🔴 Múltiplos espaços de trabalho por identidade

| Fonte | O que diz |
|---|---|
| **Drive** (PF-002, APROVADO) | Uma mesma pessoa pode pertencer a vários espaços, com permissões distintas |
| **Nosso repositório** | Assume um papel por conta |

**Recomendação: adotar.** É a realidade: o dono de agência também é criador; o gerente de marketing atende três marcas. Sem isso, ele precisa de três logins — e a plataforma parece amadora. Muda a máquina de estados da conta (§3 de `MAQUINA-DE-ESTADOS.md`).

---

## 5. 🔴 Prioridade de plataforma — web para marca, celular para criador

| Fonte | O que diz |
|---|---|
| **Drive** (PF-005, APROVADO) | **Web** é prioridade para marcas e agências. **Celular** é prioridade para criadores |
| **Nosso trabalho** | Desenhei quase tudo em celular, inclusive as telas de marca |

**Este conflito eu já estava corrigindo sem saber:** fiz o Comparador em desktop porque ninguém compara cinco propostas no celular. Estava certo — e agora sei que é decisão aprovada, não intuição minha.

**Recomendação: adotar, e refazer o canvas por superfície.** As telas de marca viram web; as de criador continuam celular.

---

## 6. ⚠️ A palavra "escrow"

| Fonte | O que diz |
|---|---|
| **Drive** (Constituição §9) | "A plataforma **não** divulga uma estrutura de escrow jurídico não verificada" |
| **Nosso repositório** | Usa "escrow" em todo lugar, e a cor roxa **"Protegido"** do sistema de design foi criada especificamente para representá-lo |

**Este é sutil e sério.** "Escrow" tem significado jurídico específico. Anunciar escrow sem a estrutura jurídica correspondente é risco de propaganda enganosa e de enquadramento regulatório.

**Recomendação: manter o mecanismo, trocar a palavra.** O funcionamento não muda (dinheiro retido pelo provedor até a aprovação). O que muda é o nome na tela: **"pagamento protegido"** ou **"valor retido até a aprovação"** — descreve o fato sem invocar um instituto jurídico. A cor roxa continua; o rótulo muda. ⚠️ Confirmar com advogado.

---

## 7. ⚠️ Cadastro fiscal — MEI obrigatório ou caminho informal?

| Fonte | O que diz |
|---|---|
| **Drive** (`CURRENT_STATUS_v0.3`, ID-001 a ID-007 aprovados) | "Caminhos de **CPF/MEI/CNPJ e negócio informal**" |
| **Nosso repositório** (SPEC §4.7) | MEI ou CNPJ **obrigatório** acima de R$ 500 acumulados |

**Recomendação: adotar a versão do Drive, com escada.** Exigir MEI de largada exclui justamente o criador iniciante, que é a maioria no lançamento — e o cold start (SPEC §14.1) já é o maior risco do projeto. O caminho certo é progressivo: começa no CPF com limite baixo, e o sistema conduz ao MEI quando o volume justifica. ⚠️ O limite e a retenção precisam de contador.

---

## 8. ⚠️ Provedor de pagamento

| Fonte | O que diz |
|---|---|
| **Drive** (Constituição §9) | "Stripe/PSP move o dinheiro" |
| **Documento antigo** (`INFORMAÇÕES IMPORTANTES...`) | JUNO |
| **Nosso repositório** (SPEC §4.1) | **Pagar.me**, com pesquisa registrada |

**Recomendação: manter Pagar.me.** É a decisão mais recente e a única com pesquisa documentada (Stripe internacional não libera Pix por padrão para empresa brasileira nem parcela cartão). A menção a Stripe na Constituição é genérica ("Stripe/PSP"), não uma decisão fechada de fornecedor.

---

## 9. 🔵 Regras do Drive que eu deveria ter adotado desde o começo

Não são conflitos — são regras boas que estavam lá e eu não conhecia. **Adoto todas:**

| Regra (Constituição do Drive) | Por que importa |
|---|---|
| §10 — "Dado ausente **nunca** é exibido como zero" | Criador novo com "0 contratos" parece ruim; "primeiro contrato" é honesto |
| §10 — Toda métrica social mostra **origem, período, atualidade e limitação** | É exatamente a dúvida que o Marco teve no comparador |
| §7.14 — "Nenhum ranking oculto ou nota de mérito inexplicada" | A busca precisa explicar por que ordenou assim |
| §7.15 — Nenhuma função está pronta sem os estados **vazio, carregando, erro, offline, sucesso e auditoria** | É a diferença entre maquete e produto |
| §7.3 — **Uma** ação óbvia por contexto | Combate a tela cheia de botões |
| §8 — IA **assiste**; regras determinísticas e humanos controlam o que é sensível | IA não libera dinheiro, não suspende conta, não decide disputa |
| §7.6 — "Celular é intencional, não desktop espremido" | |

---

## 10. O que eu recomendo fazer, nesta ordem 🟢

1. **Marco decide os 8 pontos acima.** Sem isso, tudo que eu construir pode estar contrariando algo já aprovado.
2. **Reescrever a SPEC** absorvendo a Constituição do Drive — uma fonte de verdade só, neste repositório.
3. **Fazer a Feature Matrix** (Fase 2). É ela que garante que nada falta.
4. **Refazer o mapa de superfícies** (Fase 1): Brand Web, Creator App, Agency Web, Admin Web.
5. **Só então** voltar a desenhar telas.

⚠️ **Passos 1 e 2 não são burocracia.** São o que impede que o Marco continue encontrando buracos que eu deveria ter fechado.
