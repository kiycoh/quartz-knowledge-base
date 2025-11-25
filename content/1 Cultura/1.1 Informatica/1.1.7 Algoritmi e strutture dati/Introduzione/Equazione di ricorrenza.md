---
last modified: 24/10/2025 02:55
related:
  - '[[Algoritmo (Informatica)]]'
  - '[[Ricorsione (Informatica)]]'
tags:
  - algoritmi-ordinamento
  - ricorsione
  - analisi-asintotica
---
# Definizione di equazione di ricorrenza 
==Una **equazione di ricorrenza** è un'equazione matematica che *descrive una funzione in termini del suo valore in altri argomenti.*== Le equazioni di ricorrenza permettono di descrivere matematicamente i tempi di esecuzione di un algoritmo ricorsivo.
* Se la ricorrenza è espressa con '=' allora si userà la notazione $\Theta$, se con '<' allora si userà $O$, se con '>' allora si userà $\Omega$ $\to$ [[Analisi asintotica (Matematica)]]

Formalmente, in una ricorrenza della forma: $$T(n) = aT(n/b) + f(n)$$
- $T(n)$ è il tempo di esecuzione dell'algoritmo per un input di dimensione $n$.
- $a$ è il numero di sottoproblemi in cui il problema originale viene diviso, con $a \ge 1$.
- $n/b$ è la dimensione di ciascun sotto-problema, dove $b > 1$ è una costante.
- $f(n)$ è la **[[funzione forzante]]**.

1. **Caso base**: ogni equazione di ricorrenza deve essere accompagnata da un "caso base", ovvero una condizione che non è definita in termini ricorsivi. Questo è il punto in cui la ricorsione si ferma.
2. **Passo ricorsivo**: questo è il cuore dell'equazione e di solito è composto da due parti: 
	1. il costo delle chiamate ricorsive e 
	2. il costo del lavoro svolto al di fuori di esse (come la divisione del problema o la combinazione dei risultati).


> [!EXAMPLE] Esempio di equazione di ricorrenza (MergeSort)
> L'equazione di ricorrenza T(n) = 2T(n/2) + Θ(n) descrive perfettamente questo concetto:
> - **2T(n/2)**: Il costo per risolvere ricorsivamente due sottoproblemi di dimensione dimezzata.
> - **Θ(n)**: Il costo (lineare) per combinare le soluzioni dei sottoproblemi.
> 	- In [[Analisi algoritmica]] utilizziamo sempre ricorrenze il cui caso base è $T(n)=\Theta(1)$ per una certa soglia abbastanza piccola.
# Come risolvere una ricorrenza?
Per dimostrare il valore $\Theta$ di una ricorrenza il più delle volte conviene calcolare il valore $O$ e $\Omega$.
Una ricorrenza può essere risolta utilizzando diversi metodi:
-  **[[Metodo di sostituzione]]**: si formula un’ipotesi e si usa un’induzione matematica per dimostrarla
-  **[[Albero di ricorsione (Struttura dati)|Albero di ricorsione]]**: metodo grafico in cui si utilizza un albero per rappresentare la ricorsione
- **[[Masters theorem (Algoritmo)]]**: metodo principale che permette di risolvere tramite l'analisi di 3 possibili casi di ricorrenze nella forma:
-  **Akra-Bazzi**: generalizzazione del metodo principale per ogni tipo di equazione di ricorrenza