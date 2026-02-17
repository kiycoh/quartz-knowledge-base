---
last modified: 2025, 11, 24 22:11:11
related:
  - '[[Python]]'
tags: [machine-learning, python, random]
---


# Cos'è la libreria Random di Python?
La libreria `random` fornisce diversi metodi per generare numeri casuali o manipolare sequenze in modo casuale.

```python
from random import *
for i in range (10):
	seed(2)
	x=random()
print(x)
```

> [!Note] Seed
> La generazione dei numeri è basata su un "seed", che in Python viene automaticamente generato, ma che può anche essere inserito manualmente.
> 
> Di solito, si fissa il seed una sola volta all'inizio del programma.
> 
> ```python
from random import seed, random
seed(2) # Fissa il seed all'esterno del ciclo per riproducibilità
>for i in range(10):
>	x = random()
>	print(x)
>```
## Metodi

| **Metodo**     | **Descrizione**                                                                          |
| -------------- | ---------------------------------------------------------------------------------------- |
| random()       | Restituisce un numero floating-point compreso tra 0 e 1 (escluso).                       |
| randint(a, b)  | Restituisce un numero intero casuale compreso tra a e b (inclusi).                       |
| choice(seq)    | Restituisce un elemento casuale dalla sequenza specificata.                              |
| shuffle(seq)   | Mescola la sequenza specificata.                                                         |
| sample(seq, k) | Restituisce una lista di k elementi unici scelti casualmente dalla sequenza specificata. |