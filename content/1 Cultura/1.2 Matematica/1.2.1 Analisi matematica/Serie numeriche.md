---
tags:
  - matematica
  - series-convergence
  - limits
---

Data una successione di numeri reali $\{a_n\}$ si chiama serie dei termini $a_n$ la somma degli infiniti termini della successione e si indica così
# $\displaystyle \sum_{n=0}^\infty a_n$

La successione $\{s_n\}$ è detta **successione delle somme parziali della serie** 

$s_o = a_0$
$s_1 = a_0 + a_1$
$s_2 = a_0 + a_1 + a_2$
$... = ... + ... + ... + ...$
$s_n = a_0 + a_1 + a_2 + ... + a_n = \displaystyle \sum_{k=0}^n a_k$

Se esiste il limite di $s_n$ per $n\to +\infty$ allora esso definisce la serie

$\displaystyle \sum_{n=0}^\infty a_n = \lim_{n\to\infty} s_n = \lim_{n\to\infty}\sum_{k=0}^n a_k$ 

1. Se $\displaystyle \lim_{n\to\infty}s_n=l \in \mathbb{R}$ si dice che la serie **converge** ad $l$
2. Se $\displaystyle \lim_{n\to\infty}s_n=+\infty$ si dice che la serie **diverge** a $+\infty$
3. Se $\displaystyle \lim_{n\to\infty}s_n=-\infty$ si dice che la serie **diverge** a $-\infty$
4. Se $\displaystyle \lim_{n\to\infty}s_n$ non esiste, si dice che la serie è **indeterminata** 

