---
last modified: 2025, 11, 24 2:11:03
related:
  - '[[Logica proposizionale]]'
tags:
  - logica-primo-ordine
  - logica-classica
  - conoscenza-dichiarativa
---
# Definizione di logica del primo ordine (FOL)
La **First order logic (FOL)** o **Logica di primo ordine** è la forma più comune di [[logica classica]]. È un linguaggio formale inventato da [Gottlob Frege](https://it.wikipedia.org/wiki/Gottlob_Frege) nel XX secolo, indispensabile per esprimere e manipolare la conoscenza in modo rigoroso e non ambiguo. ==L'obiettivo principale della FOL nella KRR è fornire un linguaggio in cui la conoscenza possa essere formulata per essere successivamente manipolata e da cui si possano dedurre nuove informazioni.==
$$
\underbrace{\forall x (\text{Gatto}(x) \supset \text{Mammifero}(x))}_\text{Tutti i gatti sono mammiferi}
$$
> [!WARNING]- *FOL* VS *SOL*
> La sua denominazione "*primo ordine*" deriva dalla capacità dei suoi quantificatori ($\forall$ per "per ogni" e $\exists$ per "esiste") di riferirsi unicamente a individui all'interno di un dominio specifico, e non a predicati o insiemi di individui. 
> Questa è la differenza chiave rispetto alla **[[Logica di secondo ordine (SOL)]]**, che consente la quantificazione anche sui predicati, aumentando l'espressività ma sacrificando proprietà desiderabili come la compattezza e la completezza.
## Sintassi FOL
Definisce le regole che stabiliscono quali combinazioni di simboli sono ben formate (ovvero, grammaticalmente corrette) e quali di esse esprimono proposizioni.
* **Simboli logici:** hanno un significato fisso (es. ¬, ∧, ∨, ⊃, ≡, ∀, ∃, = e variabili come x, y, z).
* **Simboli non logici:** il loro significato dipende dall'applicazione specifica. Questi includono:
	* **Simboli di funzione:** (es. bestFriendOf, fatherOf), scritti in minuscolo e camelCase.
	* **Simboli di predicato:** (es. OlderThan, Person, Company), scritti in maiuscolo e camelCase.
- **Quantificatori:**
    - **Quantificatore universale ($\forall$, "per ogni"):** afferma che una proprietà vale per tutti gli oggetti nel dominio. (es. `∀x Uomo(x) → Mortale(x)` - "Per ogni x, se x è un uomo, allora x è mortale").
    - **Quantificatore esistenziale (`∃`, "esiste"):** afferma che esiste almeno un oggetto nel dominio con una certa proprietà. (es. `∃x Gatto(x) ∧ Nero(x)` - "Esiste un x tale che x è un gatto e x è nero").

> [!NOTE] Tipi di espressioni sintattiche
> Le espressioni sintattiche consentite nella FOL sono di due tipi:
> * **Termini**: Utilizzati per riferirsi a qualcosa nel mondo (es. x, fatherOf(y), bestFriendOf(x)). Un termine è una variabile o un simbolo di funzione applicato a uno o più termini.
> * **Formule**: Utilizzate per esprimere proposizioni. Una formula può essere un predicato applicato a termini (formula atomica), un'uguaglianza tra termini, o la combinazione di formule tramite connettivi logici o quantificatori.
## Semantica FOL
Stabilisce il significato delle espressioni ben formate, specificando quali idee sul mondo esse rappresentano.
## Pragmatica FOL
Spiega come utilizzare le espressioni significative nel contesto di una base di conoscenza per trarre inferenze.
## *Modus ponens*