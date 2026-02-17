---
last modified: 2025, 11, 24 16:11:47
tags:
  - statistica-informatica
  - indipendenza-statistica
  - statistica-descrittiva
---
# Indipendenza statistica

L'**indipendenza statistica** è un concetto fondamentale nella probabilità e nella statistica che descrive l'assenza di relazione tra due o più variabili o eventi. Intuitivamente, due variabili sono statisticamente indipendenti se la conoscenza del valore o della modalità di una non fornisce alcuna informazione sul valore o sulla modalità dell'altra.

**Definizione e Implicazioni Fondamentali:**

- **Distribuzioni Congiunte:** Per due caratteri $X$ e $Y$ rilevati in una tabella a doppia entrata, l'indipendenza statistica si verifica se le frequenze osservate ($n_{ij}$) rispettano la relazione $n_{ij} = (n_{i.}n_{.j})/n$ o, analogamente, se le frequenze relative ($f_{ij}$) sono uguali al prodotto delle frequenze marginali ($f_{i.}f_{.j}$) per ogni $i, j$. Il concetto di indipendenza è **simmetrico**.
- **Covarianza:** Una delle più dirette implicazioni dell'indipendenza è che la **covarianza tra due variabili indipendenti è zero**. La covarianza stessa è una misura dell'associazione tra variabili. Tuttavia, è cruciale notare che una covarianza pari a zero indica l'assenza di una relazione *lineare*, ma non implica necessariamente l'indipendenza statistica completa (potrebbero esistere relazioni non lineari).
- **Operazioni su Variabili Casuali:** Se due variabili casuali sono indipendenti, le loro funzioni di probabilità o di densità congiunte possono essere espresse come il prodotto delle loro funzioni marginali. Ad esempio, nella teoria delle trasformazioni Z, l'indipendenza tra due variabili $X$ e $Y$ permette di esprimere il $z$-trasformato della loro somma ($Z = X + Y$) come il prodotto dei loro $z$-trasformati ($z_Z(I) = z_X(I) \cdot z_Y(I)$). Questo è possibile perché l'aspettativa di un prodotto di funzioni di variabili indipendenti può essere separata nel prodotto delle aspettative.

**Ruolo dell'Indipendenza nell'Inferenza Statistica e nei Modelli:**

L'assunzione di indipendenza è un pilastro in molte metodologie statistiche e modelli di machine learning:

- **Campionamento Casuale:** Un campione è definito **casuale** quando le variabili casuali $X_1, X_2, \ldots, X_n$ sono **indipendenti e identicamente distribuite (i.i.d.)** come la variabile casuale $X$ della popolazione che si intende studiare. Questo significa che la distribuzione di probabilità di un elemento campionario non dipende dai valori assunti dagli altri elementi e che tutti gli elementi hanno la stessa distribuzione della popolazione. Questa ipotesi è fondamentale per l'inferenza statistica.
- **Stima di Massima Verosimiglianza (MLE):** Per un campione di variabili $X_1, X_2, \ldots, X_n$ che sono i.i.d., la funzione di verosimiglianza (likelihood), che è la densità congiunta del campione, viene calcolata come il prodotto delle densità marginali individuali. Questa separabilità semplifica notevolmente la massimizzazione della log-verosimiglianza, consentendo di stimare i parametri di ciascuna distribuzione marginale indipendentemente.
- **Regressione Lineare:** Tra le "assunzioni deboli" del modello di regressione lineare vi è l'**indipendenza degli errori** ($\text{Cov}(\epsilon_i, \epsilon_j) = 0$ per $i \neq j$). Gli errori $\epsilon_i$ sono spesso assunti come campioni indipendenti da una distribuzione Gaussiana. È importante notare che, mentre gli errori $Y_i$ e $Y_j$ possono essere assunti indipendenti, i valori predetti $\hat{Y}_i$ e $\hat{Y}_j$ possono essere correlati.
- **Classificatore Naive Bayes:** Questo classificatore probabilistico è "ingenuo" proprio per la sua assunzione chiave: data la classe $Y$, **tutte le caratteristiche $X_i$ sono condizionalmente indipendenti tra loro**. Sebbene questa semplificazione sia raramente vera nel mondo reale, riduce notevolmente la complessità computazionale del modello e si è dimostrato sorprendentemente efficace in molte applicazioni.
- **Analisi Discriminante Lineare (LDA) e Quadratica (QDA):** Questi metodi classificatori si basano su ipotesi riguardo la distribuzione delle variabili esplicative condizionatamente alla classe ($X|Y=k \sim N(\mu_k, \Sigma_k)$). Nel caso della LDA, si assume che le classi condividano la stessa matrice di covarianza ($\Sigma_k = \Sigma$ per ogni $k$), il che porta a confini di decisione lineari. Nella QDA, invece, ogni classe ha la propria matrice di covarianza ($\Sigma_k$ può variare tra le classi), risultando in confini di decisione quadratici.
- **Analisi dei Dati Funzionali (FDA):** In contesti di dati funzionali, l'indipendenza può essere assunta per i residui dopo aver tenuto conto delle medie specifiche del soggetto, sebbene questa assunzione possa essere troppo restrittiva in molti studi che presentano diversi livelli di variabilità funzionale.
- **Martingale:** Una somma $S_n$ di variabili casuali integrabili indipendenti con media zero (e $S_0 = 0$) è un esempio classico di martingale, dove $E(S_n|F_{n-1}) = S_{n-1}$.

**Valutazione dell'Indipendenza:**

- **Test Chi-Quadrato di Pearson ($X^2$):** Per valutare la dipendenza in distribuzione tra due variabili qualitative, si utilizza l'indice $X^2$ di Pearson. L'ipotesi nulla ($H_0$) in questo test è che le due variabili siano indipendenti in distribuzione, mentre l'ipotesi alternativa ($H_1$) è che non lo siano. Se le variabili sono indipendenti, l'indice $X^2 = 0$. Sotto $H_0$, la statistica test $X^2$ si distribuisce asintoticamente come una distribuzione chi-quadrato.
- **Coefficiente di Correlazione:** Il coefficiente di correlazione lineare di Bravais-Pearson ($\rho_{XY}$) misura la concordanza o discordanza lineare e assume valore 0 in assenza di correlazione lineare. Come menzionato, l'assenza di correlazione lineare non implica necessariamente indipendenza, ma l'indipendenza implica assenza di correlazione (e quindi $\rho_{XY} = 0$).

In sintesi, l'indipendenza statistica è un'assunzione potente che semplifica l'analisi e la modellazione dei dati, ma la sua validità deve essere attentamente considerata e, quando possibile, verificata, poiché un'assunzione errata può portare a conclusioni distorte o inaffidabili.