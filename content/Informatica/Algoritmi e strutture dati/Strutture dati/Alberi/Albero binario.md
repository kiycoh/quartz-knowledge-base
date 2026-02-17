---
last modified: 2025-10-28T20:04:12.000Z
related:
  - '[[Struttura dati (Informatica teorica)]]'
parent note: '[[Albero (Struttura dati)]]'
tags:
  - algorithm-design
  - tree-structures
  - traversal-algorithms
---

- **Visite (Traversal)**:
    - **In-ordine**: Visita sinistra -> Radice -> Destra. `O(n)`.
    - **Pre-ordine**: Radice -> Visita sinistra -> Destra. `O(n)`.
    - **Post-ordine**: Visita sinistra -> Destra -> Radice. `O(n)`.
    - **Per Livelli (Breadth-First)**: Visita i nodi livello per livello usando una coda ausiliaria. `O(n)`.
- **Operazioni Generali**:
    - `INSERT`: `O(1)` (se la posizione di inserimento è già nota)
    - `DELETE`: Più complesso, dipende dal numero di figli del nodo da eliminare, può richiedere un `O(log m)` o `O(n)` nel caso degenere.
    - `SEARCH`: `O(n)` nel caso peggiore (albero degenere).