---
last modified: null
related: []
tags:
  - machine-learning
  - intelligenza-artificiale
  - scienze-cognitive
---
# Definizione di agente
Un agente è formato da due componenti:
- L'architettura che è costituita dai sensori e dagli attuatori (sequenza percettiva e sequenza)
- Il programma che implementa la funzione agente

- Agenti reattivi semplici
- Agenti reattivi basati su modelli
- Agenti basati su obiettivi
- Agenti basati su utilità

Si ha una stanza, una stanza può avere due stati (sporca o pulita). Il robot compire queste azioni: aspira, sposta a destra o sposta a sinistra.

```
Func pulisci_stanze(pos, stato)
	while stanza1.stato ≠ pulito
		if robot.destra or robot.sinistra:
			if stanza ≠ pulito:
				robot.aspira
			else:
				robot.sposta_sinistra
				
		pulisci_stanze
```

## Tipi di agente
Nel campo degli algoritmi e delle strutture dati, l'approccio alla costruzione di un'intelligenza artificiale (IA) si concretizza attraverso la definizione e l'implementazione di **programmi agente**. Un **agente** è un sistema capace di percepire l'ambiente e di agire su di esso. La sua operatività è descritta da una **funzione agente**, che mappa ogni sequenza percettiva (la storia delle percezioni ricevute) a una specifica azione. Tuttavia, la complessità degli ambienti reali rende impraticabile la rappresentazione di tale funzione come una tabella esaustiva di tutte le possibili sequenze percettive, che nel caso degli scacchi, ad esempio, richiederebbe circa $10^{120}$ righe. Ciò impone la necessità di limitare la lunghezza della sequenza percettiva e di sviluppare programmi che, pur non coprendo ogni scenario, agiscano razionalmente.

Per ovviare a queste limitazioni, sono stati identificati diversi **tipi di programma agente**, ciascuno con un proprio approccio alla rappresentazione della conoscenza e alla decisione dell'azione:

1. **Agenti Reattivi Semplici (Simple Reflex Agents)**
2. **Agenti Reattivi Basati su Modello (Model-Based Reflex Agents)**
3. **Agenti Basati su Obiettivi (Goal-Based Agents)**
4. **Agenti Basati su Utilità (Utility-Based Agents)**

Analizziamo ciascun tipo in dettaglio:

### 1. Agenti Reattivi Semplici

Gli agenti reattivi semplici operano sulla base di una diretta associazione tra **percezione corrente** e **azione**. Non mantengono una memoria interna delle percezioni passate o una rappresentazione dello stato dell'ambiente. La loro logica è implementata attraverso un insieme di **regole "se-allora" (condition-action rules)**.

**Meccanismo:** Il flusso decisionale è elementare: i sensori dell'agente captano l'aspetto corrente dell'ambiente; questo viene confrontato con le condizioni predefinite nelle regole; se una condizione è soddisfatta, viene eseguita l'azione associata attraverso gli attuatori.

**Esempio Pratico: Robot Aspirapolvere Semplice** Immaginiamo un ambiente con due stanze (destra e sinistra), ciascuna con uno stato (sporco o pulito).

- Se la stanza corrente è "sporco", l'agente esegue l'azione "Aspira".
- Se la stanza corrente è "pulito" e la posizione è "sinistra", l'agente si sposta a "Destra".
- Se la stanza corrente è "pulito" e la posizione è "destra", l'agente si sposta a "Sinistra".

**Pseudocodice:**

```
PROCEDURE Aspirapolvere-Reattivo([posizione, stato])
1.  If (stato == sporco) return Aspira
2.  If (posizione == ‘sinistra’) return Destra
3.  If (posizione == ‘destra’) return Sinistra
```

**Vantaggi e Limitazioni:**

- **Vantaggi:** Semplicità di implementazione e rapidità d'azione, in quanto non richiedono calcoli complessi o mantenimento di stato.
- **Limitazioni:** Sono efficaci solo in ambienti completamente osservabili e deterministici. Non possono adattarsi a situazioni non esplicitamente codificate nelle regole e non sono in grado di gestire ambienti parzialmente osservabili o stocastici, dove la percezione corrente da sola non è sufficiente a determinare la migliore azione. La mancanza di memoria impedisce loro di imparare dall'esperienza passata.

### 2. Agenti Reattivi Basati su Modello

