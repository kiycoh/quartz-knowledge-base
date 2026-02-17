---
last modified: 2025, 11, 10 22:11:05
related: null
parent note: '[[Approcci alla programmazione]]'
tags:
  - machine-learning
  - programming-paradigms
  - software-development
---
# Paradigma di programmazione
Molti linguaggi moderni sono multi-paradigma.
## Paradigmi derivati dalla [[programmazione imperativa]]
* [[Programmazione procedurale]]: Basata su una sequenza di procedure (sottoprogrammi) che modificano lo stato. (Anni '60; es. Fortran, COBOL)
* [[Programmazione strutturata]]: Evoluzione della procedurale, usa costrutti di controllo (if, while) evitando i GOTO. (Primi anni '70; es. Pascal, C)
* [[Programmazione modulare]]: Scompone il programma in moduli indipendenti e con interfacce definite. (Metà anni '70; es. Modula, CLU)
* [[Programmazione concorrente]]: Gestisce l'esecuzione simultanea di più processi o thread. (Anni '70; es. Erlang, Go, CSP, Occam)
* [[Programmazione per tipi di dati astratti]]: Definisce tipi di dati in base al loro comportamento (interfaccia) piuttosto che alla loro implementazione. (Tardi anni '70; es. OBJ, CLU)
* [[Programmazione orientata agli oggetti (OOP)]]: Basata su "oggetti" che incapsulano dati (attributi) e comportamento (metodi). (Anni '80; es. Smalltalk, C++, Java, Python)
* [[Programmazione orientata agli aspetti (AOP)]]: Estensione dell'OOP per separare le "preoccupazioni" trasversali (es. logging, sicurezza). (Anni 2000; es. AspectJ)
* [[Programmazione orientata agli eventi]]: Il flusso del programma è determinato da eventi esterni (es. click del mouse, input di rete). (Usata per GUI e real-time)

## Paradigmi derivati dalla programmazione dichiarativa
* [[Programmazione funzionale]]: Tratta il calcolo come valutazione di funzioni matematiche, enfatizzando l'immutabilità. (Anni '70; es. Lisp, Haskell)
* [[Programmazione logica]]: Basata sulla logica formale e la dimostrazione di teoremi. (Anni '70; es. Prolog)
* [[Programmazione a vincoli]]: Definisce le proprietà (vincoli) della soluzione, lasciando al sistema il compito di trovarla.
* [[Programmazione per pattern matching]]: Controlla la presenza di sequenze o strutture specifiche nei dati. (Es. Espressioni Regolari, Haskell, Rust)
* [[Programmazione strutturata secondo patterns]]: Applica soluzioni di progettazione (design pattern) riutilizzabili e standardizzate. (Es. Java Blueprints)
* [[Programmazione orientata agli utenti]]: Focalizzata sulla progettazione dell'interazione e dell'esperienza utente. (Es. Piattaforma .NET, 1998)


- [[JavaScript]]: Il linguaggio più utilizzato per il web. Fondamentale per rendere interattive le pagine web (front-end) e usato anche lato server ([[Node.js]]).
- [[PHP]]: Specifico per il web. Serve a creare pagine web dinamiche lato server; è alla base di sistemi come WordPress, Drupal e Joomla.
- [[Go (Golang)]]: Sviluppato da Google. Ottimo per microservizi, strumenti a riga di comando e sistemi di rete ad alta concorrenza. È compilato e molto veloce.
- [[Rust]]: Focalizzato su sicurezza (gestione della memoria senza garbage collector) e prestazioni. Serve per lo sviluppo di sistemi, per rimpiazzare C/C++ in contesti critici.