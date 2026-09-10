# HISTÓRICO DE DECISÕES E CORREÇÕES

> **Este arquivo existe para o registro, não para leitura.**
> Ele guarda o que mudou, quando e por quê — para que ninguém reabra uma discussão já resolvida, e para que quem entrar depois entenda a forma atual do produto.
>
> **O Marco não precisa ler este arquivo.** Os documentos de produto são a verdade atual; este é o rastro.

---

## 08/09/2026 — a sessão de correção

Um dia inteiro de auditoria. Sete correções estruturais, o produto reduzido pela metade, e três defeitos de método corrigidos. O que segue é o registro honesto, incluindo os erros que eu cometi.

### O ciclo do serviço não estava desenhado

**O erro:** o produto liberava o dinheiro contra um **arquivo aprovado**. O que a marca compra é uma **publicação no ar, no perfil do criador, que permanece por um tempo**. São coisas diferentes.

Na prática, o criador podia receber sem publicar, publicar e apagar no dia seguinte, ou publicar sem marcar parceria paga. Na disputa, a plataforma não tinha prova de nada — o escrow protegia o objeto errado.

**A correção:** nasce o estado `publicado`, conferido pela API da rede que o criador já conectou, e o campo **permanência mínima** (padrão 90 dias), que não existia em documento nenhum.

### O produto era grande demais para ser construído

**O erro:** o inventário foi de 128 para 177 funções e **nunca diminuiu uma única vez.** O time de especialistas nasceu torto — `produto` caça lacuna, `financeiro` caça risco de dinheiro, `juridico-br` caça risco legal, `design` caça inconsistência: **os quatro só sabiam acrescentar.**

Quem percebeu foi o Marco, com uma pergunta de três linhas sobre um sistema de convites que eu tinha inventado: *"pra que esse trem? So mandar baixar ou acessar via web e ele mesmo cadastrar."* Cinco funções morreram na hora. Elas nunca deveriam ter nascido — eu li na SPEC que ele chamaria os 50 primeiros criadores pessoalmente e **deduzi sozinho** que isso exigia funcionalidade.

**A correção:** nasce o especialista `cortador`, a única voz autorizada a deletar. Resultado da auditoria dele: **38 funções mortas, 22 que eram a mesma coisa contada duas vezes, 23 módulos adiados.** De 170 sobraram 97.

E o achado que justifica ele existir: **não existia função de avaliação.** O último passo do fluxo principal, com máquina de estados própria, não tinha número — enquanto tinha sido criado um gerador automático de defesa de contestação para um evento que acontece uma vez a cada 20 meses. Também não existia perfil da marca.

### As decisões defensivas não tinham sido testadas contra o cliente bom

**O erro:** o teto de R$ 2.500 por cobrança no cartão foi derivado corretamente do risco de fraude — e impediria uma empresa grande de contratar R$ 30.000. A mesma lógica escreveu "3D Secure obrigatório em 100% das cobranças", que **recusaria o cartão corporativo**, porque cartão comercial cai em isenção de autenticação.

**A correção:** o teto passa a ser só do cartão (Pix e boleto nunca tiveram), nasce a conta empresarial verificada que entra em R$ 15.000 no primeiro dia, e nasce a Fatura INFLUENTZ — pró-forma e boleto com vencimento, que é como empresa grande realmente paga e que tem exposição zero a contestação.

**Regra criada:** toda decisão de regra precisa responder **duas** perguntas — o que protege, e o que quebra para um cliente legítimo.

### A reserva de 90 dias e a verificação manual de rede

**O erro:** eu tinha escrito duas soluções que eram a opção mais fácil disfarçada de decisão. Verificação manual de rede social por captura de tela, porque a aprovação da API demora; e reserva de 90 dias do dinheiro do criador, porque a contestação de cartão pode chegar depois do saque.

O Marco recusou as duas, e a pesquisa provou que ele estava certo por um motivo que eu não tinha visto: **a reserva de 90 dias nem protegia** — a janela de contestação por serviço não recebido conta 120 dias a partir da data prevista de entrega, então a reserva fecharia antes de o risco acabar.

