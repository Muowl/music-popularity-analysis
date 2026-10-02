# Texto do workshop

O arquivo de entrada continua sendo ../main.tex para preservar o fluxo do modelo fornecido. settings.sty e abntex2cite.sty permanecem na raiz. Não duplicar o documento principal nesta pasta.

Estado atual: rascunho de uma página sobre a curadoria do piloto, com resultados verificados e a comparação de Hard Rock ainda pendente de escuta. Autores e settings.sty preservados. A bibliografia conserva o material herdado; somente as duas novas entradas citadas foram verificadas para este tema, com escopo em `data/workshop/reference-evidence.json`.

Estrutura sugerida, após fechar método e obter resultados:
- Introdução: por que investigar descritores e audiência, problema delimitado e objetivo explícito. Fundamentar a justificativa com literatura verificada; não alegar lacuna ou ineditismo sem revisão.
- Método: natureza exploratória e descritiva, fonte, seleção, grupos, audiência, correspondência de gravações, descritores e perdas de cobertura.
- Resultados: figura/tabela, número de casos e descrição de distribuições, dispersão, semelhanças e diferenças.
- Discussão: interpretação dos achados, explicações alternativas e hipóteses deles derivadas, com referência à evidência e indicação de teste futuro em novos dados. Usar [o registro de hipóteses](../docs/hipoteses.md).
- Conclusão: resposta limitada ao recorte, contribuição descritiva, limites e próximos testes. Não declarar confirmadas as hipóteses geradas pela exploração.

A divisão em seções deve respeitar o limite de páginas a confirmar. A versão curta precisa manter a ligação entre problema, objetivo, achados e hipóteses; não exige uma teoria nova. Distribuições semelhantes também devem ser relatadas, sem tratá-las automaticamente como equivalência.

Compilar a partir da raiz com `python scripts/build_paper.py`. Requer LaTeX, latexmk, BibTeX e pdfinfo; o script oferece a dependência ABNTeX2 no cache local se ausente. A compilação, referências, paginação de uma página e renderização foram verificadas. Não alterar a formatação para acomodar texto excessivo. `main.pdf` é gerado e ignorado pelo Git; a cópia `paper/workshop-pilot-draft.pdf` é um artefato próprio de revisão, não resultado da comparação pendente.
