# Resultados descritivos — gravações-base curadas

Fonte: `data/workshop/analysis-summary.json`, reproduzida por `python scripts/analyze_workshop.py`; snapshots e hashes de origem permanecem em `data/source-manifest.json`. [Protocolo](workshop-protocolo.md), [evidências de escuta](../data/workshop/recording-review-evidence.json), [caderno](../notebooks/03_hard_rock_results.ipynb) e [figura](../figures/hard-rock-validated.pdf). Não há inferência causal ou teste de significância.

## Fluxo e comparabilidade

20 candidatos de 20 artistas, com rótulo exato `hard-rock` na fonte de gênero e anos de catálogo 1980–1989. A seleção foi congelada antes da inspeção dos descritores. Após a revisão de todos os relatos: 17 incluídos, três excluídos, zero pendentes, zero perdas adicionais por descritores ausentes/fora da escala.

| Grupo histórico | Candidatos | Incluídos | Perdas | Artistas distintos |
|---|---:|---:|---:|---:|
| Menor audiência, abaixo de 89.776.313,5 visualizações | 10 | 7 | 3 (30%) | 7 |
| Maior audiência, igual/acima do corte | 10 | 10 | 0 | 10 |

O corte é a mediana **dos 20 selecionados antes da curadoria**, não dos 17 incluídos. Não foi recalculado. HR02 e HR10 apresentam extensões musicais de encerramento; HR03 tem versão alternativa proposta, mas ausente dos snapshots e com ano de catálogo 2005. O pareamento original de HR03 não foi confirmado suficientemente. As exclusões não identificam necessariamente outra execução. A interpretação conservadora das extensões musicais foi registrada depois da prévia, antes desta comparação.

Mediana do ano de catálogo: 1984 nos dois grupos. Intervalos: 1980–1988 no menor e 1980–1989 no maior. Não representam primeiros lançamentos já validados. Datas de publicação disponíveis: **17/17**, recuperadas de metadados atuais dos IDs exatos e preservadas em `data/workshop/video-metadata.json`. Tempo desde a publicação até 07/02/2023: mediana **12,80 anos** no grupo menor (0,32–13,23) e **13,03 anos** no maior (9,60–13,92). O cálculo usa dias/365,25, com precisão diária; não mede exposição efetiva nem ajusta a comparação. Formato identificado: quatro clipes e três desconhecidos no menor; um clipe e nove desconhecidos no maior. O formato não é fator controlado nesta comparação.

## Medianas, dispersão e sobreposição

Escala [0,1]; intervalos interquartis (IIQ) por interpolação linear NumPy. Valores dos descritores referem-se à edição Spotify, não ao áudio integral do clipe.

| Descritor | Menor audiência, n=7: mediana [IIQ] | Maior audiência, n=10: mediana [IIQ] | Diferença das medianas (maior − menor) |
|---|---|---|---:|
| Energy | 0,9310 [0,8950; 0,9675] | 0,7545 [0,70075; 0,8300] | −0,1765 |
| Danceability | 0,5400 [0,3355; 0,5730] | 0,3505 [0,2710; 0,49525] | −0,1895 |
| Acousticness | 0,02020 [0,00908; 0,04740] | 0,02595 [0,012675; 0,110725] | +0,00575 |

Nesta seleção, o grupo de maior audiência tem medianas menores de energia e dançabilidade. As medianas de acusticidade são próximas, mas a amplitude e a dispersão diferem; não concluir equivalência. Os IIQs de energia não se sobrepõem, enquanto os **intervalos dos valores individuais se sobrepõem nos três descritores**. Há heterogeneidade dentro dos grupos, visível nos pontos; não foram removidos pontos atípicos por seu valor musical.

| Descritor | Valores observados: menor | Valores observados: maior |
|---|---|---|
| Energy | 0,722–0,982 | 0,452–0,980 |
| Danceability | 0,303–0,679 | 0,202–0,630 |
| Acousticness | 0,00253–0,435 | 0,00322–0,638 |

Os resultados são específicos da interseção das fontes e da seleção do publicador de faixas de artistas. O rótulo comum não elimina subestilos, baladas, remasters ou diferenças de exposição. Todas as perdas estão no grupo de menor audiência, podendo alterar seu perfil. Não se mede uma fórmula do sucesso nem se demonstra que aumentar/diminuir um descritor modifica visualizações.

A exploração gera uma hipótese para avaliação independente, registrada em [hipoteses.md](hipoteses.md). Nenhum resultado atual confirma a hipótese que ele próprio sugeriu. A acusticidade não motivou uma hipótese direcional nesta etapa.

## Sensibilidade pós-hoc das extensões musicais

Fonte: `data/workshop/sensitivity-summary.json`; reprodução: `python scripts/analyze_workshop_sensitivity.py`. Acrescentam-se HR02 e HR10 apenas em cenários alternativos, mantendo HR03 excluído, o corte original e os grupos. As decisões principais e os relatos não mudam. A análise foi definida após os achados e não é confirmação independente.

| Cenário | n menor / maior | Δ energia | Δ dançabilidade | Δ acusticidade |
|---|---|---:|---:|---:|
| Principal | 7 / 10 | −0,1765 | −0,1895 | +0,00575 |
| Acrescentar HR02 | 8 / 10 | −0,1730 | −0,1790 | +0,00865 |
| Acrescentar HR10 | 8 / 10 | −0,1730 | −0,2045 | −0,00560 |
| Acrescentar ambos | 9 / 10 | −0,1695 | −0,1895 | +0,00575 |

Δ = mediana maior − mediana menor. Energia e dançabilidade mantêm diferenças negativas nos quatro cenários. A direção da pequena diferença de acusticidade muda em um deles, reforçando a ausência de hipótese direcional para esse descritor. A sensibilidade não resolve confundimento, representatividade, validade dos descritores ou correspondência técnica de master.

As medianas de idade próximas coexistem com amplitudes distintas: o grupo menor inclui um vídeo publicado poucos meses antes do snapshot. Não concluir que a exposição foi equalizada. A auditoria histórica da seleção permanece parcial, conforme `auditoria-selecao.md`.
