---
tags:
  - teoria-probabilità
  - analisi-matematica
  - teorema-di-bayes
---

Il Teorema di Esistenza degli Zeri, noto anche come Teorema degli Zeri o Teorema di Bolzano, è un altro risultato fondamentale dell'analisi matematica che riguarda le funzioni continue. Questo teorema fornisce una condizione sotto la quale possiamo affermare l'esistenza di almeno uno zero per una funzione continua in un certo intervallo.

>[!teorema] 
>Se $f(x)$ è una funzione continua su un intervallo chiuso $[a, b]$ e $f(a)$ e $f(b)$ hanno segni opposti (cioè $f(a) \cdot f(b) < 0$), allora esiste almeno un $c \in (a, b)$ tale che $f(c) = 0$.

### Applicazioni e Importanza

1. **Trovare le radici**: Questo teorema è particolarmente utile per determinare l'esistenza di radici (zeri della funzione) in un dato intervallo.
2. **Analisi numerica**: Il teorema è alla base di metodi numerici per trovare le radici delle funzioni, come il metodo di bisezione.

### Dimostrazione

- La dimostrazione si basa sulla continuità della funzione e sull'idea intuitiva che, se una funzione continua passa da un valore negativo a un valore positivo, deve attraversare l'asse delle $x$ (dove $f(x) = 0$).
- Si utilizza un approccio di bisezione, restringendo progressivamente l'intervallo di ricerca fino a trovare un intervallo sufficientemente piccolo in cui la funzione cambia segno, indicando la presenza di uno zero.

### Esempio

- Considera la funzione $f(x) = x^2 - 4$ sull'intervallo $[0, 3]$.
- Qui, $f(0) = -4$ e $f(3) = 5$. Poiché $f(0) \cdot f(3) < 0$, per il teorema, esiste almeno un valore $c \in (0, 3)$ tale che $f(c) = 0$.
- In effetti, $f(2) = 0$, quindi $c = 2$ è uno zero di $f(x)$ nell'intervallo dato.