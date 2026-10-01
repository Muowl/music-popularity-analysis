# Registro de decisões

| Data | Estado | Registro |
|---|---|---|
| 2026-09-30 | Confirmado | Repositório dedicado criado pelo usuário para organizar o workshop. |
| 2026-09-30 | Confirmado | Modelo LaTeX existente preservado na raiz; settings.sty não será alterado nesta organização. |
| 2026-09-30 | Confirmado | A seleção usada na apresentação anterior pode ser revista; não é amostra definitiva. |
| 2026-09-30 | Superada | A proposta inicial priorizava descrição de canções de grande audiência; permanece como alternativa caso a comparação seja inviável. |
| 2026-09-30 | Pendente | Aprovar pergunta, fonte de seleção, tamanho, descritores e critérios de correspondência. |
| 2026-09-30 | Observado | Repositório público no momento da organização; visibilidade mantida. |
| 2026-09-30 | Implementado | Cadastro vazio e validador estrutural; nenhum dado ou resultado novo inserido. |

## Histórico relevante
Investigamos anteriormente horário de escuta e continuidade em sessões MSSD. O novo recorte surgiu para estudar características musicais e audiência. Esses caminhos não devem ser combinados no mesmo resumo curto sem justificativa e decisão explícita.

## Revisão após avaliação do desenho — 2026-09-30

O autor aprovou priorizar um piloto comparativo, com universo comum de seleção e auditoria de cobertura por nível de audiência. A pergunta é provisória e depende da viabilidade e do alinhamento com o orientador. Nenhum piloto foi executado nesta revisão.

O autor também autorizou reescrever o histórico para organizar commits por objetivo desde o início. O commit inicial do modelo, que já seguia a convenção, foi preservado. O histórico anterior foi guardado na branch `backup/pre-rebase-2026-09-30`. A autorização é específica para esta reorganização; futuras reescritas continuam exigindo acordo explícito.

## Orientação recebida e direcionamento — 2026-09-30

Fonte: relato do autor nesta conversa sobre a resposta em áudio do orientador. O áudio original não foi analisado. O orientador recebeu uma versão resumida da proposta, sem o link do repositório.

- Linha geral aceita, com ênfase exploratória e descritiva.
- Motivação, problema de pesquisa e objetivo devem ficar explícitos.
- A exploração deve levar a hipóteses para estudos posteriores, com indicação de como avaliá-las.
- O autor aprovou a aplicação desse direcionamento ao projeto. Mantém-se a comparação descritiva condicionada ao piloto; não se infere aprovação de fonte, amostra ou método operacional pelo orientador.
- A contribuição planejada passa a incluir achados documentados, hipóteses deles derivadas e propostas de testes independentes. Não há hipótese empírica formulada nesta atualização.

O detalhamento está no README, no protocolo e em docs/hipoteses.md. A amostra continua vazia; o piloto ainda não foi executado.

## Início da execução — 2026-09-30 (horário de Brasília)

Auditoria inicial de duas fontes executada; extração registrada em UTC no manifesto. A base anterior possui 114.000 linhas e 89.741 IDs; a fonte Spotify and Youtube possui 20.718 linhas e 18.862 URIs. O cruzamento encontra 3.938 IDs distintos, com cobertura por linha desigual entre faixas de audiência. Não foram comparados perfis musicais.

Decisão operacional: concluir a etapa de acesso e auditoria, manter o desenho principal pendente e investigar enriquecimento da fonte pareada. Datas de lançamento/publicação, gênero, pareamento de gravações e duplicações precisam ser resolvidos antes da amostra. Não adotar a interseção com a base anterior como filtro automático; não preencher datas ausentes com a data de download. A eventual adoção da fonte histórica como base definitiva continua pendente.

Evidências e limitações: [relatório do piloto](relatorio-piloto-fontes.md), manifesto de fontes e saída agregada da auditoria. A ausência de hipóteses musicais nesta etapa é intencional: os resultados obtidos dizem respeito à viabilidade dos dados.

## Piloto de metadados — 2026-10-01

Regra e seleção congeladas no commit a1e029ec45a7ff69f06ce716df82439fc58d554c antes da coleta suplementar: três casos por faixa histórica de audiência, ordenados por hash; nenhum valor musical usado na seleção, nenhuma substituição.

Datas foram recuperadas para os 12 vídeos e as 12 páginas Spotify. Foram localizados candidatos a gênero em catálogo para 11 casos, sem promoção automática a rótulo final. A revisão documentou dois vínculos explícitos ao álbum, nove correspondências incertas e um conflito de versão. O limiar prático registrado de nove casos completos, com pelo menos dois por faixa, não foi atingido. O cadastro principal permanece vazio.

Decisão: manter os resultados como evidência de viabilidade parcial; não importar pareamentos automaticamente nem mudar a pergunta. Recomenda-se curadoria manual dentro de um recorte único, com datas e escopos separados. As datas de catálogo não foram aceitas como primeiro lançamento. A marca official_video da fonte não garante a identidade sonora. Critérios e casos: docs/piloto-metadados.md e docs/relatorio-piloto-metadados.md.
