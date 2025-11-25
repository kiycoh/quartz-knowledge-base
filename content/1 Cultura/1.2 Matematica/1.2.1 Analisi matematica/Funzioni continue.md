---
tags:
  - continuity
  - analisi-matematica
  - limit-theorems
---

Siano $f:A\rightarrow \mathbb{R}$ e $x_0$ punto di accumulazione per $A$ con $x_0\in A$, diciamo che $f$ è continua se 
$$\Large \lim_{x\to x_0} f(x) = f(x_0)$$
>[!definizione]
>$f$ è continua in $A$ se è continua in ogni punto di accumulazione di $A$, il che rende la continuità una proprietà locale

Una funzione che non è continua in un punto si dice discontinua in quel punto.

>[!warning] Attenzione
>Anche la continuità è una [[0 Cultura/0.3 Matematica/0.3.1 Analisi matematica/Proprietà locali|proprietà locale]]


Esistono 3 tipi di discontinuità:

-  **Eliminabile**, se il limite esiste finito e risulta   $\large \displaystyle \lim_{x\to x_0} f(x) \neq f(x_0)$ 
   Consideriamo la funzione $f:\mathbb{R} \to \mathbb{R}$ definita da $\large \displaystyle f(x) =\begin{cases} \frac{\sin x}{x} & x \neq 0 \\ \frac{7}{3} & x=0\end{cases}$ 
```functionplot
---
title: 
xLabel: 
yLabel: 
bounds: [-10,10,-10,10]
disableZoom: true
grid: true
---
f(x) = sin(x)/x
```
  $f$ presenta una discontinuità eliminabile in $x=0$, infatti essendo $$\large \displaystyle \lim_{x \to 0} = \lim_{x\to 0} \frac{\sin x}{x} = 1 \neq \frac{7}{3} = f(0)$$  basta porre $\displaystyle f(0) = \lim_{x \to 0} f(x) = 1$ per ottenere una funzione continua in $\mathbb{R}$


- **Di prima specie**, se esistono limiti sinistro e destro finiti e sono diversi fra loro

  Consideriamo la funzione $f:[-\pi, +\infty[ \to \mathbb{R}$ definita da $f(x) = \begin{cases} \sin x & x\le 0 \\ x+1 & x > 0 \end{cases}$ 
  ![[Drawing 2024-03-19 20.06.26.excalidraw|80%]]$f$ presenta una discontinuità di prima specie in $x=0$, infatti
  $$\displaystyle \large  0 = \lim_{x\to 0^-}f(x)=\lim_{x\to 0^+}\sin x \neq \lim_{x\to 0^+}(x+1) = \lim_{x\to 0^+} f(x) = 1$$


- **Di seconda specie**, se almeno uno fra i limiti sinistro e destro non esiste o non esiste finito 

  Consideriamo la funzione $f:\mathbb{R} \to \mathbb{R}$ definita da $\displaystyle \large f(x) = \begin{cases} x & x \le 0 \\ \frac{1}{x} & x>0 \end{cases}$
  ![[Screenshot 2024-03-20 alle 15.14.48.png|60%]]
 
  $f$ presenta una discontinuità di seconda specie in $x=0$, infatti
  $$\Large \displaystyle \lim_{x \to 0^+} f(x) = \lim_{x \to 0^+} \frac{1}{x} = +\infty$$

>[!warning] Osservazione
>Una funzione monotona può avere solo discontinuità di prima specie

## Proprietà

- Se $f,g:A\to \mathbb{R}$ sono due funzioni continue in $x_0 \in A$, allora lo sono anche le funzioni
  $$\large \displaystyle f+g \qquad f \cdot g  \qquad \frac{f}{g} \qquad |f|$$
- Se $f:A\to B$ e $g:B\to \mathbb{R}$ sono due funzioni continue in $x_0 \in A$ e $f(x_0) \in B$ rispettivamente, allora $g \cdot f$ è continua in $x_0$ 

- Una funzione continua su un insieme chiuso e limitato ammette massimo e minimo, [[Teorema di Weierstrass]]

- Se $f:[a,b]\to \mathbb{R}$ è continua in $[a,b]$ e se $f(a) \cdot f(b) < 0$, allora esiste almeno un punto $c \in ]a,b[$ tale che $f(c)=0$, [[Teorema di esistenza degli zeri]]

- Sia $f:[a,b] \to \mathbb{R}$ una funzione continua che assume due valori $m$ e $M$ in $[a,b]$ con $m <M$, allora assume tutti i valori compresi fra $m$ e $M$, [[Teorema dei valori intermedi]]

- Una funzione $f:A\to\mathbb{R}$ si dice **uniformemente continua** se, per ogni $\epsilon > 0$, esiste un $\delta = \delta(\epsilon)>0$ tale che $|f(x) - f(y)| < \epsilon$ per ogni $x, y \in A$ con $|x-y|<\delta$

