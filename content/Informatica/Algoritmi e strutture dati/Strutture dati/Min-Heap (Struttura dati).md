---
tags:
  - algoritmi-ordinamento
  - heap-minimo
  - alberi-binari
---

Il **Min-heap** è struttura dati basata su un array che rappresenta un albero binario _quasi completo_. Ogni nodo dell'albero corrisponde a un elemento dell'array, e i livelli sono riempiti da sinistra a destra. Soddisfa la _proprietà di heap_: il valore di un nodo è minore o uguale a quello dei suoi figli (`A[Parent(i)] <= A[i]`). Di conseguenza, l'elemento più piccolo si trova sempre nella radice.
    - **Operazioni su Indici**: `Parent(i)`, `Left(i)`, `Right(i)` sono calcolate in **O(1)**.
    - **Utilizzo per Code a Priorità**: Implementa in modo efficiente una coda a priorità.
    - **Operazioni e Complessità (per Min-Heap)**:
        - `Minimum(A)`: Restituisce la radice. **O(1)**.
        - `Extract-Minimum(A)`: Rimuove l'elemento più piccolo (la radice) e ripristina la proprietà di heap. **O(log n)**.
        - `Decrease-Key(A, x, k)`: Diminuisce la chiave di un elemento `x` al nuovo valore `k` e ripristina la proprietà di heap. **O(log n)**.
        - `Insert(A, x, n)`: Inserisce un nuovo elemento e ripristina la proprietà di heap. **O(log n)**.
    - **Utilizzo Pratico**: Implementazione di algoritmi come Prim per il Minimum Spanning Tree e Dijkstra per i cammini minimi, dove è fondamentale estrarre ripetutamente l'elemento con priorità minima.