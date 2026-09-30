# Contribuição e organização dos commits

## Padrão de mensagem

Seguir o padrão do commit inicial: título em inglês, verbo no imperativo e prefixo Conventional Commits. A documentação do projeto pode continuar em português.

```text
type(scope): summarize the change

Explain why the change is needed and what behavior or research decision changes.
Record relevant validation and known limitations when applicable.
```

O escopo é opcional. Buscar títulos de até 72 caracteres, sem ponto final. Usar o corpo para contexto, evitando títulos genéricos como `update files` ou `fix stuff`.

| Tipo | Uso |
|---|---|
| `docs` | Protocolo, decisões, redação do artigo e orientações |
| `feat` | Nova funcionalidade de coleta, processamento ou análise |
| `fix` | Correção de erro em código ou processamento |
| `refactor` | Reorganização de código sem mudar seu comportamento |
| `test` | Testes relevantes e suas correções |
| `chore` | Configuração, dependências e manutenção do repositório |
| `ci` | Automação de integração e verificações |

Exemplos de títulos para mudanças futuras, não de trabalho já realizado:

```text
docs(protocol): define eligibility criteria for the pilot
feat(selection): validate recording matches
fix(selection): reject negative view counts
chore(data): register documented pilot candidates
docs(paper): describe sample limitations
```

## Unidade de trabalho

- Cada commit deve ter um objetivo coerente, revisável e, quando possível, reversível sozinho.
- Separar mudanças independentes de protocolo, cadastro, código e artigo. Manter juntas as alterações que dependem umas das outras para funcionar ou serem compreendidas.
- Evitar misturar reformatação ampla com mudanças de método ou resultados.
- Antes de publicar, revisar o diff e os arquivos incluídos; não adicionar automaticamente tudo que estiver na pasta.
- Registrar fontes, critérios e exclusões junto das alterações de seleção. Mudanças de desenho devem atualizar `docs/decisoes.md`.
- Para análises, identificar entradas e procedimentos necessários à reprodução. Não apresentar resultados sem rastreabilidade.

## Validação e publicação

- Executar verificações proporcionais à mudança. Alterações apenas documentais pedem revisão de conteúdo e links; não exigem testes artificiais.
- Ao mudar o cadastro ou seu validador, executar `python scripts/validate_selection.py` e verificar se o resultado é o esperado. Código 2 indica cadastro vazio ou sem inclusões, não amostra aprovada.
- Informar no corpo do commit as verificações relevantes realmente executadas e suas limitações. Nunca declarar testes que não foram realizados.
- Não versionar credenciais, artefatos temporários ou dados e PDFs de terceiros sem condições de uso verificadas.
- Para mudanças maiores, usar uma branch temática e uma pull request com objetivo, alterações e validação. Mudanças pequenas e autorizadas podem ser publicadas diretamente.
- Preservar o histórico compartilhado: corrigir por novo commit ou revert. Não fazer amend, rebase ou force push de commits publicados sem acordo explícito.

A convenção vale para os próximos commits; mensagens anteriores permanecem como registro histórico.
