# Protocolo operacional do workshop — versão 1

**Estado atual:** 20 relatos recebidos, 17 incluídos e três excluídos por adjudicação conservadora. IDs, rótulo, janela, descritores e corte permanecem congelados. Ver [conferência consolidada](conferencia-hard-rock.md) e [resultados](resultados-hard-rock.md).

Implementação autorizada pelo autor nesta conversa após a proposta de Hard Rock, dois níveis de audiência e três descritores. Regras fixadas antes da leitura dos valores musicais. A autorização para implementar não constitui validação pelo orientador ou aprovação de gravações ainda não ouvidas.

## Pergunta e universo

Como se distribuem energy, danceability e acousticness entre faixas **rotuladas `hard-rock` na fonte Spotify Tracks Dataset**, com datas de catálogo Spotify de 1980–1989, associadas a vídeos de menor e maior audiência no snapshot Spotify and Youtube?

O universo é a interseção exata por ID Spotify das duas fontes já auditadas, não todo o gênero. O rótulo é operacional e não representa consenso musicológico. A interseção é necessária para este rótulo de faixa, não para obter os descritores, já presentes na fonte pareada. A cobertura desigual identificada no piloto permanece uma limitação. Manter os hashes em `data/source-manifest.json` e não atualizar contadores históricos.

A janela inicial de cinco anos não alcança 20 artistas distintos após os filtros de metadados: seu máximo é 15. Adotar a década de 1980 completa, com 20 artistas elegíveis, evita concentrar várias faixas do mesmo artista. Esta escolha usa somente volume, artistas e datas de catálogo, sem examinar os descritores. Não escolher a melhor janela pelo contraste musical. O ano é o da edição/catálogo apresentado na página de ID exato, recuperada em 2026; **não foi validado como primeiro lançamento da gravação**. Os remasters permanecem identificados no título.

## Seleção congelada

1. Filtro preliminar comum: `official_video=True` na fonte, URI única e URL de vídeo única considerando **toda** a fonte pareada, visualizações positivas inteiras, ID canônico confirmado na página Spotify e ano de catálogo disponível. A marca oficial é do publicador e não dispensa curadoria.
2. Entre os elegíveis com ano 1980–1989, ordenar pelo SHA-256 de `hard-rock-workshop-v1|<track_id>` e selecionar a primeira faixa de cada artista conforme a grafia da fonte. No máximo uma faixa por artista. Não usar valores de descritores para escolher.
3. Formar os dois grupos pela mediana das visualizações **dessas 20 faixas selecionadas**, antes da curadoria. Grupo `lower`: abaixo da mediana; `higher`: igual ou acima. O corte e os grupos ficam congelados, inclusive após perdas; não recalcular a mediana para equilibrar a amostra final.
4. Incluir todos os 20 candidatos na conferência. Não há reserva ou reposição. Perdas diminuem o tamanho da amostra e são relatadas por grupo.
5. Guardar `data/workshop/selection-lock.json`, suas fontes e o CSV de revisão. Não sobrescrever o lock. Mudanças posteriores exigem nova versão, justificativa e identificação de análise pós-hoc.

Visualizações referem-se à coleta declarada de **2023-02-07**, precisão de dia e sem instante UTC por linha. Não preencher `observed_at_utc` com download, meia-noite ou recuperação atual. A medida representa audiência do vídeo associado, não total de ouvintes da música.

## Conferência e inclusão

Revisar título, intérpretes, versão e conteúdo musical. Registrar revisor, evidência de escuta e trechos divergentes quando existirem. Uma mesma gravação-base pode ser associada ao clipe mesmo com intro, final ou interrupção narrativa, desde que a execução musical corresponda. Isso não prova identidade digital de master; remasters e edição de vídeo precisam ser explícitos. Alteração de intérprete, remix, outra execução ou corte musical incompatível excluem o par. Fala/efeito exclusivo sobre a música permanece fora da análise principal. Correspondência não resolvida permanece pendente. Os relatos antigos do piloto só podem ser reaproveitados se **ambos os IDs forem exatamente os mesmos** e a regra atual os admitir.

Aceitar clipes e uploads oficiais de áudio sob a mesma regra musical, mas registrar o formato para contexto. Não inferir formato só da coluna `official_video`. Guardar a publicação do vídeo quando recuperável; ausência permanece ausente e impede calcular sua idade. Se a data não puder ser obtida, a inclusão por correspondência ainda pode ocorrer, mas a falta de controle de tempo de exposição será uma limitação explícita. Esta é uma revisão prospectiva do requisito de completude do piloto, não aprovação retroativa daquele piloto.

Na análise principal, exigir decisão `include`, `recording_review=same_base_recording`, revisor e evidência, campos congelados intactos e três descritores finitos na escala [0,1]. Registrar casos incluídos na curadoria mas removidos por valores musicais ausentes/inválidos. Nenhuma escuta será atribuída ao assistente sem ter ocorrido. Fontes correntes de catálogo não substituem o snapshot de audiência.

