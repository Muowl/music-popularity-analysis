# Implementação e estado da entrega

## Entrega atual

Comparação exploratória de 17 pares (7/10 por grupo), com IDs, corte e decisões principais preservados. O [PDF](../paper/workshop-hard-rock.pdf) apresenta pergunta, motivação, três descritores, hipótese pós-hoc e limites. O [caderno 03](../notebooks/03_hard_rock_results.ipynb) verifica cálculos, proveniência, idade dos vídeos e sensibilidade. O piloto original e o rascunho anterior permanecem históricos.

O lock foi congelado localmente em 2026-10-02 às 00:43:06 UTC e publicado no [commit a6915da](https://github.com/Muowl/music-popularity-analysis/commit/a6915da7fd6ee7be1765c29c2631afebb3c92440). A década representa catálogo Spotify, sem validação como primeiro lançamento. O corte é 89.776.313,5 visualizações históricas; não foi recalculado após perdas.

## Reprodução offline após aquisição das fontes

```bash
python scripts/download_pilot_sources.py
python scripts/analyze_workshop.py --export-registry
python scripts/validate_selection.py
python scripts/analyze_workshop.py
python scripts/analyze_workshop_sensitivity.py
python scripts/audit_workshop_selection.py
python -m unittest discover -s tests -v
python scripts/build_paper.py
```

A etapa de figuras usa `requirements-workshop.txt`. A compilação exige LaTeX (`latexmk`, `kpsewhich`) e `pdfinfo`; se ABNTeX2 estiver ausente, há download CTAN com espelho alternativo e SHA-256 fixo. `settings.sty` permanece inalterado. O script gera `main.pdf`; após conferência visual, atualizar `paper/workshop-hard-rock.pdf` explicitamente.

Saídas analíticas ficam em `data/processed/`; as cópias publicadas são `data/workshop/analysis-summary.json`, `sensitivity-summary.json` e `selection-audit.json`. Não sobrescrever a evidência publicada sem revisão. A análise e auditoria offline não precisam atualizar páginas ou contadores.

## Enriquecimento de publicação

`python scripts/collect_workshop_video_metadata.py` faz uma nova coleta em `data/processed/workshop-video-metadata.json`, sem modificar automaticamente o cadastro. Nesta revisão, todas as 20 publicações foram verificadas por ID, anteriores ao snapshot e transferidas ao CSV. As fontes estão em `data/workshop/video-metadata.json`, com hashes do CSV antes/depois; o registro original de escuta permanece intacto. Datas usam o dia informado por `publishDate`, com valor bruto preservado. Idade até 07/02/2023 usa dias/365,25 e não estima exposição efetiva.

As 17 inclusões têm data disponível. Nenhum formato foi inferido por título, canal ou marca oficial; 12/17 permanecem desconhecidos. Não houve nova escuta pelo assistente.

## Curadoria e sensibilidade

HR02 e HR10 permanecem excluídos por extensões musicais; HR03, por correspondência não suficientemente confirmada do ID congelado. A alternativa de HR03 continua ausente dos snapshots e não recebe descritores do ID original.

Os cenários pós-hoc acrescentam HR02, HR10 e ambos, mantendo corte/grupos. A direção de energia e dançabilidade permanece; acusticidade muda de sinal em um cenário. Isso não constitui confirmação independente de H01. Ver [resultados](resultados-hard-rock.md).

## Gargalos restantes

A coleta posterior recuperou 176/176 páginas, e a verificação independente do ZIP reproduziu as 47 faixas, os mesmos 20 artistas/IDs e o corte. O cache original continua indisponível; a reprodução posterior completa está documentada na [auditoria](auditoria-selecao.md). O caderno 02 preserva a execução histórica dependente do cache original. Não executar `freeze` para substituir a seleção existente.

Persistem formato desconhecido em 12 vídeos, ausência de ajuste estatístico por exposição/artista/subestilo e ausência de validação técnica de master. A idade agora é descrita; não foi controlada. Alinhar o rascunho e os detalhes operacionais com o orientador antes da submissão.

## Verificação desta revisão

Dezoito testes passaram; cadastro com 20 candidatos, 17 inclusões, zero erros e zero avisos. As sete células de código do caderno 03 foram executadas, incluindo validação da cadeia de hashes, estatísticas, sensibilidade e idades. O resumo principal preserva integralmente estatísticas musicais e fluxo da versão revisada. Lock, evidência original de escuta e `settings.sty` permanecem byte a byte idênticos. PDF recompilado com uma página e referências resolvidas, seguido de inspeção visual. A auditoria posterior completa foi reproduzida; os 358 arquivos do manifesto do ZIP e os 176 HTML foram conferidos independentemente. A igualdade do lock com CRLF/LF foi documentada. O cache original não foi recuperado.

## Coleta posterior com um comando

Para executar no computador local com retomada e pacote de evidências: `python scripts/automate_workshop_audit.py`. Ver [coleta automatizada](coleta-automatizada.md). O comando limita tentativas, salva cada observação e gera ZIP/relatório mesmo para coleta parcial. Ele não substitui o cache histórico nem altera o estudo publicado.