**A correção:** métrica só por API oficial, usando os mecanismos de piloto que as três redes já oferecem (50 criadores no Instagram e no TikTok, ilimitado no YouTube, sem empresa verificada). E proteção contra contestação em camadas, nenhuma delas retendo dinheiro do criador.

### O parcelamento pagava o criador em prestações

**O erro, que estava na especificação sem ninguém notar:** "cartão = D+30" estava escrito como se fosse uma linha só. **No parcelado, o provedor libera uma parcela por mês.** Uma marca parcelando em 6× um contrato de R$ 6.000 faria o criador entregar tudo e receber R$ 1.000 por mês durante meio ano.

**A correção:** quem parcela paga os juros (1,99% ao mês), e esses juros financiam a antecipação que dá **data única** ao criador. A conta fecha e ainda sobra cerca de um ponto percentual. O criador nunca paga, a plataforma nunca absorve.

### A exigência de MEI empurrava o criador para irregularidade

**O erro:** a especificação exigia MEI do criador acima de R$ 500 acumulados, com "guia embutido porque abrir MEI é grátis". **Não existe ocupação de influenciador digital na lista do MEI.** O guia estaria induzindo o criador a um desenquadramento retroativo com multa de até 70%.

**A correção:** o criador recebe como pessoa física; a plataforma avisa sobre formalização e **não bloqueia o saque**. Bloquear dinheiro já ganho por regra que a plataforma inventou é exposição, não proteção.

### Becos sem saída encontrados na caminhada end-to-end

- **Aviso do provedor perdido** deixava o contrato parado com dinheiro dentro, e ninguém — nem marca, nem criador, nem operador — tinha ação possível. Nasce a reconciliação de pagamento.
- **`aguardando_revisao_manual`** tinha entrada, não tinha quem a empurrasse e não tinha saída negativa.
- **Cadastro recusado em definitivo** pelo provedor: o dinheiro ficaria retido para sempre. Agora volta à marca por estorno, sem culpa do criador.
- **Produto extraviado** tinha sido cortado por engano junto com o trabalho presencial — extravio é dos Correios, não de evento.
- **Prévia sem marca d'água** exigia a mesma transcodificação que o corte disse ser cara. Resolvido exigindo arquivo de revisão em MP4, que o criador exporta de qualquer jeito.

### Correções jurídicas

- **Cadastro assistido** — um operador aceitar os Termos no lugar do criador não forma contrato, e contamina a prova de **todos** os outros aceites. Eliminado.
- **Aceite de Termos é sempre do próprio titular**, e dado bancário nunca entra por mão de operador.
- **Alvará judicial** para criador menor de idade: exigência do ECA que nenhuma plataforma consegue emitir. Criador tem 18 anos completos no v1.

### Regulação que faltava

- **Resolução BCB 264/349**, com prazo vencido desde 01/04/2024: a agenda de recebíveis é obrigação **do marketplace**, não do provedor.
- **A invariante que mantém a plataforma fora do Banco Central:** não existe carteira da INFLUENTZ. O painel administrativo autoriza; não transfere.
- **Trilha de auditoria** com encadeamento por hash e prazos de retenção definidos — barata no dia 1, impossível de acrescentar depois.

---

## As três correções de método

Não foram correções de produto, e são as mais importantes.

**1. O protocolo de decisão.** O método dizia que decisão de dono era *"gosto, prioridade e apetite de risco"* — e a expressão "apetite de risco" virou porta dos fundos: todo parâmetro numérico que eu não queria escolher saía por ela com carimbo de decisão de dono. Não era. **Se um número tem referência de mercado, eu escolho o número e informo.** O que sobe para o Marco é curto de propósito: dinheiro do bolso dele, a lista de contatos dele, gosto de marca, quando lançar, e matar ou manter uma funcionalidade inteira.

**2. A pergunta antes de qualquer função nova.** *"O que acontece se isso não existir?"* Se a resposta for "quase nada", a função não existe. **Descrição não é pedido:** a especificação descrever uma situação não autoriza inventar funcionalidade para ela.

