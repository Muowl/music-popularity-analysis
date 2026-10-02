# Auditoria e limite de reprodução da seleção

A análise principal dos 17 pares é reproduzível a partir dos CSVs congelados, lock e curadoria publicados. A seleção histórica anterior tem uma lacuna: o lock preserva as observações de catálogo dos 20 selecionados, mas não as dos outros 156 IDs da interseção. Hash de uma página ausente não recupera seu conteúdo.

`data/workshop/selection-audit.json` registra os 176 IDs, artista, filtros reproduzidos dos snapshots, hash da regra de seleção, evidência histórica disponível e uma coleta atual separada. Foram reproduzidos 998 IDs no rótulo, 176 na interseção e 129 elegíveis antes dos campos de catálogo. As 47 faixas da década e o máximo de 15 artistas em cinco anos permanecem resultados históricos registrados, não revalidados integralmente nesta revisão.

A coleta atual recuperou 20 páginas e teve 156 falhas `URLError`. Esses 20 sucessos não são os mesmos 20 casos escolhidos no lock. A comparação completa com o lock fica **indeterminada**, não divergente: contagens de década, novos IDs, IDs ausentes e corte recalculado ficam nulos. Ausência de observação não prova mudança de catálogo. Nenhuma informação atual altera a seleção.

Reprodução offline da auditoria disponível:

```bash
python scripts/audit_workshop_selection.py
```

O script usa os metadados mínimos publicados quando não existe cache local. Para uma nova tentativa de coleta, usar `--collect-current`; os resultados ficam em `data/processed/` para revisão, sem sobrescrever o lock ou a evidência publicada.

Para resolver a lacuna histórica, procurar no ambiente que fez o congelamento: `data/processed/hard-rock-catalogue-observations.json`, `data/processed/hard-rock-eligibility-audit.json` e `data/raw/hard-rock-pages/`. Preservar as datas, hashes e bytes originais, sem apresentar uma recoleta como original. Se não existirem, manter a limitação e, em eventual novo estudo, congelar seleção e elegibilidade com evidência completa. O script `freeze` foi ajustado para preservar `selection-eligibility.json` em futuros congelamentos; ele continua recusando sobrescrever a seleção atual.
