# Dados e proveniência

O cadastro em `selection/candidates.csv` contém 20 candidatos congelados: **17 incluídos e três excluídos** após os relatos do autor e adjudicação. O cadastro de revisão é `workshop/recording-review.csv`, com evidências verbatim em `workshop/recording-review-evidence.json`. O lock preserva IDs, fontes, contagens, datas de catálogo e grupos. O resultado agregado versionado é `workshop/analysis-summary.json`, produzido a partir dos snapshots e das decisões, sem consulta de audiência atual.

Guarde originais em raw/ e derivados em processed/: ambos estão ignorados pelo Git. Mesmo metadados devem ter condições de uso verificadas antes de publicação. Não enviar áudios, PDFs, credenciais ou bases completas automaticamente.

Para cada fonte, registrar em documento versionado: URL, responsável, data de obtenção, licença/termos (ou pendência), nome do arquivo, tamanho, SHA-256, campos usados e versão do snapshot. Usar snapshots congelados; não atualizar visualizações durante a análise.

## Colunas do cadastro
- candidate_id: chave interna única.
- title, artist: identificação do caso.
- selection_source_url, selection_reason: origem e justificativa na seleção.
- video_url: URL do vídeo considerado; uma ocorrência por candidato.
- video_published_at: data de publicação ISO 8601 (AAAA-MM-DD).
- views: inteiro não negativo; sem separadores.
- observed_at_utc: consulta ISO 8601 com UTC explícito, exemplo de formato AAAA-MM-DDTHH:MM:SS+00:00.
- track_id: ID da gravação correspondente na base de descritores.
- match_status: documentary, uncertain ou not_found; no esquema v2, user_reviewed distingue a confirmação musical atribuída da evidência documental.
- match_evidence: evidências da versão; não substituir por outra gravação.
- decision: pending, include ou exclude.
- exclusion_reason: obrigatório se exclude.
- notes: limites, duplicações de obra/artista e outras observações.

Campos desconhecidos ficam vazios, nunca preenchidos com zero por conveniência. O validador verifica estrutura e consistência, não a veracidade das fontes nem licença.

## Esquema v2: audiência histórica e revisão

O validador mantém compatibilidade com o esquema inicial e aceita a extensão atual:

- `views_observed_date`: dia declarado da coleta (2023-02-07 neste snapshot).
- `views_date_precision`: `day_declared`, sem instante UTC por linha.
- `views_date_source_url`: fonte da declaração temporal.
- `recording_review`: pending, same_base_recording, different_version, audio_overlay ou uncertain.
- `reviewer`: autor da conferência; não atribuir escuta ao assistente.
- `audience_group`: lower ou higher, fixado no lock.

Não preencher simultaneamente um instante UTC com o dia declarado. Uma inclusão v2 exige gravação-base correspondente, revisor, evidência e data de audiência com origem. Publicação do vídeo ausente gera aviso e exige limitação nas notas; a idade não é calculada. O protocolo específico registra essa revisão prospectiva, sem aprovar retroativamente o piloto antigo. A análise ainda exige a revisão de todos os candidatos e os limiares operacionais do [protocolo do workshop](../docs/workshop-protocolo.md).

## Fontes candidatas auditadas

[Manifesto de fontes](source-manifest.json): URLs, versões, datas declaradas, tamanhos, SHA-256 e rótulos de licença consultados para os dois snapshots. Download verificável: `python scripts/download_pilot_sources.py`. Os CSVs ficam em `data/raw/` e não são versionados.

A fonte pareada tem audiência histórica e não contém data/hora de observação por linha. O esquema v2 distingue data declarada, precisão e obtenção. Não fabricar instante UTC para satisfazer o validador. O [relatório inicial](../docs/relatorio-piloto-fontes.md) preserva a auditoria; a seleção atual segue o protocolo específico.

## Seleção de acesso a metadados

`pilot/metadata-candidates.json` contém os 12 casos congelados para testar o enriquecimento, não inclusões na amostra principal. `metadata-observations.json` preserva fatos extraídos das páginas exatas; `catalogue-search.json` contém candidatos suplementares de catálogo, não correspondências aprovadas. `metadata-review.json` registra a revisão por caso e o resultado do critério de avanço. Descrições e HTML completos ficam apenas no cache local em `raw/`.
