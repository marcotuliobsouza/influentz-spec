# Guardas da INFLUENTZ — o que é lei, o que é aviso, o que ainda não está protegido

> Regra da casa: nenhum mecanismo é declarado como existente sem evidência.
> Esta página separa o que foi provado do que ainda depende de configuração
> manual do Founder.

## Os dois comandos

```
python3 .claude/guardas/verificar.py     # confere todos os documentos e telas
python3 .claude/guardas/testes.py        # roda a regressão dos três guardas
```

Saída `0` é PASS, saída `1` é FAIL. Rodam iguais na máquina do agente e no
GitHub — a regra existe em um lugar só e não tem cópia para divergir.

## Os três guardas

| Guarda | Quando roda | O que faz | Força |
|---|---|---|---|
| `hooks/guarda-comandos.py` | antes de todo comando de terminal | **bloqueia** comando destrutivo e comando que é decisão do Founder | **impede** |
| `hooks/guarda-documentos.py` | depois de toda escrita em `.md` / `.html` | número travado divergente, palavra proibida em rótulo de tela, autocrítica em documento de produto | avisa |
| `hooks/guarda-painel.py` | quando a sessão termina | documento de produto mudou sem o `PAINEL.md` acompanhar | avisa |

O guarda de comandos é o único que impede. Os outros dois avisam de
propósito: um falso positivo nunca pode travar o trabalho.

## As duas faixas do guarda de comandos

**DESTRUTIVO — sem escape.** Perde trabalho e não tem desfazer: descarte
forçado da árvore, reescrita de histórico remoto, remoção recursiva forçada,
limpeza de arquivos nunca commitados, remoção de branch sem conferência, e
qualquer escrita em `docs/marca/`.

**GOVERNANÇA — escape explícito.** Reversível, mas é decisão do Founder:
integrar branch, publicar direto em `main`, publicar tag ou release, deploy,
e alterar banco de fornecedor.

O escape é prefixar o comando com `APROVADO_PELO_FOUNDER=1`. Ele fica
registrado na transcrição e no histórico do terminal.

**O que esse escape é e o que não é.** É trava contra acidente e contra o
agente decidir sozinho. Não é controle criptográfico: quem escreve o comando
pode escrever o prefixo. O controle que não depende de quem executa é a
proteção de branch no GitHub — e ela ainda não existe.

## AINDA NÃO PROTEGIDO — depende do Founder

Verificado em 12/09/2026 pela API do GitHub: o branch `main` do repositório
`marcotuliobsouza/influentz-spec` responde `protected: false`. Os dois
branches do repositório estão desprotegidos.

Enquanto isso for verdade, **o repositório aceita integração sem verificação
e sem aprovação**. A trava do agente continua valendo para o agente; ela não
vale para nada que chegue por fora dele.

### O que configurar, e onde

Em `https://github.com/marcotuliobsouza/influentz-spec/settings/rules` —
criar um conjunto de regras aplicado ao branch `main` com:

1. **Require status checks to pass** — marcar a verificação `Guardas /
   Documentos, telas e comandos`. É o que impede integrar documento
   divergente. A verificação precisa ter rodado ao menos uma vez para
   aparecer na lista.
2. **Require a pull request before merging** — impede publicar direto em
   `main`.
3. **Block force pushes** — já vem ligado por padrão; confirmar.
4. **Restrict deletions** — impede apagar o branch.

Não marcar *Require approvals* com número maior que zero enquanto o
repositório tiver um dono só: o GitHub não deixa o autor aprovar o próprio
pull request, e o trabalho ficaria travado esperando um segundo humano.

### Como conferir depois

Abrir `https://github.com/marcotuliobsouza/influentz-spec/settings/rules` e
ver se o conjunto de regras está ativo, ou consultar pela API o campo
`protected` do branch `main`. Enquanto ele responder `false`, a proteção não
existe — independentemente do que qualquer documento afirme.

## Falsos positivos conhecidos, já resolvidos e travados por teste

Cada um destes já aconteceu de verdade e cada um tem um teste que impede a
volta:

- `cartão de crédito` é o nome do meio de pagamento, não o conceito proibido
  pela SPEC §4.9.1.
- Contagem de subconjunto — funções de uma fatia — não é o total do v1.
- Linha contrafactual, que compara com um cenário descartado para explicar a
  decisão, não afirma um número travado.
- Rótulo de tela já corrigido não pode voltar a disparar.
- Registro de correção em documento de processo é legítimo; a regra §2.4 vale
  para documento de produto.
- Texto que **cita** um comando perigoso não é o comando sendo executado. Foi
  o próprio guarda de comandos que bloqueou a escrita desta página, em
  12/09/2026, antes desta regra existir.

## Falsos negativos possíveis — o que estes guardas não pegam

Declarado para que ninguém confie além do que foi provado:

- Número travado escrito de forma que o padrão não reconhece. O guarda
  detecta divergência, não ausência.
- Palavra proibida em documento de produto fora de rótulo entre aspas e fora
  de linha marcada como tela.
- Comando perigoso escrito de forma que os padrões não reconhecem, ou
  escondido dentro de um script que o terminal depois executa.
- Ação feita por ferramenta que não é o terminal.
- Conteúdo dentro de bloco de código, ignorado de propósito.
