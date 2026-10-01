# Dados e proveniência

O cadastro em selection/candidates.csv começa vazio. Não há amostra aprovada.

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
- match_status: documentary, uncertain ou not_found.
- match_evidence: evidências da versão; não substituir por outra gravação.
- decision: pending, include ou exclude.
- exclusion_reason: obrigatório se exclude.
- notes: limites, duplicações de obra/artista e outras observações.

Campos desconhecidos ficam vazios, nunca preenchidos com zero por conveniência. O validador verifica estrutura e consistência, não a veracidade das fontes nem licença.

## Fontes candidatas auditadas

[Manifesto de fontes](source-manifest.json): URLs, versões, datas declaradas, tamanhos, SHA-256 e rótulos de licença consultados para os dois snapshots. Download verificável: `python scripts/download_pilot_sources.py`. Os CSVs ficam em `data/raw/` e não são versionados.

A fonte pareada tem audiência histórica e não contém data/hora de observação por linha. Antes de importar qualquer candidato, o esquema deverá distinguir data declarada, precisão temporal e data de obtenção. Não fabricar um instante UTC para satisfazer o validador. O cadastro principal permanece vazio; o [relatório](../docs/relatorio-piloto-fontes.md) contém apenas auditoria das fontes.

## Seleção de acesso a metadados

`pilot/metadata-candidates.json` contém os 12 casos congelados para testar o enriquecimento, não inclusões na amostra principal. `metadata-observations.json` preserva fatos extraídos das páginas exatas; `catalogue-search.json` contém candidatos suplementares de catálogo, não correspondências aprovadas. `metadata-review.json` registra a revisão por caso e o resultado do critério de avanço. Descrições e HTML completos ficam apenas no cache local em `raw/`.
