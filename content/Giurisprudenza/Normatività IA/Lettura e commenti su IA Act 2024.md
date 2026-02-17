---
last modified: 24/10/2025 14:12
related: null
tags:
  - intelligenza-artificiale
  - machine-learning
  - data-science
---
[[REGOLAMENTO (UE) 2024-1689 DEL PARLAMENTO EUROPEO E DEL CONSIGLIO.pdf|The Artificial Intelligence Act of the EU]], pubblicato il 12 Giugno 2024, rappresenta un grande passo per i [[Armonizzazione Europea|paesi armonizzati]].
Lo strumento principale che adopera l'Europa sono le **direttive** che possono essere di due tipi:
- *alcune saranno adottate dai singoli stati,* introducendo queste norme direttamente nel proprio sistema di leggi;
- *altre saranno condivise* per cui l'Europa interviene come legislatore.

**L'AI Act** non ha solo uno scopo politico ma mira anche all'**innovazione**. L'Europa vuole imporsi come *pioniere nella regolamentazione dell'IA,* favorendo così lo sviluppo tecnologico.
- Anziché usare *il principio di precauzione* (che avrebbe limitato molti aspetti), si è fatta un'analisi dei **costi-benefici** per costruire una regolamentazione non troppo limitante.

> [!NOTE] Termini generali dell'IA Act
> L' **IA Act** cerca di garantire che l'IA sia *antropocentrica, sostenibile, sicura e inclusiva*, adottando un approccio basato sul rischio:
> - L'IA è considerata *un **prodotto** nelle mani del cittadino*, e deve avere l'obiettivo di migliorare il benessere delle persone.
> - Classifica le pratiche di IA in base al loro rischio di **impatto sui diritti fondamentali** *(dignità umana, libertà, uguaglianza, democrazia, diritto alla non discriminazione, protezione dei dati, salute e sicurezza)*, con misure proporzionali al livello di rischio, fino al divieto di pratiche incompatibili con la tutela di tali diritti.
> 	- Vengono vietate pratiche che potrebbero manipolare o discriminare (complementare alle disposizioni in materia di pratiche commerciali sleali).
> - Le IA (in particolare quelle ad alto rischio) devono essere progettate e sviluppate in modo da garantire un **adeguato livello di accuratezza**, robustezza e cybersicurezza.
# Definizione di IA secondo l'IA Act
 *L'IA Act* definisce nell'articolo 3 "un sistema di IA" nei seguenti termini:

> *"un sistema automatizzato progettato per funzionare con livelli di autonomia variabili e che può presentare adattabilità dopo la diffusione e che, per obiettivi espliciti o impliciti, deduce dall’input che riceve come generare output quali previsioni, contenuti, raccomandazioni o decisioni che possono influenzare ambienti fisici o virtuali;"*

> [!IMPORTANT] Modelli *vs* Sistemi
> È importante la distinzione tra "*modelli*" e "*sistemi*" di IA.
> - I **modelli** sono componenti essenziali dei sistemi, ma non sono sistemi completi di per sé. 
> - I **sistemi** sono essenzialmente composti dal modello ma comprendono ulteriori componenti, come ad esempio un'interfaccia utente.

Tra i sistemi di IA non rientrano i software tradizionali e gli approcci di programmazione più semplici che utilizzano «*regole definite unicamente da persone fisiche per eseguire operazioni in modo automatico*».
# Requisiti di distribuzione
*L'AI Act* definisce l'IA come un **prodotto**, perciò deve necessariamente soddisfare dei **requisiti** (solitamente indicati con il marchio *CE*).
- Durante e dopo la produzione del *sistema di IA*, degli **organismi certificati** (o in alcuni casi il produttore stesso) devono dimostrare che il prodotto sia *a norma*.
	- *È nell’interesse dell’azienda certificare il prodotto attraverso terzi, per denotare affidabilità ed evitare errori che porterebbero a sanzioni (e in alcuni casi il ritiro del prodotto).*

