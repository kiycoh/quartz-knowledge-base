---
last modified: 27/10/2025 18:51
related: null
tags:
  - algoritmi-ordinamento
  - algoritmi-greedy
  - apprendimento-automatico
---
Un **algoritmo di visita** è un concetto fondamentale nell'ambito dei **[[Grafo (Struttura dati)|grafi]]** e delle **[[Struttura dati (Informatica teorica)|strutture dati]]**, e rappresentano le tecniche principali per esplorare sistematicamente tutti i nodi e gli archi di un grafo. Il loro scopo è garantire che ogni parte connessa del grafo venga esaminata, permettendo di raccogliere informazioni sulla sua struttura, individuare cammini, o risolvere problemi specifici.

Un **grafo G** è definito come una coppia ordinata `(V, E)` dove `V` è l'insieme dei **nodi (o vertici)** e `E` è l'insieme degli **archi (o spigoli)**, che sono coppie di nodi in `V` che li collegano. I grafi possono essere **orientati** (se gli archi hanno una direzione, come in una strada a senso unico) o **non orientati** (se gli archi non hanno direzione, come in una strada a doppio senso). Possono anche essere **pesati**, se a ogni arco è associato un valore numerico (peso).

Le visite dei grafi sono algoritmi chiave per risolvere una moltitudine di problemi, come trovare il cammino più breve tra due punti in una rete (ad esempio, un navigatore GPS), determinare l'ordine delle attività in un progetto, o identificare comunità all'interno di una rete sociale.

Esistono due algoritmi principali di visita dei grafi:

1. **Ricerca in Ampiezza (Breadth-First Search - BFS)**
2. **Ricerca in Profondità (Depth-First Search - DFS)**

Analizziamoli in dettaglio.

---

### 1. Ricerca in Ampiezza (Breadth-First Search - BFS)

La **Ricerca in Ampiezza (BFS)** è uno degli algoritmi di ricerca sui grafi più semplici e costituisce la base per algoritmi più complessi.

**Meccanismo Operativo e Strutture Ausiliarie:** Dato un grafo `G = (V, E)` e un vertice sorgente `s ∈ V`, la BFS esplora tutti i nodi raggiungibili da `s` per "strati" concentrici. Ciò significa che visita tutti i nodi adiacenti a `s` (livello 1), poi tutti i nodi adiacenti a questi (livello 2) che non sono stati ancora visitati, e così via, prima di passare ai collegamenti successivi.

Per gestire l'esplorazione, la BFS utilizza una **coda (queue)** come struttura dati ausiliaria. I nodi vengono inseriti in coda quando vengono scoperti e rimossi quando sono pronti per essere esplorati (cioè, quando i loro vicini devono essere visitati).

**Attributi dei Nodi e Loro Scopo:** Durante la visita, a ogni nodo vengono associati specifici attributi per tenere traccia dello stato e del percorso:

- `colore`: Indica lo stato di visita del nodo.
    - **BIANCO**: Il nodo non è stato ancora visitato.
    - **GRIGIO**: Il nodo è stato scoperto (inserito in coda) ma non tutti i suoi archi uscenti sono stati esplorati (o, in generale, i suoi vicini non sono ancora stati completamente elaborati).
    - **NERO**: Il nodo è stato completamente visitato (tutti i suoi archi uscenti sono stati esplorati).
- `d`: Rappresenta la distanza del nodo dalla sorgente `s` in termini di numero minimo di archi. Inizialmente tutti i nodi hanno `d = ∞`, tranne la sorgente `s` che ha `s.d = 0`.
- `π`: Indica il predecessore del nodo nell'albero di visita in ampiezza. Questo attributo permette di ricostruire il **cammino minimo** dalla sorgente a qualsiasi nodo.

**Pseudocodice della BFS (con distanza e predecessore):**

