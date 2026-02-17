---
tags:
  - statistica-inferenziale
  - statistica-descrittiva
  - coefficiente-di-variazione
---

# Definizione di coefficiente di variazione
Il **coefficiente di variazione (CV)** è un [[Misure di sintesi statistica#Indici di dispersione|indice di dispersione]] che indica ==quanto è "variabile" un insieme di dati rispetto alla sua media==. È molto utile per confrontare la variabilità tra **dataset con scale diverse**.

$$
\begin{aligned}
CV = \frac{\sigma}{\mu} \times 100
\end{aligned}
$$
dove:
- $\sigma$: deviazione standard della **popolazione**
- $\mu$: media della **popolazione**
- Il risultato viene moltiplicato per 100 per esprimerlo in **percentuale (%)**

> [!QUESTION] Come interpretare il risultato?
> - **CV alto:** maggiore variabilità rispetto alla media;
> - **CV basso:** minore variabilità, i dati sono più "concentrati" attorno alla media.

> [!EXAMPLE]- Esempio di coefficiente di variazione
> Consideriamo due campioni:
> - *Campione A*: ha media $\bar{x} = 50$ e deviazione standard $s = 10$
> - *Campione B*: ha media $\bar{x} = 5$ e deviazione standard $s = 2$
> 
> $$
> \begin{aligned}
> \text{Campione A: }CV_A &= \frac{10}{50} \times 100 = 20\% \\
> \text{Campione B: }CV_B &= \frac{2}{5} \times 100 = 40\%
> \end{aligned}
> $$
> 
> **Conclusione**: Anche se il campione B ha una deviazione standard più piccola, ha una **variabilità relativa maggiore** rispetto alla sua media.
## Definizione di coefficiente di variazione campionaria
Il **coefficiente di variazione campionaria (CV)** dice quanto è "variabile" un campione di dati rispetto alla sua media.
$$
\begin{aligned}
CV = \frac{s}{\bar{x}} \times 100
\end{aligned}
$$
dove:
- $s$: deviazione standard del **campione**
- $\bar{x}$: media del **campione**
- Il risultato viene moltiplicato per 100 per esprimerlo in **percentuale (%)**