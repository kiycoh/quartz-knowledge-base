---
last modified: 24/10/2025 14:02
tags:
  - scienze-cognitive
  - intelligenza-artificiale
  - knowledge-representation
---
I **Frames**, proposti da Marvin Minsky nel 1975, sono strutture dati che raggruppano procedure connesse a un oggetto o a una situazione.

![[Pasted image 20250620011426.png]]

**Tipi di Frame**:

- **Frame Individuali**: Rappresentano oggetti specifici e sono composti da `slot` (contenitori) riempiti con `filler` (valori specifici, che possono essere semplici o riferimenti ad altri frame). Includono lo slot speciale `:INSTANCE-OF` che li collega al frame generico corrispondente.
- **Frame Generici (o di Classe)**: Sono modelli astratti che rappresentano categorie di oggetti e servono come prototipi. Possono specializzarsi in altri frame più generali tramite lo slot `:IS-A`, stabilendo una gerarchia (tassonomia).

**Componenti e Funzionamento**:

- **Slot**: Contenitori per i `filler`.
- **Procedure associate agli slot**: Si attivano in due casi:
    - **IF-ADDED**: Quando viene aggiunto un valore a uno slot (es. calcolare il giorno della settimana specificando una data).
    - **IF-NEEDED**: Quando un valore è richiesto ma non ancora disponibile (es. calcolare l'altezza di un tavolo dalla lunghezza delle gambe).
- **Ereditarietà**:
    - **Dei valori**: Un frame individuale può ereditare valori dai frame generici a cui è collegato tramite `:INSTANCE-OF` e `:IS-A`. I valori ereditati sono usati solo se non esistono valori espliciti nell'istanza, permettendo di sovrascrivere i valori predefiniti (ereditarietà revocabile o _defeasible_).
    - **Delle procedure**: Anche le procedure `IF-ADDED` e `IF-NEEDED` possono essere ereditate.
    - **Multipla**: Un frame generico può essere una specializzazione di più frame, e un frame individuale può essere istanza di più categorie. Questo offre flessibilità ma può portare a conflitti tra valori ereditati da più fonti.
- **Classificazione**: Processo di aggiornamento dinamico della tassonomia quando si aggiunge un nuovo frame generico o una nuova istanza, collegandoli ai frame rilevanti e aggiornando i collegamenti esistenti. Il sistema trova i concetti più generali che includono il nuovo concetto (sussumitori più specifici) e i concetti più specifici inclusi dal nuovo concetto (sussunti più generali).
- **Ragionamento**: Le procedure associate ai frame permettono un ragionamento flessibile e organizzato. Il sistema riconosce un oggetto come istanza di un frame generico, attivando le procedure che possono modificare la base di conoscenza o generare nuovi dati. Il ciclo di ragionamento include la creazione dell'istanza, l'ereditarietà dei valori mancanti e l'attivazione delle procedure `IF-ADDED`. Le procedure `IF-NEEDED` vengono eseguite solo su richiesta.
- **Interrogazioni Tipiche**: I sistemi a frame facilitano interrogazioni come:
    - Trovare tutte le istanze di una categoria (es. tutti gli oggetti di tipo `TravelStep`).
    - Trovare tutte le categorie a cui appartiene un oggetto (es. a quali categorie generiche appartiene `toronto`, utile per l'ereditarietà delle proprietà). Queste interrogazioni sono efficienti grazie alla struttura gerarchica che riduce il costo computazionale e permette di navigare la tassonomia evitando ridondanze.
- **Vantaggi**: L'organizzazione a frame rende la conoscenza flessibile, modulare e automatica. L'utente non deve specificare ogni dettaglio, poiché il sistema deduce, completa, aggiorna e collega i dati intelligentemente, agendo come un "foglio di calcolo simbolico".