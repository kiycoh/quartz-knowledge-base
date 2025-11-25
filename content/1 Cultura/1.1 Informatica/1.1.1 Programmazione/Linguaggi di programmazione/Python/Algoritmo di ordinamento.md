---
last modified: 24/10/2025 02:54
related:
  - '[[Complessità temporale algoritmica]]'
  - '[[Tester algoritmi di ordinamento (Python)]]'
tags:
  - algoritmi-ordinamento
  - complessita-computazionale
  - programmazione-algoritmica
---
# Cos'è un algoritmo di ordinamento?
Dato una lista di elementi presi da un insieme disordinato, l'obiettivo è **trovare una permutazione degli elementi della lista in modo tale che la lista ottenuta risulti ordinata rispetto alla relazione d'ordine** (per esempio, rispetto alla relazione >=).
* **[[Complessità temporale algoritmica]]**: dato un problema, si sarà in grado di valutare l'esistenza o meno di un algoritmo in grado di risolverlo. Un problema è **computabile** se esiste un algoritmo in grado di risolverlo.

![[Algoritmi di ordinamento_image_1.png|600]]

Un algoritmo di ordinamento può essere:
1. **Stabile**: se preserva l'ordine iniziale tra gli elementi uguali.
2. **In-place**: l'ordinamento viene fatto direttamente in input (*senza utilizzare ulteriori liste*).

## Tipi di algoritmi di ordinamento
## [[Selection Sort]]
- Il Selection Sort **trova il minimo elemento e lo sposta a sinistra** mettendolo in coda.
- Ad ogni iterazione, seleziona il minimo dalla parte non ordinata e lo sposta nella parte ordinata.
- **Complessità di Tempo quadratica:** O($N^2$) nel caso peggiore e nel caso medio.
- **In-place**
- **Stabile**

## [[Insertion sort]]
- L'Insertion Sort **considera ogni elemento uno alla volta e lo inserisce nella posizione corretta** rispetto agli elementi già ordinati.
- Solo alla fine, gli elementi si troveranno nel giusto ordine.
- **Complessità di Tempo quadratica:** O($N^2$) nel caso peggiore e nel caso medio, ma può essere efficiente per piccoli dataset.
- **In-place**
- **Stabile**

## [[Bubble Sort]]
- Il Bubble Sort **confronta e scambia gli elementi adiacenti** finché la lista non è ordinata. Ad ogni passo, il più grande elemento "galleggia" verso la fine della lista.
- Alla fine dell'iterazione gli ultimi elementi più grandi si ritroveranno nella loro posizione definitiva.
- **Complessità di Tempo:** O($N^2$) nel caso peggiore e nel caso medio.
- **In-place**
- **Stabile

## [[Merge sort]]
- Merge Sort **divide la lista a metà**, ordina separatamente le due metà e poi le unisce in modo ordinato.
- Basato un algoritmo ricorsivo.
- **Complessità di Tempo quasi-lineare:** O(N log N) nel caso peggiore e nel caso medio.
- *Non In-place* in quanto richiede spazio aggiuntivo (crea una nuova lista).
- **Stabile**

## [[Quick Sort]]
- Quick Sort sceglie un elemento come **pivot**, divide la lista in base al pivot, e ordina ricorsivamente le parti più piccole.
- **Complessità di Tempo quadratica:** O($N^2$) nel caso peggiore (raro), O(N log N) in media.
- **In-place**
- *Instabile* perché è incentrato su un elemento pivot ma può essere implementato per essere stabile.

## [[Couting Sort]]