```
PROCEDURE BFS(G, s)
1.  For v in G.V
2.      v.color = WHITE
3.      v.d = ∞
4.      v.π = NIL
5.  s.color = GREY
6.  s.d = 0
7.  Q = Coda vuota
8.  ENQUEUE(Q, s)
9.  While not Q.isEmpty()
10.     u = DEQUEUE(Q)
11.     for v in G.Adj[u] // Per ogni vicino v di u
12.         if (v.color == WHITE)
13.             v.color = GREY
14.             v.d = u.d + 1
15.             v.π = u
16.             ENQUEUE(Q, v)
17.     u.color = BLACK
```

**Complessità Asintotica:** L'algoritmo BFS ha una complessità temporale di `O(|V| + |E|)`, dove `|V|` è il numero di vertici e `|E|` è il numero di archi del grafo. Questa efficienza deriva dal fatto che ogni vertice viene inserito ed estratto dalla coda al più una volta, e ogni arco viene esaminato al più due volte (una per ogni direzione in un grafo non orientato, una sola in un grafo orientato).

**Proprietà e Teoremi Chiave:**

- **Cammini Minimi**: La BFS calcola i cammini minimi (in termini di numero di archi) da una sorgente `s` a tutti gli altri vertici raggiungibili nel grafo. Questo è un risultato cruciale, poiché `v.d` alla fine dell'esecuzione sarà esattamente `δ(s, v)` (il peso del cammino minimo da `s` a `v`).
- **Albero di Visita**: L'insieme degli archi `(v.π, v)` per ogni `v ≠ s` forma un **albero di visita in ampiezza** (o foresta se il grafo non è connesso) radicato in `s`, che contiene i cammini minimi dalla sorgente a ogni nodo.
- **Ricostruzione del Cammino**: Utilizzando l'attributo `v.π` è possibile stampare il cammino minimo da `s` a `v` ricorsivamente.

**Esempio Pratico: Problema delle 8 Tessere:** Il problema delle 8 tessere può essere modellato come un problema di ricerca su grafo. Lo stato iniziale è una configurazione casuale di 8 tessere, e l'obiettivo è riordinarle in modo crescente con la tessera vuota alla fine. Le transizioni sono gli spostamenti di una tessera adiacente alla tessera vuota. La ricerca a costo uniforme, che è un'applicazione della BFS quando tutti i costi degli archi sono uguali, può risolvere questo problema trovando la sequenza di mosse (cammino) che porta all'obiettivo, minimizzando il numero di mosse.

---

### 2. Ricerca in Profondità (Depth-First Search - DFS)

La **Ricerca in Profondità (DFS)** esplora un grafo navigando il più a fondo possibile lungo ogni ramo prima di tornare indietro (backtracking).

