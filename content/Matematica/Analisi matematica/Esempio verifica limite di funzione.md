---
tags:
  - machine-learning
  - limiti-funzioni
  - funzione-matematica
---

Consideriamo $\Large \displaystyle \lim_{x\to 2} (3x-1) = 5$ 

![[Esempio limite di funzione 2024-03-13 23.17.29.excalidraw]]
## Risoluzione

1. $\Large |3x-6|<\epsilon$ 

2. $\Large-\epsilon < 3x-6<\epsilon$ 

3. $\Large 6-\epsilon < 3x <6 +\epsilon$ 

4. $\Large \displaystyle 2 - \frac{\epsilon}{3} < x < 2 + \frac{\epsilon}{3}$ 

___ 

Consideriamo $\Large \displaystyle \lim_{x\to0} 2^x =1$ 

```functionplot
---
title: 
xLabel: 
yLabel: 
bounds: [-5,5,-1,5]
disableZoom: true
grid: true
---
f(x)=2^x

```

## Risoluzione

1. $\Large 1-\epsilon < 2^x < 1+\epsilon$ 
2. $\Large \log_2 (1-\epsilon)<x<\log_2(1+\epsilon)$ 