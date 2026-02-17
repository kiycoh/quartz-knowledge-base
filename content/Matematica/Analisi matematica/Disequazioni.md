---
tags:
  - machine-learning
  - scienze-cognitive
  - intelligenza-artificiale
---

>[!Definizione]
>Una **disequazione** è una diseguaglianza tra due espressioni letterali e/o numeriche confrontate tra loro rispetto a una relazione d'ordine $(<,>,\le,\ge)$ $$P(x)>Q(x)$$

## Disequazioni di primo grado intere

Consideriamo la seguente disequazione $\displaystyle 2(x+1)-\frac{1}{3}x+1\le x+1$
- $\displaystyle 2x+2-\frac{1}{3}x+1\le x+1$
- $6x-x-3x\le 3 - 6 -3$ 
- $2x\le-6$
- $\displaystyle x\le-3$ 
- La disequazione è valida $\forall x \in \mathbb{R}:x\le -3$ ovvero nell'intervallo $]-\infty,-3]$


**Consideriamo la seguente disequazione $-2x\gt 10$ **

>[!warning] Attenzione
>Quando dividiamo ambi i membri di una disequazione per un numero negativo dobbiamo invertire il verso della disequazione

- $-2x\gt 10$ 
- $x<-5$ 
- La disequazione è valida $\forall x \in \mathbb{R}: x < -5$ ovvero nell'intervallo $]-\infty,-5[$ 


**Consideriamo la seguente disequazione $2x+5>2x$**
- $2x-2x>-5$
- $0x>-5$
  >[!warning] Attenzione
  >Non pensare che la disequazione sia impossibile, poiché ha validità per ogni valore di x
- La disequazione è valida $\forall x \in \mathbb{R}$ ovvero nell'intervallo $]-\infty,+\infty[$ 


**Consideriamo la seguente disequazione $0x>0$**

>[!warning] Attenzione
>La seguente disequazione non ammette soluzione in quanto nessun valore di $x$ moltiplicato per 0 è strettamente maggiore di zero

- La disequazione non è valida in quanto $\nexists x \in \mathbb{R} : 0x>0$ 
## Disequazioni di primo grado fratte

**Consideriamo la seguente disequazione $\displaystyle \frac{x-1}{x+3}>0$**
- Poniamo il numeratore maggiore di zero   $\to\;\;x-1>0$
- $x>1$
- Poniamo il denominatore maggiore di zero   $\to\;\; x+3>0$
- $x>-3$ 
![[Disequazioni 2024-03-23 18.02.26.excalidraw]]
>[!warning] Attenzione
>Il segno della disequazione ci dice per quali valori è valida, in questo caso per i valori strettamente maggiori di 0, quindi consideriamo solo le parti in cui la $x$ è positiva

- La disequazione è valida $\forall x \in \mathbb{R} : x< -3,\;x>1$ ovvero nell'intervallo $]-\infty,-3[\;\cup\;]1,+\infty[$ 

**Consideriamo la seguente disequazione $\displaystyle \frac{x-2}{x+1}\le\frac{1}{2}$** 

>[!warning] Attenzione 
>Dobbiamo sempre ricondurci alla forma $\displaystyle \frac{A(x)}{B(x)}\le 0$ prima di analizzare per quali valori la frazione è positiva

- $\displaystyle \frac{x-2}{x+1}-\frac{1}{2}\le 0$
- $\displaystyle \frac{2(x-2)-(x+1)}{2(x+1)}\le 0$ 
- $\displaystyle \frac{2x-4-x-1}{2(x+1)}\le 0$ 
- $\displaystyle \frac{x-5}{2(x+1)}\le 0$
- $\displaystyle 2\frac{x-5}{2(x+1)}\le0\cdot 2$
- $\displaystyle \frac{x-5}{x+1}\le0$ 
- Poniamo il numeratore maggiore o uguale di zero   $\to\;\;x-5\ge0$
- $x\ge5$ 
- Poniamo il denominatore maggiore di zero   $\to\;\;x+1>0$
- $x>-1$ 
![[Disequazioni 2024-03-23 18.02.26.excalidraw 1]]
- La disequazione è valida $\forall x\in\mathbb{R}:-1\lt x\le 5$ ovvero nell'intervallo $[-1,5]$ 
## Disequazioni di secondo grado

#### Maggiore o maggiore uguale ($\gt, \ge$) 

Consideriamo la generale disequazione di secondo grado $ax^2+bx+c\ge 0$ 

>[!warning] Condizione necessaria per la risoluzione
>Bisogna che il coefficiente del termine di secondo grado ($a$) sia strettamente maggiore di 0, nel caso in cui non lo fosse bisogna invertire il senso della disequazione e cambiare i segni

