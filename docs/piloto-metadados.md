# Piloto de acesso a metadados — regra v1

Definido em 2026-10-01 antes da pesquisa dos metadados dos casos selecionados.

## Pergunta desta etapa
Conseguimos recuperar publicação do vídeo, lançamento da edição/gravação, gênero com escopo explícito e evidências da correspondência Spotify–YouTube a partir de fontes públicas?

Este é um teste de acesso e curadoria em diferentes faixas de audiência. Não é a amostra final: gênero e época ainda não podem ser usados como filtros porque são precisamente os campos cuja obtenção está em teste. Não calcular diferenças dos descritores musicais nesta etapa.

## Seleção congelada
- Usar o snapshot Spotify and Youtube da etapa anterior, conferido por SHA-256.
- Excluir, nesta ordem: URL/visualizações ausentes ou inválidas; registros não marcados como official_video=True pelo publicador; URI ou URL que se repita em qualquer linha da fonte.
- Esta restrição simplifica a primeira auditoria, mas exclui ambiguidades e pode favorecer registros mais fáceis. Não é solução definitiva para as duplicações do estudo.
- Usar quatro faixas históricas: menos de 1 milhão; 1 a menos de 10 milhões; 10 a menos de 100 milhões; a partir de 100 milhões de visualizações.
- Ordenar cada faixa pelo SHA-256 de seed|Uri|Url_youtube, com seed metadata-pilot-v1-2026-10-01. Selecionar os três primeiros casos: 12 no total. Não substituir falhas de recuperação por outros casos.
- O algoritmo não lê valores dos descritores para selecionar casos. Não filtrar por familiaridade de título, artista ou idioma.
- Executar `python scripts/select_metadata_pilot.py`; resultado em data/pilot/metadata-candidates.json, separado do cadastro principal.

## Coleta e distinções obrigatórias
Consultar primeiro as páginas públicas exatas do vídeo e da faixa. Para campos ausentes, buscar páginas do artista, gravadora, distribuidor ou catálogo estruturado com identificação da edição. Preservar URL, data de consulta, status e evidência curta para cada campo.

- Publicação do vídeo não é lançamento da gravação. Data de edição/reedição não é necessariamente primeiro lançamento.
- Gênero de artista ou álbum não deve ser promovido a gênero da faixa sem indicar o escopo; taxonomias diferentes exigem regra de harmonização antes do estudo.
- Título e artista compatíveis são indícios, não prova de identidade da gravação. Créditos de edição/álbum/ISRC e duração ajudam; conflito não resolvido mantém correspondência incerta.
- Página indisponível é falha de acesso desta tentativa, não demonstra inexistência do dado ou remoção definitiva.
- Contagens novas não substituem as visualizações históricas de 2023. Data/hora de consulta de metadados não é data/hora da medição de audiência.
- Não interpretar uma data em texto livre como campo validado sem revisar seu contexto.

## Critério operacional de avanço
Para considerar a rota pronta para ampliar a curadoria, exigir ao menos 9 dos 12 casos com o conjunto completo de campos requeridos documentado e ao menos 2 dos 3 em cada faixa. Esse é um limiar prático de esforço/cobertura, não um cálculo de tamanho amostral ou garantia estatística. Gênero apenas de artista, correspondência incerta ou data de edição ambígua não satisfazem o conjunto completo.

Se não atingir esse critério, relatar quais campos/rotas falharam e propor ajuste explícito de fonte ou recorte. Não relaxar o limiar após ver o resultado. Doze casos não estimam com precisão a cobertura do dataset inteiro.
