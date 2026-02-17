---
last modified: null
related:
  - '[[Statistica inferenziale]]'
tags:
  - statistica-inferenziale
  - test-statistici
  - statistica-descrittiva
---
# Definizione di Test T di Student
Il **test T di Student** è un [[Test statistici|test statistico]] per valutare se la [[Media campionaria (Statistica)]] differisce in modo significativo da:
* un valore teorico noto
* la media di un altro campione indipendente
* la media di un altro campione appaiato

## Test T per un campione
Verifica se la media di un campione è significativamente diversa da un valore specifico.

$$
t = \frac{\bar{x} - \mu_0}{\frac{s}{\sqrt{n}}}
$$

Dove:
- $\bar{x}$ = media del campione  
- $\mu_0$ = media ipotizzata sotto H₀  
- $s$ = deviazione standard campionaria  
- $n$ = dimensione del campione 

### Gradi di libertà  
$$df = n - 1$$
Poi si confronta il valore di $t$ ottenuto con il valore critico della **t-distribution** (con df = n−1) per il livello di significatività scelto (es. α = 0.05).