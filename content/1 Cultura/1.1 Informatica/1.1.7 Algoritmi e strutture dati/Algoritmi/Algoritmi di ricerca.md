---
last modified: 2025-07-16T21:06:00.000Z
related:
  - '[[Algoritmo (Informatica)]]'
tags:
  - algoritmi-ordinamento
  - intelligenza-artificiale
  - ricerca-algoritmica
---
Gli algoritmi di ricerca costituiscono il cuore di molte applicazioni in [[Intelligenza artificiale|intelligenza artificiale]], permettendo agli agenti di navigare e risolvere problemi in ambienti complessi. Un **agente risolutore di problemi** opera attraverso un ciclo in quattro fasi:

1. **Formulazione dell'obiettivo**: Si definiscono gli scopi dell'agente.
2. **Formulazione del problema**: L'agente crea un modello astratto del mondo, descrivendo gli stati possibili e le azioni per raggiungere l'obiettivo.
3. **Ricerca**: L'agente simula le azioni per generare una sequenza che porti all'obiettivo (la soluzione).
4. **Esecuzione**: L'agente compie le azioni trovate nella soluzione.

La **formulazione di un problema di ricerca** è essenziale e include i seguenti elementi:

- Un **insieme di stati possibili** (lo spazio degli stati).
- Lo **stato iniziale** dell'agente.
- Un **insieme di stati obiettivo**.
- Un **insieme di azioni possibili** per l'agente in un dato stato.
- Un **modello di transizione** che definisce lo stato di arrivo per ogni coppia stato-azione.
- Una **funzione di costo** che assegna un valore numerico al costo di un'azione per passare da uno stato all'altro.

Un problema di ricerca può essere modellato come un **grafo** in cui i nodi sono gli stati e gli archi le azioni. Per trovare una soluzione, un algoritmo di ricerca genera un **albero di ricerca** a partire dallo stato iniziale, esplorando le possibili ramificazioni delle azioni. Ogni nodo dell'albero di ricerca contiene: lo stato, il nodo padre, l'azione che lo ha generato e il costo del cammino dallo stato iniziale a quel nodo. La **frontiera** dell'albero (i nodi ancora da esplorare) viene gestita tramite diverse strutture dati, influenzando il tipo di ricerca: una **coda a priorità** per la ricerca best-first, una **coda** per la ricerca in ampiezza, e una **pila** per la ricerca in profondità.

### 1. Ricerca Best-First (Generalizzata)

La **ricerca Best-First** è una strategia generica in cui, ad ogni passo, si sceglie il nodo da espandere con il valore minimo rispetto a una **funzione di valutazione** $f(n)$. Se il nodo scelto è uno stato obiettivo, la soluzione viene ritornata; altrimenti, la sua frontiera viene espansa aggiungendo i figli all'albero. Lo pseudocodice di base è: `PROCEDURE Best-First-Search(problema, f)`

1. `S = lista della soluzione`
2. `Aggiungi problema.stato_iniziale a S`
3. `F = coda a priorità inizializzata con frontiera di S rispetto alla funzione f`
4. `T = tabella hash con chiave il nodo`
5. `T[s].costo = 0`
6. `While F non è vuota`
7. `s = Min-Extract(F)`
8. `aggiungi s a S`
9. `if (s.obiettivo) return S`
10. `for (s,v) in problema.E`
11. `if(T[v] != NIL)`
12. `if T[v].costo > f((s,v)) T[v].costo = f((s,v)); Decrese-Key(F, v, f(u,v))`
13. `else Insert(F,v); T[v].costo = f((s,v))`

### 2. Algoritmi di Ricerca Non Informata

Questi algoritmi non utilizzano conoscenze specifiche sul problema (euristiche) per guidare la ricerca, ma esplorano lo spazio degli stati in modo sistematico.

#### a. Ricerca in Ampiezza (Breadth-First Search - BFS)

