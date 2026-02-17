---
tags:
  - algebra-relazionale
  - funzione-matematica
  - programmazione-funzionale
---

Consideriamo:
$$f(x) = x^2 \;\;e\;\; g(x)=2x$$
```functionplot
---
title: 
xLabel: 
yLabel: 
bounds: [-10,10,-10,10]
disableZoom: false
grid: true
---
f(x)=x^2
g(x) = 2x
```

Risulta:
- $(g \;\circ f)(x) = g(f(x)) = g(x^2) = 2x^2$
- $(f\;\circ g)(x)=f(g(x))=f(2x)=4x^2$ 

```functionplot
---
title: 
xLabel: 
yLabel: 
bounds: [-10,10,-5,10]
disableZoom: true
grid: true
---
f(x) = 2x^2
g(x) = 4x^2
```

Notiamo quindi come $(g\;\circ f)(x) \neq (f\;\circ g)(x)$ 