**3. O teste do cliente bom.** Toda regra defensiva responde o que protege **e** o que quebra para um cliente legítimo. Decisão defensiva não testada contra o melhor cliente possível não é decisão — é medo com número.

---

## Ferramentas avaliadas e recusadas

| O quê | Veredito | Motivo |
|---|---|---|
| **Stripe** | Recusada | Pix só por convite, teto de 3.000 dólares por transação, e sem parcelamento no Brasil. Um contrato de R$ 30.000 no Pix é impossível |
| **Obsidian** como segundo cérebro | Recusado | Roda no computador local; o desenvolvimento é na nuvem, então o cofre não seria acessível. E criaria uma segunda fonte de verdade. Este repositório já cumpre o papel, com histórico versionado |
| **Raspagem de dados** de redes sociais | Recusada | Viola os termos das plataformas e a regra de métrica só por API |
| **App sob CNPJ de terceiro** | Recusado | Quem é dono do app responde pelos dados, e o app com os acessos de todos os criadores viraria ativo de outra pessoa |
| **MEI** para a INFLUENTZ | Recusado | Intermediação de negócios não está na lista de ocupações do MEI. Formato: SLU |
| **Garantia de chargeback** contratada | Recusada no v1 | Cobre só fraude, e a rota do boleto elimina o risco de graça |
| **Faturar depois da entrega (net 30)** | Fora do v1 | Só funciona com capital de giro; sem ele, ou a plataforma adianta dinheiro que não tem, ou o criador espera |

---

*Última atualização: 08/09/2026.*

## 09/09/2026 — A conta de infraestrutura, e uma afirmação minha que não se sustentou

**O gatilho.** Marco: *"Sobre custos de storage vc sempre Menciona uns valores mas isso é valor mensal? Anual? Por gigas? Pelo o que? Vc tem especialista em infra?"* Não tinha. Os números de custo vinham do especialista financeiro, que sabe de dinheiro e não de nuvem, e saíam sem unidade e sem período — o que é o mesmo que não sair. Criado o especialista `infra`, com regra número um: **todo número tem unidade e período.**

**O que a conta refeita mudou.** Lançamento de ≈R$ 262/mês para **R$ 312,35/mês**; operação de ≈R$ 1.320/mês para **R$ 1.836,48/mês** sem o agregador. A diferença são três custos que não estavam na conta: Apple Developer (US$ 99/ano), Google Play (US$ 25 uma vez) e **cópia de segurança fora do fornecedor principal**.

**O erro que precisou ser dito ao Marco.** Eu havia afirmado a ele, como fato, que o agregador de métricas tem plano gratuito de 250 contas monitoradas — e usei isso como argumento na decisão de arquitetura. A página oficial de preços **não publica número nenhum**, só oferece orçamento sob medida. A decisão do fornecedor continua certa pelos outros motivos; o que caiu foi o "R$ 0". Corrigido na SPEC §9.1.1.1 e comunicado no painel publicado.

**Três correções de produto vieram junto:** o relógio dos brutos contado do fechamento do contrato e não do envio (um contrato de três meses perderia os próprios brutos enquanto ainda estava aberto); a trava de exclusão para contrato ou disputa aberta; e a correção automática do índice interno do MP4, que é a diferença entre 2 segundos e 90 segundos até o primeiro quadro.

**Placar da entrega:** nenhuma função nova inventada. Três correções entraram, três custos entraram na conta, uma afirmação virou pergunta em aberto.