La **BFS** è un algoritmo che esplora un grafo o un albero livello per livello. Dato un grafo $G=(V,E)$ e un vertice sorgente $s$, la BFS visita tutti i nodi raggiungibili da $s$. Utilizza un attributo `colore` per i nodi (Bianco: non visitato; Grigio: scoperto ma con archi uscenti non esplorati; Nero: completamente esplorato). La frontiera viene gestita con una **coda (FIFO)**. La BFS produce un "albero di visita" radicato in $s$ e, a differenza della DFS, può calcolare la **distanza minima** (in termini di numero di archi) da $s$ a ogni altro nodo $v$, memorizzata come `v.d`. Inoltre, memorizza il predecessore `v.π` per ricostruire il cammino.

**Pseudocodice di BFS con distanza e predecessori**: `PROCEDURE BFS(G,s)`

1. `For v in G.V: v.color = WHITE; v.d = ∞; v.π = NIL`
2. `s.color = GREY; s.d = 0`
3. `Q = Coda vuota`
4. `ENQUEUE(Q,s)`
5. `While not Q.isEmpty()`
6. `u = DEQUEUE(Q)`
7. `for v in G.Adj[u]`
8. `if(v.color == WHITE): v.color = GREY; v.d = u.d + 1; v.π = u; ENQUEUE(Q,v)`
9. `u.color = BLACK`

La **complessità temporale** della BFS è $O(V+E)$, dove $V$ è il numero di vertici ed $E$ il numero di archi, poiché ogni vertice ed ogni arco vengono esaminati al più una volta. La BFS è ottimale per trovare cammini minimi su grafi non pesati.

#### b. Ricerca a Costo Uniforme (Uniform-Cost Search)

Quando le azioni (archi) nel grafo degli stati hanno **costi diversi** ma non si hanno informazioni per stimare il costo rimanente, la ricerca Best-First diventa la **Ricerca a Costo Uniforme**. Questo algoritmo è una generalizzazione della BFS che considera i pesi degli archi. Utilizza una coda a priorità che ordina i nodi in base al costo totale del cammino $g(n)$ dallo stato iniziale al nodo corrente. Questa strategia è equivalente all'algoritmo di Dijkstra, garantendo di trovare il cammino di costo minimo.

### 3. Algoritmi di Ricerca Informata (Heuristic Search)

Questi algoritmi utilizzano una **funzione euristica $h(n)$** per stimare il costo per raggiungere l'obiettivo da un dato nodo $n$, guidando la ricerca in modo più efficiente.

#### a. Ricerca Best-First Greedy

In questo approccio, la funzione di valutazione $f(n)$ è semplicemente l'euristica $h(n)$. L'algoritmo cerca di espandere sempre il nodo che sembra più vicino all'obiettivo. Sebbene possa trovare una soluzione rapidamente, non garantisce che la soluzione trovata sia quella ottima. Un esempio pratico è l'uso della distanza in linea d'aria tra due località per stimare il percorso più breve.

#### b. Algoritmo A* (A-star)

L'algoritmo **A*** è uno degli algoritmi di ricerca informata più popolari e potenti. La sua funzione di valutazione è definita come $f(n) = g(n) + h(n)$, dove:

- $g(n)$ è il costo esatto del cammino dallo stato iniziale al nodo $n$.
- $h(n)$ è la stima (euristica) del costo del cammino dal nodo $n$ allo stato obiettivo.

