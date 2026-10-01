# Cadernos de análise

Criar os cadernos quando a fonte e o protocolo estiverem definidos. Nenhuma análise ou resultado foi fabricado para preencher a estrutura.

Sequência sugerida:
1. 01_data_quality.ipynb: esquema, origem, chaves, duplicatas, ausências e cobertura por grupo.
2. 02_descriptive_analysis.ipynb: distribuição por característica e nível de audiência, casos individuais e medidas descritivas.
3. 03_workshop_figure.ipynb: figura principal reproduzível e exportação.

Centralizar transformações reutilizadas em scripts/. Usar caminhos relativos à raiz, registrar versões de dependências, entradas e exclusões. Células devem executar do início ao fim. Não incluir snapshots brutos volumosos nem dados sensíveis nas saídas.

Ao interpretar os resultados, registrar a evidência necessária a docs/hipoteses.md: número de casos, medidas, figura/tabela, entradas e commit. Separar observação, interpretação e hipótese sugerida; nenhuma hipótese gerada nesta exploração deve ser apresentada como confirmada independentemente.
