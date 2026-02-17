---
tags:
  - statistica-informatica
  - statistica-descrittiva
  - dipendenza-statistica
---

# Definizione di dipendenza statistica
La **dipendenza statistica** (o **associazione**) tra due [[Variabile statistica|variabili]] si verifica quando la conoscenza della modalità di una variabile fornisce informazioni sulla modalità dell'altra. Questo implica che le variabili **non** si manifestano in modo casuale o indipendente l'una dall'altra.

Per contrasto, due variabili sono **statisticamente indipendenti** se la conoscenza della modalità di una variabile non fornisce alcuna informazione sulla modalità dell'altra. In tal caso, le frequenze osservate in una tabella a doppia entrata ($n_{ij}$) sono uguali alle frequenze teoriche che si avrebbero in caso di indipendenza ($n_{i.}n_{.j}/n$), ovvero $f_{ij} = f_{i.}f_{.j}$ per ogni combinazione di modalità.

## Relazione con le [[Distribuzione statistica]]
La dipendenza statistica si comprende al meglio esaminando le **distribuzioni congiunte, marginali e condizionate**:

1. **[[Distribuzione Congiunta]] (o Doppia)**: Rappresenta l'associazione tra due (o più) caratteri, elencando le frequenze per ogni combinazione di modalità. È il punto di partenza per l'analisi della dipendenza.
2. **Distribuzioni Marginali**: Si ottengono concentrandosi su un singolo carattere e ignorando le informazioni relative alle altre variabili. Sono i totali di riga o colonna in una tabella a doppia entrata (tabella di contingenza).
3. **Distribuzioni Condizionate**: Rappresentano la distribuzione di frequenza di una variabile calcolata per una **specifica modalità** di un'altra variabile. In una tabella a doppia entrata, ogni riga (o colonna) rappresenta una distribuzione condizionata.

**La chiave per la dipendenza**: Se le distribuzioni condizionate di una variabile cambiano al variare delle modalità dell'altra variabile, allora esiste una **dipendenza in distribuzione** [Lezione 5]. Se, invece, tutte le distribuzioni condizionate di una variabile sono identiche tra loro e alla distribuzione marginale della stessa variabile, allora le due variabili sono statisticamente indipendenti [Lezione 5].

> [!EXAMPLE] Esempio di dipendenza statistica
> Consideriamo la relazione tra "*Uso dei social*" (Basso, Medio, Alto) e "*Capacità di concentrazione*" (Bassa, Media, Alta). Se osserviamo la **distribuzione condizionata della "Capacità di concentrazione" per chi ha "Uso dei social" Alto**:
> 
> - Bassa: 62.5%
> - Media: 25.0%
> - Alta: 12.5% 
> 
> Se questa distribuzione è significativamente diversa dalla **distribuzione marginale della "Capacità di concentrazione"** (es. Bassa: 37.5%, Media: 33.3%, Alta: 29.2%) o dalle distribuzioni condizionate per gli altri livelli di "Uso dei social", allora le due variabili sono dipendenti in distribuzione. La differenza tra queste proporzioni indica che l'uso dei social fornisce informazioni sulla capacità di concentrazione.

### Tipi di Dipendenza
1. **Dipendenza in Distribuzione**: È il concetto più generale, descritto sopra. Si manifesta quando le distribuzioni condizionate di una variabile variano al cambiare delle modalità dell'altra.
2. **[[Dipendenza statistica perfetta]]**: Si verifica quando ad ogni modalità di una variabile corrisponde una e una sola modalità dell'altra. Questo concetto non è generalmente simmetrico.
3. **[[Interdipendenza statistica perfetta]]**: È un caso di dipendenza perfetta simmetrica, dove ad ogni modalità di una corrisponde una e una sola modalità dell'altra e viceversa.
4. **[[Dipendenza statistica in media]]**: Per caratteri quantitativi, si verifica se le **medie condizionate** di una variabile sono diverse rispetto alle modalità dell'altra variabile. Questa è una forma più debole rispetto alla dipendenza in distribuzione. La "varianza spiegata" ($\sigma^2_{YX=X_i}$) misura questa dipendenza, indicando quanto le medie condizionate si discostano dalla media generale.

### Misure di Associazione e Dipendenza

Per quantificare la forza e/o la direzione della dipendenza, si utilizzano diversi indici:

