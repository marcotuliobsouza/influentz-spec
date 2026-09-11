# ROADMAP — INFLUENTZ

> Onde estamos e a sequência até o lançamento. As 8 fases oficiais vivem em
> `docs/METODO-DE-TRABALHO.md` §2 — este arquivo só marca a posição atual.

## Sequência
```
1 Descoberta ──✅
2 Feature Matrix ──✅ (91 funções)
3 Modelo de dados / máquina de estados ──✅ (v0.3)
4 Sistema de design ──✅ (v0.4)
5 Telas / wireframes ──🟡 10 de ~40, desatualizadas desde 07/09
6 Conexões (GitHub, auth, pagamento) ──⬜ não iniciada
7 Código ──⬜ não iniciada
8 QA ──⬜ não iniciada
```

## Estamos aqui
**Recuperação controlada concluída** (11/09): trabalho integrado a `main`, violação regulatória nas telas corrigida, guardas estendidos, estado persistente criado.

## Próximo grande passo
**Não é mais telas.** Antes de re-desenhar qualquer coisa: critério de aceite da fatia 1 (ver `TODO.md`). Só depois disso as telas são re-derivadas da máquina de estados, uma jornada por vez — nunca dez telas soltas de novo.

## Depois da recuperação (não iniciar sem sinal do Marco)
Etapa dedicada de arquitetura operacional: metodologia de orquestração, skills/plugins, token/context engineering, geração de imagem, QA, infra e custo — nesta ordem: pesquisar → auditar → comparar → testar → decidir → instalar.
