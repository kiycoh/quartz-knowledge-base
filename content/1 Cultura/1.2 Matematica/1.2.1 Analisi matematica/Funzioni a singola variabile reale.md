---
last modified: 2024-08-22T18:48:00.000Z
reference: >-
  https://www.youtube.com/watch?v=R0otRo1oMo8&list=PLW4IfhQEjCpKK46Pi5jhcYUUOjQMhzalR
tags:
  - machine-learning
  - scienze-cognitive
  - intelligenza-artificiale
---
==Una funzione a singola variabile reale== ($f$) ==è una relazione tra due [[0 Cultura/0.3 Matematica/0.3.1 Analisi matematica/Insiemi]]==, chiamati **[[Dominio di una funzione|dominio]]** e **codominio**, che associa ad ogni elemento del dominio uno e un solo elemento del codominio.

>[!important] Come funziona?
>La funzione prende qualsiasi valore nel *dominio*, lo elabora e lo associa ad uno e un solo elemento del *codominio*: ciò significa che dato uno stesso criterio (o legge) un numero $x_0$ non può contemporaneamente esprimersi in due valori distinti nell'insieme $Y$ ma solo in uno, inoltre 2 o più valori del dominio possono esprimersi in uno stesso valore nel codominio.

Ad esempio $f: X \to Y \le \mathbb{R}$ (letta come *$f$ definita in $X$ ha valori in $Y$ compresa in $\mathbb{R}$*) è un criterio che associa ogni elemento di $X$ ad uno e un solo valore nell'insieme $Y$.

> [!definizione]
> Una funzione $f$ da un insieme $X$ (dominio) a un insieme $Y$ (codominio) è definita come $f: A \rightarrow B$, tale che per ogni $x \in A$, esiste un unico $y \in B$ tale che $y = f(x)$.

- **Notazione**: La notazione $y = f(x)$ indica che $y$ è l'immagine di $x$ tramite la funzione $f$.
## Tipi di funzioni
**Iniettive**: Una funzione è iniettiva se elementi distinti del dominio hanno immagini distinte nel codominio. Formalmente, $f: X \rightarrow Y$ è iniettiva se $f(x_1) = f(x_2) \Rightarrow x_1 = x_2$ per ogni $x_1, x_2 \in A$.
 ![[Funzioni a singola variabile reale 2024-03-23 08.08.48.excalidraw 1]]

**Suriettive**: Una funzione è suriettiva se ogni elemento del codominio è immagine di almeno un elemento del dominio. Formalmente, $f: X \rightarrow Y$ è suriettiva se per ogni $y \in B$, esiste un $x \in A$ tale che $f(x) = y$.
![[Funzioni a singola variabile reale 2024-03-23 08.08.48.excalidraw]]

**Biunivoche (o Biiettive)**: Una funzione è biiettiva se è sia iniettiva che suriettiva. Questo significa che esiste una corrispondenza uno-a-uno tra gli elementi del dominio e quelli del codominio.
![[Funzioni a singola variabile reale 2024-03-23 08.08.48.excalidraw 1 1]]


## Operazioni sulle Funzioni
**Inversa**: Se una funzione $f: X \rightarrow Y$ è biiettiva, allora esiste la sua funzione inversa $f^{-1}: Y \rightarrow X$ tale che $f^{-1}(f(x)) = x$ per ogni $x \in X$ e $f(f^{-1}(y)) = y$ per ogni $y \in Y$. 
    
**Composizione**: Data due funzioni $f: X \rightarrow Y$ e $g: Y \rightarrow Z$, la composizione $g \circ f$ è definita come $(g \circ f)(x) = g(f(x))$ per ogni $x \in X$. 
![[0 Cultura/0.3 Matematica/0.3.1 Analisi matematica/Esempio funzioni composte]] 

## Limiti e Continuità
- **[[0 Cultura/0.3 Matematica/0.3.1 Analisi matematica/Limiti di funzioni|Limite]]**: Il limite di $f(x)$ per $x$ che tende a $a$ è il valore a cui $f(x)$ si avvicina man mano che $x$ si avvicina ad $a$.
- **[[0 Cultura/0.3 Matematica/0.3.1 Analisi matematica/Funzioni continue|Continuità]]**: Una funzione $f(x)$ è continua in un punto $a$ se il limite di $f(x)$ per $x$ che tende ad $a$ è uguale a $f(a)$.


### Funzioni Limitate

Una funzione $f: X \rightarrow \mathbb{R}$ è **limitata superiormente** se esiste un numero reale $M$ tale che $f(x) \leq M$ per ogni $x \in X$. Analogamente, $f$ è **limitata inferiormente** se esiste un numero reale $m$ tale che $f(x) \geq m$ per ogni $x \in X$. Se una funzione è sia limitata superiormente che inferiormente, allora è semplicemente detta **limitata**.

- **Esempio Limitato Superiormente**: La funzione $f(x) = \sin(x)$ è limitata superiormente da $M = 1$ perché $\sin(x) \leq 1$ per ogni $x \in \mathbb{R}$.
```functionplot
---
title: 
xLabel: 
yLabel: 
bounds: [-2,2,-2,2]
disableZoom: true
grid: true
---
f(x) = sin(x)
g(x) = 1
```

- **Esempio Limitato Inferiormente**: La funzione $f(x) = \exp(x)$ è limitata inferiormente da $m = 0$ poiché $\exp(x) > 0$ per ogni $x \in \mathbb{R}$.

```functionplot
---
title: 
xLabel: 
yLabel: 
bounds: [-10,10,-10,10]
disableZoom: true
grid: true
---
f(x) = exp(x)
g(x) = 0
```

#### Funzioni Illimitate

Una funzione è **illimitata superiormente** se, per ogni numero reale $M$, esiste un $x \in A$ tale che $f(x) > M$. Analogamente, è **illimitata inferiormente** se, per ogni numero reale $m$, esiste un $x \in A$ tale che $f(x) < m$. Una funzione è considerata **illimitata** se è illimitata almeno in una direzione (superiormente o inferiormente).

- **Esempio Illimitata Superiormente**: La funzione $f(x) = x^2$ è illimitata superiormente perché, per ogni $M > 0$, esiste sempre un $x$ tale che $x^2 > M$.

```functionplot
---
title: 
xLabel: 
yLabel: 
bounds: [-10,10,-5,10]
disableZoom: true
grid: true
---
f(x) = x^2
```

- **Esempio Illimitata Inferiormente**: La funzione $f(x) = -x^3$ è illimitata inferiormente perché, per ogni $m < 0$, esiste sempre un $x$ tale che $-x^3 < m$.

```functionplot
---
title: 
xLabel: 
yLabel: 
bounds: [-10,10,-10,10]
disableZoom: true
grid: true
---
f(x) = -x^3
```
