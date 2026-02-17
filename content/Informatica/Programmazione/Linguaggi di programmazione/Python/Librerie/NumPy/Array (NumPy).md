---
last modified: 2024-08-11T19:10:00.000Z
related:
  - '[[Python]]'
  - '[[NumPy]]'
tags:
  - numpy
  - array-creation-routines
  - indexing-slicing
---

==Un'array NumPy== (`ndarray`) ==è una griglia di valori== contenente dati dello stesso tipo, immagazzinati in settori contigui della memoria.
- Gli array NumPy permettono operazioni semplificate e più veloci, utilizzando meno memoria rispetto alle [[List (Python)|Liste Python]].
- Gli array possono essere monodimensionali (**vettori**), bidimensionali (**matrici**), tridimensionali e oltre (**tensori**).

![[Array (NumPy)_image_1.png|600]]

## Attributi di un'array NumPy
Un'array ha diversi attributi:
- **`ndim` (intero)**: il numero di dimensioni dell'array (1 per un vettore, 2 per una matrice..)
- **`shape` (tupla di ndim interi)**: le dimensioni dell'array
- **`size` (intero)**: il numero totale di elementi dell'array
- **`dtype` (oggetto dtype)**: un oggetto che indica il tipo di dato degli elementi dell'array.
- **`itemsize` (intero)**: le dimensioni in byte di ciascun elemento
- **`data` (oggetto memoryview)**: un riferimento alla porzione di memoria che contiene i dati

>[!info] Come definire il tipo di dato dell'array
>Per definire il tipo di dati dell'array si utilizza il parametro `dtype`. 
>```python
>np.array([1.,2.,3], dtype=float)
>```
>`dtype` riconosce ad esempio: `int`, `float` `uint` (numeri interi positivi), `complex`..
#### Codice esempio
```python
>>>a = np.array([ [1,2,3] , [4,5,6] ]) # matrice 2x3
>>>print('a.ndim ({0}) = {1}'.format(type(a.ndim),a.ndim))
>>>print('a.shape ({0}) = {1}'.format(type(a.shape),a.shape))
>>>print('a.size ({0}) = {1}'.format(type(a.size),a.size))
>>>print('a.dtype ({0}) = {1}'.format(type(a.dtype),a.dtype))
>>>print('a.itemsize ({0}) = {1}'.format(type(a.itemsize),a.itemsize))
>>>print('a.data ({0}) = {1}'.format(type(a.data),a.data))

a.ndim (<class 'int'>) = 2
a.shape (<class 'tuple'>) = (2, 3)
a.size (<class 'int'>) = 6
a.dtype (<class 'numpy.dtype'>) = int32
a.itemsize (<class 'int'>) = 4
a.data (<class 'memoryview'>) = <memory at 0x02D69300>
```
# [[Array creation routines (NumPy)]]
NumPy permette di creare diversi tipi di array velocemente a seconda delle proprie esigenze. Ci sono almeno quattro possibili strategie per creare un array in NumPy:

- Conversione di altre strutture dati Python compatibili (liste, tuple..).
- Funzioni specifiche NumPy(`arange`, `ones`, `zeros`, ecc..)
- Lettura array dal disco (da formati standard e non)
- Creazione di array di byte non elaborati attraverso stringhe o buffer

# [[Indexing e slicing su NumPy array]]
Le operazioni di indexing e slicing permettono di selezionare o estrarre solo una parte degli elementi di un array NumPy.
