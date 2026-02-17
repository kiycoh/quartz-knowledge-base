---
last modified: 27/10/2025 18:51
related:
  - '[[Struttura dati (Informatica teorica)]]'
  - '[[Algoritmo di visita]]'
  - '[[Complessità algoritmica]]'
tags:
  - algoritmo-informatica
  - complessita-computazionale
  - analisi-asintotica
---
# Definizione di algoritmo in informatica
==Un **algoritmo** è una procedura di calcolo formale che prende in input uno o un insieme di valori e genera uno o un insieme di output.== In altre parole un algoritmo è una procedura ben definita che per mezzo di una sequenza finita di operazioni risolve un problema computazionale o una classe di problemi.
* **[[Efficienza algoritmica]]:** per un dato problema, possono esistere molteplici algoritmi, occorre capire quale tra i possibili algoritmi impiega meno risorse 
	* Grazie all'[[Equazione di ricorrenza|equazione di ricorrenza]] (utilizzato nell'[[Analisi asintotica (Matematica)]]è possibile descrivere in modo matematico i tempi di esecuzione di un algoritmo del tipo [[Divide et impera]]. 
* ***Proprietà di un algoritmo:***
	- Un algoritmo DEVE essere corretto.
	- Un algoritmo può essere efficiente.

> [!NOTE] Visualizzare graficamente un algoritmo
> Un algoritmo mette in relazione l'insieme di istanze del problema e l'insieme di soluzioni.
> ```mermaid
> flowchart LR
> Problemi --Algoritmo ---> Soluzioni
> Soluzioni --Verifica---> Problemi
>  ```

### [[Analisi asintotica (Matematica)]]
In informatica per calcolare la complessità computazionale di un algoritmo si utilizza l'**analisi asintotica**. 
Tuttavia, l'analisi asintotica è uno strumento della matematica che si applica alle funzioni, mentre il tempo di esecuzione non lo è.
## Correttezza
La correttezza deve essere dimostrata su ogni possibile input. Uno dei possibili metodi è quello delle *invarianti di ciclo*.

Occorre dimostrare che il valore rimanga invariato durante l'inizializzazione, il mantenimento e la conclusione del codice.

Come calcolare l'invariante? L'invariante è una condizione di soddisfacimento.

Alcuni algoritmi, anche se non corretti, possono tornare utili in ambito AI. Se ad esempio un testiamo un algoritmo e questo restituisce soluzioni quantomeno vicine ad un risultato soddisfacente ma non esattamente corrette, va bene così perché in un futuro (attraverso ad esempi il deep learning) potrebbe raggiungere al risultato atteso.
## [[Algoritmo di ordinamento]]
-  Gli algoritmi di ordinamento permettono di posizionare ordinatamente degli elementi disordinati di una lista.