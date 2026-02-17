---
last modified: 2025-10-28T19:55:55.000Z
related:
  - '[[Struttura dati (Informatica teorica)]]'
tags:
  - algoritmi-ordinamento
  - struttura-dati
  - lista-concatenata
---
# Cos'è una lista concatenata?
Una **lista concatenata** è [[Struttura dati (Informatica teorica)|struttura dati dinamica]] (rappresentabile come una "catena di nodi") che permettono l'inserzione e la rimozione di **nodi** in ogni punto della lista in tempo costante $O\text{(n)}$. Non permettono l'accesso casuale, solo quello sequenziale. organizza gli elementi in maniera lineare, ma a differenza degli [[Array (Struttura dati)|Array]], *la posizione è determinata da puntatori tra gli elementi, non da indici.* 
* Ogni nodo viene memorizzato in maniera indipendente l'uno dall'altro, diversi nodi si trovano in diverse sezioni della memoria;
* Ogni nodo contiene i dati di uno o più puntatori.

> [!EXAMPLE] Esempio di utilizzo per liste concatenate
> Possono implementare pile e code. Implementazione efficiente di insiemi disgiunti.
## Tipi di liste concatenate
- **[[Lista concatenata semplice]]**: Ogni nodo ha un puntatore `next` che indica l'elemento successivo.
- **[[Lista doppiamente concatenata]]**: Ogni nodo ha due puntatori: `next` (successivo) e `prev` (precedente). Permette la navigazione bidirezionale e, ad esempio, la stampa inversa in **$O\text{(n)}$**.
- **[[Lista concatenata circolare]]**: L'ultimo puntatore non è NIL (nullo), ma punta a un elemento della lista in modo ciclico.

## Operazioni su liste concatenate
- `SEARCH(L, k)`, `INDEX(L, i)`: Richiedono la scansione della lista. **O(n)**.
- `INSERT(L, x, y)`: Inserimento di un nodo `y` dopo un nodo `x` (o in testa). **O(1)** se si conosce il punto di inserimento.
- `DELETE(L, x)`: Cancellazione di un nodo `x`. **O(1)** se si conosce il nodo da cancellare e il suo predecessore (o se si cancella la testa).
- `MINIMUM(L)`, `MAXIMUM(L)`, `PREDECESSOR(L, k)`, `SUCCESSOR(L, k)`: Richiedono la scansione della lista. **O(n)**.