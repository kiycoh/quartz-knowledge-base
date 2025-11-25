---
last modified: 2025, 11, 24 17:11:26
related:
  - '[[Ricerca ad albero Monte Carlo (MCTS)]]'
  - '[[Struttura dati (Informatica teorica)]]'
parent note: null
tags:
  - algoritmi-ordinamento
  - alberi-binari
  - struttura-dati
---
# Cos'è un albero in informatica?
In informatica, ==un **albero** è una [[Struttura dati (Informatica teorica)|struttura dati]] con un insieme di nodi connessi.== L'implementazione più diffusa di un generico albero è un **[[Grafo (Struttura dati)|grafo]] non orientato**, **connesso** e **aciclico** che si compone di [[Lista concatenata (informatica)|liste concatenate]], ovvero di oggetti (i nodi) che referenziano altri oggetti. 
* Un albero generico non ha un "nodo radice" (come nel caso degli [[Albero radicato (Struttura dati)|alberi radicati]]) o una direzione implicita. 
	* *Tutti i nodi saranno gerarchicamente uguali.*
## Da cos'è composto un albero?
Un albero si compone di due tipi di sottostrutture fondamentali:
- il **nodo**: contiene informazioni (sono distinti il *nodo padre* dal *nodo figlio*)
	- Si chiede che ogni nodo possa avere al massimo un unico arco entrante, mentre dai diversi nodi possono uscire diversi numeri di archi uscenti.
	- Si chiede che l'albero possegga un unico nodo privo di arco entrante (**radice**).
- l'**arco**: il collegamento gerarchico fra due nodi.
	- Ogni nodo che non presenta archi uscenti è detto **foglia** (*leaf node*) e in ogni albero finito, cioè con un numero finito di nodi, si trova almeno un nodo foglia. 

> [!warning] Un nodo può essere padre e figlio
> Un nodo può essere contemporaneamente padre (se ha archi uscenti) e figlio (se ha un arco entrante, ovvero se è diverso dalla radice) $\to$ Gerarchia di nodi

Solitamente ogni nodo porta con sé delle informazioni e molto spesso anche una chiave con cui è possibile identificarlo univocamente all'interno dell'albero. L'**altezza** o **profondità** dell'albero è il massimo delle lunghezze dei suoi **cammini massimali**, cammini che vanno dalla radice alle sue foglie.
## Tipi di albero
* [[Albero radicato (Struttura dati)]]: un albero con radice è una coppia $( T , r )$ dove $T$ è un albero e $r$ un suo vertice che viene detto radice. Un albero con radice è quindi un albero in cui viene evidenziato un vertice (la radice).
* [[Albero ordinato (Struttura dati)]]
- [[Albero di ricorsione (Struttura dati)]]
- **[[Albero binario]]**: Nodi con al massimo due figli (sinistro e destro).
	- **[[Albero binario di ricerca (ABR)]]**: Un tipo speciale di albero binario dove si mantiene una relazione d'ordine: i nodi nel sottoalbero sinistro sono minori o uguali alla chiave del nodo corrente, e quelli nel sottoalbero destro sono maggiori.
- **[[Albero Rosso-Nero]]**: Un tipo di Albero Binario di Ricerca auto-bilanciante che garantisce che le operazioni `INSERT`, `DELETE`, `SEARCH`, `MINIMUM`, `MAXIMUM`, `SUCCESSOR`, `PREDECESSOR` avvengano sempre in `O(log n)` nel caso peggiore. Mantiene il bilanciamento attraverso la colorazione dei nodi (rosso o nero) e operazioni di `LEFT-ROTATE` e `RIGHT-ROTATE`.
- **[[Min-Heap (Struttura dati)]]**: Una struttura dati basata su array che rappresenta un albero binario quasi completo, dove ogni nodo ha un valore minore o uguale a quello dei suoi figli (proprietà di heap). Il minimo elemento è sempre alla radice. 



