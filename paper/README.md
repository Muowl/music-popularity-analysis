# Texto do workshop

O arquivo de entrada continua sendo ../main.tex para preservar o fluxo do modelo fornecido. settings.sty e abntex2cite.sty permanecem na raiz. Não duplicar o documento principal nesta pasta.

Estado atual: texto Lorem ipsum; autores e formatação preservados. A bibliografia em references.bib é herdada do modelo e não deve ser tratada como bibliografia validada desta pesquisa.

Estrutura sugerida, após fechar método e obter resultados:
- Introdução: por que investigar descritores e audiência, problema delimitado e objetivo explícito. Fundamentar a justificativa com literatura verificada; não alegar lacuna ou ineditismo sem revisão.
- Método: natureza exploratória e descritiva, fonte, seleção, grupos, audiência, correspondência de gravações, descritores e perdas de cobertura.
- Resultados: figura/tabela, número de casos e descrição de distribuições, dispersão, semelhanças e diferenças.
- Discussão: interpretação dos achados, explicações alternativas e hipóteses deles derivadas, com referência à evidência e indicação de teste futuro em novos dados. Usar [o registro de hipóteses](../docs/hipoteses.md).
- Conclusão: resposta limitada ao recorte, contribuição descritiva, limites e próximos testes. Não declarar confirmadas as hipóteses geradas pela exploração.

A divisão em seções deve respeitar o limite de páginas a confirmar. A versão curta precisa manter a ligação entre problema, objetivo, achados e hipóteses; não exige uma teoria nova. Distribuições semelhantes também devem ser relatadas, sem tratá-las automaticamente como equivalência.

Compilar a partir da raiz em ambiente com LaTeX e pacotes do modelo, por exemplo latexmk -pdf main.tex. Esse comando não foi validado nesta organização. Verificar paginação e renderização antes de entregar. Não alterar a formatação para acomodar texto excessivo.
