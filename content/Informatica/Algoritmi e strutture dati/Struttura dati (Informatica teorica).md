---
last modified: 2025, 11, 22 18:11:45
related:
  - '[[Algoritmo (Informatica)]]'
tags:
  - struttura-dati
  - algoritmi-ordinamento
  - complessita-computazionale
---
# Struttura dati
==Una **struttura dati** è un modo formale per organizzare i dati in un insieme, consentendo la manipolazione (processamento, conservazione) e l'esaminazione (ricerca)== tramite vari metodi. La scelta di una struttura dati è cruciale per l'[[efficienza algoritmica]], poiché influenza direttamente la [[complessità temporale algoritmica|complessità temporale]] e spaziale.
- [[Tipi di strutture dati]]
- [[Classificazione delle strutture dati]]

>![[Le strutture dati (Informatica)_image_1.png]]
>[[Array (Struttura dati)|Un'array monodimensionale]] è una delle strutture dati più semplici.

> [!warning] Correlazione tra struttura dati e algoritmi
> La scelta di una struttura rispetto ad un'altra è strettamente legata a quella degli algoritmi, per questo spesso vengono considerati insieme. In altre parole la scelta della struttura dati influisce inevitabilmente sull'efficienza computazionale degli algoritmi che la manipolano.

## 4. Strutture Dati Basate su Chiavi
Queste strutture organizzano i dati in base a una chiave associata a ciascun elemento, consentendo un accesso rapido.

- **[[Direct Address Table]]**
- **[[Hash table]]**:
- [[Tipi di strutture dati relazionali]]
## 6. Strutture Dati Specializzate per Insiemi

- **S (Disjoint Set Data Structure)**:
    - **Descrizione**: Mantiene una famiglia di insiemi dinamici disgiunti. Ogni insieme è identificato da un *elemento rappresentante*.
    - **Operazioni**:
        - `MakeSet(x)`: Crea un nuovo insieme contenente solo `x`.
        - `Union(x, y)`: Unisce i due insiemi contenenti `x` e `y`.
        - `FindSet(x)`: Restituisce il rappresentante dell'insieme che contiene `x`.
    - **Implementazione (con liste concatenate modificate)**: Ogni lista ha puntatori a `head` e `tail`, e ogni nodo ha un puntatore `back` alla testa della sua lista.
        - `MakeSet(x)`: **O(1)**.
        - `FindSet(x)`: **O(1)** (seguendo il puntatore `back`).
        - `Union(u, v)`: La lista di un insieme viene concatenata all'altra, e i puntatori `back` di tutti i nodi della lista unita devono essere aggiornati. **O(n)** nel caso peggiore (dove `n` è la dimensione dell'insieme più piccolo).
    - **Complessità Ammortizzata**: Una sequenza di `m` operazioni (`MakeSet`, `FindSet`, `Union`) su `n` elementi ha complessità **O(m + n log n)**.
    - **Utilizzo Pratico**: Algoritmo di Kruskal per il Minimum Spanning Tree.