## Análise e apresentação

Descritores da faixa Spotify, com definições da documentação Spotify; não foram calculados sobre todo o áudio do clipe. Mostrar pontos por faixa, mediana e intervalo interquartil em três painéis, escala comum [0,1]. Relatar fluxo e n por grupo, sobreposição, datas de catálogo, artistas e disponibilidade de publicação/idade do vídeo. Sem testes de significância, modelo preditivo ou interpretação causal. Não apresentar semelhança como equivalência estatística.

Antes de incorporar resultados à página, finalizar a curadoria de **todos os candidatos**, incluindo exclusões, sem interromper a revisão ao aparecer um contraste. Um grupo com menos de cinco incluídos não produz comparação principal: registrar inviabilidade e usar a contribuição sobre curadoria como alternativa de uma página. Cinco é um limiar operacional para a descrição mínima, não cálculo de poder ou precisão.

Uma execução `--preview` poderá inspecionar somente o funcionamento do pipeline com todos os candidatos; sua figura será marcada **candidatos não validados** e não entrará nos resultados principais. Depois que uma prévia existir, qualquer alteração de desenho será registrada como posterior à inspeção dos descritores. Não usar prévia para aceitar/excluir pares.

Não haverá análise de sensibilidade de sobreposição vocal nesta versão. Hipóteses futuras dependerão de achados rastreáveis e serão avaliadas em dados independentes. Para uma página, priorizar uma pergunta, uma figura e limitações materiais. Preservar `settings.sty`.

## Adjudicação dos relatos após a prévia técnica

O autor relatou os 20 casos e esclareceu HR10. Para HR02 e HR10, descreveu a base como fiel, mas apontou trechos musicais adicionais ao final do Spotify. Aplicou-se interpretação conservadora de edição/corte incompatível para a comparação principal: excluí-los sem alegar outro intérprete, remix ou outra execução. **A fronteira de extensão musical de encerramento não tinha limiar numérico na versão 1; essa interpretação foi documentada após a prévia e antes de calcular a comparação curada.** Não se introduziu limite de segundos nem se escolheu decisão pelo contraste dos descritores. Intros e finais narrativos fora da música continuam admissíveis.

HR03 ficou como correspondência do ID original não suficientemente confirmada. A alternativa proposta pelo autor está ausente dos dois snapshots e sua página apresenta ano de catálogo 2005, fora da janela operacional. Registrar a alternativa, sem trocar IDs, copiar descritores ou completar a amostra. Isso não prova que o remaster original seja outra execução; significa que sua correspondência permaneceu não resolvida para inclusão.

As três exclusões são decisões de curadoria aplicadas aos relatos reais; não constituem revisão de desenho para obter diferenças maiores. Na execução inicial não houve sensibilidade. A revisão de 2026-10-02 acrescenta os cenários pós-hoc descritos abaixo, sem mudar as decisões principais. A amostra final contém sete casos abaixo e dez acima do corte original, com perdas de 3/10 e 0/10. Todos os casos receberam decisão explícita; não há pendência de escuta exigida para esta comparação. Qualquer reconsideração futura precisa preservar essas evidências e registrar a revisão de classificação.

## Reprodução

```bash
python scripts/download_pilot_sources.py
python scripts/analyze_workshop.py
python scripts/analyze_workshop_sensitivity.py
python scripts/audit_workshop_selection.py
```

A aquisição de páginas usa cache com hash e registro do momento de recuperação; não faz parte da reexecução offline da análise. O congelamento falha se já houver lock. Fontes brutas permanecem ignoradas pelo Git; publicar apenas código, cadastro mínimo e resultados agregados, conforme as condições já registradas.

## Revisão posterior à análise — 2026-10-02

A pergunta, IDs, corte, grupos e decisões principais permanecem congelados. Após a avaliação da PR, acrescentar HR02, HR10 e ambos em três cenários de sensibilidade das extensões musicais; manter HR03 excluído e comparar as mesmas três medianas. Registrar como análise pós-hoc, não como teste independente de H01. Não escolher novas inclusões em função dos resultados.

Recuperar `publishDate` em páginas dos IDs exatos de YouTube, preservando valor bruto, data de obtenção e hash. Usar o componente de data informado pela plataforma, sem inventar hora UTC da audiência histórica. Datas posteriores ao snapshot ou IDs divergentes não são aceitos. O enriquecimento é documental: não constitui nova escuta nem classificação do formato. As 20 datas foram recuperadas; a idade é contextual e não um ajuste por exposição.

A primeira tentativa posterior ficou incompleta. Em seguida, a coleta local de 176/176 páginas foi verificada independentemente e reproduziu seleção/corte, sem alterar os grupos ou recuperar o cache original. Ver `auditoria-selecao.md`. Não recalcular grupos da análise principal com novas observações.