L'ottimalità dell'algoritmo A* è garantita se l'euristica $h(n)$ è **ammissibile**, ovvero se non sovrastima mai il costo reale per raggiungere un obiettivo ($h(n) \le h^*(n)$, dove $h^*(n)$ è il costo reale). Una proprietà più forte, la **consistenza**, implica l'ammissibilità: un'euristica è consistente se la stima da un nodo $n$ non è mai maggiore del costo per raggiungere un nodo adiacente $n'$ più la stima da $n'$ ($h(n) \le \text{costo}(n, n') + h(n')$). La consistenza assicura che il primo percorso trovato per un nodo è anche il percorso ottimale per quel nodo.

La **complessità temporale e spaziale** di A* è $O(b^d)$, dove $b$ è il fattore di ramificazione medio e $d$ la profondità della soluzione, rendendolo potenzialmente dispendioso per problemi molto grandi. Tuttavia, A* applica una **potatura** efficiente, espandendo solo i nodi con $f(n) < C^_$ (dove $C^_$ è il costo del cammino ottimo) e potendo espandere alcuni nodi con $f(n) = C^_$, ma mai nodi con $f(n) > C^_$.

Per affrontare i limiti di memoria e tempo, si possono accettare **soluzioni sub-ottime** utilizzando **euristiche inammissibili**, che possono sovrastimare il costo ma sono più accurate nella pratica e riducono significativamente il numero di nodi espansi. Un esempio è l'__A_ pesata_*, dove $f(n) = g(n) + W \cdot h(n)$ con $W > 1$. Sebbene non garantisca la soluzione ottimale, la soluzione trovata è solitamente vicina all'ottimo ($C^* \le \text{soluzione} \le W \cdot C^_$). L'A_ pesata generalizza vari algoritmi di ricerca:

- A* standard: $W=1$
- Best-First Greedy: $W=\infty$
- Costo Uniforme: $W=0$

#### c. Progettazione di Euristiche

La qualità dell'euristica è cruciale per le prestazioni di A*. Alcune tecniche per la loro progettazione includono:

- **Rilassamento del problema**: Si crea una versione del problema con meno vincoli, il cui costo ottimo è un'euristica ammissibile per il problema originale. Ad esempio, per il problema degli **8 tasselli** (un rompicapo scorrevole dove l'obiettivo è ordinare i tasselli in una griglia), rilassando i vincoli di movimento si ottengono euristiche come la **distanza Manhattan** (somma delle distanze orizzontali e verticali di ogni tassello dalla sua posizione obiettivo) o il **numero di tasselli fuori posto**. L'euristica Manhattan domina le altre, risultando più performante.
- **Database Pattern**: Si precalcola il costo esatto per risolvere sotto-problemi più semplici e si usa questo costo come euristica per il problema completo. Ad esempio, nel problema degli 8 tasselli, si possono creare database per pattern di 4 tasselli.
- **Uso di Punti di Riferimento (Landmark)**: Si selezionano punti specifici e si precalcolano i percorsi ottimi verso di essi. L'euristica è definita come la distanza dal nodo al landmark più la distanza precalcolata dal landmark all'obiettivo. Questa euristica è spesso inammissibile ma efficiente.
- **Apprendimento tramite esperienza**: Le euristiche possono essere apprese risolvendo più volte il problema e utilizzando i costi delle soluzioni trovate per migliorare le stime future.

### 4. Algoritmi di Ricerca Locale

A differenza degli algoritmi di ricerca classici che cercano l'intero percorso dalla radice all'obiettivo, la **ricerca locale** si concentra sulla ricerca della soluzione finale, esplorando solo gli stati adiacenti senza tenere traccia di quelli già visitati. Questo comporta un minore utilizzo di memoria, rendendoli adatti per spazi di stati molto ampi. Il problema viene spesso visualizzato come un "panorama degli stati", dove l'asse X rappresenta gli stati e l'asse Y il valore di una funzione di valutazione da massimizzare o minimizzare.

#### a. Hill Climbing

È una ricerca locale "greedy" che, ad ogni iterazione, sceglie lo stato adiacente che produce il maggiore miglioramento della funzione di valutazione. **Problemi**:

- **Massimi locali**: L'algoritmo può bloccarsi su un massimo locale senza raggiungere il massimo globale.
- **Creste**: Sequenze di massimi locali non collegati, che possono far muovere l'algoritmo in discesa.
- **Plateau**: Aree con valori di funzione simili, dove l'algoritmo può bloccarsi. **Varianti per mitigare i problemi**:
- **Passo laterale**: Consente spostamenti su stati con lo stesso valore, per uscire dai plateau non massimi locali.
- **Hill Climbing stocastico**: Sceglie casualmente tra gli stati che migliorano quello attuale, per evitare massimi locali.
- **Riavvio casuale**: Esegue più ricerche Hill Climbing da stati iniziali casuali diversi, scegliendo la migliore soluzione.

#### b. Simulated Annealing

