# Piloto de metadados — resultado da etapa 2

## Recomendação
**Acesso técnico demonstrado; a rota ainda não atingiu o critério de avanço deste piloto.** As 12 páginas de vídeo e as 12 páginas de faixa puderam ser consultadas. Recuperamos datas, mas o pareamento das gravações e a interpretação dos campos ainda requerem curadoria. Recomenda-se uma amostra final pequena com recorte único e conferência manual de versões, em vez de importar todos os pareamentos da base.

## Seleção e execução
A [regra v1](piloto-metadados.md) e os [12 candidatos](../data/pilot/metadata-candidates.json) foram congelados no commit `a1e029ec45a7ff69f06ce716df82439fc58d554c`, antes de pesquisar seus metadados. Três casos por faixa histórica de audiência; nenhuma substituição.

Das 20.718 linhas de origem, foram excluídas sequencialmente 470 por ausência/invalidade de vídeo ou visualizações, 4.525 por não estarem marcadas como oficiais e 3.296 por URI ou URL repetida. Restaram 12.427 linhas elegíveis para o teste de acesso: 1.766, 2.969, 5.016 e 2.676 nas quatro faixas. Seleção por ordenação de hash, sem usar valores dos descritores. Esse filtro remove ambiguidades antes da amostragem; os 12 casos não representam a dificuldade de todos os registros da fonte.

## Cobertura observada
- Datas de publicação de vídeo: **12/12**, extraídas das páginas exatas por ID. Conservado o fuso original e calculada a representação UTC.
- Datas de catálogo Spotify: **12/12**, extraídas do JSON-LD das páginas exatas das faixas. Elas não estabelecem o primeiro lançamento da gravação.
- Candidatos a gênero de catálogo: **11/12**, na busca pública Apple por artista e título, com escopo e edição preservados. São candidatos, não equivalências automáticas com IDs Spotify; a consulta de E-40 não trouxe uma correspondência aceitável.
- Vínculo documental explícito ao álbum: **2/12**; **9/12** permanecem incertos e **1/12** apresenta conflito de versão. Não foi feita identificação por áudio.

O limiar fixado exigia 9 casos completos e pelo menos 2 por faixa. Mesmo que os dois vínculos documentais fossem aceitos como completos após resolver datas/gênero, o teto seria 2/12, com distribuição 1, 0, 1 e 0 por faixa. Logo, a rota não satisfaz o critério. Esse resultado avalia este procedimento e esta seleção; não estima a taxa de erro da base inteira.

## Registro por caso
Datas de catálogo e rótulos abaixo são valores recuperados, não datas de primeiro lançamento ou classificações finais aprovadas. Datas do vídeo estão em UTC.

| Caso | Artista — faixa | Publicação do vídeo | Data Spotify | Gênero candidato Apple | Revisão da gravação |
|---|---|---|---|---|---|
| P01 | The Kooks — Seaside | 2021-07-19 | 2006-01-01 | Alternative | Pendente |
| P02 | Rosa Linn — KING | 2021-09-10 | 2021-09-10 | Indie Pop | Pendente |
| P03 | Dermot Kennedy — Innocence and Sadness | 2022-10-07 | 2022-11-18 | Pop | Vínculo ao álbum documentado |
| P04 | Crowded House — Something So Strong | 2009-02-27 | 1986-01-01 | Rock | Pendente |
| P05 | Outkast — Da Art of Storytellin' (Pt. 1) | 2014-03-15 | 1998-09-29 | Hip-Hop/Rap | Pendente |
| P06 | E-40 — B*tch | 2010-06-24 | 2010-01-01 | Não localizado | Conflito de versão |
| P07 | Papa Roach — Between Angels And Insects | 2009-10-05 | 2000-04-25 | Hard Rock | Pendente |
| P08 | Soundgarden — The Day I Tried To Live | 2010-07-13 | 1994-03-09 | Hard Rock | Pendente |
| P09 | Novo Amor — Anchor | 2015-10-02 | 2017-05-26 | Alternative | Vínculo ao álbum documentado |
| P10 | Darshan Raval — Tera Zikr | 2017-11-09 | 2017-11-09 | Pop | Pendente |
| P11 | AC/DC — Hells Bells | 2013-03-08 | 1980-07-25 | Hard Rock | Pendente |
| P12 | Imagine Dragons — Radioactive | 2012-12-10 | 2012-09-04 | Alternative | Pendente |

