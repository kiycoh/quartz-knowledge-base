---
last modified: 2025-05-26T18:50:00.000Z
related:
  - '[[Varianza campionaria]]'
  - '[[Deviazione statistica standard]]'
tags:
  - machine-learning
  - statistica-inferenziale
  - varianza-campionaria
---
# Definizione di varianza standard
La **varianza** statistica è un *[[Misure di variabilità statistica|indice di dispersione]]* che ==misura quanto i dati (di tipo quantitativo) si discostano dal valore medio==: maggiore è il valore della varianza e tanto più i dati sono dispersi. Nello specifico è la  media degli scarti quadratici dalla media aritmetica:

> [!IMPORTANT] Formula della varianza standard
> $$\sigma^2 = \frac{1}{n} \sum_{i=1}^n (x_i - \bar{x})^2$$
> dove:
> - $x_i$: ogni singolo valore
> - $\bar{x}$: media della popolazione
> - $n$: numero totale dei dati
> - $\sigma^2$: varianza della popolazione
> * **Nota:** Un valore elevato della varianza indica una maggiore dispersione dei dati dalla media, mentre un valore basso indica che i dati sono più concentrati attorno alla media.
> 

> [!EXAMPLE]- Esempio matematico di varianza standard
> Supponiamo che un insegnante abbia testato **tutti gli studenti di una classe** (stiamo considerando l'intera popolazione) e abbia ottenuto questi voti: $X = [6, 8, 10, 10]$.
> 
> 1. **Calcola la media ($\mu$)**:
> $$
> \begin{aligned}
> \mu = \frac{6 + 8 + 10 + 10}{4} = \frac{34}{4} = 8.5
> \end{aligned}
> $$
> 
> 2. **Calcola gli scarti dalla media al quadrato**:
> $$
> \begin{aligned}
> (6 - 8.5)^2 &= 6.25 \\ 
> (8 - 8.5)^2 &= 0.25 \\ 
> (10 - 8.5)^2 &= 2.25 \quad \text{(due volte)}
> \end{aligned}
> $$
> 
> 3. **Somma degli scarti al quadrato**:
> $$
> \begin{aligned}
> 6.25 + 0.25 + 2.25 + 2.25 = 11
> \end{aligned}
> $$
> 
> 4. **Calcola la varianza della popolazione ($\sigma^2$)**:
> $$
> \begin{aligned}
> \sigma^2 = \frac{11}{4} = 2.75
> \end{aligned}
> $$
> 
> 5. **Calcola la [[Deviazione statistica standard|deviazione standard]]**:
> $$
> \begin{aligned}
> \sigma = \sqrt{2.75} \approx 1.66
> \end{aligned}
> $$

> [!EXAMPLE] Esempio codice di varianza standard
> ```python
> >>> import statistics
> >>> dati = [7,5,3,7,6,9,9,6,7,3,3,3,2,4,1]
> >>> statistics.pstdev(dati)
> 2.422120283277993
> ```
