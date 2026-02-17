---
last modified: 2025-05-24T23:13:00.000Z
related: null
tags:
  - javascript
  - node-js
  - linguaggi-programmazione
---
# Cos'è Node.js?
**Node.js** è un ambiente runtime [[JavaScript]] ([V8 JavaScript engine](https://en.wikipedia.org/wiki/V8_(JavaScript_engine))) e open-source e cross-platform. È progettato per eseguire **operazioni di I/O in modo asincrono** e **non-bloccante**.

> È possibile costruire applicazioni desktop, servizi software, applicazioni mobile.

***Vantaggi:***
* *Node.js* è eseguibile in un singolo processo, senza creare nuovi thread per ogni richiesta.
* *Node.js* fornisce un insieme di [[Primitiva di IO|primitive I/O]] asincrono che impediscono al codice JavaScript di bloccarsi.
	* *Node.js* evita il problema con un architettura basata su [[Event Loop]] e [[Callback, Promise, Async/Await]].
* *Node.js* permette di programmare [[Front-end|frontend]] e [[Back-end|backend]] in un singolo [[Linguaggio di programmazione|linguaggio]]. 


> [!QUESTION] PHP vs Node.js
> * **PHP**:
> 	1. Manda task al computer file system;
> 	2. Aspetta che il file system apra e legga il file;
> 	3. Ritorna il contenuto al client;
> 	4. Pronto per accogliere la prossima richiesta.
> ---
> * **Node.js**:
> 	1. Manda la task al computer file system;
> 	2. Pronto per accogliere la prossima richiesta;
> 	3. Non appena il file system ha aperto e letto il file, il server ritorna il contenuto al client.

## Event Loop
Un ciclo continui che gestisce gli eventi 

## Callback, Promise, Async/Await
Meccanismi per specificare il codice da eseguire quando un'operazione asincrona termina, mantenendo un flusso logico ordinato senza blocchi.