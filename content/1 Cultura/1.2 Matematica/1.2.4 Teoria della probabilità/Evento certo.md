---
tags:
  - algoritmi-ordinamento
  - classificazione-statistica
  - matrice-di-confusione
---

# Partizione dell'evento certo
Data una famiglia di eventi $\{E_1, E_2, \dots, E_n\}$ non impossibili, questa costituisce una partizione dell'evento certo ($\Omega$) se valgono le seguenti proprietà:
1. Solo uno degli eventi può essere vero: $E_1 \cup E_2 \cup \dots \cup E_n \Rightarrow \sum_{i=1}^{n}|E_i|= |E_1| + |E_2| + \dots + |E_n| = 1$.
2. Eventi a due a due incompatibili se $E_i \cup E_j = \varnothing \text{ con } i \neq j$ quindi se ogni intersezione tra due eventi è un evento impossibile: $|E_1 \cup E_2 \cup \dots \cup E_n| = |E_1|+|E_2|+\dots+|E_n|$.