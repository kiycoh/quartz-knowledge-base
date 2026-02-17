---
last modified: null
related:
  - '[[Matrice di confusione]]'
tags:
  - machine-learning
  - misclassificazione
  - matrice-di-confusione
---

# Definizione di misura di misclassificazione
La **misura di misclassificazione** è una **metrica** che indica **quanto spesso il modello sbaglia a classificare** un'osservazione. In parole semplici, misura **la percentuale di errori** che fa il nostro classificatore.

$$
\text{Misclassificazione} = \frac{\text{Numero di previsioni sbagliate}}{\text{Totale delle previsioni}}
$$
## Calcolare misclassificazione dalla [[Matrice di confusione]]
$$
\begin{aligned}
\text{Errori Totali} &= FP + FN \\
\text{Totale Previsioni} &= TP + TN + FP + FN \\
\text{Misclassificazione} &= \frac{FP + FN}{TP + TN + FP + FN}
\end{aligned}.
$$