- **$X^2$ di Pearson (Chi-quadrato)**: Misura il grado di dipendenza tra due variabili qualitative. È nullo in caso di indipendenza e cresce con la dipendenza. Si usa per verificare l'ipotesi di indipendenza in distribuzione.
- **$\Phi^2$ (Phi-quadro)**: Indice di contingenza quadratica media, derivato da $X^2$, che varia tra 0 e min(R-1, C-1).
- **V di Cramer**: Normalizzazione di $\Phi^2$, che varia tra 0 (indipendenza) e 1 (perfetta associazione).
- **$\Phi$ (Phi)**: Coefficiente di associazione per tabelle dicotomiche (variabili binarie), varia tra -1 e 1.
- **Indici di Cograduazione (es. $\rho_s$ di Spearman, $\tau$ di Kendall)**: Misurano l'associazione tra due graduatorie (rX, rY) per variabili almeno ordinali. Si basano sui ranghi delle osservazioni.
- **Rapporto di Correlazione ($\eta^2_{Y|X}$)**: Indice relativo di dipendenza in media per un carattere quantitativo (Y) e un carattere qualitativo o quantitativo discreto (X). Varia tra 0 (indipendenza in media) e 1 (dipendenza perfetta in media).
- **Covarianza ($\sigma_{XY}$)**: Misura la concordanza o discordanza tra due caratteri quantitativi. È positiva se gli scarti tendono ad avere lo stesso segno.
- **Coefficiente di Correlazione Lineare di Bravais-Pearson ($\rho_{XY}$)**: Normalizzazione della covarianza, varia tra -1 e 1. Misura l'associazione _lineare_ tra due variabili quantitative.

### Dipendenza e Statistical Learning

Nel campo del **Statistical Learning**, il concetto di dipendenza è centrale, poiché molti modelli mirano a catturare e sfruttare le relazioni tra variabili per compiti di predizione o inferenza.

- **Predizione**: L'obiettivo di stimare una funzione $f(X)$ per predire un output $Y$ basato su input $X$ è intrinsecamente un'analisi di dipendenza. La "componente sistematica" $f(X; \theta)$ in un modello di regressione rappresenta la parte della risposta Y che è spiegata dai predittori X.
- **Regressione Lineare**: Questo modello quantifica la dipendenza lineare tra una variabile risposta $Y$ e una o più variabili esplicative $X_i$ attraverso parametri come $\beta$. Se $\beta$ è diverso da zero, c'è dipendenza. Il coefficiente di determinazione $R^2$ misura la frazione della varianza di $Y$ spiegata dal modello, quantificando quindi la forza di questa dipendenza.
- **Classificazione**: Algoritmi come la regressione logistica, Naive Bayes e l'Analisi Discriminante (LDA/QDA) sono progettati per assegnare osservazioni a classi basandosi sulla dipendenza tra le variabili predittive e la variabile di classe.
    - **Naive Bayes**: Nonostante il nome, assume l'**indipendenza condizionale** delle caratteristiche dato la classe. Questa semplificazione permette di calcolare la probabilità posteriore di una classe ($P(Y|X)$) in modo efficiente, ma la sua efficacia nel mondo reale dipende da quanto questa assunzione sia valida.
    - **Analisi Discriminante (LDA e QDA)**: Questi metodi assumono che le variabili esplicative seguano una distribuzione normale multivariata **condizionata** alla classe ($X|Y=k \sim N(\mu_k, \Sigma_k)$). La capacità di distinguere le classi e di trovare confini di decisione (lineari per LDA, quadratici per QDA) si basa proprio sulle differenze nelle medie ($\mu_k$) e/o nelle matrici di covarianza ($\Sigma_k$) tra le classi, che sono manifestazioni di dipendenza.
- **Modelli Lineari Generalizzati (GLM)**: Estendono i modelli lineari classici per gestire variabili risposta che non sono distribuite normalmente (es. Regressione Logistica per risposte binarie, Regressione di Poisson per conteggi, Regressione Gamma per valori continui positivi). La "componente sistematica" ($η = Xβ$) di un GLM modella come il valore atteso della risposta dipende linearmente dai predittori attraverso una funzione di collegamento (link function), quantificando direttamente la dipendenza. I coefficienti esponenziali in Logistica e Poisson sono "Odds Ratio" o "fattori moltiplicativi" che esprimono l'effetto dei predittori sulla risposta, rivelando la dipendenza.

In sintesi, la dipendenza statistica è il cuore dell'analisi dei dati, consentendo di identificare, quantificare e modellare le relazioni tra le variabili, passando da una descrizione delle singole caratteristiche a una comprensione più profonda delle dinamiche del collettivo studiato.