Combina Hill Climbing con la capacità di sfuggire ai massimi locali, ispirandosi al processo di ricottura dei metalli. L'algoritmo sceglie una mossa casuale: se è migliorativa, la accetta; se non lo è, l'accetta con una probabilità che diminuisce all'aumentare del peggioramento e con il passare delle iterazioni (la "temperatura" decresce). Inizialmente esplora liberamente, diventando più stabile col tempo.

#### c. Ricerca Locale Beam (Beam Search)

Estende la memoria a $k$ stati invece di uno solo. Ad ogni iterazione, vengono generati i successori di tutti i $k$ stati e vengono scelti i $k$ più promettenti tra tutti. Il problema è la potenziale **poca diversificazione** dei $k$ stati, che potrebbero concentrarsi in regioni di massimo locale. La **ricerca locale beam stocastica** risolve questo problema scegliendo i successori con una probabilità proporzionale al loro valore, promuovendo una maggiore esplorazione dello spazio degli stati.

#### d. Algoritmi Genetici

Si ispirano alla teoria della selezione naturale. Partendo da una popolazione di "individui" (stati), ad ogni "epoca" viene prodotta una "prole" e selezionati gli individui con il potenziale più alto. Elementi chiave includono: dimensione della popolazione, rappresentazione degli individui (es. stringa tipo DNA), numero di genitori, **funzione di fitness** (stima la bontà di uno stato), **crossover** (ricombinazione di metà di due genitori per creare figli) e **mutazione** (introduzione casuale di cambiamenti per diversificazione).

### 5. Algoritmi di Ricerca nei Giochi (Multi-Agente)

In ambienti con **agenti multipli** e competitivi, i problemi possono essere risolti attraverso **alberi di gioco**. Un **gioco** è definito da uno stato iniziale, una funzione che indica quale giocatore deve muovere, le azioni possibili in ogni stato, una funzione di transizione (risultato), una condizione di terminale e una funzione di utilità per ogni giocatore nello stato terminale. I giochi possono essere a **somma zero** (il vantaggio di un agente è il danno degli altri) e a **informazione perfetta** (ogni agente conosce tutti gli elementi del gioco) o **informazione parziale/nascosta**.

#### a. Algoritmo Minimax

L'algoritmo **Minimax** è usato per giochi a due giocatori a somma zero e informazione perfetta. Il **Giocatore 1 (MAX)** cerca di massimizzare il proprio punteggio, mentre il **Giocatore 2 (MIN)** cerca di minimizzare quello di MAX (ovvero massimizzare il proprio, che è l'opposto). L'algoritmo esplora ricorsivamente l'albero di gioco fino alle foglie (stati terminali) e propaga i valori di utilità verso l'alto, scegliendo il valore massimo per i nodi MAX e il valore minimo per i nodi MIN. La complessità di Minimax è esponenziale, $O(b^m)$, dove $b$ è il fattore di ramificazione (numero di mosse legali) e $m$ la profondità massima di ricerca. Per giochi complessi come gli scacchi, con un fattore di ramificazione di circa 35 e una profondità di 80, l'esplorazione completa è impraticabile ($10^{120}$ nodi).

#### b. Potatura Alfa-Beta (Alpha-Beta Pruning)

È una tecnica di ottimizzazione del Minimax che riduce drasticamente il numero di nodi esplorati nell'albero di gioco, senza alterare il risultato finale. Il principio è che se un nodo MIN (o MAX) trova un valore che è già peggiore di un'opzione precedentemente trovata al suo stesso livello o a un livello superiore, il resto del sottoalbero di quel nodo non verrà mai scelto e può essere "potato" (tagliato). Vengono usati due parametri, $\alpha$ (valore minimo garantito per MAX) e $\beta$ (valore massimo garantito per MIN). Nella migliore delle ipotesi (nodi ben ordinati), la complessità può ridursi a $O(b^{m/2})$.

#### c. Strategie di Ottimizzazione e Funzioni Euristiche nei Giochi

Per mitigare la complessità, si usano strategie euristiche:

- **Strategia A (Shannon)**: Limita la profondità di ricerca e usa un'euristica per valutare l'utilità nei nodi tagliati.
- **Strategia B**: Usa euristiche per scartare mosse meno promettenti e esplorare più in profondità quelle migliori (potatura in avanti).

