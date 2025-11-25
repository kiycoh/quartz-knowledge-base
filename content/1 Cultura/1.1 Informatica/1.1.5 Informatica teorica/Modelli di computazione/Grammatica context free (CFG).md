---
tags:
  - machine-learning
  - formal-grammar
  - context-free-grammar
---

*Pagina 64 Sipser PDF*.

> [!Info] Definizione informale CFG
Una grammatica context-free (CFG) è un tipo di formalismo che definisce la struttura di un linguaggio. Questo tipo di grammatica è "context-free" perché la struttura delle frasi o delle espressioni nel linguaggio può essere definita senza dover considerare il contesto circostante.
>
Questa è una grammatica libera dal contesto che chiamo $G1$:
> $A → 0A1$
>  $A → B$
>  $B → \#$
>  
>- Le variabili sono $A$ e $B$;
>- $A$ è la variabile iniziale;
>- i suoi terminali sono 0, 1 e #.

**Ogni linguaggio regolare è context-free:
![[Pasted image 20231016171537.png]]
## Definizione formale
Una **grammatica context-free (CFG)** è una quadrupla formata da:

1. Un insieme finito di simboli non terminali (o variabili), solitamente rappresentati con lettere maiuscole come A, B, S, etc.2c
<br>
2. Un insieme finito di simboli terminali, che rappresentano gli elementi del linguaggio che possono apparire nelle stringhe generate dalla grammatica. I terminali sono spesso rappresentati da lettere minuscole o altri caratteri.
<br>
3. Un insieme finito di regole di produzione, ciascuna delle quali definisce come sostituire un simbolo non terminale con una sequenza di simboli terminali e/o non terminali.
<br>
4. Un simbolo non terminale designato come simbolo iniziale, che rappresenta il punto di partenza per la generazione delle stringhe del linguaggio.
<br>

In modo formale, una CFG può essere rappresentata come:

$$G=(V,Σ,P,S)$$

Dove:

- $V$ è l'insieme delle variabili.
- $Σ$ è l'insieme dei simboli terminali.
- $P$ è l'insieme delle regole di produzione, ciascuna delle quali ha la forma $A→α$, dove $A$ è una variabile e $α$ è una sequenza di simboli terminali e/o variabili.
- $S$ è il simbolo non terminale iniziale.

Una grammatica context-free definisce un linguaggio attraverso le stringhe che possono essere generate seguendo le regole di produzione dalla variabile iniziale $S$.
## Componenti di una CFG
1. **Variabili:**
	- I simboli non terminali sono categorie grammaticali che rappresentano parti di una struttura grammaticale più complessa. Sono solitamente denotati da lettere maiuscole come A, B, S, E, etc.
	- Nei linguaggi di programmazione, i simboli non terminali possono rappresentare tipi di dichiarazioni, espressioni, o altre costruzioni sintattiche.
<br>
2. **Simboli terminali:**
	- I simboli terminali sono gli elementi effettivi del linguaggio. Sono i simboli che appaiono nel testo del programma o nell'input.
	- Nei linguaggi di programmazione, i simboli terminali possono essere parole chiave, operatori, identificatori, numeri, ecc.
<br>
3. **Produzioni (regole di sostituzione):**
	- Le produzioni definiscono come i simboli non terminali possono essere espansi o sostituiti da combinazioni di simboli terminali e/o non terminali.
	- Una produzione ha la forma $A -> β$, dove A è un simbolo non terminale e β è una sequenza di simboli terminali e/o non terminali.
	- Ad esempio, se abbiamo la produzione A -> "xyz", significa che il simbolo non terminale A può essere sostituito dalla sequenza di simboli terminali "xyz"
<br>
4. **Variabile Iniziale:**
    - Il simbolo iniziale è il punto di partenza della derivazione. Tutto il processo di derivazione inizia con questo simbolo.
    - Solitamente è un simbolo non terminale.

## Processo di derivazione (da rivedere)
Una grammatica può essere utilizzata per generare ogni stringa di un linguaggio seguendo il processo di derivazione. Il processo di derivazione inizia con il simbolo iniziale della grammatica e utilizza le regole di produzione per espandere gradualmente i simboli non terminali fino a ottenere una stringa composta solo da simboli terminali.

1. **Inizia con il Simbolo Iniziale:**
    - Il processo inizia con il simbolo iniziale della grammatica.
2. **Applica le Regole di Produzione:**
    - Sostituisci uno dei simboli non terminali nella stringa corrente con il lato destro di una delle regole di produzione associato a quel simbolo non terminale.
    - Può esserci più di una regola di produzione per un dato simbolo non terminale, quindi devi fare una scelta su quale regola applicare.
3. **Itera il Processo:**
    - Continua a iterare il processo, sostituendo i simboli non terminali con i loro corrispondenti lati destri delle regole di produzione fino a quando non ottieni una stringa composta solo da simboli terminali.
4. **Termina quando raggiungi una Stringa Terminale:**
    - Il processo termina quando tutti i simboli non terminali sono stati sostituiti da simboli terminali, ottenendo così una stringa del linguaggio

## Forma normale di Chomsky
La **Forma Normale di Chomsky** è una forma particolare che una grammatica context-free (CFG) può assumere. In questa forma, ogni regola di produzione ha una struttura specifica e semplifica l'analisi sintattica delle stringhe nel linguaggio.

- **Regole di Produzione:**
    - Ogni regola di produzione nella forma normale di Chomsky ha una delle seguenti forme:
        - A -> BC (dove A, B e C sono variabili)
        - A -> a (dove A è una variabile e "a" è un simbolo terminale)
<br>
- **Eliminazione delle ε-produzioni:**
    - Le produzioni di forma A -> ε (dove ε rappresenta la stringa vuota) sono eliminate o gestite in modo speciale.
<br>
- **Eliminazione delle Unit Productions:**
    - Le produzioni di forma A -> B (dove A e B sono variabili) vengono eliminate o gestite in modo specifico.
<br>
- **Ogni variabile genera qualcosa:**
    - Ogni variabile nella grammatica può generare qualcosa (ad eccezione di ε).
<br>
## Pumping Lemma per CFG
[[Automa finito deterministico (DFA)#⛽ Pumping Lemma*]]
E' una versione generalizzata del pumping lemma per linguaggi regolari, utilizzato per capire se un linguaggio non è context-free.