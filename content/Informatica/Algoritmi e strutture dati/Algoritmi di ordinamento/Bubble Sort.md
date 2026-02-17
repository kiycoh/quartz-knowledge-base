---
last modified: 2025-09-25T00:41:00.000Z
related: null
tags:
  - algoritmi-ordinamento
  - complessita-computazionale
  - stabilita-algoritmo
---


- Il Bubble Sort è un algoritmo di ordinamento che confronta e scambia elementi adiacenti finché la lista non è ordinata.
- Ad ogni passo, il più grande elemento "galleggia" verso la fine della lista, creando gradualmente una sequenza ordinata.
- Ad ogni iterazioni gli ultimi elementi più grandi saranno alla fine della lista, cioè nella loro posizione finale.

![[bubble-short-1964154607.png]]

**Caratteristiche:**
- **Stabilità:** Naturalmente stabile.
- **Complessità di Tempo:** O ($N$) nel caso migliore (lista già ordinata) perché il ciclo viene interrotto in quanto utilizza una variabile booleana di controllo. O($N^2$) nel caso medio e nel caso peggiore.
- **In-place:** È in-place