Una **funzione euristica `Eval(s,p)`** in un gioco deve stimare il valore di utilità atteso di uno stato $s$ per un giocatore $p$, essendo compresa tra sconfitta e vittoria e correlata alle probabilità reali di vincere. Spesso si usa una **funzione lineare pesata**, assegnando un peso a diverse caratteristiche dello stato e sommando i loro valori. Problemi come la **quiescenza** (una situazione con una mossa pendente che provoca una grossa variazione di punteggio, es. una cattura imminente negli scacchi) e l'**effetto orizzontale** (una mossa vincente nascosta oltre il punto di taglio) possono ingannare le euristiche, e richiedono tecniche di mitigazione (valutare la quiescenza o estendere la ricerca oltre il taglio). La **potatura in avanti** (forward pruning) è una forma più aggressiva di potatura, che elimina a priori mosse considerate "cattive", introducendo un grado di errore. Un esempio è la **ricerca beam** che considera solo le $n$ mosse più promettenti.

#### d. Tecniche Specifiche per Scacchi e Go

- **Scacchi**: Si usano tabelle pre-calcolate per le **aperture** e le **chiusure**.
- **Go**: Presenta una complessità molto maggiore rispetto agli scacchi, con un fattore di ramificazione di 361 e difficoltà nel definire una funzione di valutazione chiara a causa della fluidità del gioco. Per questo, Minimax con potatura non è praticabile, e si preferisce la **Ricerca ad Albero Monte Carlo (MCTS)**.

**Monte Carlo Tree Search (MCTS)**: Si basa su **simulazioni (playout)** di partite complete a partire da un dato stato. Le mosse nella simulazione possono essere casuali o guidate da **politiche di simulazione** (e.g., euristiche specifiche del gioco o apprendimento con reti neurali). L'MCTS bilancia l'**esplorazione** di stati poco visitati e lo **sfruttamento** di quelli con buoni risultati. Il processo si compone di quattro fasi cicliche:

1. **Selezione**: Scelta delle mosse nell'albero parziale esistente.
2. **Espansione**: Aggiunta di un nuovo nodo figlio alla foglia raggiunta.
3. **Simulazione**: Esecuzione di un playout completo a partire dal nuovo nodo.
4. **Retropropagazione**: Il risultato della simulazione viene propagato indietro a tutti i nodi lungo il percorso nell'albero. Una politica di selezione comune è **UCT (Upper Confidence Bounds Applied to Tree)**, che classifica le mosse in base all'utilità delle simulazioni passate e un termine di esplorazione che favorisce i nodi meno visitati. L'MCTS è molto efficiente per giochi complessi e situazioni in cui le funzioni di valutazione sono difficili da definire.

### 6. Giochi Stocastici

I **giochi stocastici** introducono un fattore probabilistico (es. lancio di dadi nel Backgammon). L'albero di gioco, oltre ai livelli MAX e MIN, include **nodi di casualità** che rappresentano i possibili risultati casuali.

#### a. Expectiminimax

Estende Minimax per gestire la casualità. Nei nodi di casualità, il valore atteso è calcolato come la somma dei valori dei risultati possibili, pesati per la loro probabilità. La complessità temporale di Expectiminimax può aumentare a $O(b^m n^m)$, dove $n$ è il numero di tiri di dado, rendendola proibitiva per giochi complessi come il Backgammon, che richiedono un taglio della ricerca a pochi livelli e l'uso di funzioni euristiche basate sulla probabilità di vincere. Per giochi altamente stocastici come lo Yahtzee, il metodo Monte Carlo è più adatto.

#### b. Giochi ad Informazione Parziale

In questi giochi, parte delle informazioni non è accessibile agli agenti. Possono essere:

- **Deterministici**: L'informazione nascosta dipende da scelte iniziali (es. Battaglia Navale).
- **Stocastici**: L'informazione nascosta dipende da una distribuzione casuale (es. Poker o Bridge). Per risolvere giochi a informazione parziale, si può trattare ogni informazione nascosta come una possibilità e applicare concetti come l'equilibrio di Nash. Oppure, si può modellare lo spazio degli stati attraverso **stati-credenza**, che sono l'insieme di tutti gli stati logicamente possibili data una sequenza percettiva passata. Un esempio è il **Kriegspiel**, una variante degli scacchi dove i giocatori non conoscono le mosse avversarie, ma solo le risposte di un arbitro.

