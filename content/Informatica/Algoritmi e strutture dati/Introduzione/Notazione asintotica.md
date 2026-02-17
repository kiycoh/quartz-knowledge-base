---
tags:
  - algoritmi-ordinamento
  - complessita-computazionale
  - notazione-asintotica
---

# Notazione asintotica
*   **Notazione O (O)**: Fornisce un **[[Limite superiore asintotico]]**. Si usa per descrivere il caso peggiore (worst-case). affermare che un algoritmo è *O(n²)* significa che il suo tempo di esecuzione, nel caso peggiore, non crescerà più velocemente di una funzione quadratica.
    *   *Esempio dalla lezione*: la complessità nel caso peggiore di InsertionSort è *Θ(n²)*, che implica anche che sia *O(n²)*.

*   **Notazione Omega (Ω)**: fornisce un **[[Limite inferiore asintotico]]**. Si usa per descrivere il caso migliore (best-case). Affermare che un algoritmo è *Ω(n)* significa che, anche nel caso più favorevole, impiegherà un tempo che cresce almeno linearmente con *n*.
    *   *Esempio dalla lezione*: La complessità nel caso migliore di InsertionSort è *Ω(n)*.

*   **Notazione Theta (Θ)**: fornisce un **[[Limite asintotico stretto]]**. Si usa quando il tempo di esecuzione è limitato sia superiormente che inferiormente dalla stessa funzione. Indica il comportamento "esatto" dell'algoritmo.
    *   *Esempio dalla lezione*: La complessità nel caso peggiore di InsertionSort è descritta come *Θ(n²)*, perché la sua funzione di costo T(n) = an² + bn - c, per *n* grande, è strettamente legata a *n²*.

Le **complessità O esponenziale** e **fattoriale** si verificano quando l'algoritmo mostra crescita esponenziale o fattoriale rispetto alla dimensione dei dati, portando a tempi di esecuzione elevati.

