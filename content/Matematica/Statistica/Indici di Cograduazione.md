---
tags:
  - statistica-informatica
  - correlazione-lineare
  - statistica-descrittiva
---

Gli **indici di cograduazione** sono strumenti statistici utilizzati per misurare l'associazione tra due variabili che sono state espresse in termini di **ranghi**. Questi indici sono particolarmente utili quando le variabili sono di natura **ordinale** o quando, pur essendo quantitative, i loro valori grezzi vengono trasformati in ranghi per analizzare l'associazione basata sull'ordinamento piuttosto che sui valori assoluti. La trasformazione in ranghi può anche rendere le misure di correlazione più stabili rispetto agli outlier.

### Ranghi: Posizione di un'unità in una serie ordinata

Un **rango (rank)** è la **posizione** che un'unità statistica occupa all'interno di una serie di valori ordinata, in modo crescente o decrescente, rispetto a una determinata caratteristica.

**Assegnazione dei ranghi:**

1. Il primo passo per convertire i valori grezzi in ranghi consiste nell'ordinare i valori e assegnare a ciascuno un rango intero, tipicamente da 1 a $n$, dove $n$ è il numero di osservazioni.
2. In caso di **valori a pari merito (ties)**, le fonti suggeriscono diverse pratiche:
    - Le fonti menzionano la possibilità di **rompere arbitrariamente i pari merito** nell'assegnazione dei ranghi.
    - Successivamente, i ranghi dei valori a pari merito vengono **mediati**, risultando in ranghi che possono essere frazionari. Ad esempio, se i ranghi 2, 3, 4 e 5 sono a pari merito nel valore grezzo, vengono tutti sostituiti da quattro occorrenze di (2+3+4+5)/4 = 3.5.

**Implicazioni per variabili ordinali:**

- Il passaggio ai ranghi per variabili qualitative ordinali implica l'**ipotesi di uguale distanza tra le modalità**.

### $\rho$ di Spearman (Coefficiente di Correlazione per Ranghi di Spearman)

Il **coefficiente di correlazione per ranghi di Spearman** ($\rho_s$ o $\hat{\rho}_{sXY}$) è una misura dell'**associazione tra due graduatorie** (ranghi).

**Calcolo e interpretazione:**

- Il coefficiente di Spearman si ottiene **sostituendo i valori numerici grezzi con i loro ranghi** e calcolando quindi il **coefficiente di correlazione di Pearson tra questi ranghi**.
- La formula per il coefficiente di Spearman è: $\hat{\rho}_{sXY} = \frac{\sum_{i=1}^{n}(a_i - \hat{\mu}_A)(b_i - \hat{\mu}_B)}{\sqrt{\sum_{i=1}^{n}(a_i - \hat{\mu}_A)^2}\sqrt{\sum_{i=1}^{n}(b_i - \hat{\mu}_B)^2}}$ dove $a_i$ è il rango di $x_i$ e $b_i$ è il rango di $y_i$.
- Esiste anche una formula semplificata che si applica quando non ci sono pari merito, utilizzando la differenza tra i ranghi $d_i = r_{X_i} - r_{Y_i}$: $\rho_s = 1 - \frac{6 \sum_{i=1}^{n} (d_i^2)}{n(n^2 - 1)}$ dove $\hat{\mu}_A$ e $\hat{\mu}_B$ (le medie dei ranghi) sono ciascuna $(n+1)/2$.
- Il valore di $\rho_s$ varia tra **-1 e 1**.
    - Un valore vicino a +1 indica una **forte associazione positiva** (le graduatorie tendono a essere simili).
    - Un valore vicino a -1 indica una **forte associazione negativa** (le graduatorie tendono a essere opposte).
    - Un valore vicino a 0 indica l'**assenza di una forte associazione basata sui ranghi**.
- Il coefficiente di Spearman è legato alla **distanza di Spearman**, una misura della differenza tra due classifiche, definita come $d_S(r, s) = \sqrt{\sum_{i=1}^{M} (r_i - s_i)^2}$.

### $\tau$ di Kendall (Coefficiente di Correlazione per Ranghi di Kendall)

Il **coefficiente di correlazione per ranghi di Kendall** ($\tau$ o $\hat{\tau}_{XY}$) è un'altra misura popolare di correlazione per ranghi. Esso indica **quante volte le coppie di osservazioni hanno lo stesso ordinamento di rango tra due attributi**, misurando la **concordanza o discordanza** tra le coppie di ranghi.

**Concetti chiave per il calcolo:**

- Una coppia di osservazioni $(i, j)$ è detta **concordante** se $x_i$ e $x_j$ hanno lo stesso ordinamento di rango di $y_i$ e $y_j$.
- Una coppia di osservazioni $(i, j)$ è detta **discordante** se $x_i$ e $x_j$ hanno un ordinamento di rango diverso da $y_i$ e $y_j$.
- Se $x_i = x_j$ o $y_i = y_j$, la coppia non è né concordante né discordante (in caso di pari merito, il termine $\text{sign}{(x_i - x_j)(y_i - y_j)}$ sarà 0).
- Per il calcolo di $\tau$, spesso si ordina la prima variabile in senso crescente. Successivamente, si contano per la seconda variabile:
    - **C (numero di coppie concordanti)**: Il numero di valori maggiori di $y_i$ che seguono l'ordinamento naturale.
    - **D (numero di coppie discordanti)**: Il numero di valori minori di $y_i$.

**Formula e interpretazione:**

- La formula per il coefficiente di Kendall è: $\hat{\tau}_{XY} = \frac{\sum_{i=1}^{n} \sum_{j=i+1}^{n} \text{sign}{(x_i - x_j)(y_i - y_j)}}{n(n - 1)/2}$ o, in termini di C e D: $\tau = \frac{C - D}{n(n - 1)/2}$
- Il coefficiente di Kendall è la **differenza normalizzata tra il numero di coppie concordanti e il numero di coppie discordanti**, dove il fattore di normalizzazione è il numero totale di coppie.
- Il valore di $\tau$ varia tra **-1 e 1**.
    - Un valore vicino a +1 indica una **forte concordanza** (ordinamento simile tra le variabili).
    - Un valore vicino a -1 indica una **forte discordanza** (ordinamento opposto tra le variabili).
    - Un valore vicino a 0 indica una **debole associazione basata sulla concordanza delle coppie**.
- Il coefficiente di Kendall è legato alla **distanza di Kendall**, una misura della differenza tra due classifiche, definita come $d_K(r, s) = #{(i, j), i < j, (r_i - r_j)(s_i - s_j) < 0}$.

In sintesi, mentre il $\rho$ di Spearman misura la correlazione lineare tra i ranghi, il $\tau$ di Kendall si concentra sulla proporzione di coppie concordanti e discordanti, offrendo prospettive leggermente diverse sull'associazione basata sull'ordinamento dei dati.