---
last modified: 2025, 11, 24 22:11:39
related:
  - '[[Circumscription]]'
tags: [default-logic, logica-primo-ordine, ragionamento-non-monotono]
---
# Definizione di ragionamento non monotono
Il ragionamento non monotono (o per Defaults) è un paradigma inferenziale in cui **l'aggiunta di nuove informazioni a una base di conoscenza può portare alla revoca di conclusioni precedentemente derivate**. Questo lo distingue dal ragionamento deduttivo classico (monotono), dove una conclusione vera rimane tale anche con l'aggiunta di nuove premesse.

In altre parole permette di trarre conclusioni plausibili in assenza di informazioni contrarie. A differenza del ragionamento deduttivo, è non-monotono: nuove informazioni possono annullare conclusioni fatte in precedenza. Le premesse per un default possono derivare da normalità, prototipi, statistiche, mancanza di informazioni contrarie, convenzioni comunicative o persistenza nel tempo.

**Necessità del Ragionamento Non Monotono** La logica del primo ordine (FOL), pur essendo espressiva e rigorosa, presenta dei limiti nell'affrontare la conoscenza comune e l'incertezza. In contesti reali, spesso si traggono conclusioni basate su assunzioni "di default" o sulla "normalità", che possono essere invalidate da nuove evidenze.

- **Generici vs. Universali**: FOL gestisce bene le affermazioni universali (vere per tutti gli elementi di una categoria), ma fatica a esprimere i "generici" (proprietà vere in generale, ma con eccezioni). Ad esempio, dire "tutti gli uccelli volano" è tecnicamente falso in FOL a causa di eccezioni come gli struzzi, ma è un'affermazione generalmente accettata nel senso comune.
- **Conoscenza Incompleta**: La conoscenza nel mondo reale è spesso parziale o incerta. Il ragionamento non monotono permette di fare inferenze plausibili anche in assenza di informazioni complete, ritrattando le conclusioni se emergono dati contrari.
- **Fonti dei Default**: Le assunzioni di default possono derivare da ciò che è normale o tipico, prototipi, statistiche, mancanza di informazioni contrarie, convenzioni comunicative o rappresentative, o persistenza nel tempo.

## Approcci al Ragionamento non monotono

- **[[Closed World Assumption (CWA)]]**: La forma più semplice, assume che tutte le frasi atomiche non dichiarate esplicitamente siano false. Simile alle convenzioni usate in guide aeree, enciclopedie e database. Può portare a inconsistenza in presenza di disgiunzioni positive.
- **Generalized Closed-World Assumption (GCWA)**: Una versione più cauta della CWA, mantiene la consistenza anche con disgiunzioni.
- **[[Circumscription]]**: Minimizza il numero di eccezioni, trattando certe informazioni come "anormali" (predicato `Ab(x)`) e assumendo che le eccezioni siano le più basse possibili. Richiede logica del secondo ordine per la sua formalizzazione. Può essere troppo drastica eliminando classi intere (es. pinguini) se non si distinguono predicati fissi e variabili.
- **Default Logic**: Introduce regole di default ($\alpha : \beta / \delta$) che permettono di concludere $\delta$ se $\alpha$ è vera e non ci sono prove contro $\beta$. Gestisce conflitti tra regole che portano a conclusioni opposte (es. paradosso di Nixon) e può generare più "estensioni" (insiemi di credenze ragionevoli).
- **Autoepistemic Logic**: Introduce un operatore `Bα` ("$\alpha$ è creduto vero") per ragionare sulle credenze e sui default stessi. Definisce "insiemi stabili di credenze" che devono essere chiusi per conseguenza logica e rispettare introspezione positiva e negativa.

A questi si aggiunge l'ereditarietà defeasible, una forma specifica di ragionamento non monotono.

### 1. Closed World Assumption (CWA)

La CWA è la forma più semplice di ragionamento per default.

