---
last modified: 2025-09-25T00:41:00.000Z
related: null
tags:
  - algoritmi-ordinamento
  - complessita-computazionale
  - programmazione-dinamica
---


# Definizione di funzione forzante
La **funzione forzante**, o _forcing function_, denotata con $f(n)$, è un componente chiave nelle relazioni di ricorrenza (solitamente equazioni) utilizzate per descrivere la [[Complessità temporale algoritmica|complessità temporale]] degli algoritmi, in particolare quelli che seguono il paradigma [[Divide et impera]].

In sintesi, la funzione forzante $f(n)$ cattura l'essenza computazionale delle operazioni dirette e non ricorsive di un algoritmo Divide et Impera, e il suo confronto con la funzione spartiacque $n^{\log_b a}$ è fondamentale per determinarne la complessità asintotica utilizzando il Master Theorem.

**Ruolo e significato di $f(n)$**: La funzione forzante $f(n)$ racchiude al suo interno tutti i costi non ricorsivi dell'algoritmo. Nello specifico, essa rappresenta la complessità temporale delle fasi di:

1. **Divide (Divisione)**: Il tempo impiegato per suddividere il problema originale in sottoproblemi.
2. **Combina (Combinazione)**: Il tempo necessario per combinare le soluzioni dei sottoproblemi per ottenere la soluzione del problema originale.

Prendendo l'esempio del MergeSort, la sua ricorrenza è $T(n) = 2T(n/2) + \Theta(n)$. Qui, $f(n) = \Theta(n)$, che rappresenta il costo della procedura `Merge` (la fase di combinazione) la quale impiega $\Theta(n)$ tempo per unire due sotto-array di lunghezza $n/2$. La fase di divisione (calcolo del centro dell'array) impiega tempo costante, $\Theta(1)$, che è assorbito da $f(n)$.
