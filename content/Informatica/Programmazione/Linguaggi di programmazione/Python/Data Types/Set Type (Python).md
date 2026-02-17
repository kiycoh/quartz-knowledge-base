---
last modified: 2024-10-02T03:38:00.000Z
related: '[[Python]]'
tags:
  - machine-learning
  - set-theory
  - python
---


==Un set== ==è una collezione disordinata (non indicizzata) di 0 o più "data objects" immutabili==. **I sets non permettono elementi duplicati**. *Il set vuoto viene invocato come set()*. I set sono eterogenei e possono essere assegnati ad una variabile. **Utili nelle operazioni matematiche**.
	E' possibile accedere agli elementi dell'insieme attraverso un ciclo che itera per l'intero insieme. **E' possibile ordinare un set con la funzione *sorted(set)***
### Operazioni su set
| **Operatore** | **Uso**      | **Spiegazione**                                                            |
| ------------- | ------------ | -------------------------------------------------------------------------- |
| **in**        | x.in(set)    | Assegna appartenenza.                                                      |
| **len**       | len(set)     | Ritorna la cardinalità (la lunghezza) del set.                             |
| \|            | set1 \| set2 | Ritorna un nuovo set con tutti gli elementi dei due.                       |
| &             | set1 & set2  | Ritorna un nuovo set con solo gli elementi in comune tra i due.            |
| -             | set1 - set2  | Ritorna un nuovo set con tutti gli elementi del primo set non nel secondo. |
| <=            | set1 <= set2 | Chiede se tutti gli elementi del primo set sono nel secondo.               |

### Metodi su set
| **Metodo** | **Uso** | **Spiegazione** |
| ---------- | --------- | --------- |
| union | set1.union(set2) | Ritorna un nuovo set con tutti gli elementi tra i due. |
| intersection | set1.intersection(set2) | Ritorna un nuovo set con soli gli elementi in comune tra i due. |
| difference | set1.difference(set2) | Ritorna un nuovo set con tutti gli elementi del primo set non nel secondo. |
| issubset | set1.issubset | Chiede se tutti gli elementi del primo sono nel secondo. |
| add | set.add(item) | Aggiungi elementi al set. |
| remove | set.remove(item) | Rimuove l'oggetto dal set, altrimenti errore. |
| discard | set.discard(item) | Rimuove l'elemento se questo appartiene all'insieme, altrimenti no effetto. |
| pop | set.pop() | Rimuove un elemento arbitrario dal set. |
| clear | set.clear() | Rimuove tutti gli elementi dal set. |
#### Esempi
``` python
>>> my_set = {False, 3, 4.5, 6, 'cat'}
>>> your_set = {99,3,100}
>>> my_set.union(your_set)
{False, 3, 4.5, 6, 99, 'cat', 100}

>>> my_set | your_set
{False, 3, 4.5, 6, 99, 'cat', 100}

>>> my_set.intersection(your_set)
{3}

>>> my_set & your_set
{3}

>>> my_set.difference(your_set)
{False, 4.5, 6, 'cat'}

>>> my_set - your_set
{False, 4.5, 6, 'cat'}

>>> {3,100}.issubset(your_set)
True

>>> {3,100} <= your_set
True

>>> my_set.add("house")
>>> my_set
{False, 3, 4.5, 6, 'house', 'cat'}

>>> my_set.remove(4.5)
>>> my_set
{False, 3, 6, 'house', 'cat'}

>>> my_set.pop()
False

>>> my_set
{3, 6, 'house', 'cat'}

>>> my_set.clear()
>>> my_set
set()
```