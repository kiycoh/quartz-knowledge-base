---
tags:
  - algoritmi-ordinamento
  - alberi-binari
  - complessita-computazionale
---

- **Alberi Rosso-Nero (Red-Black Trees)**:
    
    - **Descrizione**: Particolari alberi binari di ricerca _auto-bilanciati_. Ogni nodo ha un attributo "colore" (RED o BLACK) e seguono 5 proprietà che garantiscono il bilanciamento. La caratteristica principale è che nessun cammino dalla radice a una foglia (NIL) è mai più lungo del doppio di qualsiasi altro.
    - **Vantaggi**: Garantiscono che tutte le operazioni fondamentali siano efficienti.
    - **Operazioni e Complessità**: Tutte le operazioni chiave (`SEARCH`, `MINIMUM`, `MAXIMUM`, `SUCCESSOR`, `PREDECESSOR`, `INSERT`, `DELETE`) sono garantite in **O(log n)**.
    - **Meccanismi di Bilanciamento**:
        - `LEFT-ROTATE(T, x)`, `RIGHT-ROTATE(T, x)`: Operazioni ausiliarie che effettuano cambi di puntatori in tempo costante **O(1)** per mantenere le proprietà dell'albero dopo inserimenti o cancellazioni.
        - `INSERT-FIX(T, z)`: Procedura post-inserimento che risolve le violazioni delle proprietà (es. un nodo rosso con figlio rosso) tramite ricolorazione e rotazioni.
        - `DELETE-FIX`: Procedura post-cancellazione (esercizio).
    - **Utilizzo Pratico**: Usati in molte librerie e sistemi per strutture dati che richiedono alte prestazioni per operazioni di dizionario (es. mappe, set ordinati).