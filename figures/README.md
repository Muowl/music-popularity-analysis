# Figuras

Salvar aqui as figuras finais quando houver resultados. Cada figura deve informar amostra, unidade, escala, dados/código de origem e filtros. Exportar preferencialmente SVG/PDF e PNG. Conferir legibilidade no modelo de duas colunas. Não gerar gráficos com dados fictícios como resultados.

## Prévia técnica do workshop

`hard-rock-candidates-preview.pdf` e `.png` representam os 20 candidatos congelados, **ainda não validados por escuta**. Não entram nos resultados da página e não orientam curadoria. Gerados por `python scripts/analyze_workshop.py --preview`, com valores do snapshot de hash registrado em `data/source-manifest.json` e IDs de `data/workshop/selection-lock.json`. A figura foi inspecionada visualmente.

Pontos: faixas individuais; traço horizontal: mediana; traço vertical: intervalo interquartil com quantis lineares NumPy; escala comum [0,1]. Azul/círculos: menor audiência; laranja/triângulos: maior audiência. Audiência histórica do vídeo, corte fixado antes da leitura dos descritores. O resumo e as versões ficam em `data/processed/hard-rock-candidates-preview-summary.json`, local. Datas de publicação ausentes impedem comparar idade/exposição.

Uma figura validada será criada em outro arquivo somente depois da revisão de todos os casos, com perdas relatadas e grupos congelados. O artefato atual é uma prévia, apesar de estar neste diretório de figuras.
