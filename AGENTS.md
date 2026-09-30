# Orientações de trabalho

- Siga `CONTRIBUTING.md` para organizar commits: Conventional Commits, títulos em inglês no imperativo, mudanças agrupadas por objetivo e validação proporcional. Preserve o histórico publicado; não reescreva commits compartilhados sem acordo explícito.

- Projeto acadêmico exploratório: preserve a cadeia pergunta → dados → método → resultados → conclusão.
- Consulte README.md, docs/escopo.md, docs/protocolo.md e docs/decisoes.md antes de modificar o desenho.
- Não converta proposta em decisão nem resultado de outro projeto em resultado deste.
- Não invente dados, correspondências, referências, DOI, métricas ou resultados.
- Fontes científicas: priorizar publicações revisadas por pares; confirmar publicação, metadados e relação com a afirmação. Documentação e bases são fontes primárias para seus próprios campos.
- Preserve settings.sty: o modelo contém instrução explícita de não alterar a formatação. Mantenha os arquivos LaTeX na raiz enquanto não houver necessidade acordada de reorganização.
- references.bib é bibliografia herdada do modelo, não validada para este tema.
- Não importar automaticamente os três recortes da apresentação anterior. Toda inclusão precisa de critério e fonte.
- Ausência não é zero. Não trocar gravações ou escolher exemplos por produzirem resultados mais chamativos.
- Não publicar dados de terceiros ou PDFs sem verificar condições de uso. Não versionar credenciais.
- Scripts devem usar caminhos relativos/argumentos e registrar entradas, versões e exclusões. Valide o cadastro com python scripts/validate_selection.py.
- Não instalar bibliotecas ou criar modelos complexos sem necessidade concreta. Neste estágio, o validador usa só a biblioteca padrão.
- Atualize docs/decisoes.md ao mudar critérios ou escopo; rotule análises pós-hoc. Resultados negativos e diferenças pequenas são resultados válidos.
