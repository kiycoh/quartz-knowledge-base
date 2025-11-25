---
last modified: 2025-09-30T12:02:00.000Z
related:
  - '[[Automi finiti non deterministici (NFA)]]'
  - '[[Algoritmo (Informatica)]]'
tags:
  - informatica-teorica
  - automi-finiti-non-deterministici
  - algoritmi-ordinamento
---
# Definizione di Automi finiti non deterministici
In [[informatica teorica]] gli **automi a stati finiti non deterministici** (o DFA) sono modelli di automi che soddisfano la condizione di non determinismo, cioè per ogni coppia di stato e simbolo in ingresso, esistono più transizioni possibili allo stato successivo. 

 
> ![[2.1 Automi a stati finiti_image_3.png|center]]
> *Può essere immaginato come un albero di possibilità* dove la radice dell'albero corrisponde all'inizio della computazione e ad ogni punto di ramificazione corrisponde a un punto nella computazione.
## Definizione formale
Un NFA è definito formalmente come una quintupla $N=(Q,Σ,δ,q0,F)$, dove:
1. $Q$ è l'insieme finito degli stati dell'automa.
2. $Σ$ è l'alfabeto finito di simboli di input.
3. $δ:Q×(Σ∪{ε})→P(Q)$ è la funzione di transizione, dove $P(Q)$ è l'insieme delle parti di $Q$. In altre parole, $δ$ mappa coppie di uno stato e un simbolo di input o la stringa vuota ($ε$) a un insieme di possibili stati successivi.
4. $q0$ è lo stato iniziale dell'automa, $q0∈Q$.
5. $F$ è l'insieme degli stati accettanti o finali dell'automa, $F⊆Q$.

Ogni transizione $δ(q,a)$ è un insieme di possibili stati successivi quando l'automa si trova nello stato $q$ e legge il simbolo a, dove a può essere un simbolo dell'alfabeto di input $o$ la stringa vuota ($ε$).

### Come funziona?

![[2.1 Automi a stati finiti_image_4.png|center]]

1. L'automa riceve i simboli della stringa di input uno alla volta.
2. Per ogni simbolo letto, l'automa può transire da uno stato all'altro seguendo tutte le possibili transizioni indicate dalla funzione di transizione.
3. Se alla fine dell'input l'automa si trova in almeno uno degli stati accettanti, la stringa è accettata; altrimenti, è rifiutata.

**La chiave del non determinismo sta nel fatto che più transizioni possono essere possibili per una stessa combinazione di stato e simbolo di input**, l'automa esplora tutte queste possibilità in parallelo.

>[!Note] Non determinismo
>Il **non determinismo** può essere visto come una specie di computazione parallela dove "processi" multipli indipendenti possono essere eseguiti contemporaneamente: **esistono diverse scelte per lo stato successivo in ogni punto**.
## Automi finiti non deterministici generalizzati
Sono **automi finiti non deterministici** quando gli archi delle transizioni possono avere espressioni regolari come etichette, invece che solo elementi dell'alfabeto o "insieme vuoto". Il GNFA legge blocchi di simboli dall'input e non necessariamente solo un simbolo alla volta come negli NFA.

![[2.1 Automi a stati finiti_image_5.png|center]]
