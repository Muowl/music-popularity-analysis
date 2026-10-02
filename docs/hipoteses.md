# Registro de achados e hipóteses futuras

Estado: resultados descritivos registrados após a curadoria de 17 pares. H01 foi gerada pela exploração e permanece **não confirmada em dados independentes**. A estrutura abaixo orienta o registro; os achados da seleção atual estão ao final.

## Finalidade
Atender ao direcionamento exploratório do workshop: observação documentada → hipótese sugerida → proposta de teste futuro. Hipótese é uma proposição a avaliar; não constitui resultado confirmado nem, por si só, uma teoria.

## Como registrar
Criar uma seção por achado relevante e preencher os campos abaixo. Não escolher apenas achados com grande contraste. Hipóteses podem surgir da exploração, desde que sua origem pós-hoc seja explícita.

| Campo | Conteúdo exigido |
|---|---|
| Identificador e data | Código estável, por exemplo H01, e data de formulação |
| Origem | Exploração dos resultados ou expectativa anterior, com referência ao registro datado |
| Achado observado | Descrição restrita à amostra, tamanho dos grupos, medidas e dispersão |
| Evidência | Figura/tabela, arquivo de análise, versão dos dados e commit |
| Interpretação e alternativas | O que pode explicar o padrão e quais fatores não foram separados |
| Hipótese sugerida | Proposição testável, com população, variáveis e condições; direção apenas se justificada |
| Relação com literatura | Fonte verificada e afirmação pertinente, ou pendência explicitada |
| Teste futuro | Dados independentes necessários, seleção, variáveis, fatores a considerar e análise a definir antes de observá-los |
| Critério de avaliação | Que observação apoiaria, enfraqueceria ou contrariaria a proposição; não escolher o critério após o teste |
| Limites e estado | Gerada pela exploração; não testada independentemente neste estudo |

## Regras de interpretação
- Distinguir associação entre descritores e audiência de uma explicação causal do sucesso.
- Não concluir equivalência a partir de gráficos parecidos ou de ausência de significância.
- Não transformar diferenças pequenas, casos isolados ou perdas de cobertura em padrões gerais.
- Quando não houver suporte para uma hipótese específica, registrar o achado, a incerteza e quais dados faltam. Não preencher o registro com hipóteses artificiais.
- Não há obrigação de propor uma teoria nova. Uma explicação teórica existente só será discutida com referência verificada e ligação explícita ao achado.

## H01 — audiência, energia e dançabilidade

Data de formulação: nesta sessão, após os resultados curados; dia no contexto do autor: 2026-10-01. **Origem pós-hoc**, não expectativa anterior nem hipótese confirmatória.

**Achado:** em 17 gravações-base de artistas distintos, sete no grupo menor e dez no maior, o grupo maior tem mediana de energy 0,7545 versus 0,9310 e danceability 0,3505 versus 0,5400. Diferenças de medianas (maior − menor): −0,1765 e −0,1895. Os valores individuais se sobrepõem em ambos; não se trata de separação completa dos grupos. Evidências: [resultados](resultados-hard-rock.md), `data/workshop/analysis-summary.json`, `figures/hard-rock-validated.pdf`, `notebooks/03_hard_rock_results.ipynb`; hashes de fontes, lock e revisão no resumo.

**Interpretação e alternativas:** a composição por baladas e outros subestilos, ainda sem classificação sistemática, pode explicar parte do contraste dentro do rótulo de catálogo, além de diferenças de artista, formato e exposição. As três perdas estão no grupo menor (30% versus 0%), podendo alterar seu perfil. As datas de publicação foram recuperadas na revisão: idade mediana de 12,80 e 13,03 anos, com amplitudes distintas e sem ajuste estatístico. Formato desconhecido em 12/17. Datas de catálogo não são primeiros lançamentos validados. HR05, HR13 e HR14 usam edições Spotify identificadas como remasterizadas, sem verificação do master dos vídeos ou quantificação do efeito nos descritores. Essas alternativas não foram separadas pela análise atual.

**Hipótese sugerida:** em uma seleção independente do mesmo recorte operacional, maior audiência relativa de vídeos associados a gravações-base correspondentes acompanha medianas menores de energia e dançabilidade. É uma proposição de associação restrita; não afirma que diminuir atributos eleve visualizações.

**Relação com literatura:** Askin e Mauskapf (2017), DOI 10.1177/0003122417728662, relacionaram características musicais e sucesso no Billboard. Essa motivação não valida a direção observada aqui ou sua causalidade no YouTube. As definições dos atributos são da documentação Spotify, com evidências em `data/workshop/reference-evidence.json`.

**Teste futuro:** adquirir outros pares/novos dados independentes dos 20 candidatos, com gênero operacional e período de catálogo comuns. Antes da inspeção dos descritores, definir amostragem, dimensão necessária, faixas de audiência relativas, data da coleta, métricas, curadoria uniforme e tratamento de edições. Documentar publicação/idade do vídeo, formato e identidade de artistas; estratificar ou modelar esses fatores por plano prévio. Comparar medianas e incerteza, respeitando dependências por artista e os dois descritores planejados. Não usar a amostra atual para escolher o corte ou a significância do teste futuro.

**Critério de avaliação:** diferenças negativas nas duas medianas em dados independentes, com incerteza quantificada e análise previamente definida, apoiariam a direção proposta. Direção oposta robusta a enfraqueceria; intervalos amplos ou resultados sensíveis à exposição/curadoria seriam inconclusivos. Ausência de contraste não prova equivalência. Nenhuma magnitude mínima ou decisão de significância foi escolhida a partir do resultado atual.

**Estado e limites:** hipótese exploratória, ainda não testada independentemente. Generalização fora da interseção e do recorte não é sustentada.

## Achado A02 — acusticidade e heterogeneidade

Medianas de acousticness: 0,02020 e 0,02595; diferença +0,00575. IIQs: [0,00908; 0,04740] e [0,012675; 0,110725]; amplitudes individuais [0,00253; 0,435] e [0,00322; 0,638]. Medianas próximas coexistem com dispersão e valores altos isolados. Não concluir equivalência e não propor hipótese direcional de acusticidade a partir deste achado. Os pontos foram preservados, inclusive os atípicos.

## Revisão de robustez — 2026-10-02

A sensibilidade pós-hoc às exclusões HR02/HR10 manteve a direção negativa das diferenças de medianas de energia e dançabilidade nos cenários individual e conjunto. Os números estão em `resultados-hard-rock.md` e `data/workshop/sensitivity-summary.json`. Isso reduz a dependência desses achados em relação a essas duas decisões específicas; H01 continua não confirmada em dados independentes. A acusticidade muda de sinal ao acrescentar apenas HR10 e permanece sem hipótese direcional.
