---
last modified: 2025, 11, 10 18:11:17
tags:
  - python
  - nested-loops
  - programming-concepts
---
# Nested loop
In [[Python]], Un **nested loop (o ciclo annidato)** in programmazione si verifica quando un [[Loop (Python)|ciclo]] è posizionato all'interno di un altro ciclo. Questa [[Struttura dati (Informatica teorica)|struttura]] permette di eseguire iterazioni più complesse e di trattare con dati bidimensionali o strutture più complesse.

```python
for i in range(1, 6):
    for j in range(1, 6):
        print(i * j, end='\t')
    print()
```