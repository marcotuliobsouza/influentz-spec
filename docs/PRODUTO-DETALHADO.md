# Produto Detalhado — INFLUENTZ

> **Por que este documento existe.** A SPEC diz *o que* o produto faz. A Máquina de Estados diz *em que situação* cada coisa pode estar. Faltava a camada do meio: **quais campos, quais métricas, quais telas** — o nível em que um time de produto trabalha antes de desenhar.
>
> Ele nasceu de uma crítica do Marco que estava certa: os wireframes v1 mostravam **um** tipo de proposta, sem métricas de rede social e sem campos que qualquer campanha real precisa (a começar por "vai enviar produto?").
>
> **Versão:** v0.1
> **Base:** `SPEC-INFLUENTZ.md` v0.5, `MAQUINA-DE-ESTADOS.md` v0.2, `DESIGN-SYSTEM.md` v0.4
>
> **Legenda:** 🟢 definido · 🟡 em aberto · 🔵 proposta de Claude além do pedido · 🔴 lacuna encontrada · ⚠️ risco ou correção

---

## 0. Onde o projeto realmente está — resposta direta 🟢

**O que foi entregue até aqui é o esqueleto, não o produto.** Registrando sem rodeio, porque a pergunta foi feita:

| Etapa do desenho | Nome no mercado | Foi feito? |
|---|---|---|
| Estrutura: o que cabe em cada tela e em que ordem | **Wireframe** | ✅ v1, 9 telas |
| Aparência: cor, tipografia, foto, ícone, acabamento | **Design de alta fidelidade** | ❌ não |
| Telas que faltam (comparar candidaturas, painel, cadastro…) | **Inventário completo de telas** | ❌ não |
| Clicável, para testar o caminho | **Protótipo** | ❌ não |

⚠️ **Falha de comunicação minha, não de avaliação do Marco.** Wireframe é de propósito cru — ele existe para travar estrutura antes de gastar esforço em acabamento. Mas eu apresentei como se fosse a entrega da etapa 3 inteira, sem dizer que era o primeiro de três passos. Quem avalia não tinha como saber disso. Corrigido aqui.

**E uma segunda falha, mais grave:** eu desenhei o esqueleto **antes** de o produto estar completamente definido. A ordem certa é a que o `CLAUDE.md` §4 já manda — especificar, depois desenhar. Este documento fecha essa dívida antes de qualquer novo pixel.

---

## 1. Os três tipos de proposta 🔴

A SPEC §3 fala em "vitrine" e "pedido aberto". Na prática são **três** caminhos, e eles são diferentes o suficiente para exigir telas diferentes. Os wireframes v1 cobriram só o segundo.

| # | Nome | Quem define o preço | Quem procura quem |
|---|---|---|---|
| 1 | **Vitrine** (pré-cadastrada pelo criador) | Criador, com antecedência | Marca acha o criador |
| 2 | **Proposta direta** | Marca, na hora | Marca escolhe o criador |
| 3 | **Pedido aberto** (proposta publicada) | **Criador, ao se candidatar** | Criadores acham a marca |

### 1.1 Vitrine — o caminho rápido 🟢

O criador publica itens de preço fixo ("1 Reels — R$ 800"). A marca contrata direto.

⚠️ **Regra que decide se este caminho funciona: o formulário aqui é curto.** Preço, prazo, revisões e direitos de uso **já estão definidos no anúncio**. A marca preenche **só o que é específico daquela campanha**:

- briefing curto (o que falar sobre o produto)
- envio de produto físico? (seção 2)
- data desejada de publicação
- o que não pode aparecer

*Por quê:* se a vitrine tiver o mesmo formulário de 20 campos da proposta direta, ela perde a razão de existir. Ela existe para reduzir atrito. Fiverr funciona assim: o pacote já vem definido e o comprador só descreve o pedido.

Depois: **criador tem 48h para aceitar ou recusar** (MAQUINA-DE-ESTADOS §6.1) → pagamento → contrato.

### 1.2 Proposta direta — o caminho negociado 🟢

A marca escolhe um criador específico e monta a proposta inteira, campo a campo (seção 2 completa). O criador pode aceitar, recusar ou **pedir ajuste** em campos específicos.

É o único caminho onde os dois lados negociam antes do contrato — e é por isso que os campos precisam ser estruturados e não texto livre (SPEC §3.1): "pedir ajuste no prazo de exclusividade" é resolvível; "não gostei da proposta" não é.

### 1.3 Pedido aberto — o caminho invertido 🔴

**Aqui a lógica se inverte, e é por isso que ele precisa de telas próprias.** A marca publica o briefing e o orçamento; **cada criador preenche o próprio preço e as próprias condições** ao se candidatar.

