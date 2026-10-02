# Verificação automatizada do catálogo

Objetivo: executar uma **coleta posterior**, comparar a seleção com o lock e entregar evidências em ZIP. Não recupera o cache original, não altera a amostra e não testa a hipótese musical. Usa Python 3.10+ e biblioteca padrão.

Na branch `workshop/hard-rock-study`, executar:

```bash
python scripts/automate_workshop_audit.py
```

O comando baixa os dois CSVs se faltarem, verifica seus hashes e consulta os 176 IDs. Preserva por ID o HTML, hash e observação em `data/raw/catalogue-automation/`. Ao repetir o comando, reutiliza apenas páginas verificadas cujo hash confere e tenta as pendências. Os registros podem ter datas de obtenção diferentes; cada uma permanece explícita.

Faz no máximo duas tentativas por ID (sem repetir HTTP 401/403/404), com timeout de 15 segundos por requisição. Interrompe após cinco falhas consecutivas ou aproximadamente 15 minutos de coleta; a requisição em andamento pode exceder esse orçamento. O download inicial dos CSVs fica fora desse prazo. Para outro orçamento: `--max-minutes 5`.

Ao terminar, inclusive com coleta parcial ou Ctrl+C, imprime os caminhos de:

- `RELATORIO.md`: estado e cobertura;
- `catalogue-evidence.zip`: relatório JSON por ID, lock, manifesto das fontes, scripts, observações e HTML desta coleta;
- `catalogue-evidence.zip.sha256`: checksum externo.

Todos ficam em uma pasta com timestamp dentro de `data/processed/catalogue-automation/`. Cada ZIP inclui `manifest.json` com tamanho e SHA-256 dos demais membros. Não inclui CSVs completos, áudios ou credenciais. Não adicionar o pacote bruto ao Git; enviar para revisão separadamente.

`--offline` empacota o cache existente sem acesso à rede. A falta de CSVs, hashes incorretos ou cache inconsistente interrompe a execução com erro: não substituir arquivos silenciosamente. Uma interrupção forçada do processo pode impedir gerar o ZIP, mas os registros concluídos ficam disponíveis para a próxima execução.

Códigos de saída:

- `0`: todos os IDs verificados, seleção e corte reproduzidos com metadados posteriores;
- `2`: coleta incompleta ou diferença na seleção; ler o relatório, sem alterar a amostra;
- `1`: falha operacional ou inconsistência de entrada; examinar a mensagem.

A comparação exige os 176 IDs verificados. Coleta parcial gera resultados indeterminados, não divergência presumida. Contagem da década, artistas, novos IDs, ausentes e corte são calculados somente quando completa. O script não modifica lock, revisão, contadores, descritores, artigo ou resultados publicados; não faz commit, push ou merge. A classificação do formato dos vídeos continua sendo uma tarefa separada.
