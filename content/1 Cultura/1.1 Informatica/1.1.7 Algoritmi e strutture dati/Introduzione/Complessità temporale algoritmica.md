---
last modified: 2025-09-25T00:41:00.000Z
related:
  - '[[Analisi asintotica (Matematica)]]'
tags:
  - algoritmi-ordinamento
  - complessita-computazionale
  - efficienza-algoritmica
---

# Definizione di complessità temporale
La **complessità temporale** di un algoritmo quantifica quanto tempo impiega un [[Algoritmo (Informatica)]] per essere eseguito, in funzione della dimensione dell'input (indicata come $n$). 
In altre parole ==La **complessità di tempo** misura quanto tempo un algoritmo impiega per completare un'operazione== e viene valutata attraverso la "Big-O Notation", che indica le **prestazioni** di un'operazione specifica ([[Efficienza algoritmica]])
* *Per valutare la complessità di un algoritmo si utilizza sempre l'ipotesi del caso peggiore.*

Invece di misurare il tempo in secondi (che dipende dall'hardware e dal linguaggio di programmazione), si contano le operazioni elementari eseguite dall'algoritmo ([[Analisi asintotica (Matematica)]])
## Tipi di complessità temporale
- **Complessità O(N)**: Tempo costante, indipendente dalla dimensione dei dati (ad es. accesso al primo elemento di una lista).
- **Complessità O(log N)**: Tempo logaritmico, riduce la dimensione dei dati ad ogni passaggio dell'operazione.
- **Complessità O(N log N)**: Tempo quasi-lineare, ogni operazione sul taglio di dati ha complessità logaritmica.
- **Complessità O($N^2$)**: Tempo quadratico, proporzionale al quadrato degli elementi nella collezione.