O que os wireframes v1 não têm e este caminho exige:

| Tela que falta | Para quê |
|---|---|
| **Publicar pedido** | Briefing, faixa de orçamento, prazo, quantos criadores quer contratar, categoria |
| **Lista de candidaturas** | Ver quem se candidatou |
| **Comparador lado a lado** | 🔵 A tela que decide o negócio: comparar 5 candidaturas em preço, alcance, engajamento, prazo e histórico, na mesma linha |
| **Candidatar-se** (lado do criador) | O criador vê o briefing e monta a proposta dele |

🔵 **O comparador é a tela mais valiosa do produto para a marca**, e é a que mais justifica a comissão: escolher entre 5 criadores no olho é o problema que a agência resolve hoje na mão, em planilha. Ver os cinco lado a lado, com métrica de audiência e histórico de entrega na mesma linha, é o produto.

---

## 2. Campos da proposta — o conjunto completo 🔴

Os wireframes v1 tinham 8 campos. Uma campanha real precisa destes. Marcados com 🔴 os que não existiam em lugar nenhum da SPEC.

### 2.A Escopo da entrega

| Campo | Observação |
|---|---|
| Tipo de entrega | Reels, Stories, vídeo, post, palestra, presença em evento |
| Quantidade | |
| Plataforma de publicação | Instagram, YouTube, TikTok, offline |
| Formato / duração | ex.: até 60 segundos |
| **Data e horário de publicação** 🔴 | Livre, ou **data exata** — campanha de lançamento depende disso e não pode ser "quando der" |
| Prazo de entrega do material | Já existia |
| Revisões incluídas | Padrão 2 (MAQUINA-DE-ESTADOS §8.4) |
| **Aprovação prévia do roteiro** 🔴 | Sim/não. Se sim, vira **um marco a mais** antes da gravação — evita o criador gravar 8 minutos e a marca reprovar tudo |

### 2.B Envio de produto físico 🔴 — o bloco que faltava inteiro

O Marco apontou este, e ele traz **quatro consequências** que ninguém veria antes de acontecer:

| Campo | Por que importa |
|---|---|
| Requer envio de produto? | Chave do bloco |
| Endereço de entrega do criador | Dado sensível — só é revelado à marca **depois do contrato pago** (LGPD: mínimo necessário, e evita usar a plataforma para colher endereços) |
| Prazo para a marca enviar | |
| Código de rastreio | Preenchido pela marca |
| **O criador fica com o produto?** | Devolve, ou é permuta |
| **Valor declarado do produto** | Se ele fica, isso é **renda em espécie** — tem efeito fiscal ⚠️ |
| Quem paga o frete (ida e volta) | |

⚠️ **Consequência 1 — muda a máquina de estados.** Se a campanha exige produto, **o prazo de entrega do criador só começa a contar quando o produto é confirmado como recebido**. Sem essa regra, o criador é penalizado por um atraso que é da marca. Entra um estado novo no marco: `aguardando_produto`, entre `financiado` e `em_execucao`.

⚠️ **Consequência 2 — o produto pode não chegar.** Extraviado, endereço errado, devolvido. Precisa de um caminho: prazo limite de recebimento, depois disso a marca reenvia ou o contrato é cancelado com reembolso integral (a culpa não é do criador).

⚠️ **Consequência 3 — permuta é remuneração.** Se o criador fica com um produto de R$ 3.000 além do cachê, isso compõe o valor da operação. Precisa aparecer no contrato e no cálculo fiscal. **Precisa de contador** — entra na lista da SPEC §15.

⚠️ **Consequência 4 — permuta pura (só produto, sem dinheiro) não cabe no v1.** Sem valor em dinheiro não há escrow, não há comissão e não há o que a plataforma segurar se der errado — ou seja, o mecanismo inteiro de proteção da SPEC §4.6 deixa de funcionar. 🔵 **Proposta: v1 exige valor em dinheiro; permuta só como adicional ao cachê.**

### 2.C Direitos de uso do conteúdo 🟢

Já definido na SPEC §8.2 e já nos wireframes: prazo de uso, mídias permitidas, impulsionamento pago, exclusividade, direito de imagem, retirada.

### 2.D Conformidade publicitária 🔴 — e aqui a lei mudou este ano

| Campo | Observação |
|---|---|
| **Forma de identificação publicitária** | Ver o alerta abaixo |
| Menções obrigatórias | @marca, perfil a marcar |
| **O que não pode aparecer** 🔴 | Concorrentes, temas proibidos, outra marca no enquadramento |
| Categoria regulada? | Trava automática da SPEC §8.3 |

