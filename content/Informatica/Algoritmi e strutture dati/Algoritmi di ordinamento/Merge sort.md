---
last modified: 2025-09-25T00:41:00.000Z
related: null
tags:
  - algoritmi-ordinamento
  - algoritmi-greedy
  - complessita-computazionale
---


- Merge Sort è un algoritmo ricorsivo di ordinamento basato sul paradigma "Divide et Impera".
- Divide la lista non ordinata in due metà, ordina ciascuna metà e poi combina le due metà ordinate per ottenere una nuova lista completa ordinata.
- L'operazione di fusione (merge) coinvolge la combinazione di due liste ordinate per formarne una nuova.
- ==E' un algoritmo ottimale tra quelli basati su confronti.==

![[merge-sort-example_0-1528667924.png|400]]
# Caratteristiche
- **Ricorsività:** 
	- Caso base: lista vuota o un solo elemento. 
	- L'ordine viene effettuato con due chiamate ricorsive, al termine delle quali si applica la procedura di merge.
- **Stabilità:** Merge Sort è stabile, il che significa che preserva l'ordine relativo degli elementi equivalenti.
- **Complessità di Tempo:** O(N log N) nel caso medio e nel caso peggiore.
- **In-place:** No perché Merge Sort richiede spazio aggiuntivo per l'operazione di fusione.
# Analisi con metodo [[Divide et impera]]
- Divide: Si calcola il centro dell'array i tempo costante quindi D(n)= $\Theta(1)$
- Impera: Il passo ricorsivo divide in 2 sotto-problemi di dimensione n/2
- Combina

# Analisi con alberi

# Metodo di sostituzione
SLIDES ALGORITMI 27/02