**Processo di risoluzione:**

- Risolvere l'[[0 Cultura/0.3 Matematica/0.3.1 Analisi matematica/Equazioni di secondo grado|equazione di secondo grado]] a primo membro.

- Se $\Delta >0$, l'equazione ha due soluzioni $x_1\neq x_2$. Se la disequazione è posta a $\ge0$ allora sarà valida per i valori esterni delle due soluzioni, altrimenti se è posta a $\gt0$  sarà valida per i valori esterni alle soluzioni con quest'ultime incluse nell'intervallo
![[Disequazioni 2024-03-23 18.57.44.excalidraw]]

- Per $\gt \;\;\to$   La disequazione è valida $\forall x \in \mathbb{R} : x\le x_1,\; x\ge x_2$ ovvero nell'intervallo $]-\infty,x_1]\cup[x_2,+\infty[$ 
- Per $\ge\;\;\to$   La disequazione è valida $\forall x \in \mathbb{R}:x<x_1,x>x_2$ ovvero nell'intervallo $]-\infty,x_1[\;\cup\;]x_2,+\infty[$ 



- Se $\Delta=0$, l'equazione ha due soluzioni coincidenti $x_1=x_2$. Se la disequazione è posta a $\gt0$ allora sarà valida per i valori esterni alla soluzione, altrimenti se è posta a $\ge$ sarà valida per tutto l'asse reale 
![[Disequazioni 2024-03-23 18.57.44.excalidraw 2]] 
- Per $\gt\;\;\to$   La disequazione è valida $\forall x \in\mathbb{R}:x\neq x_{1,2}$ ovvero nell'intervallo $]-\infty,x_{1,2}[\;\cup\;]x_{1,2}, +\infty[$ 
- Per $\ge\;\;\to$   La disequazione è valida $\forall x \in \mathbb{R}$ ovvero nell'intervallo $]-\infty,+\infty[$ 



