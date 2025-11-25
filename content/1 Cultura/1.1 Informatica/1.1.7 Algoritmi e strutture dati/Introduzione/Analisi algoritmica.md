---
last modified: 24/10/2025 02:55
related:
  - '[[Analisi algoritmica]]'
tags:
  - algoritmi-ordinamento
  - analisi-asintotica-matematica
  - efficienza-algoritmica
---
# Definizione di analisi algoritmica
L'analisi algoritmica è la disciplina fondamentale che si occupa di valutare [[Efficienza algoritmica|l'efficienza di un algoritmo]], fornendo un quadro matematico per prevederne il comportamento e confrontare le diverse soluzioni a un medesimo [[Problema computazionale]].

Un [[Algoritmo (Informatica)]] è una procedura ben definita che, dato un input, produce un output in un tempo finito, e deve essere corretto, ovvero risolvere ogni possibile istanza del problema. 

L'efficienza viene misurata principalmente in termini di **tempo di esecuzione** e, secondariamente, di **spazio di memoria** richiesto. È cruciale misurare l'efficienza in modo indipendente dalla tecnologia hardware o dal linguaggio di programmazione specifico. A tal fine, si ricorre all'**[[Analisi asintotica (Matematica)]]**.
### Analisi del Caso Migliore e Peggiore
Per comprendere appieno l'efficienza di un algoritmo, l'analisi algoritmica considera tipicamente due scenari estremi:
- **Caso Migliore**: Si verifica quando l'input è quello più favorevole per l'algoritmo. Ad esempio, per l'InsertionSort, il caso migliore si ha quando l'array è già ordinato; in questa situazione, l'algoritmo impiega un tempo lineare, ovvero $T(n) = \Omega(n)$. Immaginate un mazzo di carte già in ordine crescente: un algoritmo intuitivo per ordinarle noterebbe subito che sono già a posto con pochissimi controlli.
- **Caso Peggiore**: Si verifica quando l'input è quello meno favorevole, che induce il massimo numero di operazioni. Per l'InsertionSort, questo accade quando l'array è ordinato in senso inverso, risultando in un tempo di esecuzione quadratico, $T(n) = \Theta(n^2)$. Pensate a un mazzo di carte in ordine decrescente: per metterlo in ordine crescente, la maggior parte delle carte andrà spostata ampiamente. Anche per il BubbleSort, il caso peggiore e migliore sono entrambi $\Theta(n^2)$.

L'analisi del caso peggiore è spesso la più significativa perché fornisce una garanzia sul limite massimo di tempo che l'algoritmo impiegherà, indipendentemente dall'input.

### Metodi di Analisi delle Ricorrenze
Per gli algoritmi basati sul paradigma Divide et Impera, il tempo di esecuzione è spesso descritto da equazioni di ricorrenza. L'analisi algoritmica fornisce diversi metodi per risolverle:

- **Metodo di Sostituzione**: Si formula un'ipotesi sulla soluzione e la si dimostra per induzione matematica. Richiede intuizione nella formulazione dell'ipotesi.
- **Albero di Ricorsione**: Un metodo grafico dove ogni nodo rappresenta il costo di un sottoproblema ricorsivo. Il costo totale è la somma dei costi di ogni livello.
- **Metodo Principale (Master Theorem)**: Un teorema che permette di risolvere ricorrenze della forma $T(n) = aT(n/b) + f(n)$ in tre casi distinti, confrontando la funzione forzante $f(n)$ con la funzione spartiacque $n^{\log_b a}$. È uno strumento potente per la stima asintotica rapida.

### Correttezza e Pseudocodice
L'analisi algoritmica non si limita alla performance, ma considera anche la **correttezza** dell'algoritmo. La correttezza viene tipicamente dimostrata per ogni possibile input, spesso utilizzando il metodo delle invarianti di ciclo (Inizializzazione, Mantenimento, Conclusione). Per descrivere gli algoritmi in modo indipendente dalle tecnologie, si utilizza uno **pseudocodice**, un linguaggio a metà strada tra il linguaggio naturale e quello di programmazione, con formalismi specifici per garantire non ambiguità.

In sintesi, l'analisi algoritmica è la colonna portante dello studio degli algoritmi, permettendo di comprendere non solo se un algoritmo funziona, ma anche _quanto bene_ funziona, in termini di risorse computazionali, e di guidare la progettazione verso soluzioni sempre più efficienti.

[[Analisi asintotica (Matematica)]]