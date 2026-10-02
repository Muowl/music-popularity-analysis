# Cadernos de análise

O caderno [01_source_feasibility.ipynb](01_source_feasibility.ipynb) acompanha a auditoria inicial das fontes. As células foram executadas sequencialmente em Python; execução/renderização em Jupyter não foi verificada neste ambiente. Criar os cadernos de análise musical quando fonte e protocolo estiverem definidos.

O caderno atual é [03_hard_rock_results.ipynb](03_hard_rock_results.ipynb): cinco células de código executadas, hashes e relatos auditados, resultados de 17 pares, figura e exclusões. [02_hard_rock_workshop.ipynb](02_hard_rock_workshop.ipynb) preserva a prévia histórica dos candidatos, anterior à escuta; seus valores não são os resultados curados. A conferência do piloto original permanece em [conferencia-gravacoes.ipynb](conferencia-gravacoes.ipynb).

Sequência sugerida:
1. 01_data_quality.ipynb: esquema, origem, chaves, duplicatas, ausências e cobertura por grupo.
2. 02_descriptive_analysis.ipynb: distribuição por característica e nível de audiência, casos individuais e medidas descritivas.
3. 03_workshop_figure.ipynb: figura principal reproduzível e exportação.

Centralizar transformações reutilizadas em scripts/. Usar caminhos relativos à raiz, registrar versões de dependências, entradas e exclusões. Células devem executar do início ao fim. Não incluir snapshots brutos volumosos nem dados sensíveis nas saídas.

Ao interpretar os resultados, registrar a evidência necessária a docs/hipoteses.md: número de casos, medidas, figura/tabela, entradas e commit. Separar observação, interpretação e hipótese sugerida; nenhuma hipótese gerada nesta exploração deve ser apresentada como confirmada independentemente.

## Revisão de 2026-10-02

O caderno 03 inclui agora a cadeia de proveniência do enriquecimento de publicação, idades descritivas e sensibilidade pós-hoc. O caderno 02 preserva a execução histórica; sua célula de seleção depende do cache completo de catálogo, ausente nesta revisão. Para auditar o que está disponível, executar `scripts/audit_workshop_selection.py` e consultar `docs/auditoria-selecao.md`. Não apresentar a reexecução dos resultados como reprodução integral da seleção histórica.
