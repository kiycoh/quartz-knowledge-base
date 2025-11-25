---
last modified: 2025, 11, 24 2:11:08
tags:
  - algoritmi-ordinamento
  - linguaggi-context-free
  - grammatica-context-free
---



[[Automa finito deterministico (DFA)]], [[Automa finito deterministico (DFA)]]
# Linguaggi context-free

*…o CFL, è un metodo più potente per descrivere linguaggi.*

*Es. 1: grammatica context-free che genera a^n U b^n*
$$ A \implies 0A1 $$
$$ A \implies B $$
$$ A \implies \# $$
*Questo è un c.d. albero di derivazione*

## Cos'è una grammatica?

Una grammatica consiste di un insieme di **regole di sostituzione**, anche chiamate produzioni. Ogni regola appare come una linea nella grammatica, costituita da un simbolo e una stringa separati da una freccia. Il simbolo è chiamato variabile, La stringa consiste di variabili e altri simboli chiamati **terminali**.

Ci sono dei linguaggi che possono essere espressi semplicemente dal punto di vista linguistico ma non possono essere riconosciuti dagli **automi finiti deterministici** o dagli **automi finiti non deterministici**.

*Es. 2: grammatica context-free che descrive un frammento della lingua inglese, permette di generare parole grammaticalmente corrette*
![[Linguaggi context-free_image_1.png]]

## Definizione formale di grammatica context-free

![[Linguaggi context-free_image_2.png]]

*Hint: I compilatori funzionano con grammatica context-free (Python ti aiuta nella sintassi ma non nell'espressione dell'algoritmo). Un compilatore traduce il codice scritto in un linguaggio di programmazione in un'altra forma. Per farlo il compilatore estrae il significato del codice da compilare in un processo chiamato **parsing**.

Dal DFA è facile costruire una grammatica context-free che genera un linguaggio regolare.

![[Linguaggi context-free_image_3.png]]
## Concetto di ambiguità
La grammatica può generare la stessa stringa in più modi diversi. Ciò significa che la stessa stringa può essere generata da più alberi (processi ad albero) diversi.

Una grammatica non ambigua corrisponde ad un albero sintattico unico.
**Attenzione!** Un linguaggio è context free se e solo se…

## Pumping lemma per i linguaggi context-free

