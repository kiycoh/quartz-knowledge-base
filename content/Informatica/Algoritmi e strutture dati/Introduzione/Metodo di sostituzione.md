---
last modified: 24/10/2025 02:55
related: null
tags:
  - machine-learning
  - algorithm-analysis
  - computational-complexity
---
# Cos'è il metodo di sostituzione?
Il **metodo di sostituzione** è una delle principali tecniche per risolvere le ricorrenze, in particolare per dimostrare il valore $\Theta$ di una ricorrenza, spesso calcolando separatamente i limiti $O$ e $\Omega$. Si basa sulla **formulazione intuitiva di una possibile soluzione** (ipotesi induttiva) e sulla sua **dimostrazione per induzione matematica**.

***Passi del Metodo:***
1. **Formulazione dell'Ipotesi:** Si intuisce una forma asintotica per la soluzione $T(n)$, ad esempio $T(n) = O(f(n))$, $T(n) = \Omega(f(n))$ o $T(n) = \Theta(f(n))$. L'intuizione può derivare da casi simili o dall'analisi dell'albero di ricorsione.
2. **Caso Base:** Si verifica che l'ipotesi sia valida per il caso base della ricorrenza (per $n$ sufficientemente piccolo, spesso $n_0=1$).
3. **Passo Induttivo:** Assumendo che l'ipotesi sia vera per tutti i valori $m < n$ (ipotesi induttiva), si deve dimostrare che vale anche per $n$.
    - **Per $O(f(n))$:** Si assume $T(m) \le c \cdot f(m)$ per $m < n$ e si cerca di mostrare $T(n) \le c \cdot f(n)$ per una costante $c$ opportuna e per $n \ge n_0$.
    - **Per $\Omega(f(n))$:** Si assume $T(m) \ge c \cdot f(m)$ per $m < n$ e si cerca di mostrare $T(n) \ge c \cdot f(n)$.

> [!EXAMPLE]-  Esempio di metodo di sostituzione con Merge Sort
> L'algoritmo [[Merge sort]] è un classico esempio di [[Divide et impera]].
> 
> 1. **DIVIDE:** Il problema viene suddiviso in 2 sottoproblemi di dimensione $n/2$ in tempo costante ($\Theta(1)$).
> 2. **IMPERA:** I 2 sottoproblemi vengono risolti ricorsivamente, contribuendo con $2T(n/2)$ al costo totale.
> 3. **COMBINA:** Le soluzioni dei sottoproblemi vengono fuse in tempo $\Theta(n)$.
> 
> La ricorrenza per MergeSort è $T(n) = 2T(n/2) + \Theta(n)$.
>
> ***Dimostrazione $O(n \log n)$ per MergeSort:***>
> - **Ipotesi Induttiva:** $T(n) \le c n \log n$ per qualche costante $c > 0$ e per $n \ge n_0$.
> - **Passo Induttivo:** Sostituiamo l'ipotesi nella ricorrenza: $T(n) \le 2(c \cdot (n/2) \log(n/2)) + \Theta(n)$ $T(n) \le c n \log(n/2) + \Theta(n)$ $T(n) \le c n (\log n - \log 2) + \Theta(n)$ $T(n) \le c n \log n - c n + \Theta(n)$
>
> Affinché $T(n) \le c n \log n$, dobbiamo garantire che $-c n + \Theta(n) \le 0$. Questo è possibile scegliendo una costante $c$ sufficientemente grande in modo che $c n \ge (\text{costante di } \Theta) \cdot n$. Ad esempio, se $\Theta(n)$ è bounded by $k n$, allora $c n \ge k n$, cioè $c \ge k$. Così, $T(n) \le c n \log n$, e quindi $T(n) = O(n \log n)$.
## Errori comuni e soluzioni
Un errore comune si verifica quando i termini di ordine inferiore non sono gestiti correttamente.

- **Problema:** sia la ricorrenza $T(n) = T(n/2) + \Theta(1)$. Se ipotizziamo $T(n) = O(n)$ e tentiamo di dimostrare $T(n) \le cn$: $T(n) \le c(n/2) + \Theta(1) = cn/2 + \Theta(1)$ Questo non è sufficiente per concludere $cn/2 + \Theta(1) \le cn$, poiché $cn/2 + \text{costante}$ non è necessariamente minore o uguale a $cn$ per ogni $n$ se la costante è positiva. La costante $\Theta(1)$ potrebbe essere grande abbastanza da invalidare la disuguaglianza per piccoli $n$.    
- **Soluzione (sottrazione di un termine di ordine inferiore):** per risolvere questo, si aggiunge un termine di ordine inferiore all'ipotesi induttiva, come $T(n) \le cn - d$ per qualche costante $d > 0$. $T(n) \le c(n/2) - d + \Theta(1)$ Scegliamo $\Theta(1)$ come una costante $k$. $T(n) \le c n/2 - d + k$ Vogliamo $c n/2 - d + k \le c n - d$. Questo si semplifica a $k \le c n/2$. Scegliendo $c$ sufficientemente grande (es. $c \ge 2k$), la disuguaglianza vale per $n \ge n_0$. Questo porta a $T(n) = O(n)$.
