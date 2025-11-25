---
last modified: 2025-06-23T16:54:00.000Z
related:
  - '[[Naive Bayes]]'
tags:
  - machine-learning
  - bayes-theorem
  - teoria-probabilità
---
# Teorema di Bayes
Il teorema di Bayes serve a calcolare la probabilità che un evento sia la **causa** di un evento che **si è già verificato**. *È quindi una **ricerca a posteriori delle cause***.

$$
P(H_i|E) = \frac{P(E|H_i) \cdot P(H_i)}{P(E)} = \frac{P(E|H_i) \cdot P(H_i)}{\sum_j P(E|H_j) \cdot P(H_j)}
$$



Dati due eventi $E$ ed $H$, per il teorema delle probabilità composte si ha:

$$
P(E \land H) = P(E|H) \cdot P(H) = P(H|E) \cdot P(E)
$$

Da cui, assumendo $P(E) > 0$, si ottiene:

$$
P(H|E) = \frac{P(E|H) \cdot P(H)}{P(E)}
$$

### Formula esplicita con disintegrazione

Se $H$ e $H^c$ formano una partizione:

$$
P(H|E) = \frac{P(E|H) \cdot P(H)}{P(E|H) \cdot P(H) + P(E|H^c) \cdot P(H^c)}
$$

> Qui è stata usata la **formula di disintegrazione** al denominatore.


## Versione Generale del Teorema di Bayes

Data una partizione $\{H_1, \dots, H_m\}$ e un evento $E$, per ogni $i = 1, \dots, m$ si ha:

$$
P(H_i | E) = \frac{P(E|H_i) \cdot P(H_i)}{P(E)}
$$

Applicando la disintegrazione a $P(E)$:

$$
P(H_i | E) = \frac{P(E|H_i) \cdot P(H_i)}{\sum_{j=1}^{m} P(E|H_j) \cdot P(H_j)}
$$
