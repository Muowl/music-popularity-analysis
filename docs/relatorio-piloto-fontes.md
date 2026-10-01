# Piloto — auditoria inicial das fontes

## Decisão desta etapa
**Prosseguir com a investigação, sem congelar a amostra.** Acesso aos CSVs e cruzamento exato por ID foram demonstrados. O desenho que exige gênero e período de lançamento ainda não é executável apenas com essas fontes: faltam metadados temporais e uma regra de gênero adequada. Não foram comparados descritores por audiência nem formuladas hipóteses sobre sucesso musical.

Esta é a primeira etapa executada do piloto, não a validação final da comparação. As evidências são contagens calculadas sobre arquivos completos, não estimativas obtidas dos exemplos de uma página.

## Fontes e proveniência
- [Spotify Tracks Dataset, do publicador Maharshi Pandya](https://huggingface.co/datasets/maharshipandya/spotify-tracks-dataset): a mesma origem indicada no repositório do visualizador. CSV com 114.000 linhas, 89.741 IDs distintos e 114 rótulos de gênero observados. O cartão menciona 125 gêneros; para este arquivo prevalece a contagem calculada. Data de coleta não estabelecida nesta auditoria; data de atualização do repositório não é data das medições.
- [Spotify and Youtube, do publicador Salvatore Rastelli](https://www.kaggle.com/datasets/salvatorerastelli/spotify-and-youtube): versão 2, 20.718 linhas e 18.862 URIs distintos. A descrição obtida pela API pública declara coleta em 07/02/2023; a atualização do dataset é 20/03/2023. As visualizações são históricas, não de 2026. O subtítulo informa seleção das dez músicas principais de diversos artistas, portanto não representa todo o catálogo nem uma amostra aleatória de músicas.

Metadados de licença consultados: `bsd` no Hugging Face e `CC0: Public Domain` no Kaggle. São declarações dos publicadores, não certificação independente de direitos sobre os dados de origem. Nenhum CSV bruto foi publicado neste repositório. URLs, versão, tamanhos e hashes estão em [data/source-manifest.json](../data/source-manifest.json).

## O que os dados permitem e o que falta
| Campo necessário | Spotify Tracks | Spotify and Youtube |
|---|---|---|
| ID de faixa Spotify | Presente | Presente em Uri |
| Cinco descritores candidatos | Completos e dentro de 0–1 | Duas linhas sem os cinco descritores; demais dentro de 0–1 |
| Visualizações e URL de vídeo | Ausentes | 470 linhas sem ambos |
| Gênero em coluna própria | Presente, com múltiplos rótulos para muitos IDs | Ausente |
| Lançamento da gravação | Ausente | Ausente |
| Publicação do vídeo | Ausente | Ausente |
| Data/hora da observação por linha | Ausente | Ausente; somente data geral declarada |

`official_video=True` é um campo fornecido pela base, não uma conferência nossa. Há 15.723 linhas marcadas True, 4.525 False e 470 sem informação. Não pressupor que todas as associações correspondem à mesma gravação de áudio.

## Cruzamento e cobertura
Cruzamento estrito: remover o prefixo `spotify:track:` de Uri e procurar exatamente esse ID em track_id. Não houve busca aproximada por título nem substituição de versões.

- 4.443 linhas da base pareada encontram ID na base anterior: 3.938 IDs distintos.
- A junção direta produziria 7.166 linhas, porque a base anterior repete IDs. Não usar esse resultado multiplicado como amostra.
- Os cinco descritores coincidem entre as fontes nas 4.443 linhas correspondentes. Isso confirma consistência numérica nesse cruzamento, não identidade do áudio do vídeo.
- Na base anterior, 16.299 IDs têm múltiplos rótulos de gênero. Escolher a primeira linha atribuiria um gênero arbitrário; é preciso preservar o conjunto de rótulos e definir elegibilidade explicitamente.

As faixas abaixo foram definidas por potências de dez apenas para auditar cobertura, antes de examinar contrastes musicais. Não são os grupos finais do estudo. Denominador: **linhas** com visualizações não negativas inteiras e URL de vídeo preenchida; repetições foram mantidas para revelar a estrutura da fonte.

| Visualizações históricas | Linhas elegíveis para esta auditoria | Linhas com ID na base anterior | Cobertura |
|---|---:|---:|---:|
| Menos de 1 milhão | 4,080 | 524 | 12.84% |
| 1 a menos de 10 milhões | 4,950 | 782 | 15.80% |
| 10 a menos de 100 milhões | 7,293 | 1,669 | 22.89% |
| 100 milhões ou mais | 3,925 | 1,400 | 35.67% |

A cobertura cresce entre as faixas de audiência. Logo, usar a interseção para obter gênero pode selecionar proporcionalmente mais registros de grande audiência. A diferença de cobertura está observada; seu efeito sobre uma futura comparação musical ainda não foi quantificado.

## Duplicações e correspondências
Na base pareada, as 20.248 linhas com vídeo contêm 18.154 URLs distintas e 18.820 pares Uri–URL distintos. Há 284 URIs associados a mais de um vídeo e 451 URLs associadas a mais de uma URI. Além disso, 973 URLs reaparecem com contagens de visualizações diferentes. A causa dessas diferenças não foi estabelecida; não escolher automaticamente o maior valor nem somar contagens.

Esses resultados exigem definir a unidade de análise e conferir as versões antes de deduplicar. Uma linha não equivale automaticamente a uma canção independente. Não transformar as 470 ausências de visualizações em zero.

## Riscos e encaminhamento
| Risco | Impacto no desenho | Encaminhamento |
|---|---|---|
| Ausência de datas e de gênero na fonte pareada — alto | Impede aplicar diretamente o recorte acordado | Avaliar enriquecimento documental de uma pequena seleção com fonte comum; não retirar essas restrições silenciosamente |
| Cobertura desigual no cruzamento — alto | Pode alterar a composição dos grupos | Não tornar a presença na base anterior um filtro automático; os descritores já existem na fonte pareada |
| Vídeos/URIs repetidos e contagens conflitantes — alto | Pode multiplicar observações e distorcer audiência | Auditar pares e registrar regra de exclusão/seleção antes de calcular resultados |
| Seleção das dez faixas principais por artista — alto | Restringe a população à seleção do publicador | Definir o universo como o snapshot, sem inferir sobre toda a música popular |
| Snapshot histórico e horário de coleta ausente — médio | Não sustenta análise de audiência atual nem instante exato | Manter contagens históricas separadas de qualquer consulta nova; nunca usar data do download como data de observação |
| Origem dos pareamentos não validada — alto | Vídeo pode conter versão diferente da faixa | Conferir evidências documentais; marca de vídeo oficial não é prova suficiente |

Confiança alta nas contagens e na ausência de colunas; interpretação dos mecanismos de seleção e de contagens divergentes permanece limitada pela documentação do publicador.

## Recomendação operacional
Investigar a base pareada como fonte candidata principal, pois ela já contém audiência e descritores e evita exigir a interseção enviesada apenas para obter audio features. A adoção final depende de obter gênero e datas com procedência verificável e validar gravações. Não mudar a pergunta nem adotar essa fonte como definitiva antes dessa verificação.

Próxima etapa: definir um recorte candidato com regra comum, congelar uma pequena seleção de auditoria sem olhar os contrastes dos descritores e verificar a disponibilidade de lançamento, publicação e identidade da gravação em cada caso. O tamanho e os limites de audiência devem ser registrados antes dessa seleção. Se o enriquecimento não for viável, apresentar a limitação e uma proposta explícita de ajuste ao autor/orientador.

O cadastro principal continua vazio. Há motivo adicional para ajustá-lo antes de importar: o campo observed_at_utc atual exige um instante que o snapshot histórico não fornece. Precisaremos distinguir data declarada, precisão temporal e data de obtenção, sem inventar horários.

## Reprodução e validação
```sh
python scripts/download_pilot_sources.py
python scripts/audit_sources.py --tracks data/raw/spotify_tracks.csv --youtube data/raw/spotify_youtube.csv --output docs/evidence/source-audit.json
```
O download confere hashes antes de salvar; se a fonte mudar, interrompe em vez de aceitar outra versão silenciosamente. A auditoria usa apenas a biblioteca padrão do Python. [Saída agregada](evidence/source-audit.json) e [caderno de acompanhamento](../notebooks/01_source_feasibility.ipynb) preservam os cálculos.

A junção, o total de IDs correspondentes e os quatro numeradores/denominadores de cobertura foram recalculados independentemente com pandas e coincidiram. Não houve teste de associação musical, comparação temporal, validação manual das gravações nem análise de causalidade. As bibliotecas Jupyter não estão disponíveis neste ambiente: as células do caderno foram executadas sequencialmente em Python, com saída salva; abertura/renderização em Jupyter ainda não foi verificada.
