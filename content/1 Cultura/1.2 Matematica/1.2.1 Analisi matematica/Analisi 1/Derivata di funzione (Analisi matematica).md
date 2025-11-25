---
last modified: 2025, 11, 24 22:11:39
related:
  - '[[Derivata parziale]]'
tags: [analisi-matematica, derivatives, machine-learning]
---
# Definizione di derivata di funzione
In [[Analisi matematica]], la **derivata** di una funzione è definita come limite di un [[rapporto incrementale]], ==la derivata quantifica il tipo di crescita di una funzione==.

> [!note] Derivata come strumento per lo studio di funzione
> Tramite la nozione di derivata possono essere definiti il concetto di [[Il massimo e minimo di una funzione| massimo e minimo di una funzione]], [[La concavità e la convessità|concavità e convessità]]
## Calcolare la derivata di una funzione
Tramite una lista di regole di derivazione è possibile calcolare la derivata di qualsiasi funzione definita combinando funzioni elementari.
# Definizione di derivata
La derivata di una funzione in un punto è il coefficiente angolare della retta tangente alla curva nel punto. Si tratta quindi di un numero che misura la pendenza della retta tangente.

![[Derivata 2024-03-21 19.09.26.excalidraw]]

>Siano $I$ un intervallo aperto e $f:I\to \mathbb{R}$ con $x_0 \in I$, vale che per ogni $x\in I / {x_0}$ definiamo **rapporto incrementale** di $f$ in $x_0$ la quantità
$\large \displaystyle \frac{f(x)-f(x_0)}{x-x_0}=\frac{\Delta f}{\Delta x}$


Possiamo vedere questo rapporto come il tentativo di trovare il coefficiente angolare della retta secante passante per i punti $x$ e $x_0$

![[Derivata 2024-03-21 19.09.26.excalidraw 1]]
Più avviciniamo $x$ a $x_0$, la retta passante per i due punti tenderà ad assumere lo stesso coefficiente della retta tangente alla funzione nel punto $x_0$ 


> Se esiste il limite finito diremo che la funzione $f$ è derivabile in $x_0$ 
$\large \displaystyle \lim_{x \to x_0} \frac{f(x)-f(x_0)}{x-x_0}=f'(x_0)$

>Se $f$ è derivabile in ogni punto di $I$ diremo che la $f$ è derivabile in $I$, potendo ottenere così la funzione derivata prima.


## Regole di derivazione

- Funzioni costanti $\large f(x)=k \;\; \to \;\; f'(x) = 0$
- Funzioni potenza $\large f(x)=x^n \;\; \to \;\; f'(x) = nx^{n-1}$
- Funzioni radice $\displaystyle \large f(x)=\sqrt[2]x \;\; \to \;\; x^{\frac{1}{2}} \;\;\to\;\;\frac{1}{2}x^{\frac{1}{2}-1} \;\; \to \;\; \frac{1}{2}x^{-\frac{1}{2}}\;\;\to\;\;\frac{1}{2(x)^{\frac{1}{2}}}\;\;\to\;\;f'(x)=\frac{1}{2\sqrt[2]x}$
- Funzione seno $f(x)=\sin x \;\; \to \;\; f'(x) = \cos x$
- Funzione coseno $f(x)=\cos x \;\; \to \;\; f'(x) = -\sin x$
- Funzione esponenziale $f(x)=e^x \;\; \to \;\; f'(x) = e^x$
- Funzione esponenziale con base $a$ $f(x)=a^x\;\;\to\;\;f'(x)=a^x\cdot \ln a$
- Funzione logaritmo naturale $f(x)=\ln x \;\; \to \;\; f'(x) = \frac{1}{x}$
- Funzione logaritmo $f(x)=\log_a x\;\;\to\;\;f'(x)=\frac{1}{x \log(a)}$

- Funzione logaritmo di una funzione $f(x)=\log_a(g(x))\;\;\to\;\;f'(x)=\frac{g'(x)}{g(x)}$
- Funzione tangente $f(x)=\tan x = 1+\tan ^2 x\;\;\to\;\;f'(x)=\frac{1}{\cos^2x}$
- Funzione cotangente $f(x)=\cot x = -(1+\cot^2x)\;\;\to\;\;f'(x)=-\frac{1}{\sin^2x}$


Date due funzioni $f,\;g:I\to \mathbb{R}$ derivabili in $x_0 \in I$ con $I$ intervallo aperto sussistono le seguenti regole di derivazione:

- La funzione $\large F(x)=f(x)+g(x)$ ha derivata in $x_0$ data da $\displaystyle \large F'(x_0)=f'(x_0)+g'(x_0)$


- La funzione $\large F(x)=f(x)\cdot g(x)$ ha derivata in $x_0$ data da $\displaystyle \large F'(x_0)=f'(x_0)\cdot g(x_0) + g'(x_0)\cdot f(x_0)$


- La funzione $\displaystyle \large F(x)=\frac{f(x)}{g(x)}$ ha derivata in $x_0$ data da $\displaystyle \large F'(x_0)=\frac{f'(x_0)\cdot g(x_0) - g'(x_0)\cdot f(x_0)}{[g(x_0)]^2}$


- La funzione $\displaystyle \large F(x)=\frac{1}{f(x)}$ ha derivata in $x_0$ data da $\displaystyle \large F'(x_0)=\frac{-f'(x_0)}{[f(x)]^2}$ 


- La funzione $\large F(x)=f^{-1}(x)$ ha derivata in $x_0$ data da $\displaystyle \large F'(f(x_0))=\frac{1}{f'(x_0)}$


- La funzione $\large F(x)=f(g(x))$ ha derivata in $x_0$ data da $\displaystyle \large F'(x_0)=f'(g(x_0))\cdot g'(x_0)$ 

[[11_44_Derivate_2_3.pdf|Regole di derivazione]] |       [[Esercizi derivate|Esercizi svolti]]



![250](https://my.spline.design/untitled-7bc5b0ed7f7169a0639f1efe67297f46/)


