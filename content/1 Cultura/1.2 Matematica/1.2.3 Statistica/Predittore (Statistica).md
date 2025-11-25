---
last modified: 2025, 11, 24 16:11:59
tags:
  - machine-learning
  - bayesian-methods
  - statistical-modeling
---

# Definizione di predittore

## Tipi di predittori e problematiche    
- **Predittori continui**: Possono essere gestiti assumendo che seguano una distribuzione normale (come nel Gaussian Naive Bayes) o utilizzando stime non parametriche della densità, come istogrammi o Kernel Density Estimation.
- **Predittori categorici**: Le probabilità condizionate vengono stimate direttamente dalle proporzioni osservate nel training set.
 - **Problema delle probabilità zero (Smoothing)**: Se una particolare combinazione caratteristica-classe non è presente nei dati di addestramento, la probabilità condizionata risulterebbe zero, azzerando l'intera probabilità a posteriori della classe. Per ovviare a ciò, si utilizza una tecnica di smoothing (lisciamento) come il Laplace Smoothing (add-one), aggiungendo un piccolo valore ($\alpha$) ai conteggi.
- **Caratteristiche correlate**: La forte assunzione di indipendenza è spesso violata nei dareali. Se le caratteristiche sono fortemente correlate, le prestazioni del modello possono risentirne significativamente. Le soluzioni includono la selezione delle caratteristiche, trasformazioni delle stesse (es. PCA) o l'utilizzo di modelli più complessi come le Reti Bayesiane.