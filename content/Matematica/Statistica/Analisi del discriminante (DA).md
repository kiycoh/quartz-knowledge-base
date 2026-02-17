---
last modified: 2025, 11, 24 2:11:47
tags:
  - machine-learning
  - analisi-statistica
  - discriminant-analysis
---
# Analisi del discriminante (DA)

L'**Analisi Discriminante (DA)** è una **tecnica statistica per la classificazione** che ha l'obiettivo di assegnare nuove osservazioni a classi predefinite. La sua metodologia si basa sul **Teorema di Bayes** e cerca di trovare **funzioni discriminanti** che siano in grado di separare al meglio queste classi.

Gli **obiettivi principali** dell'Analisi Discriminante includono:

- **Classificazione**: assegnare nuove osservazioni a una delle classi prestabilite.
- **Descrizione**: caratterizzare le differenze tra i gruppi di osservazioni.
- **Riduzione dimensionale**: trovare proiezioni informative dei dati che massimizzino la separazione tra le classi.
- **Interpretazione**: identificare le variabili più importanti per la discriminazione tra i gruppi.

Il **Teorema di Bayes** è fondamentale per l'Analisi Discriminante e si esprime come: $P(Y = k|X = x) = \frac{P(X = x|Y = k) \cdot P(Y = k)}{P(X = x)}$ dove:

- $P(Y = k|X = x)$ è la **probabilità a posteriori** che un'osservazione $x$ appartenga alla classe $k$.
- $P(X = x|Y = k)$ è la **verosimiglianza** dei dati $x$ data la classe $k$.
- $P(Y = k)$ è la **probabilità a priori** della classe $k$.
- $P(X = x)$ è la **probabilità marginale** di $X$.

Il **classificatore di Bayes ottimale** assegna un'osservazione $x$ alla classe $k$ che massimizza la probabilità a posteriori $P(Y = k|X = x)$. Poiché $P(X = x)$ è costante per tutte le classi, la regola di classificazione si semplifica nella massimizzazione di $P(X = x|Y = k) \cdot P(Y = k)$. Applicando il logaritmo, che è una funzione monotonicamente crescente, si massimizza $\log P(X = x|Y = k) + \log P(Y = k)$.

- Le probabilità a priori $P(Y = k)$ vengono stimate dalla proporzione di osservazioni nella classe $k$ nel training set ($n_k/n$).
- Le verosimiglianze $P(X = x|Y = k)$ richiedono specifiche ipotesi sulla distribuzione di $X$ condizionata a $Y$.

## Assunzione di Normalità Condizionale

Un'assunzione cruciale nell'Analisi Discriminante è che le variabili esplicative $X$, **condizionate alla classe $Y$**, seguano una **distribuzione Normale Multivariata**. Questo significa che la densità condizionata $f_k(x) = P(X = x|Y = k)$ è data dalla formula della distribuzione normale multivariata, caratterizzata da un vettore delle medie $\mu_k$ e una matrice di covarianza $\Sigma_k$ per ciascuna classe $k$. Per il caso di una sola variabile esplicativa ($p=1$), si assume $X|Y=k \sim N(\mu_k, \sigma^2_k)$. Se ci sono più variabili esplicative ($p>1$), si assume $X|Y=k \sim N(\mu_k, \Sigma_k)$.

## Linear Discriminant Analysis (LDA)

La **Linear Discriminant Analysis (LDA)** è una variante dell'Analisi Discriminante. La sua assunzione distintiva è che **tutte le classi condividano la stessa matrice di covarianza ($\Sigma_k = \Sigma$ per ogni classe $k$)**. Questa ipotesi semplificatrice porta a **confini di decisione lineari** nello spazio delle variabili.

**Caratteristiche e calcolo dell'LDA**:

- **Funzione discriminante lineare**: Inserendo la densità normale multivariata (con covarianza comune) nella regola di classificazione logaritmica e semplificando, si ottiene una funzione discriminante $\delta_k(x)$ che è **lineare in $x$**: $\delta_k(x) = x^T\Sigma^{-1}\mu_k - \frac{1}{2}\mu_k^T\Sigma^{-1}\mu_k + \log \pi_k$. Questa può essere scritta anche come $\delta_k(x) = w_k^T x + w_{k0}$.
- **Confini di decisione**: Il confine di decisione tra due classi $h$ e $k$ è definito dall'uguaglianza $\delta_k(x) = \delta_h(x)$, che corrisponde a un **iperpiano** (una funzione lineare) nello spazio delle variabili. Geometricamente, se le probabilità a priori sono uguali, il confine di decisione è perpendicolare alla linea che congiunge le medie delle classi.
- **Stima dei parametri**: I parametri vengono stimati dai dati di addestramento:
    - Probabilità a priori: $\hat{\pi}_k = n_k/n$.
    - Media della classe $k$: $\hat{\mu}_k = \frac{1}{n_k} \sum_{i:y_i=k} x_i$.
    - Matrice di covarianza comune: $\hat{\Sigma} = \frac{1}{n-K} \sum_{k=1}^K \sum_{i:y_i=k} (x_i - \hat{\mu}_k)(x_i - \hat{\mu}_k)^T$.

