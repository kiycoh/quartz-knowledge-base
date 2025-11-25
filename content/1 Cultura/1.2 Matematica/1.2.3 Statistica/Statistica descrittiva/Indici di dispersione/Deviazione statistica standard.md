---
last modified: 2025-06-03T17:12:00.000Z
related:
  - '[[Deviazione standard campionaria]]'
tags:
  - statistica-inferenziale
  - deviazione-standard
  - misure-sintesi-statistica
---
# Definizione di deviazione standard
La **deviazione standard** (o **scarto quadratico medio**) è un [[Misure di sintesi statistica#Indici di dispersione|indice di dispersione statistica]] ed è la ==stima di dispersione di una dei dati rispetto alla [[Media aritmetica|media aritmetica]].== Nello specifico è la *radice quadrata della media aritmetica dei quadrati degli scarti dei numeri dalla loro media aritmetica*.

> [!IMPORTANT] Formula per calcolare la deviazione standard
>  $$
>  \sigma = \sqrt{ \frac{1}{N} \sum_{i=1}^{N} (x_i - \mu)^2 },
>  $$
>  
>  dove:
>  - $\sigma$ è lo scarto quadratico medio,
>  - $N$ è il numero totale di elementi,
>  - $x_i$ è ciascun valore della popolazione,
>  - $\mu$ è la media della popolazione.

> [!EXAMPLE]- Esempio svolto di scarto quadratico medio
> 1. Supponiamo di avere un campione di 5 valori $\{5,\ 7,\ 3,\ 7,\ 8\}$, **troviamo la media aritmetica**:
> $$
> \begin{aligned}
> \mu = \frac{5 + 7 + 3 + 7 + 8}{5} = \frac{30}{5} = 6
> \end{aligned}
> $$
> 
> 2. **Calcoliamo le differenze dalla media** e le eleviamo al quadrato:
> $$
> \begin{aligned}
> (5 - 6)^2 &= (-1)^2 = 1 \\  
> (7 - 6)^2 &= (1)^2 = 1 \\  
> (3 - 6)^2 &= (-3)^2 = 9 \\  
> (7 - 6)^2 &= (1)^2 = 1 \\  
> (8 - 6)^2 &= (2)^2 = 4  
> \end{aligned}
> $$
> 3. **Sommiamo i quadrati:**
> 
> $$
> \begin{aligned}
> 1 + 1 + 9 + 1 + 4 = 16
> \end{aligned}
> $$
> 4. **Dividiamo per il numero totale dei dati** ($N = 5$):
> $$
> \begin{aligned}
> \frac{16}{5} = 3.2
> \end{aligned}
> $$
> 5. **Applichiamo la radice quadrata:**
> $$
> \begin{aligned}
> \sigma = \sqrt{3.2} \approx 1.79
> \end{aligned}
> $$
