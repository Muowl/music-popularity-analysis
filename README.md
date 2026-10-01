# Music Popularity Analysis

Pesquisa exploratória para o workshop do DCC/UFJF, vinculada à linha de pesquisa do TCC de Sistemas de Informação de Felipe Lazzarini Cunha.

**Estado: linha exploratória e descritiva aceita pelo orientador, conforme relato do autor. Piloto comparativo planejado, ainda não executado. Fonte, recorte, amostra e método operacional permanecem pendentes. Não há resultados deste estudo neste repositório.**

## Motivação, problema e objetivo

A motivação é examinar se diferentes níveis de audiência vêm acompanhados de perfis semelhantes ou distintos nos descritores disponíveis, sem presumir um perfil comum aos sucessos. Isso permitirá identificar relações que mereçam investigação posterior. Trata-se da justificativa deste projeto, não de uma lacuna da literatura já demonstrada.

**Problema de pesquisa — formulação provisória:** Dentro de um recorte definido de gênero e período de lançamento, como se distribuem os descritores musicais entre canções com diferentes níveis de audiência no YouTube?

**Objetivo geral:** descrever e comparar essas distribuições, identificar padrões e heterogeneidade e formular hipóteses para estudos posteriores, respeitando os limites da amostra.

**Contribuição esperada:** caracterização documentada da amostra e hipóteses rastreáveis aos achados, acompanhadas de propostas de teste em novos dados. Distribuições semelhantes também serão relatadas; o estudo não depende de encontrar grandes diferenças.

A prioridade é validar um grupo de comparação com origem e critérios comuns. O piloto verificará acesso, correspondência entre gravações e cobertura dos descritores por nível de audiência antes da análise principal. Se isso for inviável, a descrição de canções de grande audiência permanece como alternativa, mediante decisão registrada. Não buscamos demonstrar uma fórmula do sucesso nem causalidade.

A relação com recomendação baseada em conteúdo é motivação: o estudo examina descritores que podem representar músicas, mas não implementa nem avalia um recomendador. Visualizações não demonstram alcance geográfico global.

A [página exploratória anterior](https://muowl.dev/spotify-dataset-explorer/hits-mundiais.html) é um ponto de partida, não a amostra definitiva. Seus recortes de alcance global, metal e repertório clássico têm critérios distintos. Nenhum deles foi automaticamente importado ou aprovado para o workshop.

## Por onde começar

1. Executar o [plano do piloto](docs/piloto.md), resolver as decisões de [escopo](docs/escopo.md) e registrar os critérios no [protocolo](docs/protocolo.md).
2. Registrar fontes e condições de uso em [data/README.md](data/README.md).
3. Preencher [data/selection/candidates.csv](data/selection/candidates.csv), incluindo exclusões e correspondências incertas.
4. Executar a validação estrutural:
   ```sh
   python scripts/validate_selection.py
   ```
   Requer Python 3.10+ e apenas a biblioteca padrão. Cadastro vazio ou sem casos incluídos termina com código 2: não significa amostra pronta.
5. Congelar a seleção por commit antes da análise principal. Seguir [notebooks/README.md](notebooks/README.md).
6. Gerar figuras, registrar achados e hipóteses conforme [docs/hipoteses.md](docs/hipoteses.md) e escrever no modelo LaTeX existente, conforme [paper/README.md](paper/README.md).

## Organização

As regras de contribuição, mensagens e separação de commits estão em [CONTRIBUTING.md](CONTRIBUTING.md). Agentes devem também seguir [AGENTS.md](AGENTS.md).

| Local | Conteúdo |
|---|---|
| `docs/` | Escopo, protocolo, decisões, fontes acadêmicas e próximos passos |
| `data/selection/` | Cadastro auditável dos candidatos; inicialmente só cabeçalho |
| `data/raw/` | Dados originais locais, ignorados pelo Git |
| `data/processed/` | Dados derivados locais, ignorados pelo Git |
| `scripts/` | Verificações e, posteriormente, processamento reproduzível |
| `notebooks/` | Orientações para os cadernos de análise |
| `figures/` | Figuras finais acompanhadas de origem e método |
| `paper/` | Orientações de redação e entrega |
| `main.tex`, `settings.sty`, `abntex2cite.sty`, `references.bib` | Modelo original preservado na raiz |

## Cuidados de interpretação

Visualizações acumuladas dizem respeito ao vídeo observado, na data da coleta; não são ouvintes únicos nem audiência total da música. Idade do vídeo, exposição, gênero, idioma, artista e formato podem afetar comparações. Descritores do Spotify referem-se a uma gravação; não preencher lacunas com outra versão. Valência não mede o humor do ouvinte.

A bibliografia atual em `references.bib` foi herdada do modelo e **não constitui fundamentação deste tema**. Referências musicais só devem entrar após verificação da publicação e da afirmação sustentada.

O repositório foi encontrado público. Dados brutos, PDFs de terceiros e credenciais não devem ser adicionados automaticamente. Não foi atribuída licença a material de terceiros.