**LDA come tecnica di Riduzione Dimensionale (Criterio di Fisher)**:

- L'LDA può essere utilizzata anche per **ridurre la dimensionalità** dei dati. Cerca proiezioni che massimizzino la separazione tra le classi.
- Il **Criterio di Fisher** (o indice discriminante di Fisher) mira a massimizzare il rapporto tra la varianza *tra* i gruppi ($S_B$) e la varianza *entro* i gruppi ($S_W$): $J(w) = \frac{w^T S_B w}{w^T S_W w}$.
    - $S_W$ (dispersione intra-classe) misura quanto i punti si discostano dalla media della loro classe.
    - $S_B$ (dispersione inter-classe) cattura la distanza tra le medie delle classi dalla media globale.
- Questo si risolve come un problema agli autovalori generalizzato ($S_W^{-1} S_B w = \lambda w$). Gli autovettori corrispondenti agli autovalori maggiori definiscono le direzioni ottimali di proiezione.
- L'LDA può estrarre fino a $\min(p, K-1)$ dimensioni, dove $p$ è la dimensione originale e $K$ è il numero di classi. Per due classi, lo spazio LDA è 1-dimensionale.
- È una tecnica **supervisionata** perché utilizza le etichette delle classi.
- Fisher (1936) è accreditato per aver applicato l'idea di restringere le medie dei componenti a un sottospazio lineare e per aver proposto l'Analisi Discriminante Lineare (LDA).

**Vantaggi e limitazioni dell'LDA**:

- **Vantaggi**: Semplicità, interpretabilità, efficienza computazionale, stabilità, richiede meno dati rispetto alla QDA.
- **Limitazioni**: I confini di decisione lineari possono essere troppo rigidi. Assume che le classi abbiano covarianze simili.

## Quadratic Discriminant Analysis (QDA)

La **Quadratic Discriminant Analysis (QDA)** è un'altra variante dell'Analisi Discriminante. A differenza dell'LDA, la QDA permette a **ogni classe di avere la propria matrice di covarianza ($\Sigma_k$)**. Questa maggiore flessibilità si traduce in **confini di decisione quadratici**.

**Caratteristiche e calcolo della QDA**:

- **Funzione discriminante quadratica**: La funzione discriminante $\delta_k(x)$ nella QDA è **quadratica in $x$**: $\delta_k(x) = -\frac{1}{2} \log |\Sigma_k| - \frac{1}{2}(x - \mu_k)^T\Sigma_k^{-1}(x - \mu_k) + \log \pi_k$.
- **Confini di decisione**: Il confine di decisione tra due classi è descritto da una **quadrica** (come un'ellissoide, paraboloide o iperboloide). La forma specifica dipende dalle matrici di covarianza delle classi.
- **Stima dei parametri**: I parametri vengono stimati dai dati di addestramento:
    - Probabilità a priori: $\hat{\pi}_k = n_k/n$.
    - Media della classe $k$: $\hat{\mu}_k = \frac{1}{n_k} \sum_{i:y_i=k} x_i$.
    - Matrice di covarianza per la classe $k$: $\hat{\Sigma}_k = \frac{1}{n_k-1} \sum_{i:y_i=k} (x_i - \hat{\mu}_k)(x_i - \hat{\mu}_k)^T$.
    - La stima della matrice di covarianza per ogni classe richiede un numero maggiore di parametri ($p(p+1)/2$ per ogni $\Sigma_k$ data la simmetria) rispetto all'LDA.

**Vantaggi e limitazioni della QDA**:

- **Vantaggi**: Maggiore flessibilità e capacità di catturare confini di classe più complessi, particolarmente utile quando le covarianze delle classi sono chiaramente diverse.
- **Limitazioni**: Richiede più parametri da stimare, il che significa che necessita di **più dati per una stima affidabile**. Ha un bias minore ma una varianza maggiore rispetto all'LDA. Può essere sensibile agli outlier e incontrare difficoltà con dati ad alta dimensionalità.

In sintesi, la scelta tra LDA e QDA dipende dalla natura dei dati e dalle risorse disponibili. L'LDA è preferibile quando le covarianze delle classi sono simili o i dati di addestramento sono limitati, offrendo maggiore stabilità. La QDA, con la sua maggiore flessibilità nei confini di decisione, è più adatta quando le covarianze tra le classi differiscono significativamente e si dispone di un'abbondanza di dati. Entrambe le tecniche forniscono probabilità di appartenenza alle classi.