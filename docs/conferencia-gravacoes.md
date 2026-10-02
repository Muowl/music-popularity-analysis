# Conferência das gravações — fichas dos 12 casos

Preparado em 2026-10-01, sobre o commit `3b17fd31f25c67215419f2cdec42bc0120840292`.

**Estado: triagem documental concluída; P01, P02, P03, P04, P07, P08, P09, P11 e P12 confirmados pelo autor em comparação manual e P05 bloqueado por diferença musical relatada; P10 tem fala adicional sobre a música e elegibilidade pendente; P06 mantém conflito documental sem relato de escuta.** Esta ficha ajuda a executar a conferência do piloto. Não altera o limiar de avanço, os critérios da seleção congelada nem os resultados históricos da etapa documental. Nenhum caso foi incluído na amostra principal.

## O que foi conferido agora

As 12 páginas Spotify dos IDs exatos foram consultadas novamente. Foram registrados créditos de artistas, álbum, duração inteira informada na página e data de catálogo. Os valores do snapshot e as observações anteriores foram preservados separadamente.

As novas consultas ao YouTube falharam com `URLError`; uma consulta diagnóstica ao vídeo P05 recebeu `Tunnel connection failed: 403 Forbidden`. Os títulos, canais e durações YouTube usados aqui vêm de [metadata-observations.json](../data/pilot/metadata-observations.json), com seus horários e hashes originais. Não são novas consultas nem audição dos vídeos. A falha atual de acesso não demonstra que eles tenham sido removidos.

Os resultados estruturados estão em [recording-verification-evidence.json](../data/pilot/recording-verification-evidence.json). A [planilha CSV de conferência](../data/pilot/recording-verification.csv) tem uma linha por par; P01, P02, P03, P04, P07, P08, P09, P11 e P12 registram confirmações; P05 registra o conflito e P10 registra fala sobreposta exclusiva do clipe, com campos não informados em branco. O [caderno de verificação](../notebooks/conferencia-gravacoes.ipynb) confere sua consistência sem renovar dados da rede.

## Achados que orientam a revisão

