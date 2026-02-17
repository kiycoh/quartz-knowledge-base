---
tags:
  - javascript
  - linguaggi-programmazione
  - hoisting
---

# Definizione di hoisting ([[JavaScript]])
In *JavaScript* l'**hoisting** si riferisce ad un comportamento default del linguaggio: **poter utilizzare una variabile prima che questa venga dichiarata** muovendo tutte le dichiarazioni in cima allo scope corrente.

In altre parole, la dichiarazione viene spostata in cima allo scope e la variabile viene inizializzata come `undefined`, permettendone l'uso (restituendo `undefined`) prima della riga di dichiarazione effettiva.

```JavaScript
> x = 360;
> y = 40;

> console.log(x + y);
> var x;
> var y;

400
```