- **Principio**: Assume che **tutte le frasi atomiche non dichiarate esplicitamente nella base di conoscenza (KB) siano false**. Questo è comune in contesti come enciclopedie, dizionari, mappe e database, dove l'assenza di un'informazione implica la sua falsità.
- **Formalizzazione**: Si estende la KB originale con le negazioni di tutte le frasi atomiche che non possono essere dimostrate vere (`KB+`). Questo rende la `KB+` **completa**, poiché per ogni frase atomica se ne può determinare la verità o la falsità. La valutazione delle query diventa diretta e ricorsiva.
- **Problemi di Consistenza**: La CWA può portare a incoerenze se la KB contiene disgiunzioni positive (es. `p ∨ q`). Assumere la falsità di `p` e `q` contraddirebbe la disgiunzione.
- **Generalized Closed World Assumption (GCWA)**: Una versione più cauta che mantiene la consistenza anche con le disgiunzioni. Un atomo è assunto falso solo se la sua negazione non introduce contraddizioni con altre disgiunzioni implicate dalla KB.
- **Quantificatori e Chiusura del Dominio**: Per gestire frasi con quantificatori (es. `∃x P(x)`), la CWA richiede un'assunzione aggiuntiva: la **Chiusura del Dominio**. Questa postula che gli unici individui esistenti siano quelli esplicitamente nominati nella KB, permettendo di trattare le frasi quantificate come proposizionali.

### 2. Circumscription

La Circumscription, introdotta da John McCarthy, è un approccio più generale e flessibile per gestire le eccezioni.

- **Principio**: Si basa sull'idea di **minimizzare il numero di "eccezioni"** (spesso rappresentate da un predicato `Ab(x)`, per "abnormale"). Si cercano i "modelli più normali" della KB, dove le eccezioni sono le meno possibili. Se una frase non è vera in tutti i modelli, può essere accettata se è vera nei modelli che minimizzano le anomalie.
- **Esempio**: Affermare "tutti gli uccelli normali volano" (`∀x [Bird(x) ∧ ¬Ab(x) ⊃ Flies(x)]`). Se Tweety è un uccello e non si sa che è anormale, si conclude che vola, minimizzando le anomalie. È più prudente della CWA, ma più decisa della GCWA.
- **Formalizzazione**: A differenza della CWA, la circumscription richiede la **logica del secondo ordine**, che permette di quantificare sui predicati (come `Ab`). Si usa un "assioma di circumscription" (`τ`) per selezionare i modelli in cui l'estensione dei predicati da minimizzare è la più piccola possibile.
- **Problemi e Soluzioni**: Può essere troppo drastica ed eliminare intere classi (es. i pinguini, se sono sempre anormali per il volo). La soluzione è distinguere tra **predicati da minimizzare** (es. `Ab`) e **predicati da mantenere fissi** (es. `Penguin`), evitando l'esclusione di categorie reali. Tuttavia, decidere a priori quali predicati fissare o variare rimane complesso.

### 3. Default Logic

La Default Logic, introdotta da Ray Reiter, è un formalismo esplicito per il ragionamento non monotono basato su "regole di default".

- **Regole di Default**: Ogni regola ha tre parti:
    - **Prerequisito (α)**: Condizione che deve essere vera.
    - **Giustificazione (β)**: Ciò che non deve essere contraddetto (deve essere compatibile con le credenze attuali).
    - **Conclusione (δ)**: Ciò che si può concludere se prerequisito e giustificazione sono soddisfatti.
    - Sintassi: `α : β / δ`.
    - **Default Normali**: Quando giustificazione e conclusione coincidono (es. `Bird(x) : Flies(x) / Flies(x)`).
- **Estensioni**: Un'estensione è un insieme coerente di credenze che si possono dedurre da fatti e regole di default. Le regole sono applicabili se il prerequisito è creduto e la negazione della giustificazione non lo è.
- **Conflitti**: Regole di default possono portare a conclusioni opposte, generando **più estensioni valide** (es. paradosso di Nixon).
    - **Ragionamento Scettico**: Accetta solo ciò che è vero in *tutte* le estensioni.
    - **Ragionamento Credulo**: Sceglie *una sola* estensione e ragiona su quella.
