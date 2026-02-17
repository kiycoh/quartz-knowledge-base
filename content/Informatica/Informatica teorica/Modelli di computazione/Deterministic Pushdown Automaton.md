---
tags:
  - algoritmi-ordinamento
  - automi-finiti-deterministici
  - linguaggi-context-free
last modified: 2025, 11, 25 18:11:26
---

[[Automa finito deterministico (DFA)]] [[Linguaggi context-free]]

*Pagina 114 dal Sipser (70 in PDF)*

*...anche chiamato PDA è un modello computazionale (pushdown automata).*



## Definizione formale di automa a pila
[[Terminologia, notazione matematica, grafi, logica Booleana, stringhe e linguaggi]]

![[Automi a pila - DPDA_image_1.png]]


*Esempio 1 che riconosce il linguaggio:* ![[Automi a pila - DPDA_image_2.png]]

![[Automi a pila - DPDA_image_3.png]]

- La strada sopra si ferma in q4 se ha tante a quante sono le b.
- La strada sotto ha letto una serie di b, ma ogni volta che la legge va in q6 perché potrebbe aver finito di leggere le b. Ogni volta che tolgo una c tolgo un simbolo, rimango in q6 ma vado anche in q7. Si ferma in q7 se ha trovato tante a quante sono le c.


*Esempio 2 che riconosce il linguaggio*:
![[Automi a pila - DPDA_image_4.png]]  *con w^r = w scritta al contrario*

![[Automi a pila - DPDA_image_5.png]]

[[Automa finito deterministico (DFA)]]
