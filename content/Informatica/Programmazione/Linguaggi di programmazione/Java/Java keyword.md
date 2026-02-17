---
last modified: 2025, 11, 24 2:11:03
related: null
parent note: null
tags:
  - java
  - linguaggi-programmazione
  - software-development
---
# Java keywords
==Le *keywords* (parole chiave) di [[Java]] sono un insieme fisso di parole riservate che hanno un significato speciale per il compilatore.==
- Java utilizza le **keywords** per definire i suoi tipi di dato primitivi
## Controllo di Flusso
Sono usate per gestire il "flusso" di esecuzione del programma (cioè, quali istruzioni eseguire e in quale ordine).
- **Condizionali:** `if`, `else`, `switch`, `case`, `default`
- **Cicli (Loop):** `for`, `while`, `do`
- **Istruzioni di Salto (Jump Statements):** `break`, `continue`, `return`
## Tipi di Dati Primitivi
Sono le parole chiave usate per dichiarare i tipi di dati fondamentali.
- **Numeri interi:** `int`, `long`, `short`, `byte`
- **Numeri decimali:** `double`, `float`    
- **Booleani:** `boolean`
- **Caratteri:** `char`
## Struttura del Programma e Oggetti
Definiscono i "contenitori" del codice e gestiscono gli oggetti.
- [[Java modifier]]: `public`, `private`, `static`, `final`
- **Definizione Strutture:** `class`, `interface`, `enum`
- **Organizzazione:** `package`, `import`    
- **Creazione e Riferimenti:** `new` (per creare oggetti), `this` (riferimento all'oggetto corrente), `super` (riferimento alla classe genitore)
- **Test del Tipo:** `instanceof`
## Gestione delle Eccezioni
Usate per gestire gli errori e le situazioni anomale durante l'esecuzione.
- **Blocchi di gestione:** `try`, `catch`, `finally`
- **Lancio e dichiarazione:** `throw`, `throws`
## Altre Keyword e Valori Speciali
- **Metodi senza Ritorno:** `void`
- **Validazione (Debugging):** `assert`
- **Parole per Tipi Specifici:** `native`, `transient`, `volatile`, `strictfp`, `synchronized` (queste ultime due sono anche modificatori di comportamento)
## Categoria Speciale: Letterali (Spesso confusi con Keyword)
Tecnicamente non sono "keyword" ma "letterali", cioè valori fissi. Non puoi usarli come nomi di variabili.
- **Valori Booleani:** `true`, `false`
- **Valore Nullo:** `null`    
## Parole Riservate (Ma non usate)
Java riserva queste parole ma non assegna loro alcuna funzione (per ora). Non puoi usarle.
- `goto`
- `const`