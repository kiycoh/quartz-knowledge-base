---
last modified: 2025-07-12T17:39:00.000Z
related:
  - '[[Algoritmo (Informatica)]]'
  - '[[Complessità temporale algoritmica]]'
tags:
  - algoritmi-ordinamento
  - efficienza-algoritmica
  - analisi-asintotica
---
# Definizione di efficienza algoritmica
==L'**efficienza algoritmica** è una misura di quanto un algoritmo sia in grado di svolgere un determinato compito in relazione all'utilizzo delle risorse e al tempo: *meno risorse un algoritmo usa, più è efficiente.*==

Si definisce un algoritmo **più efficiente** rispetto ad un altro quando a parità di condizioni uno impiega meno tempo per risolvere correttamente un dato problema computazionale rispetto all'altro.
## Misurare l’efficienza algoritmica
Per poter confrontare diversi algoritmi occorre misurare l’efficienza in **modo indipendente dalla tecnologia implementativa** vera e propria. Si considerano le variabili **tempo**, e **spazio** ([[Analisi asintotica (Matematica)]]) 
* Spazio e tempo sono solitamente legati in maniera "inversamente proporzionale". 
	* *Sprecare più spazio per ottenere un algoritmo più efficiente in termini di tempo e viceversa.*
### Caso migliore e peggiore
Per comprendere appieno l'efficienza di un algoritmo, l'[[Analisi algoritmica]] considera tipicamente due scenari estremi:
- **Caso migliore**: quando l'input è quello più favorevole per l'algoritmo.
- **Caso peggiore**: quando l'input è quello meno favorevole, che induce il massimo numero di operazioni.
	- *L'analisi del caso peggiore è spesso la più significativa perché fornisce una garanzia sul limite massimo di tempo che l'algoritmo impiegherà, indipendentemente dall'input.*

