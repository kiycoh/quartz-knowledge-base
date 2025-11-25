---
last modified: 2025, 11, 24 2:11:34
related: null
parent note: null
tags:
  - machine-learning
  - analisi-statistica
  - regression-modeling
---

# Definizione di distanza di Cook
La **distanza di Cook** ($D_i$) è una metrica fondamentale nella [[Diagnostica modelli di regressione]], e [[Modello lineare generalizzato (GLM)]], utilizzata per quantificare l'influenza complessiva di una singola osservazione sulle stime dei coefficienti del modello.

**Scopo e Definizione:** Il suo obiettivo primario è identificare le osservazioni che, se rimosse dal dataset di addestramento, altererebbero significativamente i risultati del modello. A differenza di altre misure diagnostiche, la distanza di Cook combina due aspetti cruciali dell'influenza di un'osservazione: l'essere un *outlier* (ovvero avere un residuo ampio) e l'avere una *leva* elevata (ossia essere un punto estremo nello spazio delle variabili esplicative).

**Formula e Componenti:** Matematicamente, la distanza di Cook per l'i-esima osservazione è definita come: $D_i = \frac{(\hat{\beta} - \hat{\beta}_{(-i)})^T X^T W X (\hat{\beta} - \hat{\beta}_{(-i)})}{p\hat{\phi}}$ dove:

- $\hat{\beta}$ è il vettore dei coefficienti stimati utilizzando tutte le osservazioni.
- $\hat{\beta}_{(-i)}$ è il vettore dei coefficienti stimati escludendo l'i-esima osservazione.
- $X$ è la matrice del modello (design matrix).
- $W$ è la matrice dei pesi (in un GLM, questi dipendono dalla funzione legame e dalla funzione di varianza).
- $p$ è il numero di parametri nel modello.
- $\hat{\phi}$ è la stima del parametro di dispersione.

Una forma equivalente e più intuitiva, che ne evidenzia le componenti di outlier e leva, è: $D_i = \frac{(r_{Ji}^*)^2}{p} \times \frac{h_{ii}}{1 - h_{ii}}$ Questa espressione mostra come la distanza di Cook sia proporzionale al quadrato del residuo standardizzato ($r_{Ji}^*$) moltiplicato per un termine che cresce con la leva ($h_{ii}$).

1. **Residuo ($r_{Ji}^*$)**: Rappresenta la grandezza dell'errore di previsione per l'i-esima osservazione. Un residuo elevato indica un *outlier*, ovvero un'osservazione la cui risposta osservata è inaspettata rispetto a quanto previsto dal modello.
2. **Leva ($h_{ii}$)**: Gli elementi diagonali della *hat matrix* ($H$) sono gli *elementi di leva* ($h_{ii}$). Essi misurano quanto un'osservazione è "lontana" dal centro dello spazio delle variabili esplicative.
    - Un'alta leva ($h_{ii}$ vicino a 1, con soglie indicative come $h_{ii} > 2p/n$ o $h_{ii} > 3p/n$) indica che l'osservazione è isolata e ha un alto potenziale di influenzare le stime.
    - Una bassa leva ($h_{ii} \approx 0$) significa che l'osservazione è vicina al centro dei dati e ha poco potenziale di influenza, anche se può comunque essere un outlier.

**Interpretazione:** La distanza di Cook quantifica quanto la rimozione di un'osservazione modificherebbe le stime dei coefficienti. Non esiste una soglia universale per definire un punto "influente", ma delle regole empiriche comuni suggeriscono che un'osservazione è:

- **Altamente influente** se $D_i > 1$.
- **Moderatamente influente** se $D_i > 4/n$.

Un'osservazione può essere influente se è un outlier **con** alta leva, o se è un outlier così estremo da essere influente anche con bassa leva, o se ha una leva estremamente alta anche senza essere un outlier. In altre parole, l'influenza si verifica quando un'osservazione "tira" la retta di regressione verso di sé a causa della sua posizione isolata o del suo residuo elevato.

**Rappresentazione Grafica:** La distanza di Cook viene spesso visualizzata graficamente per facilitare l'identificazione di punti influenti. Un tipico "Cook's distance plot" mostra la distanza di Cook per ogni osservazione, spesso con una linea orizzontale che indica una o più soglie di riferimento (es. $D_i = 1$ o $D_i = 4/n$). Le osservazioni che superano queste soglie richiedono un'attenta analisi.

Un'altra visualizzazione utile è l'"influence plot" o "bubble plot". Questo grafico combina sui suoi assi i residui standardizzati (y-axis) e i valori di leva (x-axis), mentre la dimensione dei "bubble" (i punti) è proporzionale alla distanza di Cook.

- **Esempio immaginifico:** Immagina di modellare il prezzo di case ($\mu$) in funzione della loro dimensione ($X$). Se hai un punto dati che rappresenta una villa enorme (alta leva) ma con un prezzo molto basso (outlier), la distanza di Cook per quel punto sarà elevata perché sta tirando la linea di regressione significativamente lontano dalla sua posizione originale, distorcendo la stima del coefficiente dimensione. Se fosse una villa enorme con un prezzo coerente (alta leva, basso residuo), potrebbe non essere influente, ma se fosse una casa di dimensioni medie con un prezzo anomalo (bassa leva, alto residuo), potrebbe essere un outlier ma meno influente sulle stime complessive.

**Relazione con altre Misure Diagnostiche:** La distanza di Cook è strettamente correlata ad altre misure di influenza come DFBETAS e DFFITS:

- **DFBETAS** misura il cambiamento nei *singoli coefficienti* ($\beta_j$) quando l'i-esima osservazione viene esclusa.
- **DFFITS** misura il cambiamento nei *valori predetti* ($\hat{\mu}_i$) quando l'i-esima osservazione viene esclusa.

Mentre DFBETAS e DFFITS offrono una visione più granulare dell'influenza (su quali coefficienti o predizioni agisce un punto), la distanza di Cook fornisce una sintesi complessiva dell'impatto di un'osservazione sull'intero modello.