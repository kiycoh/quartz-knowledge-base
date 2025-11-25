---
last modified: 2024-08-11T19:10:00.000Z
related:
  - '[[Python]]'
  - '[[NumPy]]'
tags:
  - machine-learning
  - numpy
  - array-creation-routines
---
Per "array creation routines" si intendono quelle buone norme per creare vettori, matrici o tensori di diverso uso utilizzando la libreria [[NumPy]].
![[Array (NumPy)_image_2.png|600]]
## Da dati esistenti

| Nome                  | Descrizione                                                             | Sintassi                                                |
| --------------------- | ----------------------------------------------------------------------- | ------------------------------------------------------- |
| `array()`             | Crea un array.                                                          | numpy.array(object[, dtype, copy, order, subok, ndmin]) |
| `asarray()`           | Converte l'input in un array.                                           | numpy.asarray(a[, dtype, order])                        |
| `asanyarray()`        | Converte l'input in un `ndarray`                                        | numpy.asanyarray(a[, dtype, order])                     |
| `ascontiguousarray()` | Ritorna un array contiguo in memoria (Ordine C).                        | numpy.ascontiguousarray(a[, dtype])                     |
| `asmatrix()`          | Interpreta l'input come una mastrice.                                   | numpy.asmatrix(data[, dtype])                           |
| `copy()`              | Ritorna un array copia di un dato oggetto.                              | numpy.copy(a[, order]                                   |
| `frombuffer()`        | Interpreta un buffer come un array 1D.                                  | numpy.frombuffer(buffer[, dtype, count, offset])        |
| `fromfile()`          | Costruisce un array da dati in un file binario o di testo.              | numpy.fromfile(file[, dtype, count, sep])               |
| `fromfunction()`      | Costruisce un array dall'esecuzione di una funzione da ogni coordinata  | numpy.fromfunction(function, shape, \*\*kwargs)         |
| `fromiter()`          | Crea un nuovo array 1D da un oggetto iterabile.                         | numpy.fromiter(iterable, dtype[, count])                |
| `fromstring()`        | Inizializza un nuovo array 1D da codice binario o testo in una stringa. | numpy.fromstring(string[, dtype, count, sep])           |
| `loadtxt()`           | Carica dati da file di testo.                                           | numpy.loadtxt(fname[, dtype, comments, delimiter, ...]) |
### Codici esempio
#### Funzione `numpy.fromfunction`
La funzione `numpy.fromfunction` permette operazioni matematiche su array con forma specificata e li riempie con il valore restituito da una funzione che accetta come parametri gli indici che individuano ciascun elemento nell'array.

- Array monodimensionale:
```python
>>>def myfunc1(i): #restituisce i**2 se i>=5, i altrimenti
>>>	print(type(i))
>>>	print('i=',i)
>>>	return (i>=5)*(i**2)+(i<5)*(i)

>>>a = np.fromfunction(function = myfunc1 , shape=(10,) , dtype=int32)
>>>print('a=',a)

<class 'numpy.ndarray'>
i= [0 1 2 3 4 5 6 7 8 9]
a= [ 0  1  2  3  4 25 36 49 64 81]
```

- Array bidimensionale:
```python
>>>def myfunc2(i,j):
>>>	print('i =\n', i)
>>>	print('j =\n', j)
>>>	return i==j
   
>>>a = np.fromfunction(myfunc2,(5,5))
>>>print('a=\n',a)

i =
 [[ 0.  0.  0.  0.  0.]
 [ 1.  1.  1.  1.  1.]
 [ 2.  2.  2.  2.  2.]
 [ 3.  3.  3.  3.  3.]
 [ 4.  4.  4.  4.  4.]]
j =
 [[ 0.  1.  2.  3.  4.]
 [ 0.  1.  2.  3.  4.]
 [ 0.  1.  2.  3.  4.]
 [ 0.  1.  2.  3.  4.]
 [ 0.  1.  2.  3.  4.]]
a=
 [[ True False False False False]
 [False  True False False False]
 [False False  True False False]
 [False False False  True False]
 [False False False False  True]]
```
#### Vettore con dtype specifico
```python
>>>a=np.array([1,2,3],dtype=float64)
>>>print(a)
>>>print(a.dtype)
  
[ 1. 2. 3.]
float64
```

## Con zero e uno

| Nome           | Descrizione                                                                                   | Sintassi                                              |
| -------------- | --------------------------------------------------------------------------------------------- | ----------------------------------------------------- |
| `empty()`      | Ritorna un nuovo array di una data shape e tipo, senza inizializzare elementi.                | numpy.empty(shape[dtype, order])                      |
| `eye()`        | Ritorna una matrice 2D con soli uno sulla diagonale e zero nel resto.                         | numpy.eye(N[, M, k, dtype])                           |
| `identity()`   | Ritorna l'array identity                                                                      | numpy.identity(n[, dtype])                            |
| `ones()`       | Ritorna un nuovo array di una data shape e tipo, inizializzando gli elementi con uno.         | numpy.ones(shape[, dtype, order])                     |
| `zeros()`      | itorna un nuovo array di una data shape e tipo, inizializzando gli elementi con zero.         | numpy.zeros(shape[, dtype, order])                    |
| `full()`       | Ritorna un nuovo array di una data shape e tipo, inizializzando gli elementi con `fill_value` | numpy.full(shape, fill_value[, dtype, order])         |
| `empty_like()` | Ritorna un nuovo array con stessi dimensione e tipo di un dato array.                         | numpy.empty_like(a[, dtype, order, subok])            |
| `ones_like()`  | Ritorna un nuovo array di uno con stessi dimensione e tipo di un dato array.                  | numpy.ones_like(a[, dtype, order, subok])             |
| `zeros_like()` | Ritorna un nuovo array di 0 con stessi dimensione e tipo di un dato array.                    | numpy.zeros_like(a[, dtype, order, subok])            |
| `full_like()`  | Ritorna un full array con stessi dimensione e tipo di un dato array.                          | numpy.full_like(a, fill_value[, dtype, order, subok]) |
### Codici esempio
#### Funzione `numpy.ones`
Ricordiamo anche `numpy.zeros`, `numpy.empty`, `numpy.identity`, `numpy.eye`
```python
>>>np.ones(5)
>>>np.ones((5,3,2),dtype=np.int8)

array([ 1.,  1.,  1.,  1.,  1.])
array([[[1, 1],
        [1, 1],
        [1, 1]],

       [[1, 1],
        [1, 1],
        [1, 1]],

       [[1, 1],
        [1, 1],
        [1, 1]],

       [[1, 1],
        [1, 1],
        [1, 1]],

       [[1, 1],
        [1, 1],
        [1, 1]]], dtype=int8)
```
#### Funzione `numpy.ones_like`
Ricordiamo anche `zeros_like`,`empty_like`.
```python
>>>a = np.array( [ [1,2,3] , [4,5,6] ] )
>>>np.ones_like(a)
>>>b = np.array( [ [1,2,3] , [4,5,6] ] )
>>>np.ones_like(a,dtype=complex)

array([[1, 1, 1],
       [1, 1, 1]], dtype=int32)
array([[ 1.+0.j,  1.+0.j,  1.+0.j],
       [ 1.+0.j,  1.+0.j,  1.+0.j]])

```
#### Funzione `numpy.zeros`
``` Python
>>> dimensions, n_item= 2,4
>>> a = np.zeros(shape=(dimensions,n_item))
>>> a

array([[0., 0., 0., 0.], [0., 0., 0., 0.]])
```
## Con range numerici

| Nome          | Descrizione                                                                           | Sintassi                                                |
| ------------- | ------------------------------------------------------------------------------------- | ------------------------------------------------------- |
| `arange()`    | Ritorna valori uniformemente spaziati dato un intervallo.                             | numpy.arange([start,] stop[, step,][, dtype])           |
| `linspace()`  | Ritorna numeri uniformemente spaziati dato un intervallo                              | numpy.linspace(start, stop[, num, endpoint, ...])       |
| `logspace()`  | Ritorna numeri uniformemente spaziati su scala logaritmica.                           | numpy.logspace(start, stop[, num, endpoint, base, ...]) |
| `geomspace()` | Ritorna numeri uniformemente spaziati su scala logaritmica (progressione geometrica). | numpy.geomspace(start, stop[, num, endpoint, dtype])    |
| `meshgrid()`  | Ritorna le coordinate dalle coordinate vettoriali.                                    | numpy.meshgrid(\*xi, \*\*kwargs)                        |
| `mgrid()`     | Istanza `nd_grid` che ritorna una mesh-grid multidimensionale densa.                  | numpy.mgrid                                             |
| `ogrid()`     | Istanza `nd_grid` che ritorna una mesh-grid multidimensionale aperta.                 | numpy.ogrid                                             |
### Codici esempio
#### Funzione `numpy.arange`
La funzione arange di NumPy 'arrangia' ordinatamente le dimensioni del parametro.
```python
>>>a = arange(1.3 ,10.34 ,0.2 )
>>>print(a)
>>>print(a.dtype)

[  1.3   1.5   1.7   1.9   2.1   2.3   2.5   2.7   2.9   3.1   3.3   3.5
   3.7   3.9   4.1   4.3   4.5   4.7   4.9   5.1   5.3   5.5   5.7   5.9
   6.1   6.3   6.5   6.7   6.9   7.1   7.3   7.5   7.7   7.9   8.1   8.3
   8.5   8.7   8.9   9.1   9.3   9.5   9.7   9.9  10.1  10.3]
float64
```
#### Funzione `numpy.linspace`
Calcola i punti equispaziati tra due estremi:
```python
>>>np.linspace(2.0, 3.0, num=5) # cinque punti compreso stop
>>>np.linspace(2.0, 3.0, num=5, endpoint=False) # cinque punti escluso stop
>>>np.linspace(2.0, 3.0, num=5, retstep=True)

array([ 2.  ,  2.25,  2.5 ,  2.75,  3.  ])
array([ 2. ,  2.2,  2.4,  2.6,  2.8])
(array([ 2.  ,  2.25,  2.5 ,  2.75,  3.  ]), 0.25)
```

## Con numeri randomici

| Codice                                   | Descrizione                                           |
| :--------------------------------------- | :---------------------------------------------------- |
| `np.random.rand(righe,colonne)`          | Crea una matrice di numeri random positivi tra 0 e 1  |
| `np.random.randn(righe, colonne)`        | Crea una matrice di numeri random compresi tra 1 e -1 |
| `np.random.randint(0,5,[righe,colonne])` | Crea una matrice di numeri random compresi tra 0 e 5  |
### Codici esempio
#### Funzione `numpy.random`
```Python
>>>a= np.random.rand(righe,colonne)
>>>print("Matrice di numeri random positivi compresi tra 0 e 1:", a)

>>>b= np.random.randn(righe, colonne)
>>>print("Matrice di numeri random compresi tra -1 e 1:", b)

>>>c= np.random.randint(0,5, [righe,colonne])
>>>print("Array di numeri randomici interi compresi tra 0 e 5:", c)

Matrice di numeri random positivi compresi tra 0 e 1: [[0.04301602 0.83251162 0.79429375 0.88062474] [0.59928465 0.39429854 0.67796716 0.28903311]]

Matrice di numeri random compresi tra -1 e 1: [[-0.74003702 -0.24466508 -0.43028455 0.33106504] [ 0.28639915 -0.17859026 -0.58098105 0.95146962]]

Array di numeri randomici interi compresi tra 0 e 5: [[0 0 2 3] [2 0 1 4]]
```