- **P03 — Dermot Kennedy:** o título preservado é “Innocence and Sadness (Live From Mission Sound Studios, Brooklyn)”; o Spotify identifica a faixa em *Sonder*. Esse título motivou a conferência, agora recebida do autor: ele testou os dois links e confirmou a mesma música e duração. Registrado como `user_confirmed_match`, com fonte humana explícita; detalhes de tomada/master e marcos temporais não foram informados. A [notícia da gravadora](https://www.universalmusic.com.br/2022/10/07/se-preparando-para-o-lancamento-de-seu-novo-album-sonder-dermot-kennedy-disponibiliza-a-faixa-innocence-and-sadness/) confirma a disponibilidade da canção em 07/10/2022, mas não identifica a tomada do vídeo. Ela anuncia uma data futura de álbum; não a usar como comprovação da data efetiva da edição Spotify.
- **P06 — E-40:** a página Spotify credita **E-40, Too $hort**; o título preservado do vídeo credita **E-40, 50 Cent & Too Short**, com “Remix”. A divergência reforça o conflito documental já registrado. Manter esse par bloqueado até resolver a versão; não trocar silenciosamente a faixa ou o vídeo por outro ID.
- **P02 — Rosa Linn:** a página Spotify credita **Rosa Linn, Kiiara**, consistente com “ft. Kiiara” no título preservado do vídeo. O autor confirmou que a parte musical é idêntica do começo ao fim e que o tempo adicional fica no encerramento do videoclipe, sem música. Registrado como `user_confirmed_match`, com origem humana explícita e sem inventar limites temporais exatos.
- **P09 — Novo Amor:** o [site do artista](https://novoamor.co.uk/music/bathing-beach/) lista “Anchor” e seus créditos em *Bathing Beach*. Isso reforça o vínculo ao EP. Posteriormente, o autor confirmou correspondência exata na escuta dos links de P09, registrada como `user_confirmed_match`; o primeiro lançamento da gravação continua por validar.
- **P05 — Outkast:** o autor relata que as versões coincidem até aproximadamente 2:28; depois o Spotify mantém o mesmo cantor e o YouTube passa a outra voz masculina em um trecho mais suave. Isso identifica uma divergência musical no par, registrado como `user_reported_version_conflict` e bloqueado para associar os descritores dessa faixa ao vídeo. Um [catálogo secundário](https://en.wikipedia.org/wiki/Da_Art_of_Storytellin%27_(Pt._1)) lista versão de single com Slick Rick e versão de álbum, mas **a identidade do vocalista adicional não foi confirmada pela conferência relatada**. O artigo tem aviso de referências insuficientes; Slick Rick continua sendo uma pista de crédito.
- **P01 — The Kooks:** o [registro secundário do álbum](https://en.wikipedia.org/wiki/Inside_In/Inside_Out) descreve uma reedição remasterizada de 2021. É uma pista contextual para o crédito de 2021 observado anteriormente, não prova de que o vídeo use esse remaster. O autor confirmou posteriormente a correspondência musical de P01; a relação específica entre masters/edições não foi identificada.

## Pares exatos e perguntas de conferência

A diferença é **duração do vídeo menos duração da faixa no snapshot**, em segundos. A duração Spotify agora observada é inteira; não deve substituir os milissegundos históricos. A ordem sugerida serve apenas para organizar trabalho, sem substituir casos nem favorecer uma faixa de audiência.

| Caso | Par exato | Diferença (s) | Pergunta principal |
|---|---|---:|---|
| P01 | The Kooks — Seaside: [Spotify](https://open.spotify.com/track/0QCuMBeqdWkwFUTO1WlAjH) / [YouTube](https://www.youtube.com/watch?v=OgOwQvNzD-k) | −0,227 | Correspondência exata confirmada pelo autor; relação entre masters/edições pendente. |
| P02 | Rosa Linn — KING: [Spotify](https://open.spotify.com/track/4RgXmdsT0zfYXdrZPW3pV8) / [YouTube](https://www.youtube.com/watch?v=MCt9gfNSyg4) | +8,911 | Parte musical confirmada pelo autor; tempo extra no encerramento sem música. |
| P03 | Dermot Kennedy — Innocence and Sadness: [Spotify](https://open.spotify.com/track/1nJatkqxWH7TQwBrP39yNd) / [YouTube](https://www.youtube.com/watch?v=ufbDvPaVrzs) | −1,658 | Correspondência confirmada pelo autor nos links exatos; metadados e elegibilidade pendentes. |
| P04 | Crowded House — Something So Strong: [Spotify](https://open.spotify.com/track/0eDwzWuy2gf1RJzqWl0dkF) / [YouTube](https://www.youtube.com/watch?v=WyBKzBtaKWM) | +21,427 | Parte musical confirmada; intro e encerramento de cerca de 10 s cada, segundo o autor. |
| P05 | Outkast — Da Art of Storytellin' (Pt. 1): [Spotify](https://open.spotify.com/track/1KQymTxNJfWk6vCD5ywKW2) / [YouTube](https://www.youtube.com/watch?v=F0tamp9XdqU) | +10,347 | Par bloqueado: diferença de voz e trecho após aproximadamente 2:28, relatada pelo autor. |
| P06 | E-40 — B*tch: [Spotify](https://open.spotify.com/track/2twJtqTdddqsTJnEHUFZdm) / [YouTube](https://www.youtube.com/watch?v=VLOz-6V3rPk) | +40,573 | Resolver o remix com 50 Cent; o par está bloqueado por conflito documental. |
| P07 | Papa Roach — Between Angels And Insects: [Spotify](https://open.spotify.com/track/24z528iI9kZu5LbkLainjI) / [YouTube](https://www.youtube.com/watch?v=H2jCbXiEQI4) | +2,533 | Correspondência exata confirmada pelo autor; valores históricos preservados. |
| P08 | Soundgarden — The Day I Tried To Live: [Spotify](https://open.spotify.com/track/78YJJJH55MSyk7547100sW) / [YouTube](https://www.youtube.com/watch?v=dbckIuT_YDc) | −0,107 | Correspondência exata confirmada pelo autor; relação específica de master pendente. |
| P09 | Novo Amor — Anchor: [Spotify](https://open.spotify.com/track/7qH9Z4dJEN0l9bidizW7fq) / [YouTube](https://www.youtube.com/watch?v=OmKAn8rNbKg) | −1,533 | Correspondência exata confirmada pelo autor; datas e elegibilidade pendentes. |
| P10 | Darshan Raval — Tera Zikr: [Spotify](https://open.spotify.com/track/0OfaueVeRebAfWsAHajj3z) / [YouTube](https://www.youtube.com/watch?v=eK0IIyBlYew) | +15,500 | Introdução e fala feminina sobreposta relatadas; base musical no geral igual, elegibilidade pendente. |
| P11 | AC/DC — Hells Bells: [Spotify](https://open.spotify.com/track/69QHm3pustz01CJRwdo20z) / [YouTube](https://www.youtube.com/watch?v=etAIpkdhU9Q) | −2,293 | Mesma música confirmada pelo autor; clipe percebido cerca de 2 s adiantado. |
| P12 | Imagine Dragons — Radioactive: [Spotify](https://open.spotify.com/track/4G8gkOterJn0Ywt6uhqbhp) / [YouTube](https://www.youtube.com/watch?v=ktvTqknDobU) | +74,187 | Conteúdo musical confirmado pelo autor; extensão atribuída a cenas narrativas. |

P01, P02, P03, P04, P07, P08, P09, P11 e P12 já receberam confirmação do autor; P05 recebeu relato de conflito musical. P06 continua bloqueado por conflito documental de remix. P10 recebeu relato de fala sobreposta à música e continua com elegibilidade pendente. A sequência de escuta proposta foi concluída; resta adjudicar a sobreposição em P10 e os campos/recorte do estudo. Todos os mesmos 12 casos congelados continuam registrados, inclusive os conflitos.

## Como preencher uma ficha

1. Abrir a faixa e o vídeo pelos **links exatos**. Se a plataforma redirecionar ou indisponibilizar a faixa, registrar isso; uma busca pelo título pode trazer outra edição.
2. Registrar revisor, horário UTC e créditos/versão disponíveis. Anotar ISRC e edição se estiverem acessíveis. O mesmo ISRC é evidência documental útil, mas não resolve sozinho possíveis cortes ou substituições no clipe.
3. Ouvir as duas versões por inteiro, alternando trechos para comparar. Encontrar o primeiro som musical comum e anotar o instante em cada plataforma; não comparar apenas o mesmo segundo no relógio.
4. Registrar pelo menos três marcos correspondentes: começo, um trecho no meio e encerramento. Podem ser uma entrada vocal, uma palavra específica, um riff ou um golpe de bateria. Esses marcos documentam a revisão completa; três trechos isolados não provam ausência de diferenças no restante.
5. Comparar participantes, tomada vocal (fraseado, respirações e ataques), instrumentos/arranjo, palavras omitidas ou alteradas, cortes, trechos adicionais e final/fade. Explicar a diferença de duração com observações; não presumir que ela seja apenas silêncio ou narrativa.
6. Separar **mesma composição**, **mesma tomada/performance** e **mesma edição/master**. A composição pode coincidir em um remix ou numa apresentação distinta. A escuta pode apoiar a identidade da tomada, mas raramente resolve com segurança diferenças sutis de master. Registrar essa limitação.
7. Preencher a avaliação como “compatível com a mesma tomada”, “versão diferente” ou “inconclusivo”, com os tempos e as fontes que sustentam a resposta. Esses são rótulos de trabalho da ficha; não substituem os `match_status` do protocolo nem aprovam automaticamente a inclusão. Evitar “idêntico” quando a evidência só demonstra compatibilidade.

Se a dúvida persistir, manter incerto. Se houver versão diferente, registrar a diferença concreta e conservar os dois IDs como evidência do pareamento problemático. Não atribuir os descritores de uma faixa a outra gravação.

## Conferência recebida: P02

Em resposta aos links exatos de [KING no Spotify, ID 4RgXmdsT0zfYXdrZPW3pV8](https://open.spotify.com/track/4RgXmdsT0zfYXdrZPW3pV8) e [vídeo Rosa Linn no YouTube, ID MCt9gfNSyg4](https://www.youtube.com/watch?v=MCt9gfNSyg4), o autor informou:

> O tempo extra se explica no final da musica com um encerramento sem musica
>
> De resto é idêntico do começo até esses segundos extras de encerramento do videoclipe

Registrado como **correspondência da parte musical confirmada pelo autor em conferência manual** (`user_confirmed_match`). O tempo extra foi atribuído ao encerramento do clipe após a música; não foi relatada divergência dentro da parte musical. Não foram informados os instantes exatos do fim da música nem a presença de outros sons no trecho sem música. O assistente não realizou escuta independente.

Os valores históricos continuam separados: faixa com 203,089 segundos e vídeo com 212 segundos, diferença de 8,911 segundos. Essa diferença do arquivo completo não é usada para rejeitar o par diante da explicação musical relatada pelo autor. Não atribuir precisão de 8,911 segundos à duração do encerramento observado sem uma medição própria. Gênero, interpretação das datas e elegibilidade continuam pendentes.

## Conferência recebida: P03

O autor confirmou ter testado [Sonder no Spotify, ID 1nJatkqxWH7TQwBrP39yNd](https://open.spotify.com/track/1nJatkqxWH7TQwBrP39yNd) e [Live From Mission Sound Studios no YouTube, ID ufbDvPaVrzs](https://www.youtube.com/watch?v=ufbDvPaVrzs).

Relato recebido nesta conversa:

> Confirmo que P03 é o mesmo no YouTube e no Spotify, testei os links e tem mesma duração e mesma música

Registrado como **correspondência confirmada pelo autor em conferência manual** (`user_confirmed_match`). O horário de registro está na evidência JSON e no CSV; o horário exato da escuta não foi informado. O assistente não realizou escuta independente. Não foram informados marcos temporais, durações numéricas, verificação separada de voz/piano ou identificação de master; esses campos permanecem sem preenchimento.

“Mesma duração” é a observação qualitativa do autor. As medições anteriores continuam preservadas: faixa no snapshot com 252,658 segundos e vídeo com 251 segundos, diferença de −1,658 segundo. Não substituir esses valores por zero nem atribuir uma causa à pequena diferença sem evidência.

Esta confirmação avança a correspondência da gravação. Gênero, interpretação das datas e elegibilidade para o recorte principal permanecem pendentes.

## Conferência recebida: P05

Em resposta aos links exatos de [Aquemini no Spotify, ID 1KQymTxNJfWk6vCD5ywKW2](https://open.spotify.com/track/1KQymTxNJfWk6vCD5ywKW2) e [vídeo Outkast no YouTube, ID F0tamp9XdqU](https://www.youtube.com/watch?v=F0tamp9XdqU), o autor informou:

> Essa musica é identica até o minuto 2:28, o Spotify continua com o mesmo homem cantando e o YouTube com outro em um trecho mais suave
>
> YouTube tem 3:53 e Spotify 3:42

Registrado como **conflito de versão por comparação manual relatada pelo autor** (`user_reported_version_conflict`). O marco de aproximadamente 2:28 corresponde a 148 segundos; não foram informados relógios separados para cada plataforma. A mudança de voz e trecho musical sustenta bloquear o pareamento, independentemente da diferença de duração. Não foi atribuída identidade ao vocalista adicional nem um nome definitivo à edição/remix.

As durações exibidas relatadas são YouTube 233 segundos e Spotify 222 segundos, diferença de 11 segundos. Os valores históricos permanecem separados: vídeo 233 segundos e faixa no snapshot 222,653 segundos, diferença de 10,347 segundos. Não interpretar a precisão inteira do relato como revisão do snapshot.

O horário de registro está na evidência JSON e no CSV; o horário exato da escuta não foi informado. Não substituir a faixa Spotify ou o vídeo, nem transportar os descritores da faixa para a versão divergente. O caso permanece no piloto como evidência de perda de correspondência; nenhum candidato da amostra principal foi preenchido.

## Conferência recebida: P07

Em resposta aos links exatos de [Between Angels And Insects no Spotify, ID 24z528iI9kZu5LbkLainjI](https://open.spotify.com/track/24z528iI9kZu5LbkLainjI) e [vídeo Papa Roach no YouTube, ID H2jCbXiEQI4](https://www.youtube.com/watch?v=H2jCbXiEQI4), o autor informou:

> Confirmado a correspondência exata entre youtube e spotify

Registrado como **correspondência confirmada pelo autor em conferência manual** (`user_confirmed_match`). O relato não detalha marcos temporais, verificações separadas de censura ou identificação de master. O horário de registro está no JSON e no CSV; o horário exato da escuta não foi informado. O assistente não realizou escuta independente.

As medidas anteriores permanecem preservadas: faixa no snapshot com 234,467 segundos e vídeo com 237 segundos, diferença de 2,533 segundos. Não foram fornecidas novas durações nem causa específica para essa diferença. A confirmação avança a correspondência da gravação; gênero, datas e inclusão na amostra principal continuam pendentes.

## Conferência recebida: P09

Em resposta aos links exatos de [Anchor no Spotify, ID 7qH9Z4dJEN0l9bidizW7fq](https://open.spotify.com/track/7qH9Z4dJEN0l9bidizW7fq) e [vídeo Novo Amor no YouTube, ID OmKAn8rNbKg](https://www.youtube.com/watch?v=OmKAn8rNbKg), o autor informou:

> Correspondência exata

Registrado como **correspondência confirmada pelo autor em conferência manual** (`user_confirmed_match`). O assistente não realizou escuta independente; marcos temporais e master não foram detalhados. O horário de registro está no JSON e no CSV, separado do horário desconhecido da escuta.

As medidas anteriores são preservadas: faixa no snapshot com 257,533 segundos e vídeo com 256 segundos, diferença de −1,533 segundo. Não foram fornecidas novas medidas ou causa para essa diferença. A confirmação musical não resolve a distinção entre vídeo de 2015 e edição do EP de 2017, nem aprova gênero ou inclusão na amostra principal.

## Conferência recebida: P11

Em resposta aos links exatos de [Hells Bells no Spotify, ID 69QHm3pustz01CJRwdo20z](https://open.spotify.com/track/69QHm3pustz01CJRwdo20z) e [vídeo AC/DC no YouTube, ID etAIpkdhU9Q](https://www.youtube.com/watch?v=etAIpkdhU9Q), o autor informou:

> Correspondência praticamente perfeita, o clipe parece estar 2 segundos na frente da musica no Spotify, mas a rigor é a mesma musica

Registrado como **correspondência musical confirmada pelo autor em conferência manual** (`user_confirmed_match`), com observação de alinhamento: o vídeo parece aproximadamente dois segundos adiantado. Não se inferiu corte, silêncio, outra gravação ou deslocamento constante medido. O assistente não realizou escuta independente, e master/ISRC não foram identificados.

As durações históricas permanecem separadas: faixa no snapshot com 312,293 segundos e vídeo com 310 segundos, diferença de −2,293 segundos. A observação de alinhamento não substitui essas medidas nem estabelece a causa da diferença de duração. O horário de registro está no JSON e no CSV; gênero, datas e elegibilidade continuam pendentes.

## Conferência recebida: P01

Em resposta aos links exatos de [Seaside no Spotify, ID 0QCuMBeqdWkwFUTO1WlAjH](https://open.spotify.com/track/0QCuMBeqdWkwFUTO1WlAjH) e [vídeo The Kooks no YouTube, ID OgOwQvNzD-k](https://www.youtube.com/watch?v=OgOwQvNzD-k), o autor informou:

> Correspondência exata

Registrado como **correspondência confirmada pelo autor em conferência manual** (`user_confirmed_match`). O assistente não realizou escuta independente; ISRC e relação específica entre master original e possível remaster não foram identificados. O relato não atribui o áudio do vídeo à edição de 2021.

As medidas históricas permanecem: faixa no snapshot com 99,227 segundos e vídeo com 99 segundos, diferença de −0,227 segundo. O horário de registro está no JSON e no CSV; o horário exato da escuta e novas medidas não foram informados. Gênero, interpretação das datas e elegibilidade continuam pendentes.

## Conferência recebida: P04

Em resposta aos links exatos de [Something So Strong no Spotify, ID 0eDwzWuy2gf1RJzqWl0dkF](https://open.spotify.com/track/0eDwzWuy2gf1RJzqWl0dkF) e [vídeo Crowded House no YouTube, ID WyBKzBtaKWM](https://www.youtube.com/watch?v=WyBKzBtaKWM), o autor informou:

> a música a rigor é a mesma, o video no youtube tem uma intro de 10 segundos e um final com 10 segundos mostrando a capa do album, de resto a música corresponde de forma identica

Registrado como **correspondência da parte musical confirmada pelo autor em conferência manual** (`user_confirmed_match`). A introdução e o encerramento adicionais explicam qualitativamente o tempo extra do videoclipe. O relato não especifica silêncio, música ou outros sons nesses segmentos; o encerramento mostra a capa do álbum. O assistente não realizou escuta independente, nem identificou o master.

Os cerca de 10 segundos por segmento são observações inteiras relatadas, sem limites exatos medidos. As medidas anteriores permanecem separadas: faixa no snapshot com 171,573 segundos e vídeo com 193 segundos, diferença de 21,427 segundos. Não substituir essa diferença por 20 segundos. O horário de registro está no JSON e no CSV; gênero, interpretação das datas e elegibilidade continuam pendentes.

## Conferência recebida: P08

Em resposta aos links exatos de [The Day I Tried To Live no Spotify, ID 78YJJJH55MSyk7547100sW](https://open.spotify.com/track/78YJJJH55MSyk7547100sW) e [vídeo Soundgarden no YouTube, ID dbckIuT_YDc](https://www.youtube.com/watch?v=dbckIuT_YDc), o autor informou:

> correspondencia exata

Registrado como **correspondência confirmada pelo autor em conferência manual** (`user_confirmed_match`). O assistente não realizou escuta independente; ISRC e relação específica entre o master do clipe e a edição Deluxe não foram identificados. Não foram fornecidos marcos temporais ou medidas novas.

As durações históricas permanecem: faixa no snapshot com 320,107 segundos e vídeo com 320 segundos, diferença de −0,107 segundo. O horário de registro está no JSON e no CSV; gênero, interpretação das datas e elegibilidade continuam pendentes.

## Conferência recebida: P10

Em resposta aos links exatos de [Tera Zikr no Spotify, ID 0OfaueVeRebAfWsAHajj3z](https://open.spotify.com/track/0OfaueVeRebAfWsAHajj3z) e [vídeo Darshan Raval no YouTube, ID eK0IIyBlYew](https://www.youtube.com/watch?v=eK0IIyBlYew), o autor informou:

> essa musica tem uma particularidade, os primeiros 20 segundos sao uma introdução do videoclipe, começa a musica, uma mulher fala uma frase (por cima da musica, que não tem no spotify) e o resto da musica no geral é a mesma

Registrado como **base musical geralmente correspondente, com fala adicional exclusiva do videoclipe** (`user_reported_video_audio_overlay`). Há introdução de cerca de 20 segundos antes do início da música e uma frase feminina sobreposta à música. O relato diz que o restante é “no geral” igual; não se registrou correspondência exata integral nem identidade de remix ou outra tomada.

A fala altera o áudio do trecho musical. A elegibilidade permanece `pending_overlay_adjudication`: é preciso registrar o intervalo da sobreposição e resolver explicitamente como o critério existente de versão se aplica a esse caso. A duração sozinha não decide isso. Não houve exclusão definitiva nem relaxamento automático dos critérios; o cadastro principal permanece vazio.

As medidas históricas continuam separadas: faixa no snapshot com 208,500 segundos e vídeo com 224 segundos, diferença de 15,500 segundos. A introdução de cerca de 20 segundos não é uma decomposição medida dessa diferença. Não inferir cortes, duração da fala ou limites do trecho a partir desses valores. O assistente não realizou escuta independente; palavras e intervalo exato da fala não foram informados. O horário de registro está no JSON e no CSV.

## Conferência recebida: P12

Em resposta aos links exatos de [Radioactive no Spotify, ID 4G8gkOterJn0Ywt6uhqbhp](https://open.spotify.com/track/4G8gkOterJn0Ywt6uhqbhp) e [vídeo Imagine Dragons no YouTube, ID ktvTqknDobU](https://www.youtube.com/watch?v=ktvTqknDobU), o autor informou:

> Essa música é a rigor a mesma chat. O que acontece é que no videoclipe do YouTube existem sequências bem artísticas que mostram, por exemplo, no começo, no meio e ao final um cadinho. Ou seja, durante o videoclipe, sequências de animais ali de pelúcia lutando, mas o conteúdo da música acaba sendo o mesmo. Essa extensão se dá essa questão de durante o clipe ter esses pontos em que tem essa situação até mesmo antietral.

Registrado como **correspondência do conteúdo musical confirmada pelo autor em conferência manual** (`user_confirmed_match`). A extensão do clipe foi atribuída a cenas narrativas no começo, meio e final, incluindo animais de pelúcia lutando. O relato não detalha os limites dessas cenas, pausas ou efeitos/falas sobrepostos individualmente. Não se afirmou identidade da linha temporal completa do vídeo com a faixa. O assistente não realizou escuta independente nem identificou master/ISRC.

As medidas históricas permanecem: faixa no snapshot com 186,813 segundos e vídeo com 261 segundos, diferença de 74,187 segundos. Não distribuir esse tempo entre cenas sem medição. O horário de registro está no JSON e no CSV; gênero, interpretação das datas e elegibilidade continuam pendentes.

## Consolidação da conferência

A sequência reuniu 11 relatos de escuta do autor; P06 conserva o conflito documental já observado, sem novo relato de escuta. A classificação atual dos 12 pares é:

| Situação da correspondência | Casos | Quantidade |
|---|---|---:|
| Conteúdo musical confirmado pelo autor | P01, P02, P03, P04, P07, P08, P09, P11, P12 | 9 |
| Conflito de versão | P05 (escuta relatada), P06 (evidência documental) | 2 |
| Base musical geralmente correspondente com fala sobreposta; elegibilidade pendente | P10 | 1 |

Os rótulos da ficha são evidências suplementares de revisão, não substituem automaticamente os `match_status` do protocolo. Preservam-se os 12 IDs originais e os resultados históricos da etapa documental. Estas contagens não estimam a taxa de erro da fonte inteira.

### O critério de avanço continua não atendido

O mínimo do piloto era 9 casos com todos os campos completos e pelo menos 2 em cada faixa. A conferência musical isolada tem a seguinte distribuição:

| Faixa histórica de visualizações | Confirmados musicalmente pelo autor | Total congelado |
|---|---:|---:|
| Menos de 1 milhão | 3 | 3 |
| 1 a menos de 10 milhões | 1 | 3 |
| 10 a menos de 100 milhões | 3 | 3 |
| 100 milhões ou mais | 2 | 3 |

A faixa de **1 a menos de 10 milhões** tem apenas P04 confirmado; P05 e P06 apresentam conflito de versão. Assim, o requisito de pelo menos 2 nessa faixa falha mesmo antes de resolver gênero e datas. Resolver P10 também não corrige essa faixa. Nove confirmações musicais não são nove casos completos aprovados.

Não substituir P05/P06 silenciosamente nem relaxar o mínimo após observar o resultado. A amostra principal segue vazia. Para avançar, registrar explicitamente a revisão de rota/recorte e o tratamento de edições de clipe antes de uma nova seleção; manter como candidato um conjunto pequeno de um único gênero/época, com datas e versões verificadas.

### Pendência específica de P10

Registrar o início/fim da fala feminina sobreposta e identificar o que acontece à base musical nesse trecho. A elegibilidade depende de como o protocolo trata a gravação-base e a edição do clipe; esta conferência não decide esse critério. A presença de fala sobre a música foi relatada em P10; em P12 há confirmação de conteúdo musical com cenas narrativas, sem detalhamento de sobreposições. Nenhum deles foi automaticamente aprovado para a análise principal.

## Limites e uso no estudo

O assistente não fez audição, fingerprint nem extração de ISRC. Há onze relatos de comparação manual fornecidos pelo autor: confirmações em P01, P02, P03, P04, P07, P08, P09, P11 e P12, divergência musical em P05 e fala sobreposta exclusiva do clipe em P10. P06 mantém o conflito documental anterior. O resultado histórico da etapa documental — dois vínculos ao álbum, nove casos incertos e um conflito de versão — é preservado; os novos relatos constam como evidências posteriores separadas.

Mesmo depois da conferência sonora, ainda será necessário resolver gênero com escopo explícito, datas e recorte antes de aprovar a amostra principal. As visualizações históricas permanecem as do snapshot. Os 12 casos continuam sendo piloto de viabilidade, e não amostra do artigo.

Consultar o [protocolo](protocolo.md), a [regra congelada](piloto-metadados.md) e o [relatório anterior](relatorio-piloto-metadados.md). Qualquer mudança efetiva de critério, fonte ou desenho precisa de registro em `docs/decisoes.md`; esta ficha não toma essa decisão.
