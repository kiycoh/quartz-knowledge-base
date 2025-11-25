---
last modified: 2025, 11, 22 17:11:47
related: null
tags:
  - algoritmi-ordinamento
  - grafici
  - alberi-binari
---
# Tipi di strutture dati relazionali
Queste strutture modellano relazioni tra entità, rappresentate come nodi e connessioni.

- **Grafi (Graphs)**:
    - **Descrizione**: Un insieme di elementi (`nodi` o `vertici`, `V`) che possono essere collegati da linee (`archi`, `spigoli` o `lati`, `E`). `G = (V, E)`.
    - **Caratteristiche**:
        - **Orientati (Diretti) o Non Orientati**: Gli archi possono avere una direzione o essere bidirezionali.
        - **Pesati**: Agli archi può essere associato un valore (`peso`).
        - **Grado di un nodo**: Numero di archi incidenti.
        - **Cammini e Cicli**: Sequenze di vertici e archi. Un `circuito` è un cammino chiuso. Un `ciclo` non ha nodi ripetuti.
        - **Connettività**: `Connessi` se esiste un cammino tra due vertici. `Componenti connesse` sono sottografi massimali in cui tutti i vertici sono connessi tra loro. `Ponte` e `Snodo` disconnettono il grafo se rimossi.
    - **Rappresentazioni**:
        - **Matrici di Adiacenza**: Matrice `NxN` (N vertici) dove `a_ij = 1` se esiste un arco `(i,j)` (o il peso `p_ij` per grafi pesati). Non simmetrica per grafi orientati.
        - **Liste di Adiacenza**: Un array `Adj` di `N` liste, una per ogni vertice `u`. `Adj[u]` contiene tutti i vertici `v` adiacenti a `u`. Tipicamente usata per algoritmi di visita.
        - **Matrici di Incidenza**: Matrice `NxM` (N vertici, M archi) che indica quali vertici sono estremi di quali archi.
    - **Algoritmi di Ricerca sui Grafi**:
        - **Visita in Ampiezza (BFS - Breadth-First Search)**: Esplora il grafo per livelli a partire da una sorgente `s`. Utilizza una *coda* per gestire i nodi da visitare. Calcola la distanza minima (`v.d`) e il predecessore (`v.π`) da `s` a ogni nodo raggiungibile in grafi non pesati. Complessità **O(|V| + |E|)**.
        - **Visita in Profondità (DFS - Depth-First Search)**: Esplora un ramo il più in profondità possibile prima di tornare indietro. Non produce un singolo albero ma una foresta di alberi. Utilizza i tempi di scoperta (`u.d`) e completamento (`u.f`). Complessità **O(|V| + |E|)**. Classifica gli archi in base al colore dei nodi visitati (albero, all'indietro, in avanti, trasversali).
    - **Applicazioni dei Grafi**:
        - **Ordinamento Topologico**: Per Grafi Aciclici Orientati (DAG). Posiziona i nodi lungo una linea retta in modo che gli archi orientati vadano solo da sinistra a destra. Utilizzato per problemi di gestione eventi o precondizioni.
        - **Componenti Fortemente Connesse**: Insiemi massimali di vertici in cui ogni coppia di vertici è mutuamente raggiungibile. Un algoritmo per trovarle usa la DFS sul grafo originale e sul suo trasposto.
        - **Minimum Spanning Tree (MST - Albero di Connessione Minimo)**: Trovare un sottoinsieme aciclico di archi che connette tutti i vertici con peso totale minimo in un grafo connesso, non orientato e pesato. Risolvibile con algoritmi avidi:
            - **Algoritmo di Kruskal**: Aggiunge archi dal peso minimo che collegano nodi appartenenti a due alberi diversi, utilizzando una *struttura dati per insiemi disgiunti*. Complessità **O(|E| log |E|)**.
            - **Algoritmo di Prim**: Parte da una radice e aggiunge iterativamente l'arco leggero che collega l'albero corrente a un vertice non ancora incluso. Utilizza una *coda a priorità* (implementata con Min-Heap). Complessità **O(|E| log |V|)** con Min-Heap.
        - **Cammini Minimi (Shortest Paths)**: Trovare il cammino con peso minimo tra due vertici.
            - **Algoritmo di Bellman-Ford**: Risolve per cammini minimi da sorgente unica con pesi arbitrari (anche negativi, ma rileva cicli negativi). Complessità **O(|V| * |E|)**.
            - **Algoritmo per DAG**: Se il grafo è un DAG, i cammini minimi possono essere trovati in **O(|V| + |E|)** dopo un ordinamento topologico.
            - **Algoritmo di Dijkstra**: Generalizza BFS per grafi pesati con pesi *non negativi*. Utilizza una *coda a priorità* (Min-Heap) per scegliere il nodo con il `v.d` minimo. Complessità **O(|E| log |V|)** con Min-Heap.