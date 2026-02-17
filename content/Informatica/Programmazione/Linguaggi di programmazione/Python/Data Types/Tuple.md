---
tags:
  - algoritmi-ordinamento
  - tuple
  - immutabilita
---

==Una tupla== ==è una sequenza ordinata di "data objects"==, simile a una lista, ma **è immutabile**. Gli elementi all'interno di una tupla sono separati da "," e una volta creata, **non è possibile modificarne il contenuto**. La collezione può essere assegnata ad una variabile.
## Metodi su tuple
|**Nome**|**Uso**|**Spiegazione**|
|---|---|---|
|count|tuple.count(item)|Ritorna il numero di ricorrenze dell'item|
|index|tuple.index(item)|Ritorna l'indice della prima ricorrenza dell'item|
### Esempi
```python
my_tuple = (1024, 3, True, 6.5)
print(my_tuple.count(True))
print(my_tuple.index(3))
```