Evidências, URLs por campo, durações e justificativas estão em [metadata-review.json](../data/pilot/metadata-review.json). As observações brutas selecionadas estão em [metadata-observations.json](../data/pilot/metadata-observations.json); buscas suplementares em [catalogue-search.json](../data/pilot/catalogue-search.json).

## Problemas concretos encontrados
**Versão diferente apesar da marca de oficial.** P06 aponta para vídeo identificado pelo próprio canal como remix com 50 Cent e Too Short; a faixa do snapshot não é identificada como esse remix. O vídeo tem 244 segundos e a faixa cerca de 203. Não aprovar o pareamento nem substituir pelo remix sem novo registro justificado.

**Data da edição não é início da circulação.** P09 tem vídeo publicado em 2015 e data Spotify de 2017, ligada a Bathing Beach. P03 tem vídeo de outubro de 2022, enquanto a edição do álbum no Spotify informa novembro. A [gravadora já anunciava a faixa em 07/10/2022](https://www.universalmusic.com.br/2022/10/07/se-preparando-para-o-lancamento-de-seu-novo-album-sonder-dermot-kennedy-disponibiliza-a-faixa-innocence-and-sadness/). Calcular tempo de exposição pelo lançamento do álbum produziria uma medida diferente da idade do vídeo.

**Clipes têm duração própria.** P12 tem 261 segundos no vídeo e aproximadamente 187 na faixa. Isso exige verificar edição, trechos narrativos e identidade sonora; a diferença sozinha não prova gravação diferente. O mesmo cuidado vale para durações próximas: elas não provam identidade.

**Gênero e datas variam entre edições/catálogos.** Resultados Apple para a mesma canção podem incluir remasters, apresentações, compilações e covers. P05 tem candidato nominalmente compatível, mas com duração cerca de 19 segundos diferente. Não usar o primeiro resultado de busca como junção automática. Datas em 1º de janeiro e diferenças de um dia também não devem ser tomadas como precisão histórica validada.

**Descrição atual não é fotografia de 2023.** Títulos, créditos e descrição foram consultados agora; podem ter sido atualizados desde a coleta da audiência. Nenhuma visualização atual substituiu os números do snapshot histórico.

## Próxima execução recomendada
1. Manter a pergunta exploratória e comparativa e as visualizações históricas. Não converter o estudo em previsão nem concluir uma relação musical nesta etapa.
2. Definir uma única taxonomia de gênero e um recorte de época antes de selecionar a amostra principal. Os rótulos Apple podem ser uma fonte candidata, com correspondência de edição revisada; não misturá-los automaticamente com track_genre ou gênero do artista.
3. Registrar separadamente data de edição, primeiro lançamento quando verificável e publicação do vídeo. Não inventar precisão nem usar a data de download como data de audiência.
4. Priorizar curadoria manual de um conjunto pequeno dentro desse recorte, documentando exclusões e preservando um mesmo procedimento nos grupos. Excluir conflitos de versão não resolvidos; não excluir apenas por menor audiência ou por resultados musicais inconvenientes.
5. Se o custo continuar incompatível com o workshop, discutir explicitamente uma mudança de fonte/medida. Este relatório não autoriza remover o recorte temporal ou trocar audiência do YouTube por popularity silenciosamente.

A seleção principal permanece vazia. O piloto resolveu a dúvida de acesso público a datas e identificou um gargalo de identidade/semântica, que é diferente de indisponibilidade técnica.

## Reprodução e verificação
```sh
python scripts/select_metadata_pilot.py
python scripts/collect_pilot_metadata.py
python scripts/collect_catalogue_candidates.py
```
A primeira etapa é determinística sobre o snapshot; as consultas de páginas e de catálogo podem mudar. Os registros publicados preservam os valores desta execução, URLs, horários e hashes. HTML e descrições completos ficam locais e não foram publicados. Cache Apple inicial registra horário de salvamento, não um horário de requisição que não foi coletado.

O extrator foi ajustado para tratar JSON-LD em objeto ou lista. As páginas Spotify já obtidas foram reprocessadas pelo cache, sem refazer a consulta. Foram conferidos 12 IDs YouTube, 12 URLs Spotify, reconciliação de exclusões, quatro grupos de três casos e preservação das visualizações históricas. Não há avaliação de áudio nem teste de associação entre descritores e audiência.