**O corte que veio depois.** O `cortador` reviu as quatro adições e achou o que eu não tinha visto: **duas funções entraram no projeto escondidas dentro de tabelas de custo**, sem passar pelo *"o que acontece se isso não existir?"* — a opção *"enviar só no Wi-Fi"* (que não é aviso, é fila persistente com envio em segundo plano e um estado novo de "enviou mas não chegou" no dia do prazo) e a **correção automática do MP4** (que não é verificação, é reprocessar 250 MB com fila, worker e caminho de falha próprio). Também caiu a estimativa de tempo restante — em 4G ela erra por um fator de quatro — e o painel no Admin de "GB apagados no mês passado", substituído pela rotina reportando cada execução ao monitoramento que já está pago. Réplica dos arquivos num segundo fornecedor foi adiada: o versionamento do R2 cobre o risco real, que é apagar por engano. **Placar final: 19 itens entraram, 3 cortados, 2 adiados, 14 ficam.** Além disso o cortador apontou uma violação da §2.4 — autocrítica dentro da SPEC §14.5.1 — corrigida na hora. **A lição registrada: documento de custo é lugar onde funcionalidade entra sem ser notada.**

---

# ANEXO — O encerramento do conflito com o Google Drive


> **Status: FECHADO. Não reabrir.**
>
> Este documento listava divergências entre os documentos deste repositório e um corpo de trabalho de produto que eu encontrei no Google Drive, em `INFLUENTZ / 00_CLEAN_ROOM_PRODUCT_ENGINEERING`.
>
> **O Marco decidiu, e a decisão é dele:** aquele material **não é fonte de verdade** e não deve ser considerado. Ele não reconhece a origem daquele documento e não confia nele.

---

## Regra permanente 🟢

**Do Google Drive, só a pasta `INFLUENTZ / MARKETING / BRANDING` entra no projeto.**

Ela contém a identidade visual — logotipo, símbolo, ícones, avatares, padrões, guia da marca, fotos. Está integralmente espelhada em `docs/marca/`.

**Todo o resto do Drive fica fora**, inclusive:
- `00_CLEAN_ROOM_PRODUCT_ENGINEERING` e tudo dentro dele
- documentos soltos de produto, jurídico e financeiro na raiz de `INFLUENTZ`

**Fonte de verdade do produto é este repositório.** Se algo importante for decidido, é aqui que entra.

---

## O que eu levei daquele material, e por quê

⚠️ **Registro honesto, porque seria desonesto fingir que não li.**

Algumas ideias que estavam lá são boas **por mérito próprio** — e eu as adotei como recomendação minha, avaliadas de novo do zero, sem tratar aquele documento como autoridade. Elas estão hoje no `FEATURE-MATRIX.md` sob minha responsabilidade:

| Ideia | Por que eu adotaria de qualquer forma |
|---|---|
| Múltiplos espaços de trabalho por pessoa | O dono de agência também é criador. Sem isso, três logins |
| Dado ausente nunca exibido como zero | Criador novo com "0 contratos" parece ruim; "primeiro contrato" é honesto |
| Toda métrica com origem, período e limitação | É exatamente a dúvida que o Marco teve no comparador |
| Nenhuma ordenação sem explicação | Ranking oculto destrói confiança de marketplace |
| IA assiste; humano e regra decidem o que é sensível | IA não pode liberar dinheiro nem julgar disputa |

**O que eu não trouxe:** nada que contrariasse a SPEC sem o Marco ter decidido. As divergências que aquele material criava (conteúdo adulto, cadastro fiscal, provedor de pagamento) ficam **como estão na nossa SPEC**, que é a fonte de verdade.

---

## Duas ideias que ficaram de fora e eu recomendo discutir um dia 🔵

Não por causa do Drive — por mérito. Registro para não se perderem:

1. **Serviços recorrentes.** Contrato mensal com ciclos independentes. É o que transforma trabalho pontual em receita previsível, para o criador e para a plataforma. Não cabe no v1, mas muda a máquina de estados quando entrar.
2. **Criadores virtuais / gerados por IA.** É uma categoria que existe e cresce. Ser a plataforma que a regula com rótulo obrigatório e operador humano verificado — em vez de fingir que não existe — é posicionamento defensável.

Nenhuma das duas está no escopo atual. Ficam aqui como memória.

## 10/09/2026 — A entrega pela metade, e o portão que fecha isso

