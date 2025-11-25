---
tags:
  - machine-learning
  - scienze-cognitive
  - intelligenza-artificiale
---

Il Teorema di Weierstrass è uno dei teoremi fondamentali dell'analisi matematica che si occupa delle funzioni continue. Esso stabilisce delle proprietà molto importanti relative all'esistenza di valori massimi e minimi per le funzioni continue in intervalli chiusi e limitati.

>[!teorema] 
>Se una funzione $f(x)$ è continua in un intervallo chiuso e limitato $[a, b]$, allora $f(x)$ assume un valore massimo e un valore minimo in $[a, b]$.

Questo significa che esistono due punti $c$ e $d$ in $[a, b]$ tali che per ogni $x$ in $[a, b]$, $f(c) \leq f(x) \leq f(d)$.

### Applicazioni e Importanza

1. **Esistenza di massimi e minimi**: Questo teorema garantisce che ogni funzione continua in un intervallo chiuso e limitato ha un massimo e un minimo assoluto in quell'intervallo.
2. **Analisi**: Il teorema è cruciale nell'analisi, in particolare nello studio dell'ottimizzazione e nella ricerca dei punti di massimo e minimo per le funzioni.

### Dimostrazione

- La dimostrazione si basa su due concetti: la continuità della funzione e la completezza dei numeri reali.
- Si costruisce una successione di punti in $[a, b]$ dove i valori della funzione $f(x)$ sono sempre più vicini al supposto massimo (o minimo).
- Utilizzando la continuità di $f(x)$ e le proprietà dei numeri reali, si mostra che esiste un limite per questa successione e che tale limite è il valore massimo (o minimo) cercato.

### Esempio

- Considera la funzione $f(x) = x^2$ sull'intervallo $[0, 2]$. Questa funzione è continua in $[0, 2]$.
- Applicando il teorema di Weierstrass, possiamo dire che $f(x)$ raggiunge il suo valore massimo e minimo in questo intervallo.
- In questo caso, $f(x)$ ha un minimo in $x = 0$ ($f(0) = 0)$ e un massimo in $x = 2 (f(2) = 4)$.