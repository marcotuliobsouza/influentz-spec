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