**O gatilho, palavra do Marco:** *"Percebe que novamente eu que to tentando achar sempre algo? … so retorne quando tiver tudo q precisa."* Ele listou o que faltava — ponto de equilíbrio, valor mínimo de proposta, custo do repasse e quem paga, quem tem carteira, onde cai o estorno — e todos os cinco eram consequência direta de eu ter entregado **metade de um assunto**: o custo de operar sem a receita que o cobre.

**O diagnóstico.** O portão do §5.1 revisava o pedaço; **ninguém verificava o todo antes de entregar.** Criado o portão do `METODO-DE-TRABALHO.md` §9, com nove perguntas, das quais a primeira é a que mais falhou: *o assunto está inteiro, ou é uma fatia?*

**A pergunta dele — "não tem especialista pra isso? precisa de mais especialistas?" — merece a resposta honesta: não.** O `financeiro` existia e nunca tinha sido perguntado sobre o modelo de operação. Criar um especialista novo teria sido a resposta fácil para um problema de processo. **O que faltava era o portão, não mais gente.**

**O que a rodada produziu:** o `financeiro` achou que a frase *"20 contratos por mês pagam o conjunto em qualquer cenário"* estava errada — foi calculada sem imposto, sem tarifa de repasse, sem taxa do meio de pagamento e sem fundo. A 7,5% de comissão de lançamento o equilíbrio era 25 contratos/mês, **acima da própria meta**. Comissão de lançamento corrigida para 9,5% e piso de comissão efetiva de +3 para +5 pontos.

O `produto` varreu todos os documentos e devolveu **30 contradições** — a lista completa, de uma vez, para não aparecerem mais de surpresa. Entre elas, o inventário afirmava 98 funções, o painel 97, e a contagem real era 91.

O `arquiteto-produto` arbitrou as cinco que eram decisão de escopo e achou uma que ninguém tinha visto: **o fundo de contestação nascia com R$ 3.000 e o próprio piso dele era R$ 5.000** — lido ao pé da letra, o cartão não poderia existir no dia 1. Aporte corrigido.

O `infra` nomeou o fornecedor de métricas, que estava decidido pela metade, e **matou a maior bomba de custo do projeto**: a verificação de permanência chega por webhook, então as 90.000 consultas por mês nunca vão existir. E mostrou que eu vinha medindo a linha errada — **armazenamento é 2% do custo; o item caro sempre foi a métrica.**

## 10/09/2026 — Três correções por parar e ouvir de verdade

**O gatilho.** O dono pediu para eu parar antes de continuar, e listou o que estava errado com o processo: painel sem indicação de onde olhar, custos sem fonte, decisão de corte (presencial) sem propor solução antes, orçamento de métricas fora da realidade de uma startup sem CNPJ, e uma fatura de US$ 232 sem explicação. Confirmado, com a própria ferramenta de sessão: esta conversa gerou US$ 232,15 em uso — quase exatamente a fatura que ele recebeu — de rodar sete especialistas em Opus alto separadamente.

**Correção 1 — presencial volta ao v1.** Eu tinha cortado a modalidade citando a regra "dinheiro só libera com API confirmando publicação". O dono apontou a solução óbvia que eu não vi: confirmação bilateral dos dois lados, o mesmo padrão já usado em produto físico. Eu tinha confundido "não tem API" com "não tem como confirmar" — são coisas diferentes. Corrigido em MAQUINA §8.5.

**Correção 2 — fornecedor de métricas revertido de pago para gratuito.** A escolha anterior (Phyllo/Ayrshare, R$ 4.207 a R$ 34.339/mês) resolvia um problema de tempo de engenharia (três filas de aprovação) gastando um dinheiro que o dono não tem. Pesquisa confirmou: App Review da Meta é processo gratuito, TikTok e YouTube têm API oficial sem plano pago publicado, e o modo de teste de cada rede já cobre os 50 criadores sem CNPJ que já estavam na SPEC. O agregador pago vira otimização futura, não pré-requisito.

