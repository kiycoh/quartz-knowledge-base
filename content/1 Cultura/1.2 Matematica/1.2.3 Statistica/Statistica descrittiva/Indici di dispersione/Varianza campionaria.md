---
tags:
  - statistica-inferenziale
  - statistica-descrittiva
  - varianza-campionaria
---

# Definizione di varianza campionaria

> [!IMPORTANT] Formula della varianza standard campionaria
> La **varianza campionaria** è simile alla *varianza* ma si considera un [[Campionamento statistico#Definizione di campione statistico|campione]] della popolazione:
> $$
> s^2 = \frac{1}{n - 1} \sum_{i=1}^{n} (x_i - \bar{x})^2
> $$
> dove:
> - $x_i$: ogni singolo valore
> - $\bar{x}$: media del campione
> - $n$: numero campionario dei dati
> - $s^2$: varianza della popolazione
> - **Nota:** La *[[Correzione di Bessel]]* ($n-1$ invece di $n$) è utile per rendere la varianza una *stima imparziale* della varianza della popolazione.

> [!EXAMPLE] Esempio di codice di deviazione standard campionaria
>```python
> >>> import statistics
> >>> dati = [7,5,3,7,6,9,9,6,7,3,3,3,2,4,1]
> >>> statistics.stdev(dati)
> 2.5071326821120348
>```

> [!EXAMPLE]- Esempio di deviazione standard campionaria
> Supponiamo di prendere **un campione di 4 studenti** da un gruppo più grande e raccogliere i seguenti voti: $X = [5, 7, 8, 10]$.
> 
> 1. **Media del campione ($\bar{x}$)**:
> $$
> \begin{aligned}
> \bar{x} = \frac{5 + 7 + 8 + 10}{4} = \frac{30}{4} = 7.5
> \end{aligned}
> $$
> 
> 2. **Scarti al quadrato dalla media**:
> $$
> \begin{aligned}
> (5 - 7.5)^2 &= 6.25 \\
> (7 - 7.5)^2 &= 0.25 \\
> (8 - 7.5)^2 &= 0.25 \\
> (10 - 7.5)^2 &= 6.25
> \end{aligned}
> $$
> 
> 3. **Somma degli scarti al quadrato**:
> $$
> \begin{aligned}
> 6.25 + 0.25 + 0.25 + 6.25 = 13
> \end{aligned}
> $$
> 
> 4. **Calcola la varianza campionaria ($s^2$)**:
> $$
> \begin{aligned}
> s^2 = \frac{13}{n - 1} = \frac{13}{3} \approx 4.33
> \end{aligned}
> $$
> 
> 5. **Deviazione standard campionaria**:
> $$
> \begin{aligned}
> s = \sqrt{4.33} \approx 2.08
> \end{aligned}
> $$
