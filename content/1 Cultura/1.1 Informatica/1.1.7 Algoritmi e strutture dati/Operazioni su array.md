---
last modified: 2025, 11, 23 20:11:10
related: null
tags:
  - algoritmi-ordinamento
  - efficienza-algoritmica
  - array-operazioni
---
# Operazioni su array
- `INDEX(S, i)`: Accesso diretto all'elemento in posizione `i`. **O(1)**.
- `SEARCH(S, k)`: Ricerca di un elemento `k` tramite scansione lineare. **O(n)**.
- `INSERT(S, x, i)`: Inserimento di un elemento `x` in posizione `i`. Richiede lo spostamento di tutti gli elementi successivi. **O(n)**.
- `DELETE(S, x)`: Cancellazione di un elemento `x`. Richiede lo spostamento degli elementi successivi per mantenere la contiguità. **O(n)**.
- `MINIMUM(S)`, `MAXIMUM(S)`: Ricerca del valore minimo/massimo. Richiede la scansione completa. **O(n)**.
- `PREDECESSOR(S, x)`, `SUCCESSOR(S, x)`: Ricerca del predecessore/successore di `x`. Richiede la scansione completa. **O(n)**.

> [!warning] L'inserting è un'operazione costosa?
> In alcuni casi l'operazione di inserting può diventare esponenzialmente costosa (a livello temporale) a seconda di quanti elementi già esistenti nell'array bisognerebbe spostare.