### 7. Algoritmi di Ricerca di Cammini Minimi

Gli algoritmi di ricerca di cammini minimi trovano il percorso di peso minimo tra due nodi in un grafo pesato. Il peso di un cammino è la somma dei pesi degli archi che lo compongono.

#### a. Rilassamento

La tecnica di base è il **rilassamento**, che aggiorna progressivamente la stima `v.d` del peso del cammino minimo da una sorgente $s$ a un vertice $v$. Inizialmente, `v.d` è impostato a infinito. L'operazione `Relax(u,v,w)` verifica se un cammino attraverso l'arco $(u,v)$ offre un percorso migliore per $v$, e in tal caso aggiorna `v.d` e il predecessore `v.π`.

#### b. Algoritmo di Bellman-Ford

Risolve il problema dei cammini minimi da sorgente unica in grafi orientati pesati che possono contenere **archi con pesi negativi**. Se il grafo contiene cicli di peso negativo raggiungibili dalla sorgente, l'algoritmo rileva e segnala che una soluzione non esiste. L'algoritmo esegue $|V|-1$ iterazioni, rilassando tutti gli archi in ogni iterazione. La **complessità temporale** è $O(|V| \cdot |E|)$.

**Pseudocodice Bellman-Ford**: `PROCEDURE Bellman-Ford(G,w,s)`

1. `Initialize-Single-Source(G,s)`
2. `For i = 1 to |G.V| - 1`
3. `for (u,v) in G.E: Relax(u,v,w)`
4. `For (u,v) in G.E`
5. `if (v.d > u.d + w(u,v)): return FALSE`
6. `Return TRUE`

#### c. Algoritmo di Dijkstra

Generalizza la BFS per grafi pesati, ma richiede che **tutti i pesi degli archi siano non negativi**. È un algoritmo avido che, ad ogni passo, seleziona il nodo con la stima `v.d` minima tra quelli non ancora inclusi nel set di nodi visitati. Utilizza una **coda a min-priorità** (implementata tipicamente con un min-heap) per estrarre il vertice con la chiave minima. La **complessità temporale** di Dijkstra è $O(E \log V)$ o $O(V \log V + E)$ se implementata con un min-heap.

**Pseudocodice Dijkstra**: `PROCEDURE Dijkstra(G,w,s)`

1. `Initialize-Single-Source(G,s)`
2. `S = ∅`
3. `Q = Coda min-priorità`
4. `For v in G.V: Insert(Q,v)`
5. `While Q != ∅`
6. `u = Extract-Min(Q)`
7. `S = S ∪ {u}`
8. `for v in G.Adj[u]: Relax(u,v,w)`
9. `if Relax diminuisce v.d: Decrease-Key(Q,v,v.d)`

#### d. Cammini Minimi su Grafi Aciclici Orientati (DAG)

Se il grafo è un **DAG**, il problema dei cammini minimi da sorgente unica può essere risolto in tempo $O(V+E)$. L'approccio consiste nell'eseguire prima un **ordinamento topologico** del grafo (che ha complessità $O(V+E)$) e poi rilassare gli archi seguendo l'ordine topologico. Questo è più efficiente di Bellman-Ford e Dijkstra per i DAG, poiché non ci sono cicli da gestire.

**Pseudocodice DAG-Shortest-Path**: `PROCEDURE DAG-Shoretest-Path(G,w,s)`

1. `Ordinamento topologico di G`
2. `Initialize-Single-Source(G,s)`
3. `For u in ordinamento topologico`
4. `for v in G.Adj[u]: Relax(u,v,w)`

In sintesi, gli algoritmi di ricerca sono strumenti fondamentali per la risoluzione di problemi, con scelte algoritmiche che variano a seconda delle caratteristiche del problema (pesi sugli archi, presenza di cicli, informazione disponibile) e dell'ambiente (singolo o multi-agente, deterministico o stocastico, osservabile o parziale).