⚠️ **Descoberta que muda o campo: o CONAR desaconselha "#publi" desde junho de 2026.**

O CONAR publicou nova edição do *Guia de Publicidade por Influenciadores Digitais* em **12 de maio de 2026**, em vigor desde **1º de junho de 2026**. Duas mudanças que afetam este produto diretamente:

1. A identificação deve usar **preferencialmente a ferramenta nativa da própria plataforma** — "Parceria paga com" no Instagram, "contém promoção paga" no YouTube, marcação de conteúdo comercial no TikTok — **no lugar** de "#publi" e "#publicidade".
2. O CONAR **desaconselha** expressões como `#ad`, `#adv`, `#parceiro`, `#colab`, `#embaixador`.
3. A identificação vai **na primeira tela**, sem precisar clicar em "ver mais"; em vídeo, no início ou no momento exato da publicidade.

🔵 **Como isso vira produto, e não só cláusula:** o campo padrão passa a ser **"ferramenta nativa da plataforma"**, com hashtag apenas como alternativa quando a rede não oferecer a ferramenta. E a INFLUENTZ pode fazer o que ninguém faz: **lembrar o criador na hora da entrega** ("marcou como parceria paga?") e registrar a confirmação no contrato — prova documental que protege as duas pontas se o CONAR questionar depois.

