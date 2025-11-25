---
last modified: 2025, 11, 10 20:11:05
tags:
  - machine-learning
  - linguaggi-programmazione
  - python
---
# Funzione Python
==In [[Python]], le funzioni sono utili per evitare la ripetizione di un pezzo di codice e per organizzare il software in modo più ordinato.==

> [!Info] A cosa servono le parentesi?
> Se il nome della funzione viene seguito da una coppia di parentesi ricorda che *all'interno vengono inseriti i parametri*, ovvero delle variabili necessarie al funzionamento della funzione.
> Nel codice sotto, `addizione` è il nome della funzione, e `a` e `b` sono i parametri che vengono passati alla funzione. Il valore restituito dalla funzione viene assegnato alla variabile `risultato`.
> ``` python
>>>>def addizione (a,b)
>>>>	risultato = a + b
>>>>	return risultato
>>>>risultato = addizione (15, 5)
>>>>print(risultato)
>20
> ```
# Parametri 
Avere parametri opzionali nelle nostre funzioni significa fare in modo che la funzione "funzioni" anche senza l'aggiunta di quel parametro specifico. Per rendere ciò possibile, a questi parametri è sempre associato un valore di default.
Nel codice sotto il parametro opzionale è `antivirus` a cui è stato assegnato il valore di default `False`.

```python
def laptop_nuovo(ram, cpu, antivirus=False):
    print("Il nuovo laptop avrà le seguenti caratteristiche:")
    print("ram: " + ram)
    print("cpu: " + cpu)
    if antivirus == True:
        print("Hai comprato anche un antivirus!")
```

# Return
Affinché la nostra funzione **restituisca** il risultato in maniera autonoma si utilizza il comando `return`.
Potremo quindi usare questo dato passandolo ad esempio a una variabile o usando la funzione `print()`:

```python
def get_neighbours(self, i, j):
	count = 0
	for x in range(-1, 2):
		for y in range(-1, 2):
			if not (x==0 and y==0) and self.grid[(i + x)%self.row][(j + y)%self.col].get_state() == True: count += 1
	return count
```

# Funzione ricorsiva
E' una funzione che richiama se stessa.
- Funzionano similmente ad uno Stack: rimane in attesa che l'ultima funzione restituisca un valore prima di essere iterata nuovamente.
	- Maggiore dispendio di risorse all'aumentare della mole di dati.

``` Python
def factorial(x):
    """This is a recursive function
    to find the factorial of an integer"""
    if x == 1:
        return 1
    else:
        return (x * factorial(x-1))

num = 3
print("The factorial of", num, "is", factorial(num))
```
## Caso base e caso ricorsivo
1. Un algoritmo ricorsivo ha un caso base, altrimenti non si arresterebbe mai (portando all'allocazione di una quantità infinita di memoria).
2. Un algoritmo ricorsivo ha una riduzione dei parametri attuali, altrimenti la condizione del caso base non sarebbe mai vera e la funzione non si arresterebbe mai.
# Docstring
La docstring è una stringa di testo che viene inserita all'inizio di una funzione al fine di documentarne il funzionamento.

```python
def calcola_media(valori):
    """
    Calcola la media dei valori nella lista fornita.
    Args:
        valori (list): una lista di numeri
    Returns:
        float: la media dei numeri nella lista
    """
    
    somma = 0
    for valore in valori:
        somma += valore
    media = somma / len(valori)
    return media
```