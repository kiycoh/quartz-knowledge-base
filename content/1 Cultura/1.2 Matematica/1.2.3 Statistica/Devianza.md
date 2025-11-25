---
tags:
  - machine-learning
  - statistica-inferenziale
  - devianza
---

# Definizione di devianza
La **devianza** (o **somma dei quadrati degli scarti della media**, o ancora **somma dei quadrati**) è un [[Misure di variabilità statistica|indice di dispersione]] dell'adattamento di un modello ai dati.
In pratica, confronta il **modello stimato** con un **modello perfetto** (detto _modello saturo_, che spiega perfettamente i dati). Più è alta la devianza, peggiore è l’adattamento del modello.

> È simile al concetto di **somma dei quadrati dei residui** nella regressione lineare, ma più generale e adatto a modelli come la [[Regressione logistica]].

> [!IMPORTANT] Formula della devianza
> $$SS= \sum_{i=1}^{n}(x_i-\mu)^2$$
> Dove:
> * $\mu$ è la media dei dati.

## Tipi di devianza
1. **Null deviance** (**devianza nulla**):  
   È la devianza di un modello che **non ha predittori**, cioè un modello che usa solo la media (o proporzione nel caso binario).

2. **Residual deviance** (**devianza residua**):  
   È la devianza del **modello con i predittori** inclusi. Ci dice quanto del comportamento dei dati **non è stato spiegato** dal modello.

3. **Explained deviance** (**devianza spiegata**):  
   È la parte della devianza nulla che il modello riesce a spiegare. Si calcola così: