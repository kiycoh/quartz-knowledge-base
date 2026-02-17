---
last modified: 2025-09-25T00:41:00.000Z
related: null
tags:
  - algoritmi-ordinamento
  - complessita-computazionale
  - programmazione-funzionale
---


- Quick Sort è un algoritmo di ordinamento basato sul paradigma "[[Divide et impera]]".
- Sceglie un elemento chiamato "pivot" dalla lista e divide gli altri elementi in due sotto-liste concettuali: una con elementi minori del pivot e una con elementi maggiori.
- Ricorsivamente, ordina le sotto-liste e poi concatena le liste ordinate insieme.

![[Quick Sort_image_1.png|500]]

**Caratteristiche:**
- **Stabilità:** Non è naturalmente stabile, ma può essere implementato per essere stabile.
- **Complessità di Tempo:** In media O(N log N), ma nel caso peggiore può essere O($N^2$) (con scelta di pivot non ottimale).
- **In-place:** Può essere implementato in modo "in-place" senza utilizzare spazio aggiuntivo significativo