Per superare le limitazioni degli agenti reattivi semplici, gli agenti reattivi basati su modello introducono una **rappresentazione interna dello stato dell'ambiente (un "modello")**. Questo modello viene aggiornato costantemente per riflettere sia le percezioni attuali che l'evoluzione intrinseca dell'ambiente e le modifiche causate dalle azioni dell'agente stesso.

**Meccanismo:** L'agente non si basa solo su "ciò che il mondo è ora", ma anche su "ciò che il mondo è stato" e "come l'azione modifica il mondo". Il flusso di informazioni include:

- **Stato:** La rappresentazione interna dello stato corrente dell'ambiente.
- **Evoluzione:** Regole su come l'ambiente cambia indipendentemente dalle azioni dell'agente (es. il tempo che passa, eventi casuali).
- **Modifiche:** Regole su come le azioni dell'agente modificano lo stato dell'ambiente.

**Esempio Pratico: Robot Aspirapolvere con Modello** Estendiamo l'esempio precedente: se una stanza è pulita, ogni 15 secondi c'è una probabilità del 50% che si sporchi. Pulendo la stanza, il timer si resetta.

**Pseudocodice (schematico, focalizzato sul modello):**

```
PROCEDURE Aspirapolvere-Modello([posizione, stato-amb])
1.  Static stato // Variabile che persiste tra le chiamate, rappresenta il modello interno
2.  If(posizione == ‘sinistra’)
3.      if(stato-amb == ‘sporco’)
4.          stato.ts = 0 // Resetta il timer sporco
5.          stato.td = (stato.td +1)%15 // Incrementa il timer generico (ogni 15 secondi potenziale sporco)
6.          return Aspira
7.      else // Stanza pulita
8.          stato.ts = (stato.ts +1)%15 // Incrementa il timer sporco (per eventuale sporco futuro)
9.          stato.td = (stato.td +1)%15 // Incrementa il timer generico
10.         if(stato.td == 0) // Ogni 15 cicli, se la stanza è pulita, potenziale movimento
11.             return Destra
12. Else // Caso simmetrico per posizione 'destra'
13.     // ... logica speculare ...
```

**Vantaggi e Limitazioni:**

- **Vantaggi:** Capacità di operare in ambienti parzialmente osservabili, sfruttando la storia delle percezioni per inferire lo stato nascosto. Possono prendere decisioni più informate.
- **Limitazioni:** Non sono in grado di prendere decisioni che richiedono una previsione a lungo termine o la valutazione di una sequenza di azioni. Le loro regole sono ancora reattive, sebbene basate su uno stato più ricco. Sono limitati alla conoscenza del loro modello, e non sono in grado di apprendere da sé come il mondo funziona se il modello è ignoto.

### 3. Agenti Basati su Obiettivi

Gli agenti basati su obiettivi estendono il concetto di modello introducendo la nozione di **"obiettivo" (goal)**. Invece di limitarsi a reagire allo stato attuale, cercano di trovare una sequenza di azioni che li porti a uno stato desiderato. Questo implica la capacità di **cercare e pianificare**.

**Meccanismo:** Questi agenti necessitano non solo di un modello che descriva lo stato corrente e le transizioni, ma anche di informazioni su **"come cambia se azione"** (l'effetto delle azioni sull'ambiente) e un test per determinare se uno stato soddisfa l'obiettivo. Le quattro fasi fondamentali del processo di risoluzione di problemi per questi agenti sono:

1. **Formulazione dell'obiettivo:** Definire gli scopi desiderati dell'agente.
2. **Formulazione del problema:** Creare una descrizione astratta degli stati, delle azioni possibili, dei costi e degli stati obiettivo (spazio degli stati).
3. **Ricerca:** Simulare le azioni nello spazio degli stati per trovare una sequenza che porti all'obiettivo (una "soluzione" o "cammino"). Qui entrano in gioco gli **algoritmi di ricerca su alberi e grafi** (es. BFS, DFS, A*).
4. **Esecuzione:** Realizzare la sequenza di azioni trovata nell'ambiente reale.

**Struttura del Problema di Ricerca:** Un problema di ricerca è formalizzato da:

- Un **spazio degli stati**: l'insieme di tutti i possibili stati dell'ambiente.
- Uno **stato iniziale**: la configurazione di partenza dell'agente.
- Uno o più **stati obiettivo**: le configurazioni desiderate.
- Un insieme di **Azioni(s)**: le mosse possibili da un dato stato `s`.
- Un **modello di transizione (Risultato(s,a))**: la funzione che determina lo stato successivo data un'azione `a` da uno stato `s`.
- Una **funzione di costo**: che assegna un valore numerico al passaggio da uno stato all'altro tramite un'azione.

