---
last modified: 2025, 11, 24 2:11:36
tags:
  - distribuzione-condizionata
  - statistica-inferenziale
  - analisi-statistica
---

# Definizione di distribuzione condizionata
La **distribuzione condizionata** di una variabile è la distribuzione di frequenza (assoluta o relativa) di tale variabile, calcolata **per una specifica modalità di un'altra variabile**. In altre parole, essa descrive come si distribuisce un carattere all'interno di un sottogruppo del collettivo, definito da un valore particolare di un altro carattere. Questo permette di isolare e analizzare l'influenza o l'associazione che una variabile esercita sull'altra.

**Derivazione da una Distribuzione Congiunta** Le distribuzioni condizionate si ottengono a partire da una **[[Distribuzione congiunta]]** (o doppia), che rappresenta l'associazione tra due o più caratteri e ne elenca le frequenze per ogni combinazione di modalità. In una tabella a doppia entrata (o tabella di contingenza), che riassume una distribuzione congiunta di due caratteri X e Y:

- Ogni **riga** della tabella rappresenta la distribuzione condizionata della variabile Y data una specifica modalità di X.
- Ogni **colonna** della tabella rappresenta la distribuzione condizionata della variabile X data una specifica modalità di Y.

Formalmente, le **frequenze assolute condizionate** sono le frequenze $n_{ij}$ all'interno della cella. Per ottenere le **frequenze relative condizionate**, si divide la frequenza congiunta per il totale del margine condizionante:

- La distribuzione relativa condizionata di Y dato $X = x_i$ si ottiene dividendo ogni cella della riga $i$ per il totale della riga $n_{i.}$: $f_{j|i} = n_{ij} / n_{i.}$.
- La distribuzione relativa condizionata di X dato $Y = y_j$ si ottiene dividendo ogni cella della colonna $j$ per il totale della colonna $n_{.j}$: $f_{i|j} = n_{ij} / n_{.j}$.

Questo è in netto contrasto con le **distribuzioni marginali**, che si ottengono ignorando l'informazione relativa alle altre variabili e si trovano ai "margini" della tabella (i totali di riga o colonna).

**Misure di Sintesi Condizionate** Le distribuzioni condizionate consentono di calcolare misure di sintesi (es. media, varianza) specifiche per ogni sottogruppo:

- **Media Aritmetica Condizionata**: La media di una variabile quantitativa (es. X) condizionata a una modalità specifica di un'altra variabile (es. $Y = y_j$) si calcola come: $x_{Y=y_j} = \frac{1}{n_{.j}} \sum_{i=1}^{R} x_i n_{ij}$.
- **Varianza Condizionata**: La varianza di una variabile quantitativa (es. X) condizionata a una modalità specifica di un'altra variabile (es. $Y = y_j$) si calcola come: $\sigma^2_{X|Y=y_j} = \frac{1}{n_{.j}} \sum_{i=1}^{R} (x_i - x_{Y=y_j})^2 n_{ij}$. La varianza condizionata esprime la variabilità delle osservazioni della distribuzione condizionata attorno alla propria media condizionata.

**Utilità e Importanza nell'Analisi Statistica** Le distribuzioni condizionate sono fondamentali per indagare le relazioni e le dipendenze tra variabili:

