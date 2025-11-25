---
last modified: 2025-07-11T18:40:00.000Z
related:
  - '[[Analisi algoritmica]]'
  - '[[Notazione asintotica]]'
  - '[[Efficienza algoritmica]]'
tags:
  - algoritmi-ordinamento
  - analisi-asintotica
  - efficienza-algoritmica
---
# Cos'è l'analisi asintotica?
In matematica l'analisi asintotica consente di confrontare il tasso di crescita (comportamento asintotico) di una funzione nei confronti di un'altra, è utilizzato in [[Analisi algoritmica]].
Per usare l'analisi asintotica devo **trasformare il tempo di esecuzione dell'algoritmo in una funzione $T(n)$ in funzione della dimensione n dei dati input**.
* In genere la funzione $T(n)$ misura il numero di comandi eseguiti dall'algoritmo.

![[350px-Omega_e_O_grande_di_f.gif]]

* Se la ricorrenza è espressa con = allora si userà la notazione $\Theta$, se con < allora si userà O, se con > allora si userà $\Omega$
* Le **[[Equazione di ricorrenza|equazioni di ricorrenza]]** rappresentano lo strumento matematico per descrivere il tempo di esecuzione $T(n)$ di tali algoritmi in funzione della dimensione dell'input $n$.

