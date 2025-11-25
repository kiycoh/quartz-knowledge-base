---
last modified: 2024-08-11T19:12:00.000Z
tags:
  - algoritmi-ordinamento
  - struttura-dati-lineare
  - principi-lifo
---
# Definizione di stack
Una **stack** (o **pila**) è una **[[Struttura dati lineare]]** che opera secondo il [[Principio LIFO]] (Last In, First Out, ovvero che l'ultimo elemento inserito è il primo a essere rimosso). Gli elementi vengono inseriti e cancellati dalla "cima" (testa) dell'insieme.

![[Pasted image 20250716161025.png]]
## Caratteristiche di uno stack
1. **Stack Frame:** uno stack viene spesso utilizzato per gestire le chiamate di funzione. Ogni volta che una funzione viene chiamata, viene creato uno "stack frame" che contiene informazioni come i parametri della funzione, le variabili locali e l'indirizzo di ritorno. Quando la funzione termina, il suo stack frame viene  rimosso dallo stack.
2. **Gestione della Memoria:** nella gestione della memoria di un programma, uno stack è spesso utilizzato per gestire le variabili locali e i dati temporanei associati alle chiamate di funzione. L'allocazione e la de-allocazione della memoria nello stack sono molto veloci, poiché coinvolgono solo la modifica del "puntatore di stack".
3. **Overflow e Underflow:** uno "stack overflow" si verifica quando si tenta di inserire un elemento in uno stack pieno. Un "stack underflow" si verifica quando si tenta di rimuovere un elemento da uno stack vuoto.

## Operazioni su stack
![[Pasted image 20250716161006.png]]
- `STACK-EMPTY(S)`: Controlla se la pila è vuota. **O(1)**.
- `PUSH(S, x)`: Inserisce un elemento `x` in cima.
- `POP(S)`: Rimuove e restituisce l'elemento in cima.
## Implementazioni di stack
- **Con Array**: Si mantiene un puntatore `top` all'ultimo elemento. Richiede strategie di ridimensionamento per gestire l'overflow o lo spreco di spazio (es. raddoppiare la dimensione quando pieno, dimezzare quando poco utilizzato). Le operazioni di `PUSH` e `POP` hanno complessità **O(1)** ammortizzata, ma possono raggiungere **O(n)** nel caso peggiore per il ridimensionamento.
- **Con Liste Concatenate**: Simile, ma senza problemi di ridimensionamento, operando sempre in testa alla lista.
 - **Utilizzo Pratico**: Gestione delle chiamate a funzione (stack di chiamate), algoritmi ricorsivi.

### Esempio di Utilizzo:

```python
def funzione1():
    print("In funzione1")
    funzione2()
    print("Uscita da funzione1")

def funzione2():
    print("In funzione2")

# Chiamata iniziale
funzione1()
```

In questo esempio, uno stack viene utilizzato implicitamente per gestire le chiamate di funzione. Quando `funzione1` viene chiamata, uno stack frame viene creato. Quando `funzione2` viene chiamata all'interno di `funzione1`, un nuovo stack frame viene aggiunto in cima allo stack. Quando `funzione2` termina, il suo stack frame viene rimosso, e così via.

Lo stack è un concetto fondamentale in programmazione, ed è utilizzato in molteplici contesti per gestire dati in modo efficiente e organizzato.