- **Problemi e Soluzioni**: Può produrre estensioni inappropriate o nessuna estensione. Le "estensioni fondate" di Reiter mirano a risolvere questi problemi definendo più robustamente il processo di costruzione delle credenze.

### 4. Autoepistemic Logic

L'Autoepistemic Logic è un approccio che permette di ragionare non solo sul mondo, ma anche su ciò che il sistema stesso crede del mondo.

- **Operatore di Credenza**: Introduce il connettivo `Bα`, che significa "α è creduto vero".
- **Regole**: Le regole utilizzano questo operatore, es. `∀x [Bird(x) ∧ ¬B¬Flies(x) ⊃ Flies(x)]` (Ogni uccello di cui non si crede che non voli, vola).
- **Insiemi Stabili di Credenze (Espansioni)**: Un insieme di credenze `E` è stabile se soddisfa tre proprietà:
    1. **Chiusura per conseguenza logica**: Se da `E` si deduce `α`, allora `α` è in `E`.
    2. **Introspezione positiva**: Se `α` è in `E`, allora `Bα` è in `E` (si crede di credere `α`).
    3. **Introspezione negativa**: Se `α` non è in `E`, allora `¬Bα` è in `E` (si crede di non credere `α`).
- **Deducibilità**: Una frase appartiene a un'espansione stabile se è deducibile dalla KB unita alle assunzioni su ciò che è creduto o non creduto (`KB ∪ {Bα | α ∈ E} ∪ {¬Bα | α ∉ E}`).
- **Enumerazione**: Esistono procedure sistematiche per enumerare le espansioni stabili, basate sulla valutazione combinatoria delle formule con l'operatore `B`.

### Ereditarietà Defeasible

L'ereditarietà defeasible è una caratteristica chiave nei sistemi a frame e nelle reti di ereditarietà.

- **Principio**: Permette che le proprietà ereditate da categorie più generali possano essere **ignorate o annullate** da informazioni più specifiche. A differenza dell'ereditarietà rigida (strict inheritance) in cui ogni proprietà lungo un percorso è sempre ereditata, l'ereditarietà defeasible riconosce la possibilità di eccezioni.
- **Conflitti e Strategie**: Il problema sorge quando percorsi diversi portano a conclusioni opposte (es. il paradosso di Nixon: Quaccheri pacifisti vs. Repubblicani non pacifisti). Per risolvere questi conflitti, si usano strategie:
    - **Credulo (Brave)**: Accetta una delle conclusioni possibili, anche arbitrariamente.
    - **Scettico (Cautious)**: Non accetta alcuna conclusione se non è chiaramente supportata e non contraddetta.
    - **Euristica del Percorso Più Corto**: Predilige le conclusioni derivanti da percorsi più brevi nella rete, basandosi sull'idea che l'informazione più specifica è più "diretta". Tuttavia, questa può essere sensibile ad archi ridondanti.
    - **Distanza Inferenzale**: Un'alternativa più robusta che si basa sulla struttura topologica della rete, dando peso alla specificità gerarchica piuttosto che alla mera lunghezza del percorso.
    - **Preemption**: Un'informazione più specifica "blocca" o "annulla" un'informazione più generale che la contraddice lungo un percorso.
- **Percorsi Ammissibili**: Un percorso è ammissibile se i suoi archi sono ammissibili, non ci sono archi ridondanti e nessun nodo intermedio contraddice l'ultima parte del percorso (preemption).
- **Estensioni nell'Ereditarietà Defeasible**: Simili a quelle della Default Logic, sono sotto-reti coerenti, complete e massimali della rete originale. Un'**estensione preferita** è un'estensione credula che in più rispetta le regole di ammissibilità e priorità, escludendo le informazioni superate da fatti più specifici.