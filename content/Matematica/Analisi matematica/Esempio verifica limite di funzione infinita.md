---
tags:
  - algebra-lineare
  - limiti-funzioni
  - matematica
---

Consideriamo $\Large \displaystyle \lim_{x\to 3} \frac{1}{(x-3)^2} = +\infty$


```functionplot
---
title: 
xLabel: 
yLabel: 
bounds: [-5,10,-1,10]
disableZoom: true
grid: true
---
f(x) = 1/(x-3)^2

```
## Risoluzione

1. $\Large \displaystyle \frac{1}{(x-3)^2}>+M$ 
2. $\displaystyle \Large (x-3)^2<\frac{1}{M}$ 
3. $\displaystyle \Large |x-3|<\frac{1}{\sqrt{M}}$ 
4. $\displaystyle \Large -\frac{1}{\sqrt{M}} < x-3<\frac{1}{\sqrt{M}}$
1. $\displaystyle \Large 3 - \frac{1}{\sqrt{M}} < x< 3 +\frac{1}{\sqrt{M}}$ 

---

Consideriamo $\Large \displaystyle \lim_{x\to 0^+} e^{\frac{1}{x}} = +\infty$

```functionplot
---
title: 
xLabel: 
yLabel: 
bounds: [-10,10,-10,10]
disableZoom: true
grid: true
---
f(x)=2.71^(1/x)
```

## Risoluzione

1. $\displaystyle \Large e^{\frac{1}{x}}>+M$
2. $\displaystyle \Large \ln e^{\frac{1}{x}} > \ln M$ 
3. $\displaystyle \large \frac{1}{x} >\ln M$
4. $\displaystyle \Large 0<x<\frac{1}{\ln M}$ 
