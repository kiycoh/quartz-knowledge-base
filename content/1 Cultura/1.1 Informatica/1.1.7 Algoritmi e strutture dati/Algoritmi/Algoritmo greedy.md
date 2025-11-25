---
last modified: 24/10/2025 02:54
related: null
tags:
  - algoritmi-greedy
  - programmazione-dinamica
  - ottimizzazione-algoritmica
---
# Definizione di algoritmo greedy
==Gli **algoritmi greedy** sono una metodologia di progettazione algoritmica che, per risolvere un problema di ottimizzazione, ad ogni passo fa la scelta che sembra localmente ottima in quel determinato momento, con la speranza che questa conduca a una soluzione globalmente ottima.== 

> [!NOTE] DP *vs* Greedy
> A differenza della [[Programmazione dinamica|programmazione dinamica (DP)]], che valuta e memorizza le soluzioni di tutti i sotto-problemi per costruire una soluzione ottimale complessiva, *un algoritmo greedy si concentra solo sulla scelta più vantaggiosa nell'istante attuale.*
> 
> Questa strategia di **"scelta localmente ottima"** non garantisce sempre la soluzione globale ottima per tutti i problemi. Tuttavia, per alcuni problemi, l'approccio greedy è sorprendentemente efficace e porta a risultati ottimali con notevole efficienza. In altri contesti, anche quando non produce la soluzione globalmente ottimale, può comunque servire come un'euristica efficace per problemi computazionalmente complessi.
### Quando gli Algoritmi Greedy Funzionano: Il Problema di Selezione Attività
Un classico esempio in cui un algoritmo greedy fornisce la soluzione ottima è il **Problema di Selezione Attività (Activity Selection Problem)**.

**Problema:** Dato un insieme di $n$ attività, ognuna con un tempo di inizio e un tempo di fine, che devono utilizzare la stessa risorsa, si vuole trovare il più grande sottoinsieme di attività mutualmente compatibili (ovvero, che non si sovrappongono).