*Fontes:* [TozziniFreire — Novo guia do Conar](https://tozzinifreire.com.br/boletins/novo-guia-do-conar-o-que-muda-para-campanhas-com-influenciadores-digitais) · [Migalhas — Guia CONAR 2026](https://www.migalhas.com.br/depeso/456124/guia-conar-2026-o-que-todo-influenciador-precisa-saber-agora)

⚠️ Precisa de validação de advogado antes de virar contrato — entra na SPEC §15.

### 2.E Trabalho presencial 🟢

Endereço, data, horário, duração, quem paga deslocamento e hospedagem, despesas reembolsáveis declaradas. A escala de cancelamento já está em MAQUINA-DE-ESTADOS §13.2.

---

## 3. Métricas de rede social 🔴

A SPEC §9 diz que as métricas vêm por API oficial, e a §9.2 já corrigiu o que **não** dá para fazer. Faltava dizer **quais métricas, como aparecem e para que servem**.

### 3.1 A restrição que define tudo ⚠️

As APIs oficiais entregam **métricas agregadas do perfil que autorizou o acesso**. Não entregam lista de seguidores, conteúdo de comentários, nem dados de perfis de terceiros. Qualquer métrica que a INFLUENTZ prometer fora disso é impossível de cumprir por via legal — e é exatamente onde plataformas de influenciador perdem credibilidade.

### 3.2 As cinco métricas do criador 🔵

Escolhidas por serem, ao mesmo tempo, **obteníveis** e **decisórias**:

| # | Métrica | O que é | Por que essa |
|---|---|---|---|
| 1 | **Alcance médio por publicação** | Média de contas alcançadas nas últimas publicações | **É o que a marca compra de verdade.** Seguidor é estoque parado; alcance é entrega |
| 2 | **Taxa de engajamento sobre alcance** | (curtidas + comentários + salvos + compartilhamentos) ÷ alcance | Mede se a audiência responde. Comparada **contra a mediana da categoria**, nunca contra número absoluto |
| 3 | **Perfil da audiência** | Faixa etária dominante, gênero, 3 principais localizações | **É o que decide se o público dele é o cliente dela.** Alcance alto no público errado vale zero |
| 4 | **Curva de crescimento (90 dias)** | O formato da curva, não o número | Pico anormal = sinal de seguidor comprado. É a detecção de fraude viável da SPEC §9.2 |
| 5 | **Regularidade de publicação** | Frequência e constância nos últimos 90 dias | Não é vaidade: **prevê risco de atraso**. Quem some por três semanas costuma atrasar entrega |

⚠️ **Regra de honestidade, e ela vale muito:** toda métrica aparece **com a data da última atualização e a rede de origem**. Métrica sem procedência é o que faz plataforma de influenciador virar chute com gráfico bonito.

### 3.3 A sexta métrica, que vale mais que as cinco 🔵

**Histórico dentro da INFLUENTZ:** contratos concluídos · % entregue no prazo · % aprovado sem pedido de ajuste · % que virou disputa · tempo médio de resposta.

*Por que vale mais:* as cinco métricas sociais qualquer concorrente compra de um fornecedor de dados. O histórico de entrega **só existe aqui** — e é o que a marca realmente quer saber: "esse criador entrega?".

⚠️ **E aqui mora o cold start (SPEC §14.1):** no dia 1 ninguém tem histórico. Então as métricas sociais carregam o peso no lançamento, e o histórico assume conforme a plataforma roda. A interface já nasce com os dois blocos; o de histórico começa mostrando "primeiro contrato" em vez de número — sem fingir que existe dado.

### 3.4 O outro lado: métricas da marca 🔵

Ponto levantado pelo Marco, e é o que torna a plataforma bilateral de verdade. **O criador também precisa saber quem está contratando ele:**

| Métrica da marca | Por que o criador precisa |
|---|---|
| % de pagamentos confirmados no prazo | A pergunta número um de quem presta serviço |
| **Tempo médio para aprovar uma entrega** | Marca que só aprova quando o prazo automático vence é marca que trava o dinheiro dele |
| % de contratos que viraram disputa | Sinal de conflito recorrente |
| Contratos concluídos na plataforma | Experiência |
| CNPJ verificado | Confiança básica |
| Nota média dada por criadores | Avaliação double-blind, SPEC §13.1 |

*Vantagem estrutural:* quase tudo aqui é **dado da própria plataforma**, não depende de API de rede social nenhuma. Funciona desde o primeiro contrato concluído.

### 3.5 Como as métricas aparecem — três níveis 🔵

Erro clássico: jogar todas as métricas em todas as telas. Vira ruído e ninguém decide.

| Onde | O que mostra | Por quê |
|---|---|---|
| **Cartão da busca** | **Um número só** (alcance médio) + selo de verificado + faixa de preço | Em lista, a pessoa compara, não estuda |
| **Perfil do criador** | As 5 métricas + comparação com a mediana da categoria + histórico | Aqui ela decide |
| **Comparador de candidaturas** | Tabela lado a lado, mesma linha | Aqui ela escolhe entre vários |

🔵 **A comparação é mais útil que o número.** "6,8% de engajamento" não diz nada para quem não é do ramo — e o Marco é a prova. **"40% acima da mediana de tecnologia"** diz tudo, para qualquer pessoa. É essa a leitura que vai na tela; o número cru fica ao lado, menor.

---

## 4. Telas que faltam no inventário 🔴

Os wireframes v1 cobrem 9 telas. O v1 do produto precisa de aproximadamente 30. Lista honesta do que não existe ainda:

**Entrada e conta**
1. Cadastro (marca / criador / agência) · 2. Verificação de identidade · 3. Conectar rede social · 4. Cadastro fiscal (MEI/CNPJ) · 5. Dados bancários

**Criador**
6. Montar item da vitrine · 7. Meu perfil (edição) · 8. Propostas recebidas · 9. Candidatar-se a pedido aberto · 10. Entregar material · 11. Meus contratos

**Marca**
12. Publicar pedido aberto · 13. Lista de candidaturas · 14. **Comparador lado a lado** · 15. Contratar da vitrine (form curto) · 16. Aprovar entrega · 17. Pedir ajuste · 18. Meus contratos · 19. Visão de campanha

**Compartilhadas**
20. Notificações · 21. Disputa (abrir e acompanhar) · 22. Contrato em PDF · 23. Configurações · 24. Estados vazios de cada lista

**Administrativo (SPEC §7)**
25. Fila de Trust & Safety · 26. Mediação de disputa · 27. Painel financeiro · 28. Gestão de usuários · 29. Configuração de comissão e prazos

---

## 5. O que muda na SPEC e na Máquina de Estados

| Documento | Mudança que este documento exige |
|---|---|
| SPEC §8.2 | Acrescentar bloco de envio de produto e de conformidade publicitária (CONAR 2026) |
| SPEC §15 | Contador: permuta como renda em espécie. Advogado: identificação publicitária |
| MAQUINA-DE-ESTADOS §8 | Estado novo no marco: `aguardando_produto`, entre `financiado` e `em_execucao` |
| MAQUINA-DE-ESTADOS §8.3 | O prazo de entrega só começa a contar após o recebimento do produto |
| DESIGN-SYSTEM | Ícones, avatares e padrões oficiais da marca (ver `docs/marca/`) substituem os genéricos |

---

## 6. Pendências que exigem profissional humano ⚠️

Somando à SPEC §15:

| Tema | Profissional |
|---|---|
| Permuta e produto que o criador fica: renda em espécie, nota fiscal | Contador |
| Identificação publicitária conforme Guia CONAR 2026 | Advogado |
| Guarda e revelação do endereço do criador (LGPD, mínimo necessário) | Advogado |

---

*Levantamento de arquitetura de produto. Não é parecer jurídico ou contábil.*
