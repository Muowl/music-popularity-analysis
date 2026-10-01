# Cadernos de análise

O caderno [01_source_feasibility.ipynb](01_source_feasibility.ipynb) acompanha a auditoria inicial das fontes. As células foram executadas sequencialmente em Python; execução/renderização em Jupyter não foi verificada neste ambiente. Criar os cadernos de análise musical quando fonte e protocolo estiverem definidos.

Sequência sugerida:
1. 01_data_quality.ipynb: esquema, origem, chaves, duplicatas, ausências e cobertura por grupo.
2. 02_descriptive_analysis.ipynb: distribuição por característica e nível de audiência, casos individuais e medidas descritivas.
3. 03_workshop_figure.ipynb: figura principal reproduzível e exportação.

Centralizar transformações reutilizadas em scripts/. Usar caminhos relativos à raiz, registrar versões de dependências, entradas e exclusões. Células devem executar do início ao fim. Não incluir snapshots brutos volumosos nem dados sensíveis nas saídas.

Ao interpretar os resultados, registrar a evidência necessária a docs/hipoteses.md: número de casos, medidas, figura/tabela, entradas e commit. Separar observação, interpretação e hipótese sugerida; nenhuma hipótese gerada nesta exploração deve ser apresentada como confirmada independentemente.
