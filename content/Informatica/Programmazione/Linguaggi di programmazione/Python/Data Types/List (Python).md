---
tags:
  - algoritmi-ordinamento
  - lista
  - programmazione-dinamica
---


==Una lista== ==è una sequenza ordinata di "data objects"==. Gli elementi all'interno di una lista sono separati da "," e **non devono necessariamente appartenere tutti alla stessa classe**. La collezione può essere assegnata ad una variabile.
## Metodi su liste
| **Nome**   | **Uso**               | **Spiegazione**                                           |
| ---------- | --------------------- | --------------------------------------------------------- |
| ==append== | list.append(item)     | Aggiunge l'item alla fine della lista                     |
| clear      | list.clear()          | Rimuove tutti gli elementi dalla lista.                   |
| copy       | list.copy()           | Ritorna una copia della lista.                            |
| count      | list.count(item)      | Ritorna il numero di ricorrenze dell'item                 |
| extend     | list.extend(i)        | Aggiunge l'elemento *i* alla fine della lista.            |
| ==index==  | list.index(item)      | Ritorna l'indice della prima ricorrenza dell'item         |
| insert     | list.insert (i, item) | Inserisce l'item nella lista in posizione *i*             |
| pop        | list.pop()            | Rimuove e ritorna l'ultimo elemento della lista           |
| pop(i)     | list.pop(i)           | Rimuove e ritorna l'elemento della lista in posizione *i* |
| remove     | list.remove(item)     | Rimuove la prima ricorrenza dell'item                     |
| reverse    | list.reverse()        | Inverte la lista                                          |
| ==sort==   | list.sort()           | Ordina la lista                                           |
### Esempi
``` python
my_list = [1024, 3, True, 6.5]
my_list.append(False)
print(my_list)
my_list.insert(2,4.5)
print(my_list)
print(my_list.pop())
print(my_list)
print(my_list.pop(1))
print(my_list)
my_list.pop(2)
print(my_list)
my_list.sort()
print(my_list)
my_list.reverse()
print(my_list)
print(my_list.count(6.5))
print(my_list.index(4.5))
my_list.remove(6.5)
print(my_list)
del my_list[0]
print(my_list)
``` 