**Approccio con Programmazione Dinamica:** Un approccio con Programmazione Dinamica per questo problema definirebbe $c(i, j)$ come il numero ottimo di attività incluse in un intervallo. La relazione ricorsiva $c(i, j) = \max {c(i, k) + c(k, j) + 1}$ (dove $a_k$ è una delle attività incluse nell'insieme) richiederebbe di considerare tutte le possibilità, portando a una complessità temporale di $\Theta(n^3)$ per riempire una matrice $n \times n$.

**Approccio Greedy Ottimale:** È possibile fare molto meglio con un algoritmo greedy. La strategia avida consiste nel seguire questi passi:

1. Ordinare le attività in base al loro tempo di fine crescente.
2. Selezionare la prima attività (quella che termina prima).
3. Successivamente, selezionare l'attività compatibile successiva che inizia dopo la fine dell'ultima attività selezionata.

**Esempio Pratico:** Consideriamo l'esempio fornito:

|Attività (i)|Inizio|Fine|
|---|---|---|
|1|0|3|
|2|1|4|
|3|2|5|
|4|5|7|
|5|3|9|
|6|5|9|
|7|7|10|

Le attività sono già ordinate per tempo di fine.

- **Passo 1:** Si seleziona l'attività 1 ($a_1$). $S = {a_1}$.
- **Passo 2:** Si cerca la prossima attività che inizia dopo la fine di $a_1$ (fine: 3). L'attività 4 ($a_4$) inizia a 5. $S = {a_1, a_4}$.
- **Passo 3:** Si cerca la prossima attività che inizia dopo la fine di $a_4$ (fine: 7). L'attività 7 ($a_7$) inizia a 7. $S = {a_1, a_4, a_7}$.

La soluzione ottenuta è $S = {a_1, a_4, a_7}$. La correttezza di questo approccio è dimostrata da un teorema che afferma che l'attività con il tempo di fine minore appartiene sempre a un sottoinsieme massimale di attività mutualmente compatibili. La dimostrazione procede per assurdo, sostituendo l'attività con fine minore di un insieme massimale con quella scelta dall'algoritmo greedy e mostrando che le cardinalità e compatibilità vengono mantenute, implicando che sono lo stesso insieme.

La complessità di questo algoritmo è $O(n)$ dopo l'ordinamento iniziale, che se fatto con MergeSort o QuickSort è $O(n \lg n)$.

### Quando gli Algoritmi Greedy Falliscono: Il Problema dello Zaino

Non tutti i problemi di ottimizzazione possono essere risolti in modo ottimale con un approccio greedy. Un esempio emblematico è il **Problema dello Zaino (Knapsack Problem)**.

**Problema:** Si ha uno zaino con una certa capacità massima $n$ e una serie di oggetti, ognuno con un volume $V$ e un valore $G$. L'obiettivo è selezionare un sottoinsieme di oggetti da mettere nello zaino in modo da massimizzare il valore totale, senza superare la capacità.

**Esempio Pratico:** Zaino con capacità $n=15$.

|Oggetto (i)|Volume|Valore|
|---|---|---|
|1|2|10|
|2|3|5|
|3|5|15|
|4|7|7|

**Tentativo Greedy (Massimizzare il Valore):**

1. Si ordina per valore decrescente: Oggetto 3 (15), Oggetto 1 (10), Oggetto 4 (7), Oggetto 2 (5).
2. **Passo 1:** Si prende l'Oggetto 3 (Volume: 5, Valore: 15). Capacità rimanente: 10. $S = {O_3}$.
3. **Passo 2:** Si prende l'Oggetto 1 (Volume: 2, Valore: 10). Capacità rimanente: 8. $S = {O_3, O_1}$.
4. **Passo 3:** Si prende l'Oggetto 4 (Volume: 7, Valore: 7). Capacità rimanente: 1. $S = {O_3, O_1, O_4}$. Valore totale: $15 + 10 + 7 = 32$. Volume occupato: $5 + 2 + 7 = 14$. Questa soluzione **non è ottima**. La soluzione $S = {O_2, O_3, O_4}$ (valore $5+15+7=27$, volume $3+5+7=15$) non è migliore. Ma la soluzione ${O_1, O_3, O_4}$ ha valore 32. La fonte indica come soluzione ottima S = {O2, O3, O4} con valore 27, ma questo sembra un errore nella trascrizione dell'esempio. Un esempio migliore potrebbe essere ${O_1, O_2, O_3}$ che vale $10+5+15 = 30$ con volume $2+3+5 = 10$. La soluzione ${O_1, O_2, O_3, O_4}$ non è possibile. Se la capacità è 15, la combinazione ${O_1, O_3}$ dà $10+15=25$ con volume $2+5=7$. Se aggiungiamo $O_4$, valore $25+7=32$, volume $7+7=14$. Questa è la soluzione data. Ah, la fonte dice: "NO! S = {O2, O*, O+} ottiene lo stesso guadagno utilizzando tutto", il che implica che $O_2, O_3, O_4$ è $5+15+7 = 27$ ma con volume 15. Dunque, l'algoritmo greedy scelto per valore non è ottimo perché non utilizza la capacità al massimo. Un'altra combinazione come ${O_1, O_2, O_3, O_4}$ è $10+5+15+7 = 37$ con volume $2+3+5+7 = 17$, che supera la capacità. La soluzione ottimale per la capacità 15 in questo esempio è ${O_1, O_3, O_4}$ con valore 32 e volume 14. L'algoritmo greedy basato su valore trova questa soluzione. La fonte dice "NO!" per la soluzione ${O_1, O_3, O_4}$ che dà 32, e poi propone "$S = {O_2, O_3, O_4}$ ottiene lo stesso guadagno utilizzando tutto". Questo è logicamente incoerente dato che $O_2$ ha valore 5, $O_3$ ha valore 15, $O_4$ ha valore 7, per un totale di $5+15+7=27$. Il riferimento sembra indicare che $O_2$ è $O_1$ nel testo pseudocodice. Cerchiamo di chiarire l'esempio e la sua conclusione: se $S={O_1, O_3, O_4}$ ha valore 32 e volume 14, e la capacità è 15, questa è un'ottima soluzione. L'affermazione "NO! $S = {O_2, O_3, O_4}$ ottiene lo stesso guadagno utilizzando tutto" è problematica. Se si riferisse a un guadagno _uguale o migliore_ a quello ottenuto, e dovesse _utilizzare tutto_ lo spazio (il che non è richiesto per l'ottimalità, solo per i problemi di "bin packing"), sarebbe un altro tipo di problema. La frase implica che il guadagno di $O_2, O_3, O_4$ è 32, il che non è vero ($5+15+7=27$). L'errore nel testo della fonte evidenzia la necessità di verificare sempre gli assunti. Il punto chiave è che, indipendentemente dalla soluzione precisa in questo esempio, l'algoritmo greedy **non è garantito essere ottimale** per il problema dello zaino.

**Tentativo Greedy (Massimizzare il Rapporto Valore/Volume):**

1. Si calcola il rapporto valore/volume: $O_1: 10/2=5$, $O_2: 5/3 \approx 1.67$, $O_3: 15/5=3$, $O_4: 7/7=1$.
2. Si ordina per rapporto decrescente: Oggetto 1 (5), Oggetto 3 (3), Oggetto 2 (1.67), Oggetto 4 (1).
3. **Passo 1:** Si prende l'Oggetto 1 (Volume: 2, Valore: 10). Capacità rimanente: 13.
4. **Passo 2:** Si prende l'Oggetto 3 (Volume: 5, Valore: 15). Capacità rimanente: 8.
5. **Passo 3:** Si prende l'Oggetto 2 (Volume: 3, Valore: 5). Capacità rimanente: 5.
6. **Passo 4:** Si tenta di prendere l'Oggetto 4 (Volume: 7), ma non c'è spazio sufficiente. Soluzione ottenuta: ${O_1, O_3, O_2}$. Valore: $10+15+5=30$. Volume occupato: $2+5+3=10$. Anche in questo caso, la soluzione non è quella con valore 32 ottenuta prima. Questo dimostra che, per il problema dello zaino, le scelte localmente ottime non conducono necessariamente a una soluzione globalmente ottima.

### Applicazioni Avanzate: Algoritmi per Minimum Spanning Tree (MST)

Nonostante i limiti per alcuni problemi, gli algoritmi greedy sono fondamentali per la risoluzione di altri problemi complessi, come il **Problema dell'Albero di Connessione Minimo (Minimum Spanning Tree - MST)**.

**Problema:** Dato un grafo connesso, non orientato e pesato $G=(V, E)$, si cerca un sottoinsieme aciclico di archi $T \subseteq E$ che connetta tutti i vertici con il peso totale minimo $\omega(T) = \sum_{(u,v) \in T} \omega(u,v)$. Questo problema è utile, ad esempio, per collegare i PIN di un circuito elettrico minimizzando il consumo di filo.

Gli algoritmi di **Kruskal** e **Prim** risolvono il problema MST in modo efficiente utilizzando entrambi una metodologia avida.

#### Principio Generico dell'MST Greedy: `Generic-MST`

L'idea base è aggiungere iterativamente un "arco sicuro" all'insieme `A` (inizialmente vuoto) finché `A` non forma un MST. Un "arco sicuro" è un arco che, se aggiunto ad `A`, mantiene la proprietà che `A` è un sottoinsieme di qualche MST.

Per definire un arco sicuro, introduciamo il concetto di **taglio** e **arco leggero**:

- Un **taglio** $(S, V-S)$ di un grafo non orientato $G=(V, E)$ è una partizione dell'insieme dei vertici $V$ in due sottoinsiemi $S$ e $V-S$.
- Un arco $(u, v)$ **attraversa il taglio** se un estremo $u$ è in $S$ e l'altro $v$ è in $V-S$.
- Un taglio **rispetta un insieme di archi $A$** se nessun arco in $A$ attraversa il taglio (cioè, tutti gli archi in $A$ hanno entrambi gli estremi nello stesso sottoinsieme $S$ o $V-S$).
- Un **arco è leggero per un taglio** se il suo peso è il minimo tra i pesi di tutti gli archi che attraversano quel taglio.

**Lemma dell'Arco Sicuro:** Sia $G=(V,E)$ un grafo connesso non orientato e pesato. Sia $A$ un sottoinsieme di $E$ che è contenuto in qualche MST per $G$. Sia $(S, V-S)$ un taglio di $G$ che rispetta $A$. Sia $(u, v)$ un arco leggero che attraversa il taglio. Allora $(u, v)$ è un arco sicuro per $A$.

- **Dimostrazione (per "taglia e incolla"):** Si assume un MST $T$ che contiene $A$ ma non $(u,v)$ (se lo contenesse, sarebbe già dimostrato). L'aggiunta di $(u,v)$ a $T$ crea un ciclo. Poiché $(u,v)$ attraversa il taglio $(S, V-S)$, il ciclo deve contenere almeno un altro arco $(x,y)$ che attraversa lo stesso taglio. Rimuovendo $(x,y)$ dal ciclo, si ottiene un nuovo albero $T'$. Dato che $(u,v)$ è un arco leggero per il taglio, $\omega(u,v) \le \omega(x,y)$, quindi $\omega(T') \le \omega(T)$. Questo implica che $T'$ è anch'esso un MST. Poiché $A \cup {(u,v)}$ è un sottoinsieme di $T'$, $(u,v)$ è un arco sicuro per $A$.

Un **Corollario** importante derivante dal lemma dell'arco sicuro è che se $C=(V', E')$ è una componente connessa (un albero) nella foresta generata finora (dall'insieme $A$), e $(u,v)$ è un arco leggero che connette $C$ a un altro albero non in $C$, allora $(u,v)$ è un arco sicuro per $A$. Questo corollario è la base per gli algoritmi di Kruskal e Prim.

#### Algoritmo di Kruskal

L'algoritmo di Kruskal costruisce un MST aggiungendo iterativamente gli archi sicuri alla foresta di alberi di connessione, partendo da una situazione in cui ogni vertice è un albero separato senza archi.

**Strategia Greedy di Kruskal:**

1. Inizializzare un insieme `A` vuoto per contenere gli archi del MST.
2. Per ogni vertice $v \in V$, creare un insieme disgiunto contenente solo $v$ (`MakeSet(v)`).
3. Ordinare tutti gli archi del grafo in una lista $L$ in ordine non decrescente di peso.
4. Scorrere gli archi in $L$ (dal più leggero al più pesante):
    - Per ogni arco $(u, v)$, se $u$ e $v$ appartengono a insiemi disgiunti diversi (`FindSet(u) != FindSet(v)`), significa che l'arco non forma un ciclo con gli archi già selezionati.
    - In tal caso, aggiungere $(u,v)$ ad `A` e unire gli insiemi contenenti $u$ e $v$ (`Union(u,v)`).

**Implementazione delle Operazioni su Insiemi Disgiunti (DSU):** Per gestire gli insiemi disgiunti, si utilizza una struttura dati DSU che supporta le operazioni `MakeSet`, `FindSet` e `Union`. Una implementazione efficiente si basa su liste concatenate modificate:

- Ogni lista ha puntatori alla testa (`head`) e alla coda (`tail`).
- Il rappresentante dell'insieme è l'elemento in testa alla lista.
- Ogni nodo ha un puntatore `back` che punta alla testa della sua lista, facilitando `FindSet` in $O(1)$.
- `MakeSet(x)`: Crea una nuova lista con $x$ come unico elemento. Costo: $O(1)$.
- `FindSet(x)`: Restituisce il rappresentante dell'insieme di $x$ (seguendo `x.back`). Costo: $O(1)$.
- `Union(u,v)`: Concatena la lista di $v$ (o del suo rappresentante) alla coda della lista di $u$ (o del suo rappresentante). Tutti i nodi nella lista di $v$ devono aggiornare il loro puntatore `back` per puntare alla testa della lista di $u$. Costo: $O(n)$ nel caso peggiore (se la lista di $v$ è lunga $n$).

**Analisi della Complessità di Kruskal:**
1. Inizializzazione (`MakeSet` per ogni vertice): $O(V)$.
2. Ordinamento degli archi: $O(E \lg E)$ (es. con MergeSort).
3. Ciclo principale (`for e in L`): Esegue $|E|$ iterazioni. Ogni iterazione include due `FindSet` ($O(1)$ ciascuno) e potenzialmente una `Union` ($O(n)$ nel caso peggiore con liste concatenate semplici). Utilizzando un'analisi ammortizzata più avanzata (non trattata in dettaglio nella fonte ma accennata), che sfrutta l'implementazione DSU con alberi e compressione dei percorsi, una sequenza di $m$ operazioni `MakeSet`, `FindSet`, `Union` su $n$ elementi impiega $O(m + n \alpha(n))$ dove $\alpha(n)$ è la funzione inversa di Ackermann, estremamente lenta, rendendo il tempo quasi costante. In pratica, la complessità delle operazioni DSU è quasi $O(1)$. Pertanto, la complessità totale di Kruskal è dominata dall'ordinamento degli archi: $O(E \lg E)$. Poiché in un grafo connesso $E \ge V-1$, $\lg E \approx \lg V$, quindi può essere visto come $O(E \lg V)$.

**Esempio Visivo (Kruskal):** Immagina un grafo con 9 vertici e vari archi pesati. Kruskal selezionerà gli archi in ordine di peso:

1. Arco (d,e) peso 1. A = {(d,e)}. Union(d,e).
2. Arco (g,h) peso 2. A = {(d,e), (g,h)}. Union(g,h).
3. Arco (c,f) peso 2. A = {(d,e), (g,h), (c,f)}. Union(c,f). ... e così via, unendo le componenti connesse con gli archi più leggeri che non formano cicli.

#### Algoritmo di Prim
A differenza di Kruskal, l'algoritmo di Prim costruisce l'MST a partire da un singolo vertice sorgente `r` e fa crescere un solo albero.

**Strategia Greedy di Prim:**

1. Inizializzare per ogni vertice $v$: `v.key = ∞` (costo per connettersi all'albero in crescita) e `v.pi = NIL` (predecessore nell'albero MST).
2. Impostare `r.key = 0` per la radice scelta, in modo che sia il primo nodo estratto.
3. Creare una coda a min-priorità `Q` contenente tutti i vertici di $V$.
4. Finche `Q` non è vuota:
    - Estrarre il vertice `u` con il `key` minimo da `Q` (`Extract-Min(Q)`). Questo `u` viene aggiunto all'MST.
    - Per ogni vertice `v` adiacente a `u` (`for v in G.Adj[u]`):
        - Se `v` è ancora in `Q` (non è ancora stato aggiunto all'MST) e il peso dell'arco $(u,v)$ è minore del `v.key` corrente:
            - Aggiornare `v.pi = u` (impostando `u` come predecessore di `v` nell'MST).
            - Aggiornare `v.key = w(u,v)` (nuovo costo minimo per connettere `v` all'MST) e aggiornare la priorità di `v` in `Q` (`Decrease-Key(Q, v, w(u,v))`).

**Struttura Dati per Coda a Min-Priorità:** L'efficienza di Prim dipende crucialmente dall'implementazione della coda a min-priorità. I **min-Heap** sono una scelta comune.

- Un min-heap è un array che rappresenta un albero binario quasi completo, dove ogni nodo genitore ha un valore minore o uguale a quello dei suoi figli.
- Operazioni chiave per min-heap: `Insert`, `Minimum`, `Extract-Min`, `Decrease-Key`.

**Analisi della Complessità di Prim:**

- Inizializzazione: $O(V)$ per impostare `key` e `pi`.
- Popolamento della coda a priorità: Inserire $V$ elementi in un min-heap costa $O(V \lg V)$ se fatto element by element, o $O(V)$ se si costruisce l'heap direttamente.
- Ciclo `while Q != ∅`: Esegue $V$ volte `Extract-Min` (costo $O(\lg V)$ ciascuno). Totale $O(V \lg V)$.
- Ciclo `for v in G.Adj[u]`: Tutti gli archi vengono esaminati al più una volta, in totale $O(E)$ volte. Ogni `Decrease-Key` costa $O(\lg V)$. Totale $O(E \lg V)$.
- Complessità totale: $O(V \lg V + E \lg V) = O(E \lg V)$ (poiché in un grafo connesso $E \ge V-1$).

**Esempio Visivo (Prim):** Immagina un grafo con 9 vertici e vari archi pesati, partendo dal nodo 'a'.

1. Inizializzazione: tutti i nodi hanno `key = ∞`, `pi = NIL`, tranne 'a' che ha `key = 0`.
2. `Extract-Min` estrae 'a'.
3. Per i vicini di 'a' (b,h): `b.key` diventa 4 (da `a`), `h.key` diventa 8 (da `a`). Aggiornate le priorità in `Q`.
4. `Extract-Min` estrae 'b' (key 4).
5. Per i vicini di 'b' (a,c,h,i): `c.key` diventa 8 (da `b`), `i.key` diventa 7 (da `b`). `h.key` diventa 7 (da `b`) perché $w(b,h)=7 < h.key=8$. ... e così via, facendo crescere l'albero MST.

### Relazione con Ricerca A* e Euristiche

Il concetto greedy emerge anche nel campo della ricerca informata, in particolare nella **ricerca A*** e nella **ricerca Best-First Greedy**.

- Una **Ricerca Best-First Greedy** utilizza una funzione di valutazione $f(n) = h(n)$, dove $h(n)$ è una funzione euristica che stima il costo per raggiungere l'obiettivo dal nodo $n$. Fa una scelta localmente ottima basandosi solo sulla stima del costo rimanente, senza considerare il costo già sostenuto per raggiungere $n$. Non è garantita la soluzione ottima.
- L'algoritmo **A*** è un'estensione più sofisticata, che utilizza una funzione di valutazione $f(n) = g(n) + h(n)$, dove $g(n)$ è il costo effettivo dal nodo iniziale a $n$, e $h(n)$ è l'euristica. A* è ottimo se l'euristica $h(n)$ è _ammissibile_ (non sovrastima mai il costo reale per raggiungere l'obiettivo).

È possibile concettualizzare questi algoritmi come casi particolari di una __Ricerca A_ Pesata (Weighted A*)_*, dove la funzione di valutazione è $f(n) = g(n) + W \cdot h(n)$ con un peso $W > 1$ sull'euristica.

- **Ricerca Costo Uniforme** (equivalente a Dijkstra): $W=0$, quindi $f(n) = g(n)$. Si basa solo sul costo accumulato.
- **Ricerca A***: $W=1$, quindi $f(n) = g(n) + h(n)$. Bilancia costo accumulato e stima rimanente.
- **Ricerca Best-First Greedy**: $W=\infty$ (o molto grande, enfatizzando solo $h(n)$), quindi $f(n) \approx h(n)$. Si basa solo sulla stima del costo rimanente.

Gli algoritmi greedy, pur non essendo una soluzione universale per l'ottimalità, rimangono strumenti computazionalmente efficienti e fondamentali nel panorama degli algoritmi, spesso utilizzati in combinazione con euristiche per problemi complessi dove una soluzione esaustiva sarebbe impraticabile.