---
tags:
  - algoritmi-ordinamento
  - ricorrenze
  - algoritmi-greedy
---

Il **Master Theorem** (o Teorema Principale) è uno strumento potente per risolvere ricorrenze del tipo $T(n) = aT(n/b) + f(n)$. La chiave per applicare questo teorema è confrontare la funzione forzante $f(n)$ con una funzione ausiliaria chiamata "funzione spartiacque", definita come $n^{\log_b a}$.

Il Master Theorem si articola in tre casi principali, ciascuno basato su questo confronto:
1. **Caso 1**: Se la funzione spartiacque $n^{\log_b a}$ cresce asintoticamente **più velocemente** di $f(n)$ di almeno un fattore polinomiale, ovvero se $f(n) = O(n^{\log_b a - \epsilon})$ per qualche costante $\epsilon > 0$, allora il costo totale è dominato dalla radice dell'albero di ricorsione. In questo caso, $T(n) = \Theta(n^{\log_b a})$.
    - **Esempio**: Per la ricorrenza $T(n) = 9T(n/3) + n$:
        - $a=9$, $b=3$.
        - La funzione spartiacque è $n^{\log_3 9} = n^2 = \Theta(n^2)$.
        - La funzione forzante è $f(n) = n$.
        - Poiché $n = O(n^{2 - \epsilon})$ per $\epsilon = 1$, rientriamo nel Caso 1.
        - Quindi, $T(n) = \Theta(n^2)$.
2. **Caso 2**: Se le due funzioni $n^{\log_b a}$ e $f(n)$ hanno all'incirca lo **stesso tasso di crescita**, ovvero se $f(n) = \Theta(n^{\log_b a} \lg^k n)$ per qualche costante $k \ge 0$, allora il costo totale è distribuito uniformemente su tutti i livelli dell'albero di ricorsione. In questo caso, $T(n) = \Theta(n^{\log_b a} \lg^{k+1} n)$.
    
    - **Esempio**: Per la ricorrenza $T(n) = T(2n/3) + 1$:
        - $a=1$, $b=3/2$.
        - La funzione spartiacque è $n^{\log_{3/2} 1} = n^0 = 1$.
        - La funzione forzante è $f(n) = 1$.
        - Poiché $f(n) = \Theta(1 \lg^0 n) = \Theta(1)$, rientriamo nel Caso 2 con $k=0$.
        - Quindi, $T(n) = \Theta(1 \cdot \lg^{0+1} n) = \Theta(\lg n)$.
3. **Caso 3**: Se la funzione forzante $f(n)$ cresce asintoticamente **più velocemente** di $n^{\log_b a}$ di almeno un fattore polinomiale, e soddisfa una condizione di regolarità ($a f(n/b) \le c f(n)$ per una costante $c < 1$), allora il costo totale è dominato dalla funzione forzante stessa (cioè dalle operazioni non ricorsive). In questo caso, $T(n) = \Theta(f(n))$.
    
    - **Esempio**: Per la ricorrenza $T(n) = 3T(n/4) + n\lg n$:
        - $a=3$, $b=4$.
        - La funzione spartiacque è $n^{\log_4 3} \approx n^{0.792}$.
        - La funzione forzante è $f(n) = n\lg n$.
        - Poiché $n\lg n = \Omega(n^{\log_4 3 + \epsilon})$ per $\epsilon \approx 0.2$ (ad esempio, $\log_4 3 + 0.2 = 0.792 + 0.2 = 0.992$, che è meno di 1, quindi $n\lg n$ cresce più velocemente), e verificando la condizione di regolarità: $a f(n/b) = 3(n/4)\lg(n/4) = (3/4)n(\lg n - \lg 4) = (3/4)n\lg n - (3/2)n$. Possiamo scegliere $c=3/4 < 1$ in modo che $3f(n/4) \le c f(n)$ per $n$ sufficientemente grande.
        - Rientriamo nel Caso 3.
        - Quindi, $T(n) = \Theta(n\lg n)$.