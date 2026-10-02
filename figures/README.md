# Figuras

## Resultados curados

`hard-rock-validated.pdf` e `.png`: 17 gravações-base incluídas por relato de escuta, sete no grupo menor e dez no maior; identidade digital de master não comprovada. `hard-rock-validated-paper.pdf` e `.png` são a exportação compacta da mesma figura para uma coluna do artigo. Geradas por `python scripts/analyze_workshop.py`, com fonte, lock, revisão, fluxo, quantis e versões em `data/workshop/analysis-summary.json`. A figura compacta e sua renderização no PDF de uma página foram inspecionadas.

Pontos individuais, medianas e IIQs, escala [0,1], cores e marcadores distinguíveis. Os três pares excluídos não aparecem nos pontos; pertenciam ao grupo menor. A idade do vídeo não foi controlada. Descritores referem-se à edição Spotify; a audiência, ao vídeo histórico. Não são resultados de teste causal, preditivo ou de significância.

Salvar aqui as figuras finais quando houver resultados. Cada figura deve informar amostra, unidade, escala, dados/código de origem e filtros. Exportar preferencialmente SVG/PDF e PNG. Conferir legibilidade no modelo de duas colunas. Não gerar gráficos com dados fictícios como resultados.

## Prévia técnica do workshop

`hard-rock-candidates-preview.pdf` e `.png` representam os 20 candidatos congelados, **ainda não validados por escuta**. Não entram nos resultados da página e não orientam curadoria. Gerados por `python scripts/analyze_workshop.py --preview`, com valores do snapshot de hash registrado em `data/source-manifest.json` e IDs de `data/workshop/selection-lock.json`. A figura foi inspecionada visualmente.

Pontos: faixas individuais; traço horizontal: mediana; traço vertical: intervalo interquartil com quantis lineares NumPy; escala comum [0,1]. Azul/círculos: menor audiência; laranja/triângulos: maior audiência. Audiência histórica do vídeo, corte fixado antes da leitura dos descritores. O resumo e as versões ficam em `data/processed/hard-rock-candidates-preview-summary.json`, local. Datas de publicação ausentes impedem comparar idade/exposição.

A figura curada acima usa arquivos próprios. Esta prévia histórica permanece separada e não integra os resultados do artigo atual.
