---
tags:
  - algoritmi-ordinamento
  - complessita-computazionale
  - omega
---

se un'equazione di ricorrenza è espressa con un simbolo di disuguaglianza del tipo "$>$" (o più frequentemente "$\ge$"), significa che stiamo fornendo un **limite inferiore** per il tempo di esecuzione. Questo indica che il costo dell'algoritmo sarà sempre asintoticamente almeno pari al valore definito dalla ricorrenza. Pertanto, si utilizza la notazione Omega, che formalizza il concetto di limite inferiore asintotico.


> [!EXAMPLE] Esempio di limite inferiore asintotico
> Consideriamo l'algoritmo [[Insertion sort]]. Nel suo caso migliore, ovvero quando l'array di input è già ordinato, l'algoritmo esegue un numero di operazioni proporzionale a $n$. Questo comportamento è descritto come $T(n) = \Omega(n)$. 
> 
> Un altro esempio è la dimostrazione dei limiti inferiori per gli algoritmi di ordinamento basati su confronti: un albero di decisione per l'ordinamento con $n$ elementi ha almeno $n!$ foglie, e la sua altezza minima (che rappresenta il numero minimo di confronti nel caso peggiore) è $\Omega(n \log n)$. Questo ci dice che qualunque algoritmo di ordinamento basato su confronti impiegherà almeno $\Omega(n \log n)$ tempo nel caso peggiore.
