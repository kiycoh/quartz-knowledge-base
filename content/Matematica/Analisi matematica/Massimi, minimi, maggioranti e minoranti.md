---
tags:
  - algebra-lineare
  - matematica
  - statistica-inferenziale
---

### Maggioranti e Minoranti

Un **maggiorante** di un insieme $S \subseteq \mathbb{R}$ è un numero $M \in \mathbb{R}$ tale che $x \leq M$ per ogni $x \in S$. Se esiste un tale $M$, allora $S$ è detto limitato superiormente. Analogamente, un **minorante** di $S$ è un numero $m \in \mathbb{R}$ tale che $m \leq x$ per ogni $x \in S$. Se esiste un tale $m$, allora $S$ è detto limitato inferiormente.

#### Esempi

- Se $S = {1, 2, 3, 4}$, allora $5$ è un maggiorante di $S$ e $0$ è un minorante.
- Per l'insieme $T = {x \in \mathbb{R} | x < 10}$, $10$ è un maggiorante ma non appartiene a $T$.

### Massimi e Minimi

Un insieme $S \subseteq \mathbb{R}$ ha un **massimo** se esiste un elemento $M \in S$ tale che $M \geq x$ per ogni $x \in S$. In questo caso, $M$ è anche un maggiorante di $S$, ma è un maggiorante speciale perché appartiene a $S$. Analogamente, $S$ ha un **minimo** se esiste un elemento $m \in S$ tale che $m \leq x$ per ogni $x \in S$. Questo $m$ è un minorante di $S$ e appartiene a $S$.

#### Esempi

- L'insieme $S = {1, 2, 3, 4}$ ha il massimo $4$ e il minimo $1$.
- L'insieme $T = {x \in \mathbb{R} | 0 \leq x < 1}$ non ha un massimo, ma ha un minimo, che è $0$.

### Proprietà

- Ogni insieme di numeri reali ha al massimo un massimo e un minimo.
- Se un insieme ha un massimo (minimo), allora tale massimo (minimo) è l'unico maggiorante (minorante) che appartiene all'insieme.
- Non tutti gli insiemi hanno massimi o minimi. Per esempio, l'insieme dei numeri reali non ha né massimo né minimo.