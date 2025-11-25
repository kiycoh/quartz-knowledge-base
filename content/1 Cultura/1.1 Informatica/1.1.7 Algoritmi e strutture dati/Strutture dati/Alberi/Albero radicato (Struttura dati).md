---
last modified: 27/10/2025 18:51
related:
  - '[[Albero (Struttura dati)]]'
tags:
  - algoritmi-ordinamento
  - strutture-dati
  - alberi-binari
---
# Definizione di albero radicato
In informatica, un albero albero radicato è una [[Struttura dati (Informatica teorica)|struttura dati]] concatenata che permette di organizzare i dati di un insieme dinamico secondo una **gerarchia di nodi**. C'è un solo nodo radice che non è figlio di nessun altro. I nodi collegati direttamente a un nodo padre sono i suoi "figli".
* Gli alberi binari sono un caso specifico CON AL MASSIMO DUE FIGLI PER NODO.
## Operazioni su alberi radicati
Le operazioni di **visita** (o _traversal_ in inglese) di un albero radicato sono algoritmi che permettono di **esplorare sistematicamente tutti i nodi dell'albero**, assicurandosi che ogni nodo venga "visitato" esattamente una volta.
### Operazioni di visita
Gli elementi possono essere visualizzati in-ordine (sinistra, radice, destra), pre-ordine (radice, sinistra, destra), post-ordine (sinistra, destra, radice), o per livello (non menzionato direttamente nelle definizioni ma implicito).
- **Visita in Ampiezza (BFS o per Livelli: Questa strategia esplora l'albero **livello per livello**, da sinistra a destra. Prima visita tutti i nodi al livello 0 (la radice), poi tutti quelli al livello 1, e così via.
- **Visita in ordine (Inorder)**: Visita il sottoalbero sinistro, poi la radice, poi il sottoalbero destro. **O(n)**.
- **Visita in preordine (Preorder)**: Visita la radice, poi il sottoalbero sinistro, poi il sottoalbero destro. **O(n)**.
- **Visita in postordine (Postorder)**: Visita il sottoalbero sinistro, poi il sottoalbero destro, poi la radice. **O(n)**.
- **Visita per livelli (Level-Order)**: Visita i nodi di ogni livello prima di passare al successivo, utilizzando una coda ausiliaria. **O(n)**.
### Operazioni generiche
-  `INSERT(T, x, y, scelta)`: Inserisce un nodo `y` come figlio di `x`. **O(1)** se si conosce il nodo padre e la scelta del figlio.
- `DELETE(T, z)`: Eliminare un nodo `z` è complesso e dipende dal numero di figli di `z`. Possono esserci 3 casi: `z` senza figli, `z` con un figlio, `z` con due figli. La complessità dipende dalla ricerca del successore nel caso di due figli.
- `SEARCH(T, k)`: Nella forma generica (visita per livelli) è **O(n)**.
## Tipi di alberi radicati
* [[Albero binario (Struttura dati)]]: ogni nodo ha al massimo due figli (sinistro e destro).
	* **[[Albero binario di ricerca (Struttura dati)]]** 
	- **[[Albero rosso-nero (Struttura dati)]]**
* [[Albero bilanciato]]: tutti i nodi hanno esattamente `n` figli.
* [[Albero degenere]]: tutti i nodi hanno un solo figlio, risultando in una lista concatenata.