---
tags:
  - algoritmi-ordinamento
  - matematica
  - insiemi-ordinati
---

# Cos'è un insieme ordinato?
In matematica, un **insieme ordinato** è una coppia formata da un insieme $A$ e una relazione d'ordine su di esso. La relazione d'ordine è una regola che specifica come confrontare due elementi distinti $a$ e $b$ di $A$, determinando se $a$ precede $b$, $b$ precede $a$, oppure se non sono comparabili.

## Proprietà
**1. Riflessività:** Per ogni elemento a di A, si ha a⪯a. In altre parole, ogni elemento è in relazione con se stesso.

**2. Transitività:** Se a⪯b e b⪯c, allora a⪯c. In parole povere, se a precede b e b precede c, allora a deve precedere anche c.

**3. Antisimmetria:** Se a⪯b e b⪯a, allora a=b. Cioè, se a precede b e b precede a, gli elementi a e b devono essere uguali.


## Tipi di insiemi ordinati
**- Insiemi totalmente ordinati:** In questo caso, per ogni coppia di elementi distinti a e b di A, in altre parole, ogni coppia di elementi è comparabile. Esempi di insiemi totalmente ordinati includono i numeri reali con la relazione d'ordine usuale ≤, i numeri interi con ≤, e l'insieme delle lettere dell'alfabeto ordinate alfabeticamente.

**- Insiemi parzialmente ordinati:** In questo caso, è possibile che esistano coppie di elementi distinti a e b di A per cui non vale né a⪯b né b⪯a. In altre parole, alcune coppie di elementi potrebbero non essere comparabili. Un esempio di insieme parzialmente ordinato è l'insieme dei numeri reali con la relazione di divisibilità "è divisibile per".