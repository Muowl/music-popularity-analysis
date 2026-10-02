# Literatura a verificar

Esta lista é uma fila de leitura, não uma bibliografia validada para citar.

| Material já discutido | Papel possível | Verificação pendente |
|---|---|---|
| Content-driven music recommendation: Evolution, state of the art, and challenges | Conexão entre descritores e recomendação por conteúdo | Metadados, publicação e trechos pertinentes |
| Considering emotions and contextual factors in music recommendation: a systematic literature review | Delimitar conteúdo, emoção e contexto | Evitar usar emoção percebida como estado do ouvinte |
| Current challenges and visions in music recommender systems research | Contextualização em MRS | Relação direta com a pergunta do workshop |
| Estudos específicos de características musicais e popularidade | Trabalhos relacionados centrais | Buscar e verificar publicações revisadas por pares |

Para cada referência, registrar autores, ano, veículo, DOI/identificador, evidência de publicação/revisão por pares, afirmação sustentada e limites. Relatórios de IA não são fundamentação científica. Não copiar PDFs para o repositório automaticamente.

`references.bib` conserva exemplos herdados não validados; duas entradas verificadas foram acrescentadas e são as únicas citadas na página atual.

## Fontes verificadas para o rascunho

Metadados e resumo das duas publicações foram conferidos via Crossref, com data, URL e hash em `data/workshop/reference-evidence.json`. A verificação **não incluiu leitura integral dos artigos**. As afirmações citadas estão limitadas ao escopo verificado.

| Publicação | Publicação e DOI confirmados | Afirmação sustentada e limite |
|---|---|---|
| Schedl, Gómez e Urbano (2014), Music Information Retrieval: Recent Developments and Applications | Foundations and Trends in Information Retrieval, 8(2–3), 127–261; [10.1561/1500000042](https://doi.org/10.1561/1500000042) | Revisão de representações de áudio/contexto e tarefas de recuperação; não demonstra relação dos nossos três atributos com visualizações. |
| Askin e Mauskapf (2017), What Makes Popular Culture Popular? Product Features and Optimal Differentiation in Music | American Sociological Review, 82(5), 910–944; [10.1177/0003122417728662](https://doi.org/10.1177/0003122417728662) | Estudo relacionou características musicais e desempenho no Billboard Hot 100; não valida causalidade no YouTube ou generalização desta seleção. |

São publicações em periódicos acadêmicos; a identificação como tal foi conferida nos registros de publicação. Crossref não constitui auditoria do processo individual de revisão editorial.

As definições de energy, danceability e acousticness foram conferidas na [documentação primária Spotify](https://developer.spotify.com/documentation/web-api/reference/get-audio-features), também registrada no arquivo de evidências. Audiência e seleção são do snapshot Rastelli; gênero é do rótulo da fonte Pandya, com versões e condições de uso em `data/source-manifest.json`. A documentação das fontes serve aos seus campos, sem substituir fundamentação científica.
