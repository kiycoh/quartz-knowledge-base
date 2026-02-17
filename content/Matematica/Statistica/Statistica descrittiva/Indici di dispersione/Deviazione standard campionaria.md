---
last modified: 2025-06-03T17:17:00.000Z
related:
  - '[[Deviazione statistica standard]]'
tags:
  - statistica-descrittiva
  - deviazione-standard-campionaria
  - variabilita-statistica
---
# Definizione la deviazione standard campionaria

La **deviazione standard campionaria (o scarto quadratico medio campionario)** è una [[Indici di variabilità (Statistica)|misura di variabilità]] (o **dispersione**) dei dati in un **campione**. In parole semplici, ti dice ==quanto i dati si allontanano in media dalla media del campione.==

> [!WARNING] Formula per calcolare la la deviazione standard campionaria
> 
> $$
> s = \sqrt{\frac{1}{n - 1} \sum_{i=1}^{n} (x_i - \bar{x})^2}
> $$
> 
> Dove:
> 
> - $x_i$ = ogni singolo valore del campione  
> - $\bar{x}$ = media del campione  
> - $n$ = numero di dati nel campione  
> - La somma $\sum$ è fatta per tutti i dati 
> - Si divide per $n - 1$ (e non per $n$) perché si tratta di un **[[Campione statistico|campione]]**, non dell’intera popolazione. Questo serve per correggere una distorsione chiamata **[[Bias]]**.
 
> [!EXAMPLE]- Esempio svolto di scarto quadratico medio campionario
> 1. Supponiamo di avere un campione di 5 valori $\{4,\ 6,\ 8,\ 6,\ 10\}$, **troviamo la media aritmetica**:
> $$
> \bar{x} = \frac{4 + 6 + 8 + 6 + 10}{5} = \frac{34}{5} = 6.8
> $$
> 2. **Troviamo le differenze dalla media** e le eleviamo al quadrato:
> $$
> \begin{aligned}
> (4 - 6.8)^2 &= (-2.8)^2 = 7.84 \\  
> (6 - 6.8)^2 &= (-0.8)^2 = 0.64 \\  
> (8 - 6.8)^2 &= (1.2)^2 = 1.44 \\  
> (6 - 6.8)^2 &= (-0.8)^2 = 0.64 \\  
> (10 - 6.8)^2 &= (3.2)^2 = 10.24  
> \end{aligned}
> $$
> 3. **Sommiamo i quadrati delle differenze**:
> $$
> 7.84 + 0.64 + 1.44 + 0.64 + 10.24 = 20.8
> $$
> 4. **Dividiamo per $n - 1 = 4$**:
> $$
> \frac{20.8}{4} = 5.2
> $$
> 5. **Facciamo la radice quadrata**:
> $$
> s = \sqrt{5.2} \approx 2.28
> $$