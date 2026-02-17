---
last modified: 2025, 11, 24 2:11:05
related:
  - '[[Linguaggio (Informatica teorica)]]'
  - '[[Teoria dei linguaggi formali]]'
parent note: null
tags:
  - informatica-teorica
  - linguaggio-formale
  - stringhe-informatica
---
# Definizione di linguaggio formale
In [[Informatica teorica]],un **linguaggio formale** è un insieme di [[Stringa (Informatica teorica)|stringhe]] costruite su di un [[Alfabeto (Informatica teorica)|alfabeto]].

Formalmente, un linguaggio formale $L$ è definito come un sottoinsieme di $\sum^*$ (l'universo) che rappresenta l'insieme di tutte le sequenze finite (stringhe) che si possono formare con i simboli di un alfabeto $\sum$, che è un insieme finito e non vuoto di simboli (o caratteri), ad esempio $\sum = \{a, b, c\}$.

1. **Potenze dell'alfabeto ($\sum^n$)**:
    - $\sum^0 = \{\epsilon\}$ (l'insieme contenente solo la **[[Stringa vuota (Informatica teorica)|stringa vuota]]**, indicata con $\epsilon$ o talvolta $\lambda$).
    - $\sum^1 = \{a, b, c\}$ (l'insieme di tutte le stringhe di lunghezza 1).
    - $\sum^2 = \{aa, ab, ac, ba, bb, bc, ca, cb, cc\}$ (l'insieme di tutte le stringhe di lunghezza 2).
    - $\sum^n$ è l'insieme di tutte le stringhe di lunghezza $n$.
2. [[Chiusura di Kleene]]: l'insieme $\sum^∗$ è definito come l'unione di tutte le possibili potenze dell'alfabeto, da zero a infinito: $\sum^* = \sum^0 \cup \sum^1 \cup \sum^2 \cup \dots = \bigcup_{n \ge 0} \sum^n$

> [!EXAMPLE] Esempio pratico di linguaggio formale
> Consideriamo un alfabeto binario $\sum = \{0, 1\}$.
> 
> Applicando la chiusura di Kleene:
> - $\sum^0 = \{\epsilon\}$
> - $\sum^1 = \{0, 1\}$
> - $\sum^2 = \{00, 01, 10, 11\}$
> - $\sum^3 = \{000, 001, 010, 011, 100, 101, 110, 111\}$
> - … e così via.
>     
> Quindi, $\sum^*$ per l'alfabeto binario è l'insieme infinito che contiene tutte le possibili stringhe binarie:
> $$\sum^* = \{\epsilon, 0, 1, 00, 01, 10, 11, 000, \dots\}$$
