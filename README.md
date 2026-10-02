# Music Popularity Analysis

Pesquisa exploratória para o workshop do DCC/UFJF, vinculada à linha de pesquisa do TCC de Sistemas de Informação de Felipe Lazzarini Cunha.

Comparação exploratória de descritores musicais em 17 pares Spotify–YouTube rotulados Hard Rock, com datas de catálogo de 1980–1989.
Versão de uma página preparada para submissão: [artigo em PDF](paper/workshop-hard-rock.pdf), com hipótese pós-hoc e limitações explícitas.

O caminho de execução está em [implementacao-workshop.md](docs/implementacao-workshop.md), com [protocolo e adjudicação](docs/workshop-protocolo.md), [conferência](docs/conferencia-hard-rock.md), [resultados](docs/resultados-hard-rock.md) e [caderno executado](notebooks/03_hard_rock_results.ipynb). O [PDF de uma página](paper/workshop-hard-rock.pdf) é a versão preparada para submissão. A década se refere ao catálogo Spotify, não a primeiros lançamentos já validados.

## Motivação, problema e objetivo

A motivação é examinar se diferentes níveis de audiência vêm acompanhados de perfis semelhantes ou distintos nos descritores disponíveis, sem presumir um perfil comum aos sucessos. Isso permitirá identificar relações que mereçam investigação posterior. Trata-se da justificativa deste projeto, não de uma lacuna da literatura já demonstrada.

**Problema de pesquisa:** Como se distribuem energia, dançabilidade e acusticidade entre faixas rotuladas `hard-rock`, com datas de catálogo Spotify de 1980–1989, associadas a vídeos abaixo e acima do corte de audiência histórica da seleção?

**Objetivo geral:** descrever e comparar essas distribuições, identificar padrões e heterogeneidade e formular hipóteses para estudos posteriores, respeitando os limites da amostra.

**Contribuição esperada:** caracterização documentada da amostra e hipóteses rastreáveis aos achados, acompanhadas de propostas de teste em novos dados. Distribuições semelhantes também serão relatadas; o estudo não depende de encontrar grandes diferenças.

A comparação foi executada com critérios comuns, 17 pares curados e grupos congelados. A sensibilidade pós-hoc de HR02/HR10 preserva a direção dos contrastes de energia e dançabilidade. Datas de publicação foram recuperadas para os 20 candidatos; o tempo desde a publicação é descrito, sem ajuste estatístico da comparação. Não buscamos demonstrar uma fórmula do sucesso nem causalidade.

A relação com recomendação baseada em conteúdo é motivação: o estudo examina descritores que podem representar músicas, mas não implementa nem avalia um recomendador. Visualizações não demonstram alcance geográfico global.

A [página exploratória anterior](https://muowl.dev/spotify-dataset-explorer/hits-mundiais.html) é um ponto de partida, não a amostra definitiva. Seus recortes de alcance global, metal e repertório clássico têm critérios distintos. Nenhum deles foi automaticamente importado ou aprovado para o workshop.

## Resultados do piloto

A [auditoria das fontes](docs/relatorio-piloto-fontes.md) encontrou cobertura desigual no cruzamento e ausência de datas de lançamento/publicação. A recomendação é investigar a base já pareada Spotify–YouTube e a viabilidade de enriquecimento documental antes de fixar o recorte. As contagens de audiência disponíveis são históricas, declaradas como coletadas em fevereiro de 2023.

A [segunda etapa, com 12 casos congelados](docs/relatorio-piloto-metadados.md), recuperou datas dos 12 vídeos e das 12 páginas Spotify e encontrou candidatos a gênero para 11 casos. Só dois pares tiveram vínculo documental explícito ao álbum; nove permanecem incertos e um tem conflito de versão. A recomendação é curadoria manual com um recorte único, sem importar automaticamente os pareamentos.

A [conferência suplementar relatada pelo autor](docs/conferencia-gravacoes.md) preserva essa etapa histórica e registra a avaliação musical atual: nove confirmações, dois conflitos e uma fala exclusiva. Confirmação musical não é aprovação de todos os campos ou da amostra principal. A nova seleção não reaproveita automaticamente esses casos.

## Reprodução e revisão atual

Seguir os comandos de [implementação](docs/implementacao-workshop.md). O [protocolo específico](docs/workshop-protocolo.md) governa a análise atual; documentos do piloto preservam o histórico.

Consultar [resultados e sensibilidade](docs/resultados-hard-rock.md), [metadados dos vídeos](data/workshop/video-metadata.json) e [auditoria da seleção](docs/auditoria-selecao.md). Uma coleta posterior em 2026-10-02 verificou 176/176 páginas e reproduziu as 47 faixas elegíveis, os mesmos 20 artistas/IDs e o corte original. O ZIP foi conferido independentemente por hashes e nova extração dos HTML. Isso reproduz a seleção com metadados posteriores; o cache original permanece indisponível.

A revisão editorial final explicita os grupos relativos ao recorte, a composição por subestilo como explicação alternativa e a incerteza sobre masters. Permanecem a ausência de validação técnica de master, o formato desconhecido de 12 vídeos e a indisponibilidade do cache original, distinguida da reprodução posterior concluída.

## Organização

As regras de contribuição, mensagens e separação de commits estão em [CONTRIBUTING.md](CONTRIBUTING.md). Agentes devem também seguir [AGENTS.md](AGENTS.md).

| Local | Conteúdo |
|---|---|
| `docs/` | Escopo, protocolo, decisões, fontes acadêmicas e próximos passos |
| `data/selection/` | Cadastro dos 20 candidatos, 17 incluídos e três excluídos |
| `data/workshop/` | Lock dos IDs e grupos, cadastro de revisão e evidências bibliográficas |
| `data/raw/` | Dados originais locais, ignorados pelo Git |
| `data/processed/` | Dados derivados locais, ignorados pelo Git |
| `scripts/` | Coleta, auditoria, análise principal, sensibilidade e compilação |
| `notebooks/` | Auditoria, prévia histórica e resultados curados executados |
| `figures/` | Figuras finais acompanhadas de origem e método |
| `paper/` | Orientações de redação e entrega |
| `main.tex`, `settings.sty`, `abntex2cite.sty`, `references.bib` | Modelo original preservado na raiz |

## Cuidados de interpretação

Visualizações acumuladas dizem respeito ao vídeo observado, na data da coleta; não são ouvintes únicos nem audiência total da música. Idade do vídeo, exposição, gênero, idioma, artista e formato podem afetar comparações. Descritores do Spotify referem-se a uma gravação; não preencher lacunas com outra versão. Valência não mede o humor do ouvinte.

A bibliografia em `references.bib` conserva as entradas herdadas, não validadas para este tema. A página cita somente duas novas referências musicais com publicação, metadados e relação com a afirmação verificados, conforme `data/workshop/reference-evidence.json`; a verificação se limitou aos metadados e resumos disponíveis.

O repositório foi encontrado público. Dados brutos, PDFs de terceiros e credenciais não devem ser adicionados automaticamente. Não foi atribuída licença a material de terceiros.
