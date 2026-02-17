---
last modified: 2024-08-11T19:09:00.000Z
tags:
  - machine-learning
  - numpy
  - indexing-slicing
---

| Codice         | Descrizione                                                                                 |
| -------------- | ------------------------------------------------------------------------------------------- |
| `array[n]`     | Seleziona l'elemento nell'array alla posizione n. Il primo elemento è in posizione `a[0]`   |
| `a[-n]`        | Seleziona l'ennesimo elemento dalla fine dell'array                                         |
| `array[n,m]`   | Seleziona gli elementi nell'array a partire da `n` fino a `m`-1                             |
| `array[:]`     | Seleziona tutti gli elementi dell'array                                                     |
| `array[n,:]`   | Seleziona la riga                                                                           |
| `array[:,n]`   | Seleziona la colonna                                                                        |
| `array[n:m:p]` | Seleziona gli elementi dall'elemento `n`-esimo all'elemento `m`-esimo escluso con passo `p` |
### Codici esempio
- Creo una matrice 2x4 composta da due righe e da quattro elementi:
```python
>>>m=np.array([[1,2,3,4],[5,6,7,8]])
>>>m[1][2]

7
```
---
- Vari tipi di idexing e slicing:
```python
>>>v=np.array([1,2,3,4,5,6,7,8,9])
>>>v[0]
>>>v[-1]
>>>v[1:-1]
>>>v[1:-1:2]
>>>v[:3]
>>>v[-3:]
>>>v[::-1]
>>>v[::-2]

1
9
array([2,3,4,5,6,7,8])
array([2,4,6,8])
array([1,2,3])
array([7,8,9])
array([9,8,7,6,5,4,3,2,1])
array([9,7,5,3,1])
```
