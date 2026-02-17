---
tags:
  - statistica
  - distribuzione-frequenza
  - frequenze-assolute
---

# Definizione di distribuzione di frequenza (Statistica)
Una **distribuzione di frequenza** è una struttura grafica (tabelle o grafici) che condensa e organizza i dati grezzi di una [[Distribuzione statistica|distribuzione]]) al fine di presentare tutte le modalità di un carattere insieme alle loro rispettive frequenze. Sono il punto di partenza per il calcolo degli [[Misure di posizione statistica|indici di posizione]].

| Modalità ($x_1$) | Frequenze assolute ($n_i$) | Frequenze relative ($f_i=\frac{n_i}{n}$) | Frequenze percentuali ($p_i=f_i\cdot100$) | Frequenze assolute cumulate ($N_i=\sum_{j=1}^{i}n_j$) | Frequenze relative cumulate ($F_i=\sum_{j=1}^{i}f_j$) | Frequenze percentuali cumulate ($P_i=\sum_{j=1}^{i}p_j$) |
| ---------------- | -------------------------- | ---------------------------------------- | ----------------------------------------- | ----------------------------------------------------- | ----------------------------------------------------- | -------------------------------------------------------- |
| $x_1$            | $n_1$                      | $f_1$                                    | $p_1$                                     | $n_1$                                                 | $f_1$                                                 | $p_1$                                                    |
| $x_2$            | $n_2$                      | $f_2$                                    | $p_2$                                     | $n_1+n_2$                                             | $f_1+f_2$                                             | $p_1+p_2$                                                |
| $x_3$            | $n_3$                      | $f_3$                                    | $p_3$                                     | $n_1+n_2+n_3$                                         | $f_1+f_2+f_3$                                         | $p_1+p_2+p_3$                                            |
| $\dots$          | $\dots$                    | $\dots$                                  | $\dots$                                   | $\dots$                                               | $\dots$                                               | $\dots$                                                  |
| $x_k$            | $\frac{n_k}{n}$            | $\frac{f_k}{1}$                          | $\frac{p_k}{100}$                         | $n$                                                   | $1$                                                   | $100$                                                    |
dove:
* $x_1, x_2, \dots, x_k$ sono le $k$ modalità del *carattere* (o le classi in cui vengono raggruppate).
* $n_1, n_2, \dots, n_k$ sono le frequenze assolute il cui totale $n$ è il numero complessivo delle *unità statistiche*.
* $f_1, f_2, \dots, f_k$ sono le frequenze relative (ottenute come rapporti tra le frequenze assolute ed il numero complessivo delle unità statistiche) il cui totale è $1$.
* $N_1, N_2, \dots, N_k$ sono le frequenze assolute cumulate (ottenute sommando alla frequenza assoluta della *i*-esima modalità le frequenze assolute delle modalità precedenti).
* $F_1, F_2, \dots, F_k$ sono le frequenze relative cumulate (ottenute sommando alla frequenza relativa della *i*-esima modalità le frequenze relative delle modalità precedenti).

## Tipi di distribuzione
- **[[Frequenza assoluta (Statistica)]]  ($n_j$)**: Il numero di volte in cui una modalità è osservata.
- **[[Frequenza relativa (Statistica)]] ($f_j$)**: La proporzione di osservazioni per una modalità ($n_j/n$).
- **[[Frequenza cumulata (Statistica)]] ($N_j$, $F_j$)**: La somma delle frequenze (assolute o relative) fino a una data modalità, per variabili ordinali o quantitative.
- **Distribuzione per Classi**: Raggruppamento di modalità contigue per variabili quantitative con molte modalità.