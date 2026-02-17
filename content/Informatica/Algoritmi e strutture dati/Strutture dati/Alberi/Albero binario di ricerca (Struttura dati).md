---
last modified: 2025, 11, 23 20:11:11
tags:
  - algoritmi-ordinamento
  - struttura-dati
  - albero-binario
---
# Albero binario di ricerca (Struttura dati)
Un **albero binario di ricerca** (anche chiamato **binary search tree**) è un tipo speciale di [[Albero binario (Struttura dati)]] che mantiene una relazione d'ordine tra gli elementi: per ogni nodo `x`, tutti i valori nel suo sottoalbero sinistro sono minori o uguali a `x.key`, e tutti i valori nel suo sottoalbero destro sono maggiori di `x.key`.
    - **Vantaggi**:
        - Una visita in ordine stampa i nodi in ordine crescente.
        - `MINIMUM` e `MAXIMUM` sono facili da determinare.
        - La ricerca di un elemento è efficiente.
## Operazioni su albero binario di ricerca 
La complessità dipende dall'altezza dell'albero `h`, che nel caso peggiore (albero degenere) è `O(n)` e nel caso migliore/medio (albero bilanciato) è `O(log n)`):
- `SEARCH(N, k)`: Ricorsiva o iterativa. Segue i rami in base al confronto con `k`. **Ω(log n)** nel caso migliore, **O(n)** nel caso peggiore. - `INSERT(T, z)`: Trova la posizione appropriata per `z` mantenendo la proprietà di ordinamento. **Ω(log n)** nel caso migliore, **O(n)** nel caso peggiore.
- `DELETE(T, z)`: Più complessa a causa del mantenimento dell'ordinamento. Utilizza una procedura `TRANSPLANT` per sostituire i nodi. La complessità dipende dalla ricerca del successore. **O(h)**.
- `MINIMUM(T)`, `MAXIMUM(T)`: Seguono rispettivamente il ramo sinistro estremo e il ramo destro estremo. **O(h)**, quindi **O(log n)** nel caso migliore.
- `PREDECESSOR(T, k)`, `SUCCESSOR(T, k)`: Simili alla ricerca, ma cercano il nodo con chiave immediatamente inferiore/superiore. **O(h)**.

## Problemi di un albero di ricerca
Le performance possono degradare rispetto a quelle di una [[Lista concatenata (Struttura dati)]] se l'albero diventa degenere (es. inserendo elementi già ordinati).