Questa procedura, per quanto possa sembrare limitante, effettivamente **agevola la distribuzione** del sistema di IA poiché solitamente ogni stato applica un proprio standard di sicurezza che serve non tanto a garantire la sicurezza stessa, ma ad impedire l'immissione di determinati prodotti nel proprio paese.

> [!EXAMPLE] Enti di armonizzazione europea
> **L'International Organization for Standardization (ISO)**, ad esempio, è un ente che sancisce delle norme tecniche mirate all'armonizzazione tra i paesi.
> - Ricordiamo l'obbligo di utilizzo di *cavi Type-C* invece di connettori proprietari o le prese elettriche.
## Mitigazione dei rischi
In Europa, essendo l'IA un *prodotto*, ==i produttori hanno delle responsabilità anche dopo l'immissione del mercato.== In questo ambito riconosciamo la figura del **danneggiato** e del **danneggiante**:
- In Europa si tende a tutelare maggiormente *il danneggiato*, poiché vi è ciò che chiamiamo **"Responsabilità oggettiva del produttore"**.
	- *Dimostrato il nesso di causalità, il produttore è responsabile del danno e deve ritirare ogni prodotto difettoso attraverso "l'allerts safety gate".*
- In Europa **le sanzioni hanno scopo compensativo**: si risarcisce il consumatore per la sua perdita.
	- *Il produttore sarà responsabile solo per danni arrecati da **un uso improprio ragionevolmente prevedibile.***
	- Negli USA *le sanzioni sono punitive*: quindi maggiori del danno arrecato.
- In Europa a *responsabilità dei consumatori* varia in base al **tipo d'uso**:
	- Un **uso professionale** addossa spesso la responsabilità al consumatore (*computer aziendali*).
# Capacità inferenziale
Il regolamento pone particolare attenzione sulla **capacità inferenziale** dell'IA:
- L’inferenza si riferisce al processo attraverso il quale il sistema di IA trae conclusioni o fornisce previsioni a partire da dati o informazioni disponibili, ==è la capacità di un modello di IA che consente al sistema «l’apprendimento, il ragionamento o la modellizzazione»==. Vengono distinti due approcci su cui si basa l'inferenza: 
	- **L’apprendimento automatico:** consente al sistema di imparare «dai dati come conseguire determinati obiettivi»;
	- **La logica e la conoscenza:** trae «inferenze dalla conoscenza codificata o dalla rappresentazione simbolica del compito da risolvere».
# La piramide di rischio
La classificazione si basa su una **valutazione del rischio**, considerando sia la gravità del potenziale danno, che la probabilità che si verifichi.
## IA *vietate*
Il Regolamento Europeo sull'IA vieta ogni sistema che presenta **rischi inaccettabili** e che quindi ==potrebbe andare contro (anche solo potenzialmente) i diritti fondamentali==:
- **Sistemi che adottano tecniche di controllo subliminali:** questi sistemi agiscono in modo ingannevole senza che la vittima ne sia consapevole, con lo scopo o l'effetto di distorcerne il suo comportamento, pregiudicandone la capacità di prendere decisioni informate.
	- *È importante notare che la distorsione del comportamento deve derivare da fattori interni al sistema di IA e non da fattori esterni non controllabili.*
- **Sistemi che categorizzazione biometrica:** questi sistemi classificano dati biometrici come vulnerabilità dovute a età, disabilità o specifiche condizioni sociali o economiche.
- **Sistemi di controllo e valutazione sociale (*social scoring*):** questi sistemi valutano o classificano le persone fisiche in base al loro comportamento sociale o caratteristiche personali, sfociando in un trattamento sfavorevole
	- *È vietato anche l'uso di sistemi di IA per attività di contrasto che utilizzano la **categorizzazione biometrica**.*

## IA *ad alto rischio*
Un sistema di IA è classificato ad **alto rischio** se potrebbe avere un ==impatto nocivo significativo sulla salute, sicurezza o sui diritti fondamentali delle persone.== Ecco alcuni sistemi IA ad alto rischio:

