---
tags:
  - machine-learning
  - analisi-matematica
  - continuous-functions
---

Il Teorema dei Valori Intermedi è un concetto fondamentale nell'analisi matematica, che riguarda il comportamento delle funzioni continue. Questo teorema afferma che una funzione continua su un intervallo assumerà ogni valore tra il suo valore massimo e minimo in quell'intervallo.

>[!teorema]
>Se $f(x)$ è una funzione continua su un intervallo chiuso $[a, b]$ e $k$ è un numero tra $f(a)$ e $f(b)$ (inclusi), allora esiste almeno un punto $c \in [a, b]$ tale che $f(c) = k$.

Questo teorema garantisce che, se hai una funzione continua su un intervallo e scegli un valore $k$ tra il minimo e il massimo della funzione su quell'intervallo, ci sarà almeno un punto nell'intervallo in cui la funzione assume quel valore $k$.

### Applicazioni e Importanza

1. **Esistenza di valori**: Il teorema aiuta a stabilire l'esistenza di valori specifici per le funzioni in determinati intervalli.
2. **Analisi topologica**: Fornisce un'importante connessione tra la continuità delle funzioni e le proprietà topologiche degli intervalli.

### Dimostrazione

- La dimostrazione si avvale della continuità della funzione e delle proprietà degli intervalli chiusi e limitati.
- Si considerano i valori di $f(x)$ agli estremi dell'intervallo e si applica un ragionamento simile a quello usato nel Teorema di Bolzano per mostrare che tutti i valori intermedi devono essere assunti dalla funzione.

### Esempio

- Prendi la funzione $f(x) = x^3 - x$ sull'intervallo $[-2, 2]$.
- Nota che $f(-2) = -6$ e $f(2) = 6$. Se scegliamo un $k$ qualsiasi tra $-6$ e $6$, per esempio $k = 0$, il teorema garantisce che c'è almeno un $c$ in $[-2, 2]$ tale che $f(c) = 0$.
- In questo caso, si può verificare che $f(0) = 0$, quindi $c = 0$ soddisfa la condizione.