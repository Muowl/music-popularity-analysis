# Protocolo de seleção e análise — rascunho

Status: não congelado. Direção atual: estudo exploratório e descritivo, com piloto para avaliar a viabilidade da comparação. Campos abaixo devem ser definidos antes da coleta principal; o piloto de viabilidade segue docs/piloto.md.

## Definições
- Unidade candidata: um vídeo associado a uma gravação específica.
- Medida proposta: visualizações acumuladas do vídeo, com data/hora UTC da consulta.
- Fonte dos descritores: a definir e documentar; registrar versão/snapshot do CSV.
- População-alvo, ranking/fonte, regra de inclusão, tamanho e data de corte: pendentes.
- Atributos candidatos: danceability, energy, acousticness, valence e instrumentalness. Lista final pendente; não selecionar apenas os que produzem maior contraste.

## Comparação planejada
- Selecionar candidatos de um universo comum, com regras compatíveis de gênero, época e formato. Não escolher o segundo grupo por familiaridade ou pelos descritores observados.
- Definir níveis de audiência, data de corte e tamanho antes de comparar os descritores; os limites ainda estão pendentes.
- Registrar lançamento da gravação e publicação do vídeo separadamente. A idade do vídeo não representa toda a exposição da música.
- Registrar no cadastro a fonte de elegibilidade e o grupo antes do cruzamento. A versão atual do cadastro é estrutural; campos específicos do piloto serão definidos antes de preenchê-lo.
- Auditar cobertura, exclusões e concentração por artista em cada grupo. Não substituir ausentes silenciosamente para completar cotas.

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
- Comparar distribuições por nível de audiência, preservando pontos individuais e dispersão; definir medidas e análises de sensibilidade antes da análise principal.
- Tratar repetição de artistas e versões como possível dependência entre observações. Não assumir independência automaticamente.
- Não interpretar diferenças entre grupos como efeito causal nem generalizar além do universo de seleção.
- Registrar análises exploratórias/post-hoc e hipóteses geradas a partir dos resultados, distinguindo-as de expectativas registradas antes da análise. Não apresentá-las como hipóteses previamente definidas ou confirmadas pela mesma exploração.
- Não declarar significância, efeito causal ou qualidade preditiva sem método e evidência apropriados.

## Dos achados às hipóteses
- Registrar primeiro o achado, com número de casos, medida, figura/tabela e versão dos dados/código que o sustentam.
- Separar a observação na amostra de sua interpretação; discutir cobertura, exposição, época e concentração por artista como possíveis explicações alternativas.
- Formular proposições testáveis somente quando os achados as sustentarem, com população, variáveis e condições delimitadas. Seguir [o registro de hipóteses](hipoteses.md).
- Propor teste futuro em dados independentes da exploração, com critérios e análise definidos antes de observá-los. Reanalisar os mesmos dados não constitui confirmação independente.
- Relatar também sobreposição e ausência de contraste aparente. Elas não demonstram equivalência nem ausência de associação, sobretudo em amostra pequena.
- Não exigir quantidade mínima de hipóteses nem inventar teorias. Se os dados não sustentarem uma hipótese específica, registrar a limitação e a pergunta em aberto.

## Reprodutibilidade
Registrar fonte, data, hash SHA-256, esquema, filtros, versão do código e comandos. A aquisição precisa ser separada da análise: reexecutar cálculos não deve atualizar contadores da plataforma.
