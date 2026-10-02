# Implementação e estado da entrega

## Entregas concretas

- Seleção congelada de **20 candidatos**, uma faixa por artista, dez em cada nível de audiência: `data/workshop/selection-lock.json`. Congelada localmente antes da leitura dos descritores, às 00:43:06 UTC de 2026-10-02; versão publicada no [commit a6915da](https://github.com/Muowl/music-popularity-analysis/commit/a6915da7fd6ee7be1765c29c2631afebb3c92440).
- Protocolo executável: [workshop-protocolo.md](workshop-protocolo.md). Rótulo `hard-rock` por ID exato, janela de **catálogo** 1980–1989, corte de 89.776.313,5 visualizações históricas, sem reposição.
- [Lista com os dois links por caso](conferencia-hard-rock.md) e CSV `data/workshop/recording-review.csv`, ainda pendentes. Usar IDs HR01–HR20 ao registrar respostas.
- Pipeline com auditoria de hashes e do lock, barreira de curadoria, três descritores, pontos, medianas/IIQ e relatório de fluxo/ausências.
- [Caderno executado](../notebooks/02_hard_rock_workshop.ipynb) e prévia técnica em `figures/hard-rock-candidates-preview.pdf`. **Prévia de candidatos não validados; não é resultado principal nem critério de revisão.**
- `main.tex`: rascunho de uma página que reporta os achados verificados do piloto e descreve a comparação pendente. Não representa uma comparação musical concluída.

## Gargalos atuais

O acesso ao primeiro novo vídeo retornou `URLError: Tunnel connection failed: 403 Forbidden` neste ambiente, registrado localmente em `data/processed/workshop-youtube-access.json`. Os novos pares não coincidem, nos dois IDs, com as escutas anteriores. Portanto, **a conferência humana dos 20 pares é necessária para concluir a comparação**. O autor recebeu solicitação dos primeiros quatro; o restante pode seguir em blocos iguais. Não houve escuta pelo assistente.

As datas de publicação dos novos vídeos permanecem ausentes. O protocolo permite inclusão por correspondência musical com essa ausência explicitada; nesse caso, não haverá avaliação da idade do vídeo. Datas de catálogo de páginas Spotify foram recuperadas por ID canônico, mas não foram comprovadas como primeira circulação das gravações. A seleção estuda a interseção das fontes, e o rótulo de gênero é catalográfico. Essas limitações precisam permanecer na discussão.

O modelo exigiu ABNTeX2 ausente na instalação LaTeX. O script de compilação obtém uma dependência com hash fixado no cache ignorado pelo Git; não altera `settings.sty`. Requer rede somente no primeiro uso quando o pacote não está instalado. O PDF foi compilado com bibliografia resolvida, uma página e inspeção visual.

## Reprodução offline da análise

```bash
python scripts/download_pilot_sources.py
python scripts/analyze_workshop.py --export-registry
python scripts/validate_selection.py
python scripts/analyze_workshop.py --preview
python -m unittest discover -s tests -v
python scripts/build_paper.py
```

O download é separado da análise. Os CSVs de origem ficam em `data/raw/`, ignorados pelo Git. Somente a etapa de figura requer NumPy/Matplotlib (`requirements-workshop.txt`); demais scripts novos usam a biblioteca padrão. O resumo JSON local registra versões, hashes, fluxo, contexto e método de quantis.

O caderno também recalcula a seleção a partir do cache de catálogo. Em uma instalação nova, executar `python scripts/prepare_workshop.py collect-catalogue` para adquirir essas páginas; como são páginas correntes, qualquer mudança nos anos em relação ao lock será um alerta, nunca uma alteração automática dos candidatos. Os anos e hashes usados no congelamento estão preservados no lock. Não executar `freeze` para sobrescrever a seleção existente: o script recusa isso.

## Como concluir a curadoria e a comparação

Editar **somente** as colunas mutáveis do CSV de revisão: `video_published_at`, `video_format`, `recording_review`, `reviewer`, `review_evidence`, `decision`, `exclusion_reason`. Usar os relatos reais, com autoria e origem na conversa, sem inventar marcos de escuta. Para mesma gravação-base, usar `same_base_recording`; versão divergente, `different_version`; fala/efeito sobreposto, `audio_overlay`; dúvida, `uncertain`. Casos incertos não são incluídos. Formatos: `music_video`, `official_audio`, `other`, `unknown` (ausência explícita); `pending` enquanto aguardam revisão.

Uma inclusão exige evidência atribuída, mesma gravação-base, formato registrado e ausência de motivo de exclusão. Uma exclusão exige evidência e motivo. IDs, fontes, contadores, datas de catálogo, grupos e hashes não mudam. Depois que **todos os casos** estiverem decididos:

```bash
python scripts/analyze_workshop.py --export-registry
python scripts/validate_selection.py
python scripts/analyze_workshop.py
```

A análise principal recusa casos pendentes ou menos de cinco gravações válidas por grupo. Com curadoria suficiente, gera `figures/hard-rock-validated.pdf` e `data/processed/hard-rock-validated-summary.json`; registrar esses resultados, revisar o texto e recompilar uma página. Não inserir a prévia técnica no artigo nem recalcular o corte após perdas. A alternativa existente é manter uma contribuição sobre curadoria, com reformulação explícita da pergunta do workshop.

## Verificação realizada

Seis testes de barreiras passaram: lock estrutural, ID/grupo imutáveis, inclusão sem evidência, exclusão da fala sobreposta, publicação posterior ao snapshot e exclusão sem motivo. O cadastro tem 20 candidatos, zero incluídos e zero erros estruturais; o código 2 é a pendência esperada. Os seis blocos de código do caderno novo e todos os blocos do caderno de conferência do piloto foram executados. A prévia foi inspecionada visualmente; as escalas, grupos e rótulos correspondem ao resumo. O PDF foi conferido como rascunho de uma página, com fontes e limites explícitos.