- **Sistemi di IA nei componenti di sicurezza:** cioè un sistema che controlla un componente di sicurezza di un prodotto regolamentato dalla *normativa di armonizzazione dell'UE*.
	- La *normative di armonizzazione* stabiliscono specifiche tecniche ritenute adatte o sufficienti per conformarsi ai requisiti tecnici previsti dalla legislazione dell'Unione Europea.
- **Sistemi di IA applicate nei settori sensibili:** cioè quei sistemi che comprendono settori quali la biometria, l'istruzione, il lavoro, l'accesso a servizi essenziali, le attività di contrasto, la gestione della migrazione e l'amministrazione della giustizia.
	- *Esempi di questi prodotti includono macchine, giocattoli, ascensori, dispositivi medici, dispositivi di selezione del personale, sistemi impiegati per il contrasto alla criminalità*
### Obblighi dei fornitori
I sistemi di IA ad alto rischio sono soggetti a una valutazione della conformità per verificare il rispetto dei requisiti del Regolamento:
- **Dati di addestramento:** i sistemi di IA devono essere addestrati su dati pertinenti, rappresentativi, esenti da errori e completi. Inoltre devono possedere le proprietà statistiche appropriate per i gruppi di persone sui quali il sistema è destinato ad essere utilizzato.
- **Gestione del rischio:** il regolamento richiede che i modelli di IA siano costantemente e iterativamente valutati al fine di mitigare i potenziali rischi, attraverso aggiornamenti repentini.
	- Il Regolamento prevede un **monitoraggio *ex post*** per assicurare che le autorità pubbliche abbiano il potere di intervenire nel caso in cui un sistema di IA generi rischi o imprevisti.
	- I *fornitori* e *utilizzatori* sono **responsabili** dell'uso e degli impatti di IA ad alto rischio.
- **Trasparenza:** i modelli di IA devono garantire che il processo decisionale, il funzionamento e l'output siano interpretabili e comprensibili dall'utente finale.
- ***Supervisione umana:*** è richiesto il controllo umano durante l'utilizzo di sistemi di IA ad alto rischio, con la possibilità di interrompere il funzionamento in caso di necessità.
- **Registrazione del sistema di IA:** i fornitori dei sistemi di IA hanno l'obbligo di registrare i loro sistemi in una banca dati dell'UE accessibile al pubblico.
	- Inoltre i sistemi devono conservare registrazioni degli eventi generati dai sistemi di IA per tutta la durata del ciclo di sistema.


> [!question] Da chi è effettuata la valutazione?
> Per alcuni sistemi, la valutazione è effettuata dall'**autorità di vigilanza del mercato**, mentre per altri è sufficiente un **controllo interno del fornitore**.

## IA *con rischi specifici*
Il regolamento prevede una deroga per alcuni sistemi di IA che hanno **specifici rischi** in base ai casi d'uso, e che non presentano un rischio significativo di danno per la salute, la sicurezza o i diritti fondamentali delle persone fisiche ma che ==generano contenuti manipolati== come i deep fake, o IA che interagiscono con le persone in modo da non far loro capire che stanno interagendo con un'IA. 
- *Il sistema quindi non deve influenzare «materialmente il risultato del processo decisionale».*
## IA *con rischi limitati o minimi*
Il regolamento definisce IA con **rischi limitati o minimi** per cui il regolamento non prevede una disciplina specifica, ma incoraggia l'adozione di codici di condotta e buone pratiche per garantire un utilizzo etico e affidabile dell'IA.
- *Ad esempio l'IA nei videogiochi o nelle applicazioni di fotoritocco.*

> [!WARNING] AI generativa e rischi sistemici
> I modelli di IA per finalità generali più avanzati possono presentare **rischi sistemici**. Questi rischi si riferiscono a potenziali impatti negativi sulla salute pubblica, la sicurezza, i diritti fondamentali o la società nel suo complesso.
> - I modelli con rischi sistemici sono soggetti a obblighi più rigorosi, come la valutazione e mitigazione dei rischi, il tracciamento degli incidenti e la garanzia di un adeguato livello di cybersicurezza.