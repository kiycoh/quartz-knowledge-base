---
last modified: 2025-07-16T21:02:00.000Z
related:
  - '[[Albero (Struttura dati)]]'
tags:
  - machine-learning
  - intelligenza-artificiale
  - algorithm-design
---
La Ricerca ad Albero Monte Carlo (MCTS) è una tecnica avanzata utilizzata per risolvere problemi in ambienti complessi, in particolare nei giochi, dove algoritmi di ricerca tradizionali, come Alpha-Beta, risultano impraticabili a causa della loro elevata complessità computazionale.

**Contesto e Necessità:** Nei giochi con un fattore di ramificazione (branching factor) molto elevato, come il Go (con un fattore medio di 361, rispetto ai 35 degli scacchi) o dove è difficile definire una funzione di valutazione euristica affidabile (ad esempio, per l'assenza di un valore materiale dei pezzi e la fluidità della disposizione sulla scacchiera nel Go), gli algoritmi come MiniMax con potatura Alpha-Beta non riescono a esplorare il grafo di gioco oltre pochi livelli di profondità (ad esempio, 4-5 mosse nel Go). Per superare questi limiti, si abbandona la ricerca Alpha-Beta in favore della MCTS.

**Concetto Principale: Simulazione (Playout)** A differenza degli algoritmi che si basano sulla stima di valori di utilità attesi tramite funzioni euristiche, la MCTS opera sul concetto di **simulazione**. Invece di calcolare euristiche, vengono effettuate delle simulazioni complete (chiamate _playout_) di partite a partire da un determinato stato. Durante queste simulazioni, le mosse possono essere scelte in modo casuale, e i risultati (vittoria/sconfitta) vengono registrati. Tuttavia, in giochi complessi, le mosse puramente casuali raramente corrispondono alle giocate ottimali di entrambi i giocatori.

**Politiche di Simulazione:** Per rendere le simulazioni più efficaci, è necessario introdurre delle **distorsioni** o **politiche di simulazione** che spingano le simulazioni verso mosse migliori. Queste politiche possono essere stabilite tramite:

- Euristiche specifiche del gioco (es. negli scacchi).
- Apprendimento iterativo e reti neurali (es. nel Go).

La scelta del numero di simulazioni (N) e dello stato di partenza per la simulazione è cruciale. Nella **ricerca Monte Carlo pura**, si simula sempre dallo stato corrente, registrando la mossa con il più alto tasso di vittorie. Sebbene in giochi semplici l'aumento di N porti a una convergenza verso il gioco ottimo, nella maggior parte dei casi non è sufficiente.

**Bilanciamento Esplorazione/Sfruttamento:** Per migliorare le prestazioni e bilanciare la ricerca, è fondamentale una **politica di selezione** che equilibri due fattori:

1. **Esplorazione**: Visitare stati per i quali sono state effettuate poche simulazioni, per scoprire nuove possibilità.
2. **Sfruttamento**: Utilizzare le informazioni derivanti da stati che hanno prodotto buoni risultati nelle simulazioni precedenti, per approfondire le aree promettenti.

Per implementare queste politiche, la MCTS mantiene un **albero di ricerca parziale** in memoria. Ad ogni simulazione, questo albero viene fatto crescere e i risultati vengono propagati ai nodi già presenti, seguendo un ciclo di quattro operazioni fondamentali:

1. **Selezione (Selection)**: Partendo dalla radice, vengono effettuate scelte basate sulla politica di selezione, navigando l'albero fino a raggiungere una foglia (un nodo non ancora completamente espanso).
2. **Espansione (Expansion)**: Viene generato un nuovo nodo figlio dalla foglia raggiunta. Questo nodo rappresenta uno stato potenziale da esplorare.
3. **Simulazione (Simulation)**: Viene eseguita una simulazione completa della partita a partire dal nodo appena creato, scegliendo le mosse secondo la politica di simulazione. I risultati di queste mosse non vengono registrati nell'albero.
4. **Retropropagazione (Backpropagation)**: Il risultato della simulazione (es. vittoria/sconfitta) viene retropropagato a tutti i nodi lungo il percorso dall'albero fino alla radice, aggiornando le statistiche dei nodi (es. numero di visite, utilità totale).

Queste operazioni vengono ripetute per un tempo o un numero di iterazioni prestabilito. Alla fine, viene restituita la mossa con il più alto numero di simulazioni o il miglior tasso di vittoria.

**Esempio di Politica di Selezione: Upper Confidence Bounds Applied to Tree (UCT)** Una politica di selezione comune è la UCT, che classifica ogni mossa potenziale in base alla formula UCB1: `UCB1 = U(n) / N(n) + C * sqrt(ln(N(PADRE(n))) / N(n))` Dove:

- `U(n)` è l'utilità delle simulazioni passate per il nodo `n`.
- `N(n)` è il numero totale di simulazioni effettuate a partire dal nodo `n`.
- Il termine `U(n) / N(n)` rappresenta il **termine di sfruttamento**, ovvero l'utilità media del nodo `n`.
- Il termine `C * sqrt(ln(N(PADRE(n))) / N(n))` è il **termine di esplorazione**. Il suo valore è alto per i nodi esplorati poche volte e basso per quelli con più simulazioni, incentivando l'esplorazione di rami meno battuti. `C` è una costante che bilancia l'esplorazione e lo sfruttamento.

**Efficienza e Vantaggi:** Ogni singola simulazione in MCTS richiede tempo lineare poiché considera solo una mossa alla volta. Questo permette di eseguire un elevato numero di simulazioni con relativa facilità. La MCTS è particolarmente efficiente per **giochi complessi con un alto fattore di ramificazione** (come il Go) o per giochi in cui è **difficile stimare una buona funzione di valutazione** (a differenza di Alpha-Beta che dipende fortemente da euristiche accurate). Le sue prestazioni dipendono molto dalla politica di selezione, ma a differenza delle euristiche fisse, un'eventuale scelta sbagliata nella politica di selezione non influisce sulla singola scelta, bensì sulla strategia generale, riducendo il rischio di fallimenti catastrofici dovuti a euristiche errate.

**Applicazioni e Combinazioni:**

- **Giochi Stocastici**: La MCTS è l'approccio privilegiato per giochi con un alto fattore di casualità (es. Yahtzee, che prevede il lancio di 5 dadi) dove l'albero ExpectiMinimax risulta impossibile da esplorare per la sua complessità esponenziale `O(b^m * n^m)`.
- **Senza Esperienza Precedente**: L'algoritmo MCTS può essere applicato anche a giochi di cui non si ha esperienza pregressa per creare una funzione di valutazione, poiché richiede solo la conoscenza delle regole del gioco.
- **Combinazione con Alpha-Beta**: È possibile combinare MCTS con la ricerca Alpha-Beta, interrompendo le simulazioni dopo un certo numero di mosse e utilizzando una funzione euristica al termine della simulazione per la valutazione.

In sintesi, la MCTS è un algoritmo potente e flessibile per la ricerca in spazi di stati ampi e complessi, specialmente quando le euristiche non sono facilmente definibili o quando la casualità rende impraticabili le tecniche deterministiche basate sugli alberi di gioco tradizionali.