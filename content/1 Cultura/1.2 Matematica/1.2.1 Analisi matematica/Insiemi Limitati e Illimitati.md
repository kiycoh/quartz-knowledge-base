---
tags:
  - algoritmi-ordinamento
  - analisi-matematica
  - insiemi-limitati
---

### Insiemi Limitati

Un insieme limitato è un concetto fondamentale nell'analisi matematica, soprattutto quando si lavora con gli insiemi di numeri reali. Un insieme è considerato limitato se esiste un confine numerico entro il quale tutti gli elementi dell'insieme si trovano.

>[!definizione] 
>Un insieme $S \subseteq \mathbb{R}$ è detto limitato superiormente se esiste un numero reale $M$ tale che $x \leq M$ per ogni $x \in S$. Analogamente, $S$ è detto limitato inferiormente se esiste un numero reale $m$ tale che $m \leq x$ per ogni $x \in S$. Un insieme è considerato limitato se è sia limitato superiormente che inferiormente.

#### Notazione e Terminologia

- Se $S$ è limitato superiormente, $M$ è chiamato un maggiorante di $S$.
- Se $S$ è limitato inferiormente, $m$ è chiamato un minorante di $S$.
- Se un insieme è limitato, significa che esiste un intervallo reale $[m, M]$ tale che ogni elemento $x$ di $S$ soddisfa la relazione $m \leq x \leq M$.

#### Esempi

1. L'insieme $A = {x \in \mathbb{R} | -2 \leq x \leq 5}$ è limitato perché tutti i suoi elementi sono compresi tra -2 e 5.
2. L'insieme $B = {1, 2, 3, 4, 5}$ è limitato perché tutti i valori sono minori o uguali a 5 e maggiori o uguali a 1.
3. L'insieme dei numeri naturali $\mathbb{N}$ non è limitato, poiché per qualsiasi numero naturale $n$, esiste sempre un numero naturale più grande (ad esempio, $n+1$).

#### Proprietà

- Un insieme in $\mathbb{R}$ è limitato se e solo se è contenuto in qualche intervallo chiuso $[a, b]$.
- Ogni sottoinsieme di un insieme limitato è anch'esso limitato.
- L'unione di due insiemi limitati non è necessariamente limitata, ma l'intersezione di due insiemi limitati è sempre limitata.

### Insiemi Illimitati

Un insieme è considerato illimitato se non è limitato, ovvero se si estende all'infinito in almeno una direzione. Ci sono due tipi principali di insiemi illimitati:

1. **Illimitati Superiormente**: Un insieme $S \subseteq \mathbb{R}$ è illimitato superiormente se per ogni numero reale $M$, esiste un $x \in S$ tale che $x > M$. Questo significa che l'insieme non ha un limite superiore.
    
2. **Illimitati Inferiormente**: Un insieme $S \subseteq \mathbb{R}$ è illimitato inferiormente se per ogni numero reale $m$, esiste un $x \in S$ tale che $x < m$. Questo significa che l'insieme non ha un limite inferiore.
    

#### Esempi

1. L'insieme dei numeri reali $\mathbb{R}$ è illimitato sia superiormente che inferiormente.
2. L'insieme dei numeri naturali $\mathbb{N}$ è limitato inferiormente (per esempio, da 0 o 1 a seconda della definizione) ma illimitato superiormente.
3. L'insieme $A = {x \in \mathbb{R} | x > -2}$ è illimitato superiormente perché per qualsiasi $M$, esiste sempre un $x$ in $A$ tale che $x > M$.

#### Proprietà

- Un insieme illimitato non può essere contenuto interamente in alcun intervallo finito $[a, b]$.
- Se un insieme contiene un intervallo del tipo $[a, +\infty)$ o $(-\infty, b]$, allora è illimitato.
- L'unione di un insieme illimitato con qualsiasi altro insieme (limitato o illimitato) è illimitata.