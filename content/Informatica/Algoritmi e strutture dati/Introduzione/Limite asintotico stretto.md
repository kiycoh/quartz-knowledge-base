---
tags: [algoritmi-ordinamento, complessita-computazionale, ricorrenze]
last modified: 2025, 11, 24 22:11:36
---
# Limite asintotico stretto


Quando un'equazione di ricorrenza è espressa con un simbolo di uguaglianza, come $T(n) = aT(n/b) + f(n)$, significa che la funzione $T(n)$ è precisamente definita da quella relazione. Questo implica che la funzione $T(n)$ non è né asintoticamente più veloce né più lenta della soluzione ottenuta dalla ricorrenza. Pertanto, la soluzione asintotica è un limite stretto, rappresentato dalla notazione $\Theta$.

> [!EXAMPLE] Esempio di limite asintotico stretto
> Consideriamo l'algoritmo [[Merge sort]]. La sua complessità è descritta dalla ricorrenza $T(n) = 2T(n/2) + \Theta(n)$. Questa equazione descrive il comportamento esatto del tempo di esecuzione in base al modello di calcolo, considerando che la fase di divisione è in $\Theta(1)$ e la fase di combinazione (Merge) è in $\Theta(n)$. Risolvendo questa ricorrenza (ad esempio, con il Metodo Principale o il metodo di sostituzione), si dimostra che $T(n) = \Theta(n \log n)$. Questo significa che il tempo di esecuzione del Merge sort cresce esattamente come $n \log n$ per input grandi, sia come limite superiore che inferiore.