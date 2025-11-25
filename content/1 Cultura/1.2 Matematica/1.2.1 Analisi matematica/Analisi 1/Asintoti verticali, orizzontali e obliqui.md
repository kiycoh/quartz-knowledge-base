---
tags:
  - algebra-relazionale
  - limiti-funzioni
  - teorema-di-lhopital
---

>[!note]
>Il professore metterà esercizi con asintoto orizzontale = 0
## Gli asintoti orizzontali
Gli asintoti orizzontali si trovano calcolando il limite per $x$ tendente a più o meno infinito agli estremi del campo di definizione della funzione.

$$\lim _{x\to \infty} \frac {x}{x-1} = \frac {\infty}{\infty}$$
$$\lim _{x\to -\infty} \frac {x}{x-1} = \frac {\infty}{\infty}$$
Per risolvere i due limiti utilizzeremo il [[Teorema di L'Hopital]].
$$\lim _{x\to \infty} \frac {D[x]}{D[x-1]} = \lim _{x\to \infty} \frac11 = 1$$
$$\lim _{x\to -\infty} \frac {D[x]}{D[x-1]} = \lim _{x\to -\infty} \frac11 = 1$$
In questo modo i limiti saranno due numeri finiti.

Quindi, per $x$ tendente a $+\infty$ e $-\infty$ la funzione ha due asintoti orizzontale all'altezza dell'ordinata $y=1$.
$$\lim _{x\to \infty} \frac {x}{x-1} = 1$$
$$\lim _{x\to -\infty} \frac {x}{x-1} = 1$$![[Piano_1 1.png]]

## Gli asintoti verticali
L'asintoto verticale è una retta verticale che approssima l'andamento del grafico di una funzione nell'intorno di un punto $x_0$.

Prendendo in considerazione il dominio $D: \forall x \in \mathbb{R}, (- \infty,1) \cup (1, -\infty)$, la funzione non è definita nel punto $x=1$.

$$\lim _{x\to 1^+} \frac {x}{x-1} = \frac {1}{0^+} = \infty$$
$$\lim _{x\to 1^-} \frac {x}{x-1}= \frac {1}{0^-} = -\infty$$
Quindi a destra di $x=1$ la funzione tende a $+\infty$ mentre a sinistra di $x=1$ rende a $-\infty$.

![[Piano_1 2.png]]
## Gli asintoti obliqui

>[!note]
>*Se gli asintoti orizzontali sono = 0 non c'è bisogno di calcolare asintoti obliqui.*

Un asintoto obliquo è una retta che approssima l'andamento del grafico di una funzione all'infinito.

Se l'estremo è $+\infty$ o $-\infty$ è possibile verificare l'eventuale presenza di un asintoto obliqui $mx+q$ calcolando i seguenti limiti.

$$m= \lim _{x\to \infty} \frac{f(x)}{x}= \lim _{x \to \infty} \frac{\frac {x}{x-1}}{x} = 0$$
$$q= \lim _{x \to \infty} f(x) -mx = \lim _{x \to \infty} \frac {x}{x-1} - 0 * x=1$$

Se i limiti esistono e sono finiti, con $m \neq 0$, allora c'è un asintoto obliquo $mx+q$.

In questo caso, non esiste un asintoto obliquo né per $+\infty$ che per $-\infty$.