- Se $\Delta<0$, l'equazione non ammette soluzioni reali, ma non per questo la disequazione non risulta valida, infatti lo è per $\forall x \in \mathbb{R}$ ovvero nell'intervallo $]-\infty,+\infty[$ 



**Consideriamo la seguente disequazione $2x^2+x-1\ge 0$** 
- Risolviamo l'[[0 Cultura/0.3 Matematica/0.3.1 Analisi matematica/Equazioni di secondo grado|equazione di secondo]] grado a primo membro
  - $\Delta = (1)^2 - 4(2\cdot-1) = 1-4(-2) = 1+8 = 9$
  - Il $\Delta$ è positivo quindi ci aspettiamo due soluzioni reali
  - $\displaystyle \frac{-1\pm\sqrt{9}}{2(2)}=\frac{-1\pm3}{4}=\begin{cases}x_1 =\frac{-4}{4} =-1 \\ x_2=\frac{2}{4}=\frac{1}{2}\end{cases}$ 
  - Disegniamo il grafico   ![[Disequazioni 2024-03-23 18.57.44.excalidraw 1]]
  - Nella disequazione abbiamo un $\ge$ quindi dobbiamo considerare i valori esterni alle due soluzioni, includendo anche le due soluzioni
  - La disequazione è valida $\forall x\in\mathbb{R}:x\le -1, x\ge \frac{1}{2}$ ovvero nell'intervallo $]-\infty,-1]\;\cup\;[\frac{1}{2},+\infty[$ 

```functionplot
---
title: 
xLabel: 
yLabel: 
bounds: [-10,10,-10,10]
disableZoom: false
grid: true
---
f(x)=2x^2+x-1
```



**Consideriamo la seguente disequazione $4x^2-12x+9>0$** 
- Risolviamo l'[[0 Cultura/0.3 Matematica/0.3.1 Analisi matematica/Equazioni di secondo grado|equazione di secondo grado]] a primo membro
  - $\Delta = (-12)^2-4(4\cdot 9)=144-4(36)=144-144=0$
  - Il $\Delta$ è nullo quindi ci aspettiamo due soluzioni reali coincidenti
  - $\displaystyle \frac{12}{2(4)}=\frac{12}{8}=\frac{3}{2}=x_{1,2}$ 
  - Disegniamo il grafico ![[Disequazioni 2024-03-23 18.57.44.excalidraw 2 1]]
  - Nella disequazione abbiamo un $\gt$ quindi dobbiamo considerare i valori esterni alla soluzione
  - La disequazione è valida $\forall x \in \mathbb{R} :x<\frac{3}{2},x>\frac{3}{2}$ ovvero nell'intervallo $]-\infty,\frac{3}{2}[\;\cup\;]\frac{3}{2}, +\infty[$ 

```functionplot
---
title: 
xLabel: 
yLabel: 
bounds: [-10,10,-10,10]
disableZoom: false
grid: true
---
f(x)=4x^2-12x+9
```


```functionplot
---
title: 
xLabel: X
yLabel: Y
bounds: [-10,10,-10,10]
disableZoom: false
grid: true
---
f(x)=(2x+1)/(x^2-2x+1)
```


#### Minore o minore uguale ($\lt,\le$) 

Consideriamo la generale disequazione di secondo grado $ax^2+bx+c\le 0$ 

**Processo di risoluzione:**

- Risolvere l'[[0 Cultura/0.3 Matematica/0.3.1 Analisi matematica/Equazioni di secondo grado|equazione di secondo grado]] a primo membro.

- Se $\Delta >0$, l'equazione ha due soluzioni $x_1\neq x_2$. Se la disequazione è posta a $\lt0$ allora  sarà valida per i valori interni delle soluzioni, altrimenti se è posta a $\le0$ allora lo sarà per i valori interni comprese le due soluzioni 
![[Disequazioni 2024-03-23 18.57.44.excalidraw]]

- Per $\lt \;\;\to$   La disequazione è valida $\forall x \in \mathbb{R} : x_1<x<x_2$ ovvero nell'intervallo $]x_1,x_2[$ 
- Per $\le\;\;\to$   La disequazione è valida $\forall x \in \mathbb{R}:x_1\le x\le x_2$ ovvero nell'intervallo $[x_1,x_2]$ 


- Se $\Delta =0$, l'equazione ha due soluzioni coincidenti $x_1=x_2$. Se la disequazione è posta $\lt0$, allora non esisterà alcuna soluzione, se invece è posta $\le0$, sarà valida solo per $x=x_{1,2}$ 


- Se $\Delta <0$ allora la disequazione non sarà valida per alcun valore di $x$ 


**Consideriamo la seguente disequazione $x^2-x-6\le 0$** 
- Risolviamo l'[[0 Cultura/0.3 Matematica/0.3.1 Analisi matematica/Equazioni di secondo grado|equazione di secondo]] grado a primo membro
  - $\Delta = (-1)^2-4(1\cdot-6)=1-4(-6)=1+24=25$
  - Il $\Delta$ è positivo quindi ci aspettiamo due soluzioni reali
  - $\displaystyle \frac{1\pm\sqrt{25}}{2(1)}=\frac{1\pm5}{2}=\begin{cases}x_1 =\frac{-4}{2} =-2 \\ x_2=\frac{6}{2}=3\end{cases}$  
  - Disegniamo il grafico   ![[Disequazioni 2024-03-23 18.57.44.excalidraw 1 1]]
  - Nella disequazione abbiamo un $\le$ quindi dobbiamo considerare i valori interni alle due soluzioni, includendo anche le due soluzioni
  - La disequazione è valida $\forall x\in\mathbb{R}:-2\le x \le 3$ ovvero nell'intervallo $[-2,3]$ 

```functionplot
---
title: 
xLabel: 
yLabel: 
bounds: [-10,10,-10,10]
disableZoom: false
grid: true
---
f(x)=x^2-x-6
```



**Consideriamo la seguente disequazione $x^2-2x+1<0$** 
- Risolviamo l'[[0 Cultura/0.3 Matematica/0.3.1 Analisi matematica/Equazioni di secondo grado|equazione di secondo grado]] a primo membro
  - $\Delta = (-2)^2-4(1\cdot1)=4-4(1)=4-4=0$ 
  - Il $\Delta$ è nullo quindi dato che è posta $\lt0$ non sarà valida per alcun valore della x
  - Se invece fosse $x^2-2x+1\le0$, possiamo calcolare le soluzioni
  - $\displaystyle \frac{2}{2(1)}=\frac{2}{2}=1=x_{1,2}$ 
  - Disegniamo il grafico ![[Disequazioni 2024-03-23 18.57.44.excalidraw 2 1 1]]
  - Nella disequazione abbiamo un $\le$, quindi la soluzione è l'unico valore per cui è valida
  - La disequazione è valida per $x=1$

```functionplot
---
title: 
xLabel: 
yLabel: 
bounds: [-10,10,-10,10]
disableZoom: false
grid: true
---
f(x)=x^2-2x+1
```



## Disequazioni irrazionali

>[!definizione] 
>Una disequazione si dice irrazionale se l'incognita compare come argomento di almeno una radice $$\Large \sqrt[n]{f(x)}\lesseqgtr g(x)$$


**Processo di risoluzione:**

- Radice ad indice pari
    - Maggiore o maggiore uguale
      1. Risolvere questi due sistemi
      ![[Drawing 2024-03-27 14.16.05.excalidraw|100%]]
      2. 