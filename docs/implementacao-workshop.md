# Implementação e estado da entrega

## Entregas concretas

- Seleção congelada de **20 candidatos**, uma faixa por artista, dez em cada nível de audiência: `data/workshop/selection-lock.json`. Congelada localmente antes da leitura dos descritores, às 00:43:06 UTC de 2026-10-02; versão publicada no [commit a6915da](https://github.com/Muowl/music-popularity-analysis/commit/a6915da7fd6ee7be1765c29c2631afebb3c92440).
- Protocolo executável: [workshop-protocolo.md](workshop-protocolo.md). Rótulo `hard-rock` por ID exato, janela de **catálogo** 1980–1989, corte de 89.776.313,5 visualizações históricas, sem reposição.
- [Conferência dos 20 casos](conferencia-hard-rock.md) e CSV `data/workshop/recording-review.csv`, com 17 incluídos e três excluídos. Relatos verbatim e esclarecimento de HR10 em `data/workshop/recording-review-evidence.json`.
- Pipeline com auditoria de hashes e do lock, barreira de curadoria, três descritores, pontos, medianas/IIQ e relatório de fluxo/ausências.
- [Caderno de resultados executado](../notebooks/03_hard_rock_results.ipynb), figuras curadas em `figures/hard-rock-validated.pdf` e exportação compacta `hard-rock-validated-paper.pdf`. Resumo agregado versionado em `data/workshop/analysis-summary.json` e [relatório](resultados-hard-rock.md).
- `main.tex` e [PDF de uma página](../paper/workshop-hard-rock.pdf): comparação descritiva dos 17 pares, figura, hipótese pós-hoc e limitações. O PDF anterior do piloto é histórico. A prévia de candidatos permanece separada, sem integrar os resultados atuais.

## Gargalos atuais

O acesso ao primeiro vídeo retornou `URLError: Tunnel connection failed: 403 Forbidden` neste ambiente, registrado localmente em `data/processed/workshop-youtube-access.json`. O autor resolveu o gargalo de escuta fornecendo relatos dos 20 pares e esclarecimento de HR10. Não houve escuta pelo assistente. HR02 e HR10 foram excluídos conservadoramente por trechos musicais adicionais de encerramento; HR03 ficou fora pela correspondência não suficientemente confirmada do ID congelado. Sua alternativa não aparece nos snapshots e tem ano de catálogo 2005; foi documentada, sem troca de ID ou descritores.

As datas de publicação dos 17 vídeos permanecem ausentes; não houve avaliação da idade/exposição. Formato desconhecido em 12 casos. O protocolo permite inclusão por correspondência musical com essas ausências explícitas. Datas de catálogo não foram comprovadas como primeira circulação das gravações. A seleção estuda a interseção das fontes, com rótulo catalográfico. As três perdas ocorreram no grupo menor, reduzindo-o de dez a sete; o maior conservou dez. Essas limitações permanecem na página e no relatório.

O modelo exigiu ABNTeX2 ausente na instalação LaTeX. O script de compilação obtém uma dependência com hash fixado no cache ignorado pelo Git; não altera `settings.sty`. Requer rede somente no primeiro uso quando o pacote não está instalado. O PDF foi compilado com bibliografia resolvida, uma página e inspeção visual.

## Reprodução da análise

```bash
python scripts/download_pilot_sources.py
python scripts/analyze_workshop.py --export-registry
python scripts/validate_selection.py
python scripts/analyze_workshop.py
python -m unittest discover -s tests -v
python scripts/build_paper.py
```

O download é separado da análise. Os CSVs de origem ficam em `data/raw/`, ignorados pelo Git. Somente a etapa de figura requer NumPy/Matplotlib (`requirements-workshop.txt`); demais scripts novos usam a biblioteca padrão. O resumo JSON local registra versões, hashes, fluxo, contexto e método de quantis.

O caderno também recalcula a seleção a partir do cache de catálogo. Em uma instalação nova, executar `python scripts/prepare_workshop.py collect-catalogue` para adquirir essas páginas; como são páginas correntes, qualquer mudança nos anos em relação ao lock será um alerta, nunca uma alteração automática dos candidatos. Os anos e hashes usados no congelamento estão preservados no lock. Não executar `freeze` para sobrescrever a seleção existente: o script recusa isso.

## Como revisar a curadoria e a comparação

Editar **somente** as colunas mutáveis do CSV de revisão: `video_published_at`, `video_format`, `recording_review`, `reviewer`, `review_evidence`, `decision`, `exclusion_reason`. Usar os relatos reais, com autoria e origem na conversa, sem inventar marcos de escuta. Para mesma gravação-base, usar `same_base_recording`; versão divergente, `different_version`; fala/efeito sobreposto, `audio_overlay`; dúvida, `uncertain`. Casos incertos não são incluídos. Formatos: `music_video`, `official_audio`, `other`, `unknown` (ausência explícita); `pending` enquanto aguardam revisão.

Uma inclusão exige evidência atribuída, mesma gravação-base, formato registrado e ausência de motivo de exclusão. Uma exclusão exige evidência e motivo. IDs, fontes, contadores, datas de catálogo, grupos e hashes não mudam. Depois que **todos os casos** estiverem decididos:

```bash
python scripts/analyze_workshop.py --export-registry
python scripts/validate_selection.py
python scripts/analyze_workshop.py
```

A análise principal recusa casos pendentes ou menos de cinco gravações válidas por grupo. A condição foi atendida e gera `figures/hard-rock-validated.pdf`, `hard-rock-validated-paper.pdf` e `data/processed/hard-rock-validated-summary.json`. A cópia agregada `data/workshop/analysis-summary.json` é a evidência publicada da execução. Não inserir a prévia técnica no artigo nem recalcular o corte após perdas. Reconsiderações de classificação exigem evidência, registro de revisão e atualização dos resultados e da hipótese; não usar contrastes musicais para decidir pareamentos.

## Verificação realizada

Oito testes de barreiras passaram; seus fixtures começam no estado pendente do lock, independentes das decisões reais. Testes temporários usam casos sintéticos identificados, sem persistência no cadastro. O cadastro atual tem 20 candidatos, 17 incluídos e zero erros estruturais; 17 avisos refletem datas de publicação ausentes, não foram ocultados. A execução principal retorna sucesso. Os cinco blocos de código do caderno de resultados foram executados, auditando hashes, medianas, amplitudes, sobreposição e ausência da alternativa de HR03 em ambas as fontes. Figuras ampla/compacta e PDF de uma página foram inspecionados visualmente, com bibliografia resolvida. `settings.sty` e o lock permaneceram idênticos à versão anterior. A hipótese em `hipoteses.md` é pós-hoc e não confirmada pelos mesmos dados.