**Esempio Pratico: Agente Navigatore** Un agente navigatore, come un GPS, ha come obiettivo raggiungere una destinazione. Deve formulare il problema identificando la mappa (spazio degli stati), la posizione attuale (stato iniziale), la destinazione (stato obiettivo), le strade percorribili (azioni), i tempi di percorrenza (costi) e poi utilizzare un algoritmo di ricerca (es. A* con euristica della distanza in linea d'aria) per trovare il percorso ottimale.

**Vantaggi e Limitazioni:**

- **Vantaggi:** Capacità di pianificare a lungo termine, di trovare sequenze di azioni per raggiungere stati non immediatamente accessibili. Possono operare in ambienti sequenziali.
- **Limitazioni:** La complessità della ricerca negli spazi degli stati può essere proibitiva (esponenziale, $O(b^d)$). La qualità della soluzione dipende dalla completezza del modello e dall'efficacia dell'algoritmo di ricerca e dell'euristica (per gli algoritmi informati). In ambienti non deterministici, la soluzione non è più una sequenza fissa, ma una "strategia ramificata".

### 4. Agenti Basati su Utilità

Gli agenti basati su utilità sono il tipo più sofisticato. Vengono impiegati quando il raggiungimento di un obiettivo non è sufficiente o quando ci sono **più modi per raggiungere l'obiettivo**, o ancora quando è presente **incertezza (stocasticità)**. In queste situazioni, l'agente non solo si preoccupa di raggiungere un obiettivo, ma di raggiungere il **miglior obiettivo possibile** o di ottenere il risultato che massimizza la sua "soddisfazione".

**Meccanismo:** Introducono una **funzione di utilità** che quantifica la desiderabilità di ogni stato o sequenza di stati per l'agente. L'agente cercherà di scegliere l'azione che massimizza l'utilità attesa del risultato. Questo implica la capacità di pesare diversi obiettivi, di gestire compromessi e di valutare rischi e benefici in ambienti incerti.

**Esempio Pratico: Gioco del Poker** In un gioco come il poker (un ambiente stocastico e parzialmente osservabile), l'agente non ha un obiettivo binario (vincere o perdere la mano), ma deve massimizzare il valore atteso delle sue azioni. Deve considerare le probabilità di vincita, il valore delle fiches, il bluff degli avversari, e scegliere l'azione (puntare, passare, ritirarsi) che massimizza l'utilità a lungo termine, non solo la singola mano.

**Vantaggi e Limitazioni:**

- **Vantaggi:** Capacità di prendere decisioni ottimali in scenari complessi con incertezza, trade-off tra obiettivi e costi variabili. Possono gestire giochi stocastici e con informazione parziale, come il backgammon o il poker, dove l'algoritmo ExpectiMinimax o la Ricerca ad Albero Monte Carlo (MCTS) diventano cruciali.
- **Limitazioni:** La definizione e il calcolo della funzione di utilità possono essere estremamente complessi, specialmente in ambienti con molte variabili o incertezze. Richiede modelli probabilistici accurati dell'ambiente.

### Concetti Trasversali

Tutti i tipi di programma agente sono influenzati dalle proprietà dell'ambiente operativo, descritte tramite l'acronimo **PEAS (Performance, Environment, Actuators, Sensors)** e classificazioni come osservabilità (completa/parziale/inosservabile), numero di agenti (singolo/multiplo), determinismo (deterministico/non deterministico/stocastico), episodicità (episodico/sequenziale), dinamismo (statico/dinamico/semi-dinamico), e conoscenza (noto/ignoto).

La **razionalità** di un agente dipende dalla misura di prestazione che cerca di massimizzare, dalla sua conoscenza pregressa dell'ambiente, dalle azioni che può compiere e dalla sequenza percettiva. Un agente **razionale** non è necessariamente **onnisciente** (non conosce il risultato reale che la sua azione produrrà), ma cerca di massimizzare la prestazione del risultato atteso, basandosi su una visione parziale dell'ambiente. L'abilità di recuperare informazioni (information gathering) e di apprendere dall'esperienza è fondamentale per migliorare le prestazioni attese e rendere l'agente **autonomo**.