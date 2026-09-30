# Protocolo de seleção e análise — rascunho

Status: não congelado. Campos abaixo são decisões a preencher antes da coleta principal.

## Definições
- Unidade candidata: um vídeo associado a uma gravação específica.
- Medida proposta: visualizações acumuladas do vídeo, com data/hora UTC da consulta.
- Fonte dos descritores: a definir e documentar; registrar versão/snapshot do CSV.
- População-alvo, ranking/fonte, regra de inclusão, tamanho e data de corte: pendentes.
- Atributos candidatos: danceability, energy, acousticness, valence e instrumentalness. Lista final pendente; não selecionar apenas os que produzem maior contraste.

## Seleção
1. Registrar a lista de candidatos antes de verificar seus descritores.
2. Aplicar critérios de inclusão comuns. Registrar todos os excluídos e motivos.
3. Registrar formato do vídeo, publicação e consulta; não somar uploads distintos.
4. Conferir título, artista, versão, intérpretes e outros metadados disponíveis.
5. Classificar correspondência como documentary, uncertain ou not_found. Documentary é conferência de metadados, não identificação por áudio.
6. Usar somente correspondências documentadas na análise principal; informar a perda de cobertura e possível viés.
7. Registrar duplicação de vídeo, gravação e artista. Não remover casos silenciosamente.
8. Congelar protocolo e seleção por commit. Alterações posteriores recebem justificativa.

## Análise proposta
- Auditar chaves, ausências, escalas e duplicatas antes do cruzamento.
- Informar candidatos, incluídos, excluídos e faixas distintas.
- Mostrar pontos por faixa e medidas como mediana e intervalo interquartil, sem esconder dispersão.
- Não interpretar descritores como experiência subjetiva do ouvinte.
- Não extrapolar a seleção intencional para todos os hits ou gêneros.
- Se houver comparação com outra seleção, definir regras compatíveis antes dos cálculos.
- Registrar análises exploratórias/post-hoc; não escolher hipótese pelo resultado.
- Não declarar significância, efeito causal ou qualidade preditiva sem método e evidência apropriados.

## Reprodutibilidade
Registrar fonte, data, hash SHA-256, esquema, filtros, versão do código e comandos. A aquisição precisa ser separada da análise: reexecutar cálculos não deve atualizar contadores da plataforma.
