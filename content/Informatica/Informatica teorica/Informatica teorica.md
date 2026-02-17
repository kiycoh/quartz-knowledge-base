---
last modified: 2025, 11, 10 16:11:06
related: null
tags:
  - complessita-computazionale
  - teoria-probabilità
  - computazione
---
# Teoria della complessità
La teoria della complessità computazionale affronta la domanda fondamentale di cosa rende alcuni [[Problema computazionale|problemi computazionali]] complessi e cosa li differenziano da quelli semplici.

In termini generali, **la complessità di un problema è legata alle risorse computazionali minime necessarie per risolverlo** *(difficoltà computazionale relativa)*, principalmente tempo di calcolo e memoria. I problemi sono classificati in diverse classi di complessità in base all'efficienza dell'algoritmo più efficiente conosciuto in grado di risolvere quel problema specifico.

## Risoluzione algoritmica di un problema
Nel processo di affrontare un problema complesso, ci sono alcune strategie chiave:

1. **Comprendere il problema:**
	- Modificare il problema per renderlo più gestibile. Questo potrebbe coinvolgere la suddivisione del problema in sotto-problemi più semplici o la riformulazione del problema in modo da renderlo più adatto a un approccio algoritmico.
2. **Accettare soluzioni non esatte:**
	- Riconoscere che alcuni problemi potrebbero non avere soluzioni esatte. In tal caso, si potrebbe mirare a soluzioni approssimative che soddisfano i requisiti nella pratica, anche se non sono perfettamente corrette.
3. **Valutare le alternative:**
	- Esplorare diverse strategie di risoluzione. Un problema può essere affrontato in modi diversi, e la scelta dell'approccio può dipendere dalle risorse disponibili, dalla velocità di esecuzione desiderata e da altri fattori.
4. **Analisi della Complessità:** 
	- Valutare la complessità dell'algoritmo in termini di tempo e spazio. Questa analisi aiuta a comprendere quanto tempo l'algoritmo richiederà per eseguire e quanta memoria consumerà in base alla dimensione dei dati di input.
5. **Ottimizzazione:** 
	- In alcuni casi, è possibile ottimizzare l'algoritmo per ridurre il tempo di esecuzione o l'utilizzo di risorse. Questo processo coinvolge la revisione e l'ottimizzazione dei passi dell'algoritmo senza comprometterne la correttezza.

La definizione completa di un problema è essenziale per determinare la sua complessità. Una definizione chiara del problema aiuta a stabilire i confini e le limitazioni, consentendo di valutare meglio le risorse richieste per risolverlo.
# 💻 Teoria della computabilità
[[Macchine di Turing#^Godel-incompletezza]]

Stabilire se un enunciato matematico è *vero* o *falso* è fondamentale in matematica, ma la teoria della computabilità dimostra che non esiste un algoritmo universale in grado di risolvere questo problema in modo generale. L'algoritmo è la descrizione di una procedura che risolve un problema, e può esserci più di un algoritmo per un dato programma.

Matematici come Gödel, Turing e Church hanno dimostrato che esistono problemi irrisolvibili per un computer. Questo significa che ci sono enunciati matematici la cui veridicità o falsità non può essere determinata da un algoritmo. **La teoria della computabilità è cruciale nel rivelare i limiti della computazione.**

> [!tip] Definizione formale di computazione
> La **computazione** è un processo sequenziale di esecuzione di istruzioni o passi, in cui uno stato iniziale evolve attraverso una serie di transizioni seguendo regole specifiche definite da un modello di calcolo. Tale processo può produrre un output che rappresenta la soluzione del problema o il risultato desiderato.

## Il "Salto algoritmico"
Il determinismo negli algoritmi indica che ogni passo dell'esecuzione dell'algoritmo è completamente determinato dalla situazione corrente. In altre parole, dati gli stessi input in condizioni identiche, un algoritmo deterministico produrrà sempre lo stesso risultato.

L'espressione "Salto nel buio algoritmico" sottolinea come, una volta che un algoritmo è stato scritto, esso può essere eseguito su una macchina senza ulteriori interventi o decisioni esterne. Non c'è incertezza o "salto nel buio" nel processo di esecuzione dell'algoritmo, poiché è completamente guidato dalle istruzioni scritte nell'algoritmo stesso.

## Perché devono esistere problemi indecidibili
La dimostrazione che non è possibile assegnare un numero intero a ogni linguaggio in modo che ogni linguaggio corrisponda a un intero e ogni intero sia assegnato a un unico linguaggio suggerisce che ci sono infinitamente meno programmi rispetto ai problemi. Questo concetto contribuisce alla comprensione degli "infiniti" nel contesto dei linguaggi di programmazione e dei problemi computazionali.
### [[Decidibilità]]
# Teoria degli automi
La **teoria degli automi** si occupa delle definizioni e delle proprietà dei modelli di calcolo. Questi modelli hanno un ruolo all'interno delle varie aree dell'informatica.

**[[Automa finito deterministico (DFA)]]:** Questi modelli rappresentano un tipo di automa con una capacità di memoria limitata. Sono utilizzati in diverse applicazioni, come il trattamento automatico dei testi, i compilatori e la progettazione hardware. La capacità limitata di memoria li rende adatti a compiti specifici in cui è necessario un controllo finito e deterministico.

**Grammatiche Context-Free:** Queste grammatiche sono modelli di calcolo che trovano ampio utilizzo nell'ambito dei linguaggi di programmazione e dell'intelligenza artificiale. Sono fondamentali per la definizione della sintassi dei linguaggi di programmazione e la generazione di strutture grammaticali. [[2.2 Grammatiche]]

## Proprietà degli algoritmi
1. **Proprietà della finitezza** ➨ L'algoritmo deve essere composto da un numero finito di passaggi.
2. **Proprietà di non ambiguità** ➨ Ogni passo deve essere diretto ed univoco nella sua successione
3. **Proprietà del determinismo** ➨ Ad ogni passo di esecuzione dell'algoritmo il passo successivo dipende interamente dal passo attuale dell'input.
4. **Proprietà della generalità** ➨ L'algoritmo deve risolvere classi di problemi, non problemi singoli.

# [[Logica proposizionale]]  

# [[Linguaggi context-free]]
## [[Linguaggi non context-free]]

# [[Logica dei predicati]]