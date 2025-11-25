---
last modified: 2025-09-06T16:37:00.000Z
related:
  - '[[Dipendenza statistica]]'
tags:
  - statistica-inferenziale
  - statistica-descrittiva
  - dipendenza-statistica
---
# Definizione di dipendenza statistica perfetta
La **dipendenza perfetta** si verifica quando la conoscenza delle modalità di una variabile determina in modo univoco le modalità dell'altra variabile. Formalmente, si dice che un carattere $Y$ dipende perfettamente da un carattere $X$ se ad ogni modalità di $X$ corrisponde una e una sola modalità di $Y$. In questo scenario, se si conosce il valore assunto da $X$, è possibile prevedere con certezza il valore di $Y$.

> [!EXAMPLE] Esempio pratico
> Consideriamo una tabella a doppia entrata dove le righe rappresentano le modalità di $X$ e le colonne le modalità di $Y$. La dipendenza perfetta si manifesta con una struttura specifica delle frequenze:
> 
> |Carattere $Y$|$y_1$|$y_2$|$y_3$|Totale $X$|
> |:--|:-:|:-:|:-:|:-:|
> |$x_1$|43|0|0|43|
> |$x_2$|0|0|15|15|
> |$x_3$|0|0|20|20|
> |$x_4$|0|52|0|52|
> |Totale|43|52|35|130|
> 
> In questo esempio, ogni modalità di $X$ (ad es., $x_1$) è associata esclusivamente a una singola modalità di $Y$ (ad es., $y_1$). Nonostante ciò, una modalità di $Y$ ($y_1$) può essere associata a più modalità di $X$ (qui, solo $x_1$). Questo implica che, sebbene $Y$ dipenda perfettamente da $X$, il contrario non è necessariamente vero; la dipendenza, in generale, non è un concetto simmetrico.

### [[Interdipendenza statistica perfetta]]

### Confronto e Indicatori
La dipendenza perfetta e l'interdipendenza perfetta sono i casi estremi di associazione tra variabili, contrapponendosi all'**indipendenza statistica**, dove conoscere le modalità di una variabile non fornisce alcuna informazione sulle modalità dell'altra. L'indipendenza statistica si verifica quando le frequenze osservate in una tabella a doppia entrata soddisfano la condizione $n_{ij} = (n_{i.}n_{.j}) / n$ per ogni $i, j$.

Per quantificare il grado di associazione, si utilizzano indici quali il $\chi^2$ di Pearson e il coefficiente $V$ di Cramer.

- Il $\chi^2$ di Pearson è nullo ($X^2 = 0$) in caso di indipendenza.
- Il coefficiente $V$ di Cramer, che varia tra 0 e 1, assume valore $V=1$ in caso di perfetta associazione. Nello specifico, $V=1$ quando:
    - Il numero di modalità delle due variabili è uguale ($R=C$) e i caratteri sono perfettamente associati (interdipendenza perfetta).
    - La variabile $X$ dipende perfettamente da $Y$ (se $R < C$).
    - La variabile $Y$ dipende perfettamente da $X$ (se $C < R$).

