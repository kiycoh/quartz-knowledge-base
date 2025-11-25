---
last modified: 2025-09-08T01:13:00.000Z
related: null
tags:
  - statistica-informatica
  - statistica-inferenziale
  - indice-di-associazione
---
# Definizione di V di Cramer

Il **V di Cramer** è un indice di associazione utilizzato per misurare la forza della dipendenza tra due variabili qualitative nominali (o categoriche) in una tabella a doppia entrata. È una versione normalizzata dell'indice Phi-quadro (Φ²) e varia tra 0 e 1.

**Relazione con altri indici:**

1. **Chi-quadro di Pearson (X²)**: Questo indice misura il grado di dipendenza tra due variabili confrontando le frequenze osservate (nij) con le frequenze teoriche (n̂ij) che si avrebbero in caso di indipendenza. La formula è: $X^2 = \sum_{i=1}^{R} \sum_{j=1}^{C} \frac{(n_{ij} - \hat{n}_{ij})^2}{\hat{n}_{ij}}$ dove R è il numero di righe e C è il numero di colonne della tabella. Un $X^2 = 0$ indica indipendenza, mentre $X^2 > 0$ indica dipendenza, ma non ne quantifica l'intensità in modo confrontabile tra tabelle diverse a causa della sua dipendenza dalla dimensione del collettivo e dal numero di categorie.
    
2. **Phi-quadro (Φ²)**: Pearson ha proposto l'indice di contingenza quadratica media Φ² come normalizzazione del Chi-quadro per la dimensione del campione $n$: $\Phi^2 = \frac{X^2}{n}$ Questo indice varia tra 0 e $\min{(R-1), (C-1)}$.
    
3. **V di Cramer**: Per ottenere un indice che vari tra 0 e 1, Cramer ha ulteriormente normalizzato il Φ²: $V = \sqrt{\frac{\Phi^2}{\min{(R-1), (C-1)}}}$
    

**Proprietà e Interpretazione:**

- Il V di Cramer assume valori nell'intervallo.
- **$V = 0$**: Indica che i due caratteri sono statisticamente indipendenti. Le frequenze osservate sono uguali a quelle teoriche di indipendenza.
- **$V = 1$**: Indica una perfetta associazione tra i due caratteri. Ciò si verifica in situazioni specifiche:
    - Se $R = C$ (la tabella è quadrata) e i caratteri sono perfettamente associati.
    - Se $R < C$ e la variabile X dipende perfettamente dalla variabile Y.
    - Se $C < R$ e la variabile Y dipende perfettamente dalla variabile X.

**Esempio Pratico: Relazione tra Residenza e Tempo per Trovare Lavoro** Immagina un gruppo di laureati della facoltà di Economia, intervistati per analizzare la relazione tra la loro zona di residenza (variabile X, qualitativa nominale) e il tempo impiegato per trovare lavoro dopo la laurea (variabile Y, qualitativa ordinale categorizzata in mesi: 6, 12, 18, 24). I risultati sono riportati nella seguente tabella di contingenza:

|Residenza|Tempo (mesi)|Totale|
|:--|:--|:--|
||6|12|
|N-OVEST|3|2|
|N-EST|1|2|
|Centro|45|26|
|Sud|9|5|
|**Totale**|**58**|**35**|

Per valutare l'associazione tra residenza e tempo di impiego, si calcolano prima le frequenze teoriche di indipendenza e poi il Chi-quadro:

- **Frequenze Teoriche (Esempio per N-OVEST, 6 mesi)**: $(\frac{5 \times 58}{135}) \approx 2.148$
- **Calcolo del Chi-quadro di Pearson (X²)**: $X^2 = \sum \frac{(n_{ij} - \hat{n}_{ij})^2}{\hat{n}_{ij}} = \frac{(3 - 2.148)^2}{2.148} + \dots + \frac{(5 - 4.356)^2}{4.356} \approx 5.396$.

Successivamente, si calcola il Phi-quadro: $\Phi^2 = \frac{X^2}{n} = \frac{5.396}{135} \approx 0.04$.

Infine, si calcola il V di Cramer. Il valore di $\min{(R-1), (C-1)}$ è $\min{(4-1), (4-1)} = \min{3, 3} = 3$. $V = \sqrt{\frac{\Phi^2}{\min{(R-1), (C-1)}}} = \sqrt{\frac{0.04}{3}} \approx 0.115$.

**Commento sull'esempio:** Un valore di $V \approx 0.115$ indica una debole associazione tra la zona di residenza e il tempo impiegato per trovare lavoro. Se il valore fosse stato più vicino a 1, avremmo dedotto un'associazione più forte. Questo indice è particolarmente utile per confrontare la forza di associazione tra coppie di variabili in diverse tabelle di contingenza, poiché è stato normalizzato e non dipende dalla dimensione del campione o dal numero di categorie, rendendolo un indicatore robusto.