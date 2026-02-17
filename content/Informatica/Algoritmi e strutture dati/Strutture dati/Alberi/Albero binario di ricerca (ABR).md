---
last modified: 2025-10-28T20:06:44.000Z
related: null
parent note: null
tags:
  - algoritmi-ordinamento
  - alberi-binari
  - complessita-computazionale
---

**Particolarità**: La visita in-ordine stampa i valori in ordine crescente. Operazioni come `MINIMUM`, `MAXIMUM`, `SEARCH`, `PREDECESSOR`, `SUCCESSOR`, `INSERT`, `DELETE` sono più efficienti che in alberi binari generici.
- **Complessità (caso peggiore - albero degenere)**:
    - `SEARCH`/`INSERT`/`DELETE`: `O(n)`.
    - `MINIMUM`/`MAXIMUM`/`PREDECESSOR`/`SUCCESSOR`: `O(n)`.
- **Complessità (caso medio/ottimo - albero bilanciato)**:
    - `SEARCH`/`INSERT`/`DELETE`: `O(log n)`.
    - `MINIMUM`/`MAXIMUM`/`PREDECESSOR`/`SUCCESSOR`: `O(log n)`.

 **Esempio**: Un sistema di archiviazione di file basato su nomi, dove i file sono organizzati in una gerarchia alfabetica per un accesso rapido.