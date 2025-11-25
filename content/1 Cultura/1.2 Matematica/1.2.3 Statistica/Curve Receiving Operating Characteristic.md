---
tags:
  - machine-learning
  - classificazione-binaria
  - receiver-operating-characteristic
---

# Definizione di curva Receiver Operating Characteristic (ROC)
Le **ROC curve** (Receiver Operating Characteristic) servono a **valutare quanto è buono un classificatore binario** quando si **varia la soglia di decisione**.

![[Pasted image 20250331105630.png]]

Un [[Classificatore bi nario]] spesso **non restituisce direttamente 0 o 1**, ma una **probabilità**:

> "Con il 72% di probabilità, questa email è spam"

Poi, si decide una **soglia (threshold)**: ad esempio, se la probabilità è **≥ 0.5**, allora diciamo "spam" (classe 1), altrimenti "non spam" (classe 0).

Ma se cambi la soglia, **cambiano anche gli errori** che fai!  
La curva ROC serve proprio per **vedere come si comporta il modello al variare della soglia**.


> [!EXAMPLE] Esempio
> | Caso | Classe reale | Probabilità (classe 1) |
|------|--------------|------------------------|
| A    | 1            | 0.95                   |
| B    | 0            | 0.90                   |
| C    | 1            | 0.85                   |
| D    | 0            | 0.40                   |
| E    | 1            | 0.20                   |
> Ora vari la soglia da 1 $\to$ 0 e a ogni passo calcoli **TPR** e **FPR**, e li disegni nel grafico. Il risultato è la curva ROC.
