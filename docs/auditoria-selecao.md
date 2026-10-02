# Reprodução da seleção por coleta posterior

**Estado:** coleta posterior completa, com 176/176 páginas verificadas e seleção reproduzida. O cache da coleta original não foi recuperado; essa distinção permanece explícita.

O autor executou a automação localmente sobre o commit `0c3c80c` e forneceu `catalogue-evidence.zip` (8.308.934 bytes). As páginas foram obtidas em 2026-10-02, entre 04:52:55 e 04:56:04 UTC (01:52:55–01:56:04 em Brasília). O pacote contém 359 membros: 358 arquivos listados no manifesto e o próprio manifesto.

## Verificação independente

`scripts/verify_catalogue_package.py` verificou tamanho e SHA-256 dos 358 arquivos, releu os 176 HTML, conferiu cada ID canônico/data e recalculou a seleção diretamente dos CSVs congelados. Não executou o código contido no ZIP. Resultados:

| Etapa | Resultado |
|---|---:|
| IDs únicos com rótulo `hard-rock` | 998 |
| Interseção exata | 176 |
| Elegíveis antes dos campos de catálogo | 129 |
| Faixas elegíveis com catálogo 1980–1989 | 47 |
| Artistas e faixas selecionados | 20 |
| Máximo de artistas em janelas de cinco anos iniciadas entre 1965 e 2022 | 15 |
| Corte de visualizações | 89.776.313,5 |
| IDs novos ou ausentes frente ao lock | 0 |

Os 20 artistas, vídeos, contadores, grupos e datas de catálogo dos selecionados conferem com o lock. A seleção usa o menor SHA-256 de `hard-rock-workshop-v1|<track_id>` por artista. Não houve alteração de candidatos, decisões, descritores ou resultados musicais.

## Hash do lock no Windows

O lock no pacote tem CRLF e SHA-256 `56715069f0631936f0cfaf4b5ac740475348a0d5bd1717fb874c7f71517097c6`; o arquivo publicado tem LF e SHA-256 `d69e21e986e05dbe8fff536cb7b8d64a71ba3a877c5a7c9efb78a5a4e649e304`. Foi verificado que **a única diferença são as quebras de linha**: os bytes normalizados e o JSON são idênticos. Os arquivos originais e seus hashes foram preservados, sem confundir equivalência de conteúdo com igualdade de bytes.

## Evidências e reprodução

- `data/workshop/selection-audit.json`: metadados mínimos dos 176 IDs, fontes, datas, hashes, filtros e comparação completa. A tentativa anterior, com 20 páginas e 156 falhas, permanece no histórico Git, no commit `0c3c80c`.
- `data/workshop/catalogue-package-verification.json`: resultado da verificação independente e proveniência do pacote.
- SHA-256 do ZIP: `10f348b13c7446113f464b36141536c593c572e52b1e42c3ea59e21358d4fb61`.

Após obter os CSVs pelos downloads com hash fixado, a auditoria dos metadados mínimos publicados é offline:

```bash
python scripts/audit_workshop_selection.py
```

Em ambiente sem cache, o comando usa o JSON publicado. Um cache local antigo pode produzir o estado antigo; preserve-o e use uma cópia limpa para conferir a evidência publicada.

Para verificar também os bytes dos HTML, com o pacote fornecido pelo autor:

```bash
python scripts/verify_catalogue_package.py /caminho/catalogue-evidence.zip
```

O pacote bruto não é publicado no GitHub. Os metadados mínimos permitem repetir a seleção; a conferência dos HTML depende do ZIP identificado pelo hash. Nenhuma verificação exige atualizar as visualizações históricas.

## Limite remanescente

O resultado demonstra reprodução com metadados posteriores. Não prova o conteúdo de todas as páginas na coleta original, não recupera seu cache e não é teste independente de H01. A busca pelo workspace original pode ser retomada se o acesso voltar, mas a seleção agora tem uma reprodução posterior completa e documentada.
