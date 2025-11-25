---
last modified: 24/10/2025 14:12
related:
  - '[[Lettura e commenti su IA Act 2024]]'
tags:
  - machine-learning
  - intelligenza-artificiale
  - scienze-cognitive
---
### Garanzie contro la manipolazione dei predittori
**La manipolazione dei dati** non è un problema nuovo, ma nel contesto dell'IA può essere esacerbato, portando a risultati ingiusti. Per questo motivo è necessario introdurre delle garanzie nella progettazione dei sistemi AI4SG. Tali garanzie possono vincolare:
- La selezione degli indicatori da utilizzare nella progettazione.
	- *Gli indicatori non causali non devono distorcere in modo inappropriato gli interventi.*
- La misura in cui gli indicatori modellano gli interventi.
- Il livello di trasparenza del modo in cui gli indicatori influenzano le decisioni.
	- *In caso, limitano la conoscenza di come gli input influenzano gli output.*
==L'obiettivo è quello di prevenire la manipolazione e garantire che gli interventi siano basati su dati affidabili e non distorti.==
### Semantizzazione adatta all'umano
La **semantizzazione** adatta all'umano si concentra sulla necessità di consentire agli esseri umani di curare e promuovere il proprio "capitale semantico". 

> *Il capitale semantico si riferisce a qualsiasi contenuto che può aumentare la capacità di un individuo di dare significato e senso alle cose.* 

Questo concetto è fondamentale per mantenere e promuovere l'autonomia umana.

- **Rischi di automatismi:** Se la semantizzazione fosse delegata interamente all'IA, si corre il rischio che il software definisca il significato in modo divergente dalle nostre scelte. Questo può accadere quando una procedura definisce arbitrariamente i significati.
	- Un esempio che illustra questo rischio è l'utilizzo di software di IA per prevedere il significato giuridico di "violazione" basandosi su casi precedenti: *se il software definisce arbitrariamente il significato, si limita il ruolo dei giudici e della giustizia, impedendo loro di analizzare e ridefinire il significato di "violazione" nell'interpretazione della legge.* L'uso passato non sempre anticipa come semantizzeremmo gli stessi concetti in futuro.
- **Importanza della supervisione umana:** è fondamentale garantire che gli essere umani mantengano un ruolo attivo nella semantizzazione e che l'IA non diventi un ostacolo alla capacità delle persone di dare senso.
	- Questo implica la necessità di un **intervento umano** nel processo decisionale, in modo da interpretare i dati contestualmente e di non lasciare che il sistema di IA definisca autonomamente il significato delle cose. L'uomo partecipa attivamente al funzionamento dell'IA stessa.

==I progettisti di AI4SG non dovrebbero ostacolare la capacità delle persone di semantizzare (cioè di dare significato e conferire senso a) qualcosa.==

# IA e giustizia predittiva
Per **giustizia predittiva** ci si riferisce all'impiego di algoritmi di IA per prevedere il rischio di recidiva, supportare decisioni giudiziarie e valutare le probabilità di esito in procedimenti legali.

