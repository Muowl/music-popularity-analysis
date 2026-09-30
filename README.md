# Music Popularity Analysis

Pesquisa exploratória para o workshop do DCC/UFJF, vinculada à linha de pesquisa do TCC de Sistemas de Informação de Felipe Lazzarini Cunha.

**Estado: estrutura inicial. Pergunta, amostra e método ainda aguardam definição e alinhamento com o orientador. Não há resultados deste estudo neste repositório.**

## Pergunta de trabalho — provisória

Como se distribuem os descritores musicais em uma seleção de canções de grande audiência no YouTube?

O objetivo inicial proposto é descrever características e heterogeneidade dos casos selecionados. Investigar associação entre características e níveis de popularidade é uma alternativa que exige outro desenho, com grupo de comparação. Não buscamos demonstrar uma fórmula do sucesso nem causalidade.

A [página exploratória anterior](https://muowl.dev/spotify-dataset-explorer/hits-mundiais.html) é um ponto de partida, não a amostra definitiva. Seus recortes de alcance global, metal e repertório clássico têm critérios distintos. Nenhum deles foi automaticamente importado ou aprovado para o workshop.

## Por onde começar

1. Resolver as decisões de [escopo](docs/escopo.md) e registrar os critérios no [protocolo](docs/protocolo.md).
2. Registrar fontes e condições de uso em [data/README.md](data/README.md).
3. Preencher [data/selection/candidates.csv](data/selection/candidates.csv), incluindo exclusões e correspondências incertas.
4. Executar a validação estrutural:
   ```sh
   python scripts/validate_selection.py
   ```
   Requer Python 3.10+ e apenas a biblioteca padrão. Cadastro vazio ou sem casos incluídos termina com código 2: não significa amostra pronta.
5. Congelar a seleção por commit antes da análise principal. Seguir [notebooks/README.md](notebooks/README.md).
6. Gerar figuras e escrever no modelo LaTeX existente, conforme [paper/README.md](paper/README.md).

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
