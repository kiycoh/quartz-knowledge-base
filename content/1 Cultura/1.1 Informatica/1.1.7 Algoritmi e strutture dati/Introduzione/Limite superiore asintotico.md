---
tags:
  - algoritmi-ordinamento
  - complessita-computazionale
  - time-complexity
---

Se un'equazione di ricorrenza è espressa con un simbolo di disuguaglianza del tipo "$<$" (o più frequentemente "$\le$"), significa che stiamo fornendo un limite superiore per il tempo di esecuzione. Questo indica che il costo dell'algoritmo non supererà mai asintoticamente il valore definito dalla ricorrenza. Di conseguenza, si utilizza la notazione Big O, che formalizza proprio questo concetto di limite superiore asintotico.


> [!EXAMPLE] Esempio di limite superiore asintotico
> Immaginiamo di analizzare un algoritmo e di poter dire che, nel peggiore dei casi, ogni passo ricorsivo impiega "al più" una certa quantità di tempo, o che la funzione di costo delle operazioni "Divide" e "Combina" è "al più" $f(n)$. Questo porta a una ricorrenza del tipo $T(n) \le aT(n/b) + f(n)$. Se, per esempio, tramite il metodo di sostituzione, si fa un'ipotesi $T(n) \le cn \log n$ per il MergeSort, questa è una dimostrazione per $O(n \log n)$. Se la dimostrazione non può essere resa bidirezionale (perché magari l'analisi è volutamente più pessimistica o non completa), allora si rimane nell'ambito del limite superiore.