- [[Aspetti etici dell'IA#Opacità degli algoritmi|Opacità degli algoritmi]]: è stato sollevato il dubbio se agli imputati debba essere garantito il diritto di sapere se la sentenza si è basata su risultati prodotti da un sistema di IA opaco, e se debba essere data la possibilità di richiedere un processo basato esclusivamente sulle decisioni di esseri umani.
## Nuovo
L'intelligenza artificiale (IA) sta trovando applicazione anche nel sistema giudiziario, in particolare attraverso la **giustizia predittiva**, sollevando questioni complesse relative a equità, trasparenza e responsabilità.

**Applicazioni della Giustizia Predittiva:**

- **Valutazione del rischio di recidiva:** L'IA viene utilizzata per valutare la probabilità che un individuo commetta reati futuri, influenzando decisioni come la scarcerazione anticipata o la concessione della libertà condizionale.
- **Supporto alle decisioni giudiziarie:** I sistemi di IA possono essere impiegati per aiutare i giudici nella ricerca e interpretazione dei fatti e del diritto e nell'applicazione della legge a casi specifici.
- **Analisi delle prove:** L'IA può essere utilizzata per valutare l'affidabilità degli elementi probatori durante le indagini e i procedimenti penali.
- **Identificazione di frodi fiscali**: L'IA viene impiegata per identificare le frodi fiscali

**Rischi e Criticità:**

- **Pregiudizi e discriminazione:** Gli algoritmi di IA possono perpetuare e amplificare i pregiudizi esistenti nei dati di addestramento, portando a decisioni discriminatorie nei confronti di specifici gruppi sociali, etnici o di genere. Ad esempio, i modelli di IA utilizzati nelle udienze per la scarcerazione anticipata hanno dimostrato di essere parziali nei confronti delle minoranze, poiché tendono a riprodurre le disuguaglianze esistenti nel sistema giudiziario.
- **Opacità dei processi decisionali (Black Box):** Molti sistemi di IA operano come "black box", rendendo difficile comprendere come giungano a determinate conclusioni. Questa mancanza di trasparenza solleva preoccupazioni etiche, specialmente quando le decisioni basate sull'IA hanno un impatto significativo sulla vita delle persone.
- **Distorsione dell'automazione:** Esiste il rischio di fare eccessivo affidamento sull'output prodotto da un sistema di IA, senza mantenere un approccio critico.
- **Manipolazione dei dati:** I dati di input possono essere manipolati per ottenere esiti desiderati, compromettendo l'integrità del processo decisionale.
- **Eccessiva dipendenza da indicatori non causali:** L'IA potrebbe basare le sue previsioni su indicatori che non sono causalmente legati all'esito previsto, portando a decisioni errate. Per esempio, l'indirizzo di casa (spesso un proxy per razza ed etnia) o i precedenti penali degli amici potrebbero essere utilizzati come criteri di valutazione del rischio di recidiva, creando circoli viziosi.
- **Mancanza di contestualizzazione:** L'utilizzo di algoritmi sviluppati in un contesto specifico in un ambiente diverso può portare a decisioni imprecise e viziate. Ad esempio, un algoritmo progettato per un ospedale di ricerca potrebbe non essere adatto a una clinica rurale.
- **Soggettività nei dati:** I dati utilizzati per addestrare i modelli di IA sono spesso influenzati da considerazioni personali e soggettive, che possono portare a risultati distorti.

**Requisiti e Tutele:**

- **Trasparenza e spiegabilità:** È fondamentale che i sistemi di IA utilizzati nel sistema giudiziario siano trasparenti e spiegabili, consentendo di comprendere il processo decisionale.
- **Equità e non discriminazione:** I sistemi di IA devono essere progettati e implementati per evitare discriminazioni e garantire pari trattamento a tutti gli individui.
- **Valutazione d'impatto:** Si dovrebbero condurre valutazioni sull'impatto dei sistemi di IA per identificare e mitigare potenziali rischi di discriminazione.
- **Sorveglianza umana:** Le decisioni prese con l'aiuto dell'IA non dovrebbero sostituire il giudizio umano, ma esserne supportate. È necessaria una sorveglianza umana per garantire che le decisioni siano giuste e appropriate.
- **Diritto di contestazione:** Gli individui dovrebbero avere il diritto di sapere se una decisione che li riguarda si è basata su risultati prodotti da un sistema di IA e di richiedere un processo esclusivamente basato su decisioni umane.
- **Qualità e affidabilità dei dati:** Gli algoritmi devono essere addestrati con dati di elevata qualità per evitare risultati errati o ingiusti.
- **Meccanismi di ricorso:** Devono essere previste misure di ricorso efficaci per i casi in cui i sistemi di IA generano risultati ingiusti.

**Regolamentazione:**

- Il **Regolamento Europeo sull'Intelligenza Artificiale (AI Act)** classifica come ad alto rischio i sistemi di IA utilizzati nell'amministrazione della giustizia e nei procedimenti penali. Questi sistemi sono soggetti a requisiti più stringenti in termini di valutazione della conformità, trasparenza e sorveglianza umana.
- Il regolamento vieta l'uso di sistemi di IA per effettuare valutazioni del rischio che si basino unicamente sulla profilazione o sulla valutazione dei tratti della personalità per prevedere la commissione di un reato.
- L'AI Act prevede la creazione di una banca dati dell'UE per i sistemi di IA ad alto rischio.

**Principi Etici:**

- I principi di giustizia ed equità sono fondamentali nell'utilizzo dell'IA nel sistema giudiziario.
- È importante bilanciare la necessità di accuratezza con la necessità di trasparenza e spiegabilità.

In sintesi, l'IA offre opportunità per migliorare l'efficienza e l'obiettività del sistema giudiziario, ma è fondamentale affrontare le sfide etiche e i rischi associati al suo utilizzo. Un quadro normativo solido, insieme a un'attenzione costante ai principi di equità, trasparenza e responsabilità, è essenziale per garantire che l'IA sia utilizzata in modo giusto e a beneficio di tutti.

# IA e protezione dei dati
La protezione dei dati (personali e non) è un aspetto cruciale nello sviluppo e nell'uso responsabile dell'IA, con particolare attenzione alla tutela della privacy e dei diritti fondamentali delle persone.

**Dati Personali e IA:**
- I sistemi di IA si perfezionano continuamente grazie ai dati personali forniti dagli utenti, spesso senza che questi ne siano pienamente consapevoli. Questi dati diventano preziose risorse per le aziende, ma sollevano importanti questioni sulla privacy.
- La raccolta di dati personali, soprattutto nel campo medico o attraverso dispositivi per il fitness, può avvenire in modo non trasparente. È quindi fondamentale garantire che le persone abbiano il controllo sulle proprie informazioni personali.
- Il Regolamento generale sulla protezione dei dati (GDPR) riconosce che i dati personali sono collegati all'identità di una persona e la loro protezione è legata alla dignità umana.
- Il GDPR stabilisce che il trattamento dei dati personali deve essere lecito, corretto e trasparente. I dati devono essere raccolti per finalità specifiche, esplicite e legittime e conservati per un periodo limitato.
- Inoltre, il GDPR disciplina i diritti degli interessati, compresi il diritto di accesso, rettifica, cancellazione, limitazione del trattamento e opposizione.
- Il trattamento di categorie particolari di dati personali, come quelli relativi all'origine razziale, alle opinioni politiche, alle convinzioni religiose, ai dati genetici, biometrici o relativi alla salute, è soggetto a maggiori restrizioni.
- I sistemi di IA che trattano dati biometrici per l'identificazione sono classificati come ad alto rischio e il loro uso è soggetto a specifiche condizioni e garanzie.
- È vietato l'uso di sistemi di IA per la creazione di banche dati di riconoscimento facciale tramite scraping non mirato da internet o da telecamere.
- Anche i sistemi di IA per l'identificazione o l'inferenza delle emozioni sono soggetti a limitazioni, specialmente nei contesti lavorativi e scolastici.
- **La pseudonimizzazione** dei dati personali è incoraggiata come misura per ridurre i rischi per gli interessati.
- Le violazioni dei dati personali devono essere notificate alle autorità di controllo e, in alcuni casi, anche agli interessati.
- I fornitori di sistemi di IA devono adottare misure tecniche e organizzative adeguate per garantire la sicurezza dei dati personali, la protezione fin dalla progettazione e per impostazione predefinita.
- Il trattamento di dati personali a fini di ricerca scientifica o storica o a fini statistici è consentito, ma soggetto a garanzie adeguate.

**Dati Non Personali e IA:**

- L'espansione dell'Internet delle cose e dell'IA genera una grande quantità di dati non personali, come quelli relativi ai processi di produzione industriale, all'agricoltura di precisione o alla manutenzione delle macchine.
- Il regolamento sulla libera circolazione dei dati non personali sancisce il principio della libera circolazione di questi dati all'interno dell'Unione, con alcune limitazioni per motivi di sicurezza pubblica.
- I dati non personali sono definiti come qualsiasi dato diverso dai dati personali.
- Il regolamento si applica alle attività di trattamento dei dati elettronici non personali fornite come servizio agli utenti dell'Unione o effettuate da persone fisiche o giuridiche residenti o stabilite nell'Unione per le proprie esigenze.
- Nel caso di set di dati composti sia da dati personali che non personali, il regolamento si applica alla parte dei dati non personali, mentre per i dati personali si applica il GDPR.
- Il regolamento sulla libera circolazione dei dati non personali non pregiudica il trattamento dei dati effettuato al di fuori del diritto dell'Unione, ad esempio per motivi di sicurezza nazionale.

**Intersezione tra Dati Personali e Non Personali:**

- I progressi tecnologici consentono di trasformare dati anonimizzati in dati personali; in questi casi, si applica il GDPR.
- Il GDPR e il regolamento sulla libera circolazione dei dati non personali forniscono un insieme coerente di norme che disciplinano diversi tipi di dati.
- Il regolamento sull'IA stabilisce che il trattamento dei dati personali deve avvenire nel rispetto dei principi della minimizzazione e della protezione fin dalla progettazione e per impostazione predefinita.

**Sfide e Rischi:**

- I sistemi di IA possono creare profili delle preferenze individuali per influenzare il comportamento delle persone senza il loro consenso.
- C'è il rischio che i sistemi di IA vengano utilizzati per diffondere informazioni inattendibili o per manipolare le persone.
- I sistemi di IA possono essere utilizzati per imitare o alterare l'aspetto, la voce o altre caratteristiche individuali delle persone al fine di danneggiarne la reputazione o manipolare gli altri.
- L'uso di tecniche che catturano l'attenzione o imitano le caratteristiche umane può creare dipendenza e confusione tra IA e persone.
- Le decisioni basate sulla profilazione possono comportare discriminazioni e devono essere soggette a garanzie.
- Le distorsioni nei set di dati possono portare a risultati discriminatori e ingiusti.
- La mancanza di trasparenza e tracciabilità di alcuni algoritmi può rendere difficile l'attribuzione di responsabilità in caso di danni.
- È fondamentale garantire la sicurezza delle reti e dell'informazione per prevenire l'accesso non autorizzato ai dati.

In sintesi, la protezione dei dati, sia personali che non personali, è un elemento essenziale per lo sviluppo e l'uso responsabile dell'IA. È necessario garantire che le persone abbiano il controllo sulle proprie informazioni, che i dati siano trattati in modo lecito e trasparente e che i sistemi di IA siano progettati per evitare discriminazioni e altri rischi per i diritti fondamentali. Le normative europee, come il GDPR, il regolamento sulla libera circolazione dei dati non personali e il regolamento sull'IA, forniscono un quadro di riferimento per affrontare queste sfide.

### Tutela della privacy e consenso dell'interessato
La privacy è riconosciuta come un diritto fondamentale e una **condizione necessaria per la dignità umana**. 
- **Importanza della privacy:** le informazioni personali sono considerate elementi costitutivi di un individuo, e la sottrazione di dati senza consenso può costituire una violazione della dignità umana. La protezione della privacy è essenziale per la sicurezza e la coesione sociale.
	- *Il trattamento dei dati personali deve avvenire nel rispetto della normativa sulla protezione dei dati personali e con il consenso libero, specifico, informato e inequivocabile dell'interessato.*
- **Privacy come condizione per l'autonomia:** la privacy permette alle persone di agire diversamente da quanto previsto dalle norme sociali senza subire danni.
- **Impatto delle tecnologie digitali:** le prime ondate di tecnologia digitale hanno già avuto un notevole impatto sulla privacy, e la centralità dei dati personali in molte applicazioni di IA (e di AI4SG) ne accresce il significato etico. L'incapacità di cogliere gli effetti involontari del trattamento e della commercializzazione di massa dei dati personali è un problema noto.
	- *La sicurezza delle persone può essere compromessa quando uno Stato o un attore malintenzionato ottiene il controllo sugli individui tramite violazioni della privacy.*
- **Principi del GDPR:** il Regolamento generale sulla protezione dei dati (GDPR) stabilisce che il trattamento dei dati personali deve basarsi sul consenso dell'interessato o su altra base legittima prevista per legge. 
	- Il titolare del trattamento deve essere in grado di dimostrare che l'interessato ha acconsentito al trattamento dei dati.
	- Il consenso deve essere espresso liberamente e l'interessato deve essere informato sull'identità del titolare del trattamento, sulle finalità del trattamento e sulle conseguenze della mancata comunicazione dei dati. 
	- L'interessato ha il diritto di accedere ai dati personali che lo riguardano, di chiederne la rettifica o la cancellazione, e di opporsi al trattamento. Il titolare del trattamento deve garantire un'adeguata sicurezza dei dati personali.

==L'[[Aspetti etici dell'IA#AI for Social Good (*AI4SG*)|AI4SG]] deve operare nel rispetto dei principi etici e dei diritti fondamentali, garantendo la trasparenza e la responsabilità nell'utilizzo dei dati personali.==

> [!NOTE] Tipologie di consenso
> Il consenso dovrebbe essere espresso tramite un atto positivo inequivocabile. Il silenzio, l'inattività o la preselezione di caselle non dovrebbero essere considerati come consenso. Il livello o il tipo di consenso richiesto può variare in base al contesto:
> - In ambito sanitario, può essere adottata una soglia di **consenso presunto**, dove segnalare un problema medico costituisce un presunto consenso da parte del paziente.
> - In altre circostanze, una soglia di **consenso informato** è più appropriata. Il consenso informato richiede che i ricercatori ottengano il consenso specifico del paziente prima di utilizzare i suoi dati per uno scopo non autorizzato.
> - Una soglia di **consenso esplicito** può essere usata per il trattamento generale dei dati medici, senza la necessità di informare il paziente su tutte le possibili modalità di utilizzo dei suoi dati.
> - Il **consenso dinamico** è un'alternativa che permette agli individui di monitorare e regolare le proprie preferenze sulla privacy a livello granulare.
# IA e responsabilità civile
L'intelligenza artificiale (IA) e la responsabilità civile sono temi complessi e in rapida evoluzione, con implicazioni significative per la tutela dei diritti dei cittadini e la corretta allocazione dei rischi. Le fonti affrontano diverse sfaccettature di questa relazione, tra cui la responsabilità da prodotto difettoso, la responsabilità "da algoritmo" e la responsabilità medica.

**Responsabilità da prodotto difettoso e IA:**

- La **direttiva europea sulla responsabilità da prodotti difettosi** è stata aggiornata per includere i software, compresi quelli integrati in altri beni mobili o immobili. Questo significa che l'IA, in quanto software, rientra nell'ambito di applicazione della direttiva.
- La direttiva si applica a tutti i beni mobili, incluse le materie prime come gas e acqua, e l'elettricità. I **file per la fabbricazione digitale**, come quelli per la stampa 3D, sono considerati prodotti.
- I **servizi digitali integrati o interconnessi** con un prodotto sono considerati componenti del prodotto se sono sotto il controllo del fabbricante. Ad esempio, i servizi di monitoraggio della salute o i sistemi di navigazione rientrano in questa categoria.
- Un prodotto può essere considerato difettoso anche a causa della sua **vulnerabilità in termini di cibersicurezza**.
- Il fabbricante è responsabile dei **difetti sopravvenuti** dopo l'immissione sul mercato causati dal software o dai servizi correlati di cui ha il controllo. Questo include aggiornamenti, migliorie e algoritmi di apprendimento automatico.
- La **responsabilità è oggettiva**, il che significa che il fabbricante risponde del danno anche in assenza di colpa.
- Il fabbricante può essere **esonerato dalla responsabilità** se prova che il difetto non esisteva al momento dell'immissione sul mercato, che il difetto è dovuto a cause esterne o che lo stato delle conoscenze scientifiche e tecniche non permetteva di scoprire il difetto.
- In caso di **pluralità di soggetti responsabili**, tutti sono responsabili in solido. Il danneggiato può chiedere il risarcimento sia al fabbricante del prodotto finale che a quello del componente difettoso.
- La direttiva mira a tutelare le persone fisiche nei loro **interessi privati**, ma riconosce la necessità di risarcire i danni causati ai beni ad "uso misto" (personale e professionale).
- Il risarcimento copre sia le **perdite materiali** che **immateriali**, incluse quelle derivanti da danno psicologico se riconosciuto dal punto di vista medico.
- La direttiva stabilisce un sistema di **presunzioni a favore del danneggiato**, in particolare quando vi siano complessità tecniche o scientifiche che rendono difficile provare il difetto o il nesso di causalità.

**Responsabilità "da algoritmo" e IA:**

- La crescente **opacità** di alcuni algoritmi di IA rende difficile individuare le cause di un danno e attribuire la responsabilità.
- I sistemi di IA possono causare danni non intenzionali a causa di errori di programmazione, dati di addestramento distorti o comportamenti imprevisti.
- L'**autonomia** dell'IA pone nuove sfide per i modelli di responsabilità esistenti. Chi è responsabile se un'IA causa un danno? Il programmatore, l'utente, il fornitore, o l'IA stessa?.
- È necessario stabilire linee guida chiare sulla responsabilità professionale per chi utilizza sistemi di IA.
- È importante distinguere tra la responsabilità causale (l'IA è la causa del danno) e la responsabilità morale (chi deve rispondere del danno).
- L'approccio della **responsabilità oggettiva**, senza colpa, può essere una soluzione per i danni causati dall'IA, specialmente in caso di azioni morali distribuite.
- La responsabilità può essere distribuita tra tutti gli agenti (umani) coinvolti, come ingegneri, utenti e fornitori.
- Sono stati proposti diversi modelli di responsabilità, tra cui la responsabilità diretta (attribuita all'IA stessa), la perpetrazione per mezzo di altri, la responsabilità di comando e la responsabilità per conseguenza naturale e probabile.
- Il modello di responsabilità per **conseguenza naturale e probabile** si applica quando uno sviluppatore o un utente non intendono né hanno conoscenza a priori di un reato, ma il danno è una conseguenza naturale della loro condotta negligente.
- L'importanza della **tracciabilità** delle decisioni dell'IA è cruciale per la responsabilità morale.
- L'**elusione dell'etica** è un problema quando gli agenti umani cercano di trasferire la responsabilità altrove, ad esempio all'IA.
- La **mancanza di controllo** sui sistemi di IA può rendere difficile prevenire o intervenire in caso di danni.
- È necessario un sistema di **riparazione o compensazione** per gli errori o i torti causati dall'IA.
- Potrebbe essere utile l'istituzione di un "difensore civico dell'IA".
- Le aziende dovrebbero essere **responsabili della qualità e della sicurezza** della tecnologia che creano.

**Responsabilità medica e IA:**

- L'uso dell'IA in ambito medico solleva interrogativi sulla responsabilità professionale dei medici che si affidano a tali tecnologie.
- Se un'analisi effettuata da un'IA si rivela errata, i medici che utilizzano la tecnologia saranno comunque personalmente responsabili della decisione presa?.
- Oppure, la responsabilità sarà dei costruttori della macchina o degli sviluppatori del software?.
- Si pone anche il problema di come valutare la responsabilità di un medico che decide di discostarsi dalla raccomandazione di una macchina.
- I sistemi sanitari che utilizzano l'IA devono tenere conto dell'importanza delle relazioni del paziente con familiari e personale sanitario.
- È necessario che i sistemi diagnostici e di supporto alle decisioni siano affidabili e accurati.

**Regolamentazione e AI Act:**

- Il **regolamento europeo sull'IA (AI Act)** stabilisce un quadro giuridico uniforme per lo sviluppo, la commercializzazione e l'uso dei sistemi di IA.
- L'AI Act adotta un **approccio basato sul rischio**, classificando i sistemi di IA in base al potenziale danno che possono causare.
- I sistemi di IA ad **alto rischio** sono soggetti a requisiti più stringenti, inclusa la valutazione della conformità, la tracciabilità e la supervisione umana.
- L'AI Act prevede **divieti** per alcune pratiche di IA considerate incompatibili con i diritti fondamentali, come la manipolazione subliminale e il social scoring.
- L'AI Act introduce obblighi per i **fornitori** di sistemi di IA, inclusa la valutazione dei rischi e l'implementazione di misure di sicurezza.
- Anche i **deployer** (utenti) dei sistemi di IA ad alto rischio hanno obblighi, tra cui la sorveglianza umana e la valutazione d'impatto sui diritti fondamentali.
- Il regolamento promuove una cultura della **responsabilità** e dell'etica nell'IA, garantendo che le persone si sentano responsabili della qualità e della sicurezza della tecnologia.

**Principi etici e responsabilità:**

- I principi etici dell'IA includono **l'intervento e la sorveglianza umana**, la **robustezza tecnica e la sicurezza**, la **privacy e la governance dei dati**, la **trasparenza**, la **diversità e la non discriminazione**, il **benessere sociale e ambientale**, e la **responsabilità**.
- La **replicabilità**, intesa sia come intelligibilità che come responsabilità, è un principio fondamentale per garantire l'affidabilità dell'IA.
- La responsabilità dovrebbe essere distribuita, e il principio della responsabilità oggettiva può essere applicato ai casi di azioni morali distribuite.
- La mancanza di una chiara allocazione di responsabilità è un problema, e si dovrebbe evitare che la responsabilità venga trasferita altrove.

In conclusione, la responsabilità civile nell'era dell'IA è un tema complesso che richiede un approccio multidisciplinare e una costante attenzione all'evoluzione tecnologica. Le normative, come la direttiva sulla responsabilità da prodotti difettosi e l'AI Act, offrono un quadro di riferimento per affrontare le sfide poste dall'IA, ma è fondamentale promuovere una cultura della responsabilità e dell'etica che coinvolga tutti gli attori in gioco, dai produttori ai consumatori.

# IA e procedimento amministrativo
L'intelligenza artificiale (IA) sta diventando sempre più rilevante nel contesto del procedimento amministrativo, offrendo opportunità per migliorare l'efficienza e l'efficacia, ma sollevando anche importanti questioni etiche e giuridiche. Le fonti forniscono diverse prospettive su come l'IA può essere applicata nel procedimento amministrativo e quali sono le implicazioni in termini di governance, responsabilità e diritti dei cittadini.

**Applicazioni dell'IA nel Procedimento Amministrativo:**

- L'IA può essere utilizzata per **ottimizzare la gestione delle risorse** e **semplificare i compiti logistici** all'interno delle amministrazioni sanitarie. Ciò potrebbe includere l'ottimizzazione della catena di fornitura medica o l'allocazione di risorse scarse.
- I sistemi di IA possono essere impiegati per **automatizzare** e **efficientare i processi amministrativi**, migliorando la qualità dei servizi offerti ai cittadini.
- L'IA può supportare la **pianificazione strategica** e la **presa di decisioni** all'interno della pubblica amministrazione.
- L'IA può essere utilizzata per la **verifica della conformità degli atti e delle decisioni amministrative** alle leggi e ai regolamenti. Può anche fornire **feedback** e **raccomandazioni automatizzate** durante la redazione degli atti.
- Piattaforme per la **digitalizzazione** e **annotazione automatica** di documenti possono essere implementate per migliorare l'efficienza del procedimento amministrativo.
- L'IA può fornire **supporto ai Responsabili Unici del Procedimento (RUP)** per la gestione e il monitoraggio dei contratti pubblici.
- I sistemi di IA possono essere utilizzati per **semplificare l'accesso ai servizi pubblici** per i cittadini e le imprese.
- In generale, l'obiettivo è di **automatizzare ed efficientare i processi** e di **supportare la pianificazione strategica**.

**Governance e Regolamentazione:**

- È necessario definire un **modello quadro di governance** con processi e routine ad hoc per la supervisione dei programmi legati all'etica dell'IA nel contesto amministrativo.
- Le **valutazioni** dei progetti basati sull'IA devono estendersi a tutto il loro ciclo di vita.
- È essenziale istituire un **comitato etico dell'IA** per valutare i progetti e la loro attuazione rispetto ai principi fondamentali.
- Il **regolamento europeo sull'IA (AI Act)** classifica i sistemi di IA in base al loro rischio. I sistemi ad alto rischio, che potrebbero includere applicazioni nel procedimento amministrativo, sono soggetti a requisiti più stringenti in termini di valutazione della conformità, tracciabilità e sorveglianza umana.
- I **fornitori** di sistemi di IA sono responsabili della conformità al regolamento, anche nella fase post-commercializzazione. Sono tenuti ad istituire un **sistema di gestione della qualità** e un **sistema di gestione dei rischi**.
- Gli **enti pubblici** che utilizzano sistemi di IA ad alto rischio devono adottare e attuare regole per il sistema di gestione della qualità, tenendo conto delle specificità del settore.
- Anche gli **utenti** dei sistemi di IA ad alto rischio, o "deployer", hanno obblighi, tra cui la sorveglianza umana e la valutazione d'impatto sui diritti fondamentali.
- L'AI Act prevede la creazione di una **banca dati dell'UE** per i sistemi di IA ad alto rischio.
- **Autorità di vigilanza del mercato** a livello nazionale sono responsabili del controllo dell'applicazione del regolamento.
- Il **Consiglio per l'IA** ha il compito di promuovere la cooperazione tra gli Stati membri, mentre l'**Ufficio per l'IA** ha competenze esclusive per la vigilanza e l'esecuzione delle norme relative ai modelli di IA per finalità generali.
- La **Commissione Europea** può adottare atti di esecuzione per specificare le modalità di attuazione del regolamento.
- È fondamentale garantire che l'uso dell'IA nel procedimento amministrativo sia conforme al **regolamento generale sulla protezione dei dati (GDPR)**.
- Il **GDPR** definisce i principi relativi al trattamento dei dati personali, incluso il diritto alla trasparenza, alla rettifica dei dati e alla cancellazione dei dati.

**Sfide e Considerazioni Etiche:**

- È cruciale garantire **trasparenza** e **tracciabilità** dei processi decisionali supportati dall'IA.
- La **responsabilità** per le decisioni prese con l'aiuto dell'IA deve essere chiaramente definita.
- I sistemi di IA devono essere sviluppati e implementati tenendo conto dei principi di **equità** e **non discriminazione**.
- È necessario evitare che l'IA agisca come un "moltiplicatore delle disuguaglianze".
- Le autorità pubbliche devono assicurare che le tecnologie IA siano progettate in modo da **proteggere i diritti fondamentali** dei cittadini.
- L'IA per l'amministrazione della giustizia dovrebbe essere **a supporto del potere decisionale dei giudici, ma non sostituirlo**.
- L'implementazione dell'IA nella pubblica amministrazione richiede **competenze** adeguate e formazione del personale.

**Strategie Nazionali:**

- L'Italia ha definito una "Strategia Italiana per l'Intelligenza Artificiale 2024-2026" con l'obiettivo di rendere più efficienti i processi amministrativi e migliorare la qualità dei servizi offerti ai cittadini.
- La strategia prevede azioni per la **formazione**, la **ricerca**, la **pubblica amministrazione** e le **imprese**.
- È prevista la creazione di una **Fondazione per l'Intelligenza Artificiale** per coordinare e monitorare l'attuazione delle azioni strategiche.
- Vengono definiti **obiettivi** e **azioni strategiche** specifici per la pubblica amministrazione, tra cui l'adozione di linee guida e lo sviluppo di applicazioni di IA.
- Si prevede l'istituzione di un **Dipartimento dedicato all'Intelligenza Artificiale** presso la Scuola Nazionale dell'Amministrazione per la formazione del personale pubblico.
- L'Italia dovrà definire un **'agenzia di vigilanza'** per l'implementazione della normativa sull'IA.

In sintesi, l'IA offre grandi potenzialità per migliorare il procedimento amministrativo, ma richiede un approccio regolamentato e responsabile, che tenga conto dei rischi, dei diritti dei cittadini e della necessità di trasparenza ed equità. Le istituzioni, sia a livello europeo che nazionale, stanno lavorando per creare un quadro normativo e strategico che possa guidare l'adozione dell'IA nella pubblica amministrazione in modo efficace ed etico.
