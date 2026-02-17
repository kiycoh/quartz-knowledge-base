---
tags:
  - matematica
  - limiti-funzioni
  - teorema-di-unicità
---


>[!definizione ]
>Il teorema afferma che se una funzione $f(x)$ ha un limite quando $x$ si avvicina a un punto $c$, allora quel limite è unico. In altre parole, se esistono limiti $L$ e $M$ tali che $\lim_{x \to c} f(x) = L$ e $\lim_{x \to c} f(x) = M$, allora $L = M$.
>- Se $\lim_{x \to c} f(x) = L$ e $\lim_{x \to c} f(x) = M$, allora $L = M$.

### Dimostrazione:

1. Supponiamo per assurdo che $L \neq M$.
2. Per la definizione di limite, per ogni $\varepsilon > 0$ esistono $\delta_L > 0$ e $\delta_M > 0$ tali che $|f(x) - L| < \varepsilon$ quando $0 < |x - c| < \delta_L$ e $|f(x) - M| < \varepsilon$ quando $0 < |x - c| < \delta_M$.
3. Scegli un $\varepsilon$ piccolo, ad esempio $\varepsilon = \frac{|L - M|}{2}$.
4. Scegli $\delta = \min(\delta_L, \delta_M)$. Per $0 < |x - c| < \delta$, sia $|f(x) - L| < \varepsilon$ che $|f(x) - M| < \varepsilon$ devono essere veri, il che porta a una contraddizione.

### Esempi:

- Considera la funzione $f(x) = \frac{\sin(x)}{x}$ per $x \neq 0$ e $f(0) = 1$. Il limite di $f(x)$ mentre $x$ si avvicina a 0 è 1, e per il teorema di unicità, non può esistere un altro limite diverso da 1.

```functionplot
---
title: 
xLabel: 
yLabel: 
bounds: [-10,10,-10,10]
disableZoom: false
grid: true
---
f(x) = sin(x)/x
```
