---
tags:
  - statistica-inferenziale
  - statistica-descrittiva
  - correlazione-lineare
---



La **correlazione lineare** per variabili quantitative è un concetto fondamentale nella statistica che descrive la **forza** e la **direzione** di una relazione lineare tra due variabili. Quando si studiano due variabili, come ad esempio il rischio di infarto e il numero di sigarette fumate al giorno, o l'età di un'automobile usata e il suo valore di vendita, si è interessati a quantificare la loro dipendenza. A differenza delle relazioni deterministiche, le relazioni statistiche sono affette da incertezza, il che significa che a ogni valore di una variabile possono esserne associati più di uno dell'altra.

### Covarianza: Misura la variazione congiunta di due variabili

La **covarianza** di due variabili casuali $X$ e $Y$, denotata come $\text{Cov}(X, Y)$, misura la **variazione congiunta** di queste variabili. È definita come il valore atteso del prodotto degli scarti di ciascuna variabile dalla propria media: $\text{Cov}[X, Y] = E[(X - E[X])(Y - E[Y])]$.

Una formula alternativa e spesso più pratica per il calcolo della covarianza è: $\text{Cov}(X, Y) = E[XY] - E[X]E[Y]$.

**Cosa misura la covarianza:** La covarianza indica se valori superiori alla media di una variabile tendono a verificarsi con valori superiori alla media dell'altra variabile (e viceversa), oppure se valori superiori alla media di una variabile tendono a verificarsi con valori inferiori alla media dell'altra.

- Se $\text{Cov}(X, Y) > 0$, le variabili sono dette **positivamente correlate** o in **concordanza**. Ciò significa che tendono a prendere valori piccoli o grandi all'unisono. Ad esempio, l'età e l'altezza di una persona sono tipicamente associate positivamente.
- Se $\text{Cov}(X, Y) < 0$, le variabili sono dette **negativamente correlate** o in **discordanza**. Ciò implica che tendono a prendere valori in controtendenza, cioè quando una variabile assume valori grandi, l'altra tende ad assumere valori piccoli.
- Se $\text{Cov}(X, Y) = 0$, le variabili sono dette **non correlate** (o ortogonali se variabili complesse).

**Proprietà importanti della covarianza:**

- **Generalizzazione della varianza**: La varianza di una variabile è un caso speciale della covarianza, ovvero $\text{Var}(X) = \text{Cov}(X, X)$.
- **Linearità**: La covarianza è bilineare. Ad esempio, $\text{Cov}(aX + b, Y) = a\text{Cov}(X, Y)$ per costanti $a, b$.
- **Varianza della somma di variabili**: La covarianza influisce sulla varianza della somma di variabili: $\text{Var}(X + Y) = \text{Var}(X) + \text{Var}(Y) + 2\text{Cov}(X, Y)$.
- **Sensibilità alla scala**: Il valore assoluto della covarianza è sensibile alle unità di misura delle variabili. Ad esempio, cambiare le unità di altezza da metri a centimetri aumenterebbe la covarianza età-altezza di un fattore 100. Questa sensibilità rende la covarianza non adatta per quantificare la _forza_ dell'associazione tra due quantità in modo universale.
- **Relazione con l'indipendenza**: Se due variabili casuali sono indipendenti, la loro covarianza è zero. Tuttavia, la conversione non è generalmente vera: una covarianza pari a zero non implica necessariamente l'indipendenza delle variabili. Ci sono eccezioni, come nel caso delle distribuzioni normali multivariate, dove una covarianza pari a zero _implica_ l'indipendenza. In generale, non essere correlati è una condizione molto più debole dell'indipendenza.

### Coefficiente di Correlazione Lineare di Pearson ($\rho_{XY}$): Indice relativo di correlazione lineare, varia tra -1 e 1.

Il **coefficiente di correlazione lineare di Pearson** ($\rho_{XY}$) è un **indice relativo** che misura la **forza** e la **direzione** di una **relazione lineare** tra due variabili quantitative $X$ e $Y$. È una versione **normalizzata** della covarianza, ottenuta dividendo la covarianza per il prodotto delle deviazioni standard delle due variabili: $\rho_{XY} := \frac{\text{Cov}(X, Y)}{\sigma_X \sigma_Y}$.

**Caratteristiche e interpretazione del coefficiente di correlazione di Pearson:**

- **Intervallo di variazione**: Il coefficiente di correlazione di Pearson varia sempre tra **-1 e 1**, ovvero $-1 \le \rho_{XY} \le 1$. Questo intervallo è una conseguenza della disuguaglianza di Cauchy-Schwarz.
- **Invarianza alla scala**: A differenza della covarianza, $\rho_{XY}$ è **invariante alle trasformazioni di scala**. Se le unità di misura di $X$ o $Y$ vengono cambiate, il coefficiente di correlazione rimane lo stesso, il che lo rende più utile per confrontare la forza delle relazioni in contesti diversi.
- **Direzione della relazione lineare**:
    - $\rho_{XY} > 0$: Indica una **correlazione positiva**. Quando i valori di $X$ aumentano, i valori di $Y$ tendono ad aumentare.
    - $\rho_{XY} < 0$: Indica una **correlazione negativa**. Quando i valori di $X$ aumentano, i valori di $Y$ tendono a diminuire.
    - $\rho_{XY} = 0$: Indica **assenza di correlazione lineare**. Questo non significa che non ci sia alcuna relazione tra le variabili, ma solo che non c'è una relazione lineare.
- **Forza della relazione lineare**:
    - $\rho_{XY}$ vicino a +1 o -1: Indica una **forte correlazione lineare**. Un valore di 1 o -1 implica una **perfetta correlazione lineare**, significando che tutti i punti giacciono esattamente su una retta (con pendenza positiva o negativa, rispettivamente). In questo caso, i residui di una regressione lineare sarebbero tutti zero.
    - $\rho_{XY}$ vicino a 0: Indica una **debole correlazione lineare**. I valori critici per interpretare la forza variano, ma come regola generale, $|\rho| \le 0.5$ può indicare una correlazione debole, mentre $|\rho| \ge 0.8$ può indicare una forte correlazione.
- **Prevedibilità e regressione**: Un'alta correlazione implica un'alta prevedibilità. Il coefficiente di correlazione è strettamente legato al coefficiente angolare della retta di regressione lineare. La migliore predizione lineare di $Y$ data $X$ è la **regressione lineare** di $Y$ su $X$, e l'errore quadratico minimo di questa predizione è direttamente proporzionale a $(1 - \rho^2_{XY})$.
- **Coefficiente di determinazione ($R^2$)**: Il quadrato del coefficiente di correlazione di Pearson, $R^2 = \rho^2_{XY}$, è chiamato **coefficiente di determinazione**. Questo valore indica la **proporzione della varianza totale della variabile dipendente $Y$ che è spiegata dal modello lineare** (cioè dalla variazione di $X$). Varia tra 0 e 1. Ad esempio, se $R^2 = 0.2667$, il 26.67% della variazione di $Y$ è spiegato dalla relazione lineare con $X$, mentre il restante 73.33% rimane inspiegato. $R^2 = 1$ significa che il modello spiega completamente la varianza di $Y$ e i residui sono tutti nulli.
- **Test di ipotesi**: È possibile testare l'ipotesi nulla che il coefficiente di correlazione della popolazione sia zero ($\rho = 0$).

In sintesi, mentre la covarianza misura la direzione della relazione lineare e la sua variazione congiunta, il coefficiente di correlazione di Pearson normalizza questa misura per fornire un indice relativo della forza e della direzione della relazione lineare, indipendente dalle unità di misura e variabile tra -1 e 1.