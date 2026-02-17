---
last modified: 2025, 11, 24 2:11:01
related:
  - '[[Informatica teorica]]'
tags:
  - logica-proposizionale
  - linguaggio-formale
  - connettivi-logici
---
# Definizione di logica proposizionale
La **Propositional Logic** (**PL** o in italiano **logica proposizionale** oppure **logica enunciativa**) è un linguaggio formale con una struttura sintattica semplice basata su proposizioni elementari (atomiche) e connettivi logici di tipo vero-funzionale, che restituiscono il valore di verità di una proposizione in base al valore di verità delle proposizioni connesse. Vengono concatenate delle proposizioni per ottenerne una nuova, sintatticamente corretta.
# Grammatica PL
L'unità di espressione del linguaggio è la sentenza. Le sentenze sono dei *nomi* in senso astratto dove per *nome* si intende un'espressione linguistica che determina o denota in modo univoco una qualche entità.

**==La Logica intende trattare le sentenze in base alla loro struttura== e non al loro contenuto. Dal punto di vista logico non si è interessati a ciò che la sentenza asserisce** (cioè il suo valore connotazionale), **ma unicamente a ciò che essa denota ed al modo in cui la denotazione di una sentenza composta**, ottenuta da altre più semplici mediante l'uso di connettivi, **dipende dalle denotazioni delle componenti**. 
	**Esempio:** quattro = il quadrato di due = il predecessore di cinque = tre più uno.
	→ Dal punto di vista logico, diremo che sono tutti nomi che denotano il numero quattro.

> [!Esempio]
Immagina di star parlando parlando di puzzle e delle sue parti. In questo caso, il "contenuto" delle frasi sarebbe come appaiono le singole parti del puzzle, mentre la "struttura" sarebbe come queste parti si incastrano l'una con l'altra. Da un punto di vista logico, ciò che ci interessa è come le frasi si collegano tra loro. Non ci concentriamo tanto su cosa stai dicendo in sé, ma su come le tue frasi si combinano logicamente per formare nuove frasi.


==Ogni sentenza denota un valore di verità== ("Vero" o "Falso") ed esprime un *senso* (che tuttavia non è oggetto diretto dell'indagine logica). Il *senso* determina la denotazione, o diremo anche che è un *concetto* della denotazione. Ogni concetto di un valore di verità è detto **proposizione**.
	**Esempi:** quattro è il predecessore di cinque, quattro è quattro.
	→ Cos'hanno in comune le due frasi? Il fatto che entrambe siano **vere**!

> [!nota]
Quando parliamo di "concetto di un valore di verità", ci riferiamo a idee generali che possono essere vere o false, come "Il cielo è blu" o "La Terra è piatta". Queste idee sono chiamate "proposizioni".


Le **proposizioni** possono essere **atomiche** e **composte**:
- *Le proposizioni atomiche* (A, B, C..) sono le più semplici, non possono essere scomposte.
- *Le proposizioni composte* (P, Q, R..) sono costruite a partite da quelle atomiche, mediante l'utilizzo di **connettivi**.

# Connettivi

| Connettivo  | Simbolo |
| ----------- | ----------- |
| "non"| ¬ |
| "e" | ∧ |
| "o" | ∨ |
| "se.. allora" | → |
| "negazione" | ⊥ |

L'operazione espressa dal connettivo "==non==" è chiamata ==negazione== e la proposizione ottenuta dalla sua applicazione è detta **proposizione negata** (della proposizione di partenza).
	**Esempio:** "2 è un numero primo" → La sua negata è "2 *non* è un numero primo".

L'operazione espressa dal connettivo "==e==" viene detta ==congiunzione==.
	**Esempio:** "3 è un numero dispari *ed* è primo" → E' una proposizione composta costruita congiungendo le due proposizioni atomiche "3 è un numero dispari" con "3 è un numero primo".

L'operazione espressa dal connettivo "==o==" è detta ==disgiunzione==.
	**Esempio:** "2 è un numero dispari *o* è primo".

L'operazione espressa dal connettivo "==se.. allora==" viene detta ==implicazione== e la proposizione composta ottenuta dalla sua applicazione è chiamata **proposizione condizionale**.
	**Esempio:** "*se* 3 è dispari *allora* è primo" → La proposizione "3 è dispari" è detta *premessa* (dell'implicazione), mentre "3 è primo" è la sua *conseguenza*.

# Sintassi
Per definire formalmente la logica proposizionale bisogna specificare un **alfabeto** (**cioè i simboli che lo compongono**), quindi le regole che a partire da esso consentono di costruire **frasi sintatticamente corrette**.

Nell'**alfabeto** della logica proposizionale abbiamo:
- **simboli** (P, Q, R..) ➨ che rappresentano *proposizioni*. *Simboli ausiliari "(",")" ;
 - **connettivi** (¬, ∧, ∨, →, ⊥) ➨ corrispondono alle "regole grammaticali" di una lingua. Ci permettono di combinare le preposizioni

- **Regole di Costruzione:**
    - Le regole sono come le regole grammaticali di una lingua. Ad esempio, possiamo combinare le proposizioni usando connettivi logici come AND (∧), OR (∨), e NOT (¬).

    - **Frasi Sintatticamente Corrette:**
    - Seguendo le regole, possiamo costruire frasi logiche in modo corretto. Ad esempio, "P ∧ Q" (P e Q) o "¬Q" (non P) sono frasi sintatticamente corrette.

## Cos'è un FBF?
L'insieme di FBF (Formula Ben Formulata) è il minimo insieme X tale che
1. A, B, … ∈ X per ogni simbolo atomico di proposizione;
2. ⊥ ∈ X.
3. Se P ∈ X, (¬P) ∈ X.
4. Se P, Q ∈ X, (P ∧ Q), (P ∨ Q), (P → Q) ∈ X

> [!nota]
L'insieme FBF è fondamentalmente un set che contiene tutte le frasi atomiche, il simbolo di falso, le negazioni di frasi esistenti e le combinazioni di frasi esistenti usando connettivi logici. È il minimo insieme che soddisfa queste regole di costruzione.