---
tags: [javascript, linguaggi-programmazione, variable-declaration]
last modified: 2025, 11, 24 22:11:02
---

# Cos'è JavaScript?
**JavaScript (JS)** è un [[Linguaggio di programmazione|linguaggio di programmazione]], molto utilizzato nei browser insieme a [[HTML]] e [[CSS]]. È progettato per **aggiungere interattività** alle pagine web (sliders, allerte, click interactions, popups, ecc..).

*JavaScript* è utilizzato anche in [[Node.js]], [[Electron]] per applicazioni desktop e [[React|React Native]] per applicazioni mobile.

## Dichiarare una [variabile JavaScript](https://javascript.info/variables)
Una **variabile** *JavaScript* può essere considerata come un "contenitore di informazioni".

![[variable.svg#center]]

Per utilizzare una **variabile** *JavaScript* bisogna innanzitutto dichiararla: si utilizzano `var`, `let` o `const`.

***In cosa differiscono?***
* [[Scope (JavaScript)|Scope]] (ambito di visibilità);
* [[Hoisting (JavaScript)|Hoisting]] (sollevamento);
* Riassegnazione (cambiare valore di una variabile dopo averla dichiarata);
* Ri-dichiarazione (dichiarare una stessa variabile più volte nello stesso scope).

```JavaScript
> let nome = "Alex", id = 2
> console.log(nome)

Alex
```
> In *JavaScript*, ogni riga deve finire con ";".
### `var`
> [!help] Caratteristiche
> **Scope**: *function scope* o *global scope* se dichiarata al di fuori di una funzione
> **Hoisting**: sì
> **Riassegnazione**: permessa
> **Ri-dichiarazione**: permessa

**Evita `var`** nel codice moderno per prevenire problemi legati allo scope e all'hoisting. Opzionalmente può essere inizializzata con un valore. Usato prevalentemente in codici "old-school".
### `let`
Usa **`let`** solo se hai bisogno di riassegnare il valore della variabile. Opzionalmente può essere inizializzata con un valore.

> [!help] Caratteristiche
> **Scope**: *block scope* (può essere utilizzata solo all'interno del blocco `{}` in cui è definita, ad esempio dentro un `if`, un `for` o un blocco isolato)
> **Hoisting**: sì ma non vengono inizializzate ([[Temporal Dead Zone (TDZ)]])
> **Riassegnazione**: permessa
> **Ri-dichiarazione**: non permessa ([[Syntax Error]])

```JavaScript
> let desc;
> desc = "Questa è una descrizione";
> desc = "Sto aggiornando la descrizione";
> console.log(desc);

Sto aggiornando la descrizione
```
### `const`
Usa **`const`** di default per tutte le dichiarazioni. Passa a `let` solo se sai specificamente che avrai bisogno di riassegnare il valore. Questo rende il codice più prevedibile e facile da seguire. Se una costante è un oggetto o un array le sue proprietà o componenti possono essere modificati o rimossi.

> [!help] Caratteristiche
> **Scope**: *block scope*
> **Hoisting**: sì ma non vengono inizializzate
> **Riassegnazione**: non permessa
> **Ri-dichiarazione**: non permessa