1. **Valutazione della Dipendenza in Distribuzione**: Se le distribuzioni condizionate di una variabile cambiano al variare delle modalità dell'altra variabile, significa che esiste una **dipendenza in distribuzione**. Ad esempio, se la distribuzione della "Capacità di concentrazione" cambia significativamente tra i gruppi di "Uso dei social" (Basso, Medio, Alto), allora le due variabili sono dipendenti in distribuzione.
2. **Valutazione della Dipendenza in Media**: Per caratteri quantitativi, se le medie condizionate di una variabile rispetto alle modalità dell'altra sono diverse, si parla di **dipendenza in media**. La varianza delle medie condizionate ($\sigma^2_{YX=X_i}$) è detta "varianza spiegata" e quantifica questa dipendenza.
3. **Classificazione**: Molti algoritmi di classificazione si basano esplicitamente sul concetto di probabilità condizionata (o distribuzioni condizionate):
    - **Teorema di Bayes**: La base di classificatori come Naive Bayes, LDA (Linear Discriminant Analysis) e QDA (Quadratic Discriminant Analysis) è il teorema di Bayes, che calcola la probabilità a posteriori di una classe ($P(Y|X)$) basandosi sulla verosimiglianza ($P(X|Y)$) e la probabilità a priori ($P(Y)$).
    - **Naive Bayes**: Questo classificatore si distingue per l'assunzione "ingenua" (da cui "naive") che le caratteristiche ($X_i$) siano **condizionatamente indipendenti** data la classe ($Y$). Questo significa che, una volta nota la classe di un oggetto, le relazioni tra i suoi attributi diventano irrilevanti. Nonostante questa semplificazione, che spesso non è vera nel mondo reale, il Naive Bayes è sorprendentemente efficace e computazionalmente efficiente.
    - **LDA e QDA**: Questi metodi assumono che le variabili esplicative ($X$) seguano una distribuzione normale multivariata condizionata alla classe ($Y=k$), ovvero $X|Y=k \sim N(\mu_k, \Sigma_k)$. La differenza sta nel fatto che LDA assume una matrice di covarianza comune a tutte le classi ($\Sigma_k = \Sigma$), portando a confini di decisione lineari, mentre QDA consente matrici di covarianza diverse per ogni classe ($\Sigma_k \ne \Sigma$), risultando in confini di decisione quadratici.
4. **Modelli Lineari Generalizzati (GLM)**: La componente casuale di un GLM specifica la distribuzione della variabile risposta ($Y$) condizionatamente alle variabili esplicative ($X$), e questa distribuzione appartiene alla famiglia esponenziale naturale. Ad esempio, nella **regressione logistica**, la variabile risposta binaria è modellata come una Bernoulli condizionata ai predittori. Questo approccio non trasforma direttamente la variabile risposta $Y$, ma il suo valore atteso $E[Y|X]$, tramite una funzione di collegamento (link function), $g(E[Y|X]) = \eta = X\beta$.

**Esempio Pratico:** Consideriamo l'esempio dell'associazione tra "Uso dei social" e "Capacità di concentrazione" in un campione di 120 studenti, come nell'Esercitazione 5:

|Uso dei social \ Capacità di concentrazione|Bassa|Media|Alta|**Totale**|
|:--|:--|:--|:--|:--|
|Basso|5|10|20|**35**|
|Medio|15|20|10|**45**|
|Alto|25|10|5|**40**|
|**Totale**|**45**|**40**|**35**|**120**|

Per determinare la **distribuzione condizionata della "Capacità di concentrazione" dato un livello di "Uso dei social" alto**: Ci concentriamo sulla riga "Alto" della tabella congiunta. La sua somma è 40.

- Capacità di concentrazione Bassa (condizionata a Uso dei social Alto): $25 / 40 = 0.625$ (o 62.5%).
- Capacità di concentrazione Media (condizionata a Uso dei social Alto): $10 / 40 = 0.250$ (o 25.0%).
- Capacità di concentrazione Alta (condizionata a Uso dei social Alto): $5 / 40 = 0.125$ (o 12.5%).

Questa distribuzione condizionata ci dice che, tra gli studenti che fanno un "Uso dei social" alto, la maggior parte (62.5%) ha una capacità di concentrazione bassa, mentre solo una piccola percentuale (12.5%) ha una capacità alta. Confrontando questa distribuzione con quelle ottenute per gli altri livelli di "Uso dei social" (Basso, Medio) o con la distribuzione marginale della "Capacità di concentrazione", possiamo valutare la dipendenza tra le due variabili.