**Meccanismo Operativo e Strutture Ausiliarie:** La DFS procede selezionando un nodo e esplorando uno dei suoi vicini, poi un vicino di quel vicino, e così via, fino a quando non può più proseguire (raggiungendo una "foglia" dell'esplorazione o un nodo già visitato). A quel punto, torna indietro (backtrack) per esplorare altri rami non ancora visitati.

A differenza della BFS, la DFS non necessita di una struttura dati esplicita come una coda; la sua natura ricorsiva sfrutta implicitamente la **pila di chiamate (call stack)** del sistema.

**Attributi dei Nodi e Loro Scopo:** Anche la DFS utilizza attributi per tracciare lo stato e i tempi di visita:

- `colore`: Simile alla BFS, ma con un significato leggermente diverso per GRIGIO.
    - **BIANCO**: Nodo non ancora scoperto.
    - **GRIGIO**: Nodo scoperto, ma l'esplorazione di tutti i suoi archi uscenti non è ancora stata completata (cioè, il nodo è nel percorso di ricorsione corrente).
    - **NERO**: Nodo completamente visitato e l'esplorazione da esso è terminata.
- `d`: **Tempo di scoperta (discovery time)**. Registra l'istante (usando una variabile globale `time`) in cui il nodo passa da BIANCO a GRIGIO.
- `f`: **Tempo di completamento (finish time)**. Registra l'istante in cui il nodo passa da GRIGIO a NERO.
- `π`: Predessore del nodo nella foresta di visita. La DFS non produce un singolo albero, ma una **foresta di alberi** che riflettono le chiamate ricorsive di `DFS-VISIT`.

**Pseudocodice della DFS:**

```
PROCEDURE DFS(G)
1.  For v in G.V
2.      v.color = WHITE
3.      v.π = NIL
4.  time = 0 // Variabile globale
5.  For v in G.V // Per ogni vertice nel grafo
6.      if (v.color == WHITE)
7.          DFS-VISIT(G, v)

PROCEDURE DFS-VISIT(G, u)
1.  time = time + 1
2.  u.d = time
3.  u.color = GRAY
4.  For v in G.Adj[u] // Per ogni vicino v di u
5.      if (v.color == WHITE)
6.          v.π = u
7.          DFS-VISIT(G, v)
8.  time = time + 1
9.  u.f = time
10. u.color = BLACK
```

**Complessità Asintotica:** La complessità temporale della DFS è `O(|V| + |E|)` [236 (per Transpose, parte di algoritmo SCC che include DFS), 207 (per BFS che ha stessa logica)]. Ogni vertice viene visitato e ogni arco esaminato un numero costante di volte.

**Proprietà e Teoremi Chiave:**

- **Struttura a Parentesi**: I tempi di scoperta (`d`) e completamento (`f`) di ogni nodo formano una struttura a parentesi, indicando relazioni di discendenza. Un nodo `v` è discendente di `u` nella foresta di visita se e solo se l'intervallo `[v.d, v.f]` è completamente contenuto in `[u.d, u.f]`.
- **Classificazione degli Archi**: La DFS può classificare gli archi in base al colore del nodo `v` quando si attraversa l'arco `(u, v)`:
    - **Archi d'Albero**: `v` è BIANCO (viene scoperto).
    - **Archi all'Indietro (Back Edges)**: `v` è GRIGIO (connette `u` a un suo antenato nel DFS tree). La presenza di archi all'indietro indica un **ciclo** nel grafo orientato.
    - **Archi in Avanti (Forward Edges)**: `v` è NERO e `u.d < v.d` (connette `u` a un suo discendente non diretto).
    - **Archi Trasversali (Cross Edges)**: `v` è NERO e `u.d > v.d` (connette nodi tra alberi di visita diversi o rami diversi dello stesso albero).
- **Grafi Aciclici Diretti (DAG)**: Un grafo orientato `G` è aciclico se e solo se una DFS su `G` non produce archi all'indietro.
- **Ordinamento Topologico**: Per un DAG, la DFS può produrre un ordinamento topologico dei nodi. Questo ordinamento posiziona i nodi lungo una linea retta in modo che tutti gli archi orientati vadano da sinistra a destra. Si ottiene inserendo i nodi completati (`u.f`) in cima a una lista in ordine decrescente dei tempi di completamento.
- **Componenti Fortemente Connesse (Strongly Connected Components - SCC)**: Per un grafo orientato `G`, una SCC è un sottoinsieme massimale di vertici in cui ogni coppia di vertici è mutuamente raggiungibile. Un algoritmo per calcolarle utilizza due esecuzioni di DFS: una su `G` per calcolare i tempi di completamento, e una seconda sul **grafo trasposto `Gᵀ`** (dove tutti gli archi sono invertiti), visitando i nodi in ordine decrescente dei loro tempi di completamento `f` ottenuti dalla prima DFS.

**Esempio Pratico: Pianificazione di Progetti:** Un esempio pratico di applicazione della DFS e dell'ordinamento topologico è la pianificazione di progetti. Le attività sono nodi e le dipendenze tra attività sono archi. Un ordinamento topologico fornisce una sequenza valida per eseguire le attività, garantendo che i prerequisiti siano soddisfatti.

In sintesi, gli algoritmi di visita su grafi, BFS e DFS, sono strumenti algoritmici essenziali con applicazioni trasversali in informatica e ingegneria, dalle reti al machine learning. La loro scelta dipende dalle proprietà specifiche del grafo e dal problema che si intende risolvere.