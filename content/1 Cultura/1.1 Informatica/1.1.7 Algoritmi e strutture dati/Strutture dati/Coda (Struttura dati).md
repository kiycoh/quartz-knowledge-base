---
last modified: 2025, 11, 24 21:11:01
related: null
tags: [algoritmi-ordinamento, informatica, struttura-dati-lineare]
---
# Definizione di coda
In informatica, ==una **coda** (o **queue** in inglese) è una [[Struttura dati lineare]], utilizzata per immagazzinare e gestire dati in ordine specifico, in cui il primo elemento viene inserito da un'estremità denominata REAR (o "posteriore") e la rimozione dell'elemento esistente avviene dall'altra estremità denominata FRONT (chiamato anche testa)==.
* ==Segue il [[Principio FIFO]]==

## Implementazioni di code
- **Con array**: Si mantengono puntatori `head` e `tail` per gestire l'inizio e la fine della coda, spesso in modo circolare per riutilizzare lo spazio. Richiede ridimensionamento come per le pile. Le operazioni `ENQUEUE` e `DEQUEUE` hanno complessità **O(1)** ammortizzata.
- **Con liste concatenate**: Operando in testa e in coda alla lista.
## Operazioni su coda
- `QUEUE-EMPTY(Q)`: Controlla se la coda è vuota. **O(1)**.
- `ENQUEUE(Q, x)`: Inserisce un elemento `x` in testa (o fine logica della coda).
- `DEQUEUE(Q)`: Rimuove e restituisce l'elemento dalla coda (o inizio logico della coda).
## Uso pratico di una coda
- Algoritmi di ricerca su grafi come la BFS (Breadth-First Search), gestione di processi.
- Gestione degli interrupt nei sistemi in tempo reale. Le interruzioni vengono gestite nello stesso ordine in cui sono arrivate, ovvero chi "prima arriva, meglio alloggia".
- I sistemi telefonici del Call Center utilizzano le code per trattenere le persone che li chiamano in un ordine, fino a quando un rappresentante dell'assistenza non è libero.
- Servire le richieste su una singola risorsa condivisa come una stampante, la pianificazione delle attività della CPU ecc.