---
tags:
  - frequenza-cumulata
  - statistica-descrittiva
  - analisi-statistica
---

# Definizione di frequenza cumulata assoluta
La **frequenza cumulata ($N$)** di un valore è la **somma delle frequenze assolute** di tutti i valori **fino a quel valore** (incluso).
* Questa misura è fondamentale per il calcolo di [[Indici di posizione]] come la mediana e i quantili. La mediana è la modalità o classe per cui la frequenza relativa cumulata è pari o superiore a 0.5, mentre un quantile di ordine $\alpha$ è il valore $q_\alpha$ tale che $F(q_\alpha) = \alpha$.
* Le frequenze cumulate permettono di rispondere alla domanda: "quante unità statistiche presentano una modalità inferiore o uguale a $x_j$?"

In altre parole dice **quante osservazioni** sono **minori o uguali** a quel valore. 

> [!IMPORTANT] Formula della frequenza cumulata assoluta
> 
> $$
> F_j = f_1 + f_2 + \dots + f_j = \sum_{k=1}^{j} f_k
> $$
> dove: 
> * $f_k = \frac{n_k}{n}$ è la frequenza relativa della $k$-esima modalità o classe,
> * $n_k$ è la frequenza assoluta della $k$-esima modalità,
> * $n$ è il numero totale di osservazioni.

> [!EXAMPLE]- Esempio di frequenza cumulata
> Hai questi dati (numerici e ordinati):
> 
> | Valore $x_i$ | Frequenza assoluta $f_i$ |
> |----------------|----------------------------|
> | 1              | 2                          |
> | 2              | 3                          |
> | 3              | 4                          |
> | 4              | 1                          |
> Ora calcoliamo la **frequenza cumulata**:
> 
> | Valore $x_i$ | $f_i$ | Frequenza cumulata $F_i$ |
> | -------------- | ------- | -------------------------- |
> | 1              | 2       | 2                          |
> | 2              | 3       | 2 + 3 = 5                  |
> | 3              | 4       | 5 + 4 = 9                  |
> | 4              | 1       | 9 + 1 = 10                 |
> Questo significa che **fino al valore 3 incluso**, ci sono **9 osservazioni**.
## Definizione di frequenza cumulata relativa
Esiste anche la **frequenza cumulata relativa ($F$)**, che è la *somma cumulata* delle frequenze **relative**:
$$
F_i^r = \sum_{j=1}^{i} f_j^r = \frac{F_i}{n}
$$

