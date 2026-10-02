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

## Requisitos da entrega informados pelo autor

O autor informou nesta conversa prazo aproximado de 24 horas para montar o trabalho e extensão de uma página para o workshop. Não forneceu um horário absoluto de submissão. Esses requisitos orientam a dimensão da proposta e a organização do trabalho.

A recomendação inicial é avaliar Hard Rock por um rótulo único de catálogo, com dois níveis de audiência e três descritores na apresentação compacta. Gênero, período, seleção e alteração da lista de descritores permanecem propostas descritas em [proposta-continuidade.md](proposta-continuidade.md); não foram promovidos a protocolo aprovado nem usados para selecionar uma amostra principal.

## Implementação autorizada — 2026-10-02 UTC

O autor autorizou prosseguir com a implementação e pediu aviso de gargalos. A proposta anterior é o histórico da recomendação; as regras executáveis passam a ser as de [workshop-protocolo.md](workshop-protocolo.md), versão 1. Isso não atribui ao orientador aprovação dos detalhes operacionais.

Antes de examinar descritores, a auditoria do rótulo exato `hard-rock` encontrou 998 IDs distintos na fonte de gênero e 176 na interseção com a fonte pareada. Após filtros de metadados, restaram 129 linhas de 39 artistas. A janela de cinco anos alcança no máximo 15 artistas; a década de catálogo 1980–1989 tem 47 faixas de 20 artistas. Adotar essa década e uma faixa por artista reduz concentração e viabiliza 20 candidatos, em lugar da meta inicialmente proposta de 24–30. A interseção constitui agora um universo deliberadamente restrito para obter o rótulo de faixa; sua cobertura não representa todo o Hard Rock.

Selecionar uma faixa por artista pelo menor hash com semente fixa, sem utilizar descritores. O lock registra os 20 IDs e URLs, dez casos em cada grupo e corte de 89.776.313,5 visualizações (mediana dos 20 candidatos). Não há reserva; exclusões não alteram o corte. Manter energy, danceability e acousticness, pontos, mediana e intervalo interquartil. Congelar as regras de mesma gravação-base, exclusão de fala sobreposta e revisão de todos os candidatos antes de análise principal. As datas utilizadas são de catálogo, não primeiras datas de lançamento validadas; visualizações são históricas, com dia declarado e sem timestamp por linha.

O acesso direto ao YouTube neste ambiente retornou falha de túnel HTTP 403 para HR01, como no piloto anterior. O autor foi informado e recebeu solicitação de conferência por IDs. Os 20 pares continuam pendentes; nenhum coincide nos dois IDs com as escutas anteriores. Datas de publicação dos novos vídeos ficam ausentes até recuperação documentada. A versão 1 permite inclusão musical com essa data ausente, mas exige relatar que a exposição do vídeo não foi controlada. Essa revisão prospectiva não altera a reprovação do piloto original.

Uma prévia técnica dos candidatos, se gerada, ficará separada e marcada como não validada. Não será um resultado principal nem critério de curadoria. A redação inicial de uma página poderá reportar apenas os resultados verificados do piloto; a comparação musical continuará explicitamente pendente até a escuta.

## Conferência dos 20 candidatos — 2026-10-01, horário de Brasília

O autor forneceu relatos para HR01–HR20 e esclareceu que o trecho final adicional em HR10 contém música. As falas originais, sem horários de escuta inventados, estão em `data/workshop/recording-review-evidence.json`; o horário UTC de registro é distinto do instante desconhecido da escuta. Nenhum áudio foi ouvido pelo assistente.

Incluir 17 gravações-base por relato. Excluir conservadoramente HR02 e HR10 por extensão musical de encerramento, preservando que o autor relatou fidelidade geral, sem afirmar mudança de execução. Essa interpretação da fronteira de edição foi feita após a prévia dos candidatos e antes da comparação curada, explicitada no protocolo; não havia limiar numérico de duração e nenhum foi introduzido. HR03 conserva o ID congelado como não confirmado suficientemente e recebe exclusão; a versão alternativa indicada, `3pIU81Fd7sTMdaaZ5GI9Vj`, não aparece em nenhum snapshot. Sua página pública, com ID canônico exato, indica Peace Sells, compilação Greatest Hits: Back To The Start, ano de catálogo 2005. Não atribuir os descritores do ID antigo ao novo.

Conservar corte de 89.776.313,5, IDs e grupos, sem reposição. Resultado do fluxo: 7/10 incluídos no grupo menor e 10/10 no maior; nenhum perdeu os três descritores por ausência/escala inválida. As datas de publicação dos 17 vídeos continuam ausentes, impedindo controle de exposição. Formato identificado no relato em cinco clipes; nos outros 12 fica desconhecido.

O limiar operacional da nova comparação, cinco gravações por grupo, é atendido. Isso não aprova retroativamente o piloto original, nem representa poder estatístico ou identidade técnica de master. A página passa a tratar a comparação curada de Hard Rock; o artigo anterior sobre curadoria permanece preservado como rascunho histórico. Resultados e hipóteses pós-hoc têm registro próprio, com limites de cobertura, rótulo e edição de catálogo.

## Revisão da PR autorizada — 2026-10-02

Após a avaliação do commit c42edff, o autor autorizou tratar os pontos possíveis e informar gargalos. Manter todos os IDs, corte e decisões principais. Explicitar pergunta e motivação no artigo, sincronizar documentos atuais e acrescentar sensibilidade pós-hoc das duas exclusões por extensão musical. A direção de energia/dançabilidade permanece nos três cenários alternativos; não interpretar como confirmação independente.

Recuperadas publicações dos 20 vídeos em páginas com IDs exatos, sem atualizar visualizações. Preservar o registro original de escuta, inclusive a ausência de datas naquele momento; a cadeia dos hashes anterior/posterior ao enriquecimento está em `data/workshop/video-metadata.json`. Classificação de formato permanece desconhecida em 12 casos. Não houve nova escuta pelo assistente.

O cache histórico completo do catálogo não foi encontrado. A nova tentativa de coleta teve 20 páginas disponíveis e 156 falhas de acesso (`URLError`); não permite conferir a seleção integral. Publicar auditoria mínima de todos os 176 IDs com ausências explícitas e observações atuais separadas das 20 originais preservadas no lock. Não afirmar divergência de seleção com base em coleta incompleta. Novos congelamentos pelo script passarão a preservar as observações de elegibilidade completas; essa mudança não fabrica evidência para o lock existente.

A dependência ABNTeX2 foi obtida de um espelho CTAN com o mesmo SHA-256 fixado. Acrescentar fallback de download com verificação de hash, preservando `settings.sty`.