**Correção 3 — a tarifa de saque não pode ser "por conta da plataforma" por configuração.** Fonte oficial do Pagar.me: a taxa de saque é sempre debitada de quem transfere — o criador — sem opção de redirecionar via configuração. A forma real de a plataforma absorver o custo é embutir o valor no split no momento da transação, não por uma chave que não existe. Corrigida em SPEC §4.6.1.1, com a tela de extrato do criador (bloqueado/aguardando prazo/disponível/enviado) que faltava.

**Mudança de processo, permanente:** `/model opusplan` ativado — troca automática entre Opus (planejamento) e Sonnet (execução), sem precisar perguntar a cada resposta. E menos subagentes por rodada: pesquisa direta quando não precisa de uma "persona" especialista, evitando o padrão que gerou a fatura.

## 10/09/2026 (continuação) — O painel duplicava conteúdo, e a métrica precisava de linha do tempo

**O gatilho.** Depois de reorganizar o painel em três zonas fixas, o dono apontou que ficou "a mesma coisa, porém mais bagunçada" — e estava certo: a caixa nova do topo (🔴🟡🟢) tinha sido inserida sem remover a seção antiga equivalente mais abaixo, que ainda citava "duas decisões" quando já era uma só. E as três caixas eram só cor, sem link nenhum — ele pediu clique, não resumo.

**Corrigido:** removida a seção duplicada; a caixa vermelha do topo agora tem links reais (`<a href="#id">`) que pulam para a tela de contratar, para o pedido do fundo de contestação, e para a conta de dinheiro. A caixa amarela liga cada linha "antes → depois" à seção correspondente.

**E a métrica direta tinha um problema real de comunicação, não de decisão.** O dono perguntou: integração direta não exige CNPJ, infraestrutura e aprovação que pode demorar ou ser recusada? Sim — mas eu não tinha separado quando cada coisa acontece. Pesquisa confirmou, com fonte: modo de desenvolvimento da Meta e sandbox do TikTok (até 50 contas) não passam por revisão nenhuma — a aprovação só é necessária para crescer além disso, com receita entrando. A decisão de usar API direta continua certa; o que faltava era a linha do tempo, agora em SPEC §9.1.4 e no painel.

## 10/09/2026 (continuação 2) — O time de código, e a numeração de fases que se contradizia

**O gatilho.** O dono comparou o projeto a uma empresa de desenvolvimento com setor por setor trabalhando com excelência, e pediu pesquisa em repositórios públicos de devs e na documentação da Anthropic antes de continuar — e que eu trouxesse pronto o que precisa ser instalado, sem ele ter que adivinhar termos técnicos.

**O que a pesquisa confirmou:** a Anthropic não distribui pacote pronto de subagentes — o padrão é criar os próprios, exatamente o que já vínhamos fazendo. Dois repositórios públicos de qualidade (VoltAgent/awesome-claude-code-subagents, rohitg00/awesome-claude-code-toolkit) confirmaram o padrão de equipe de código de mercado. Criados quatro especialistas novos, só os que preenchiam lacuna real: `arquiteto-tecnico`, `qa-estrategia`, `devops`, `fullstack-dev` — `code-review` e `security-review` já existiam prontos, nativos, não precisaram ser recriados.

**Nenhuma instalação foi necessária do dono.** São arquivos de texto no repositório.

**E apareceu uma contradição real ao escrever isso:** `CLAUDE.md` §4 numerava a metodologia em 6 passos, `METODO-DE-TRABALHO.md` §2 numerava em 8 fases — para o mesmo processo. Corrigido: `METODO-DE-TRABALHO.md` §2 vira a única numeração oficial, e a tabela de estado das fases (que estava desatualizada, marcando Feature Matrix como "não feita" quando já existia em v3.2) foi atualizada para refletir a realidade.

**Também corrigido nesta rodada:** eu tinha afirmado que o seletor de modelo mostraria um texto fixo do modo `opusplan`. O print do dono mostrou "Sonnet 5" puro — errado da minha parte. O mecanismo (`opusplan`) está confirmado ativo via ferramenta de sessão; o chip visual mostra o modelo que realmente serviu aquele turno, não um rótulo do modo.
