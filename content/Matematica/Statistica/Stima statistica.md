---
tags:
  - statistical-inference
  - estimators
  - bias-variance-tradeoff
---


# Stima Statistica

La **Stima Statistica** è il processo inferenziale che permette di utilizzare i dati raccolti da un campione per inferire o generalizzare i valori dei parametri sconosciuti di una popolazione più ampia. Questo processo è intrinsecamente caratterizzato da incertezza, che può derivare dalla variabilità campionaria (l'analisi di campioni diversi produrrebbe risultati differenti) e dagli errori di misurazione. L'obiettivo principale è stimare un vettore di parametri $\theta$ che caratterizza la distribuzione di probabilità di un carattere di interesse $X$ nella popolazione. Questo ragionamento è induttivo, passando dal campione osservato alla popolazione ignota.

#### [[Stimatore]]

Uno **stimatore** è una funzione delle variabili aleatorie (v.a.) che compongono un campione casuale $X_1, X_2, \ldots, X_n$, denotata come $T = t(X_1, X_2, \ldots, X_n)$, utilizzata per approssimare il valore di un parametro ignoto $\theta$ della popolazione. Per esempio, se si vuole stimare l'altezza media della popolazione italiana, assumendo che $X \sim N(\mu, \sigma^2)$, la media campionaria $\bar{X}$ è uno stimatore di $\mu$.

#### Stima

La **stima** è la realizzazione numerica dello stimatore ottenuta applicando la funzione $t(\cdot)$ ai valori osservati in un particolare campione $x_1, x_2, \ldots, x_n$. Mentre lo stimatore è una variabile aleatoria (funzione del campione), la stima è un valore fisso derivato da un singolo campione.

#### Proprietà degli Stimatori

Per valutare la "bontà" di uno stimatore, si considerano diverse proprietà desiderabili:

1. **Non Distorsione (Correttezza)**: Uno stimatore $\hat{\theta}$ è definito **non distorto** (o corretto) per un parametro $\theta$ se il suo valore atteso coincide con il vero valore del parametro, ovvero $E[\hat{\theta}] = \theta$. Ciò significa che, se si potessero ripetere infinite volte il processo di campionamento e di stima, la media delle stime ottenute sarebbe esattamente uguale al parametro vero. La **distorsione (Bias)** di uno stimatore è la differenza tra il suo valore atteso e il parametro vero: $B(\hat{\theta}) = E[\hat{\theta}] - \theta$. Uno stimatore non distorto ha un bias pari a zero.
    
    - **Esempio pratico**: La media campionaria $\bar{X}$ è uno stimatore non distorto della media della popolazione $\mu$. La varianza campionaria $S^2 = \frac{1}{n-1}\sum_{i=1}^n (X_i - \bar{X})^2$ è uno stimatore non distorto della varianza della popolazione $\sigma^2$, a differenza di $\tilde{S}^2 = \frac{1}{n}\sum_{i=1}^n (X_i - \bar{X})^2$, che è uno stimatore distorto. La correzione di Bessel ($n-1$ al denominatore) serve proprio a eliminare questo bias.
2. **Efficienza**: L'efficienza di uno stimatore è una misura della sua precisione, spesso valutata attraverso l'**Errore Quadratico Medio (MSE)**. Dati due stimatori $T_1$ e $T_2$ del parametro $\theta$, $T_1$ è considerato più efficiente di $T_2$ se $MSE_\theta(T_1) \leq MSE_\theta(T_2)$ per ogni $\theta$, e la disuguaglianza è stretta per almeno un $\theta$. L'MSE di uno stimatore $\hat{\theta}$ è definito come $MSE_\theta(\hat{\theta}) = E[(\hat{\theta} - \theta)^2]$. L'MSE può essere decomposto come la somma della varianza dello stimatore e del quadrato della sua distorsione: $MSE_\theta(\hat{\theta}) = Var(\hat{\theta}) + [B(\hat{\theta})]^2$. Per stimatori non distorti, l'MSE coincide con la varianza, rendendo il confronto di efficienza equivalente al confronto delle varianze.
    
    - **Trade-off Bias-Varianza**: Questo concetto è fondamentale nella statistica e nell'apprendimento statistico. Modelli statistici più flessibili tendono ad avere un bias minore ma una varianza maggiore, mentre modelli meno flessibili presentano un bias maggiore ma una varianza minore. L'obiettivo è trovare un equilibrio che minimizzi l'errore di previsione su dati non visti (test MSE). Un modello troppo flessibile può "overfittare" i dati di training, imparando anche il rumore e i pattern casuali, risultando in un MSE di training basso ma un MSE di test elevato. La figura 2.11 illustra la curva a U dell'MSE di test all'aumentare della flessibilità del modello, mostrando il punto ottimale tra bias e varianza.
3. **Consistenza**: Uno stimatore è **consistente** se, all'aumentare della dimensione campionaria $n$, la successione di stimatori $T_n$ converge in probabilità al vero valore del parametro $\theta$. Formalmente, per ogni $\epsilon > 0$ arbitrariamente piccolo, $\lim_{n \to \infty} P(|T_n - \theta| < \epsilon) = 1$. Perché uno stimatore sia consistente, sono sufficienti due condizioni:
    
    - **Non distorsione asintotica**: $\lim_{n \to \infty} E[T_n] = \theta$.
    - **Varianza tendente a zero**: $\lim_{n \to \infty} Var(T_n) = 0$.
    - **Esempio pratico**: La media campionaria $\bar{X}$ è uno stimatore consistente della media della popolazione $\mu$, poiché è non distorta e la sua varianza ($\sigma^2/n$) tende a zero all'aumentare di $n$.
4. **Statistiche Sufficienti**: Una **statistica sufficiente** per un parametro $\theta$ è una funzione del campione che riassume tutte le informazioni rilevanti contenute nel campione riguardo a quel parametro. Formalmente, una statistica $T(X)$ è sufficiente per $\theta$ se la distribuzione condizionata di $X$ dato $T(X)$ non dipende da $\theta$. Ciò implica che, una volta conosciuto il valore della statistica sufficiente, ulteriori dettagli del campione non aggiungono informazioni su $\theta$. Lo stimatore di massima verosimiglianza, se esiste, è una funzione di una statistica sufficiente.
    

#### Metodi di Costruzione degli Stimatori

Esistono diversi metodi per costruire stimatori:

1. **Metodo dei Momenti**: Questo metodo consiste nell'eguagliare i momenti campionari (come la media campionaria, la varianza campionaria, ecc.) ai corrispondenti momenti teorici della popolazione (espressi in termini dei parametri ignoti) e risolvere il sistema di equazioni risultante per ottenere le stime dei parametri.
    
2. **Metodo della Massima Verosimiglianza (MLE - Maximum Likelihood Estimation)**: Il Metodo della Massima Verosimiglianza (MLE) è il più diffuso e potente per la costruzione di stimatori. Si basa sull'idea di scegliere come stima dei parametri $\theta$ il valore $\hat{\theta}_{MLE}$ che rende massimamente probabile l'osservazione del campione dato.
    
    - **Funzione di Verosimiglianza**: Data una popolazione con funzione di probabilità/densità $f(x; \theta)$ e un campione casuale $X_1, X_2, \ldots, X_n$ (indipendenti e identicamente distribuite), la densità congiunta del campione è il prodotto delle densità marginali: $f(x_1, \ldots, x_n; \theta) = \prod_{i=1}^n f(x_i; \theta)$. La **funzione di verosimiglianza** $L(\theta|x_1, \ldots, x_n)$ è questa densità congiunta, interpretata come una funzione del parametro $\theta$ per un campione $x$ osservato.
        
    - **Log-Verosimiglianza**: Per motivi computazionali e analitici, è spesso più conveniente massimizzare il logaritmo della funzione di verosimiglianza, chiamato **log-verosimiglianza**, $\ell(\theta|x) = \ln L(\theta|x) = \sum_{i=1}^n \ln f(x_i; \theta)$. Massimizzare la log-verosimiglianza equivale a massimizzare la verosimiglianza, dato che la funzione logaritmo è monotona crescente.
        
    - Per trovare lo stimatore $\hat{\theta}_{MLE}$, si calcola la derivata prima della log-verosimiglianza rispetto a $\theta$ e la si pone uguale a zero, risolvendo l'equazione (o un sistema di equazioni se $\theta$ è un vettore).
        
    - **Esempio pratico**: Per una variabile $X_i \sim Bern(\pi)$, lo stimatore di massima verosimiglianza per $\pi$ è la media campionaria $\bar{X} = \frac{1}{n}\sum_{i=1}^n X_i$. Nell'ambito dei Modelli Lineari Generalizzati (GLM), i parametri $\beta$ sono stimati tramite massima verosimiglianza.
        
    - **Proprietà degli Stimatori di Massima Verosimiglianza (MLE)**:
        
        - **Invarianza**: Se $\hat{\theta}_{MLE}$ è lo stimatore di massima verosimiglianza di $\theta$, e $g(\cdot)$ è una funzione biunivoca, allora $g(\hat{\theta}_{MLE})$ è lo stimatore di massima verosimiglianza di $g(\theta)$.
        - **Efficienza Asintotica**: L'MLE è asintoticamente efficiente. Se esiste uno stimatore non distorto ed efficiente per $\theta$, allora questo è lo stimatore di massima verosimiglianza.
        - **Non Distorsione Asintotica**: L'MLE è asintoticamente non distorto.
        - **Consistenza**: L'MLE è consistente.
        - **Distribuzione Asintoticamente Normale**: L'MLE si distribuisce asintoticamente come una distribuzione Normale.
    - **Informazione di Fisher**: La **Matrice di Informazione di Fisher** misura la quantità di informazione che i dati campionari contengono riguardo al parametro $\theta$. Matematicamente, l'Informazione di Fisher è definita come meno la derivata seconda attesa della log-verosimiglianza, $E[-\frac{\partial^2 \ell(\theta|x)}{\partial \theta \partial \theta^T}]$, che per le distribuzioni della famiglia esponenziale spesso coincide con $E[\frac{\partial \ell(\theta|x)}{\partial \theta} (\frac{\partial \ell(\theta|x)}{\partial \theta})^T]$. Nell'ambito dei GLM, la matrice di informazione di Fisher $I(\beta)$ assume una forma compatta come $\frac{1}{a(\phi)}X^T W(\beta) X$, dove $a(\phi)$ è il parametro di dispersione, $X$ è la matrice del design, e $W(\beta)$ è una matrice di pesi che dipende dal modello. Questa matrice è cruciale negli algoritmi iterativi per la stima dei GLM, come l'Iterative Weighted Least Squares (IWLS), dove sostituisce la matrice Hessiana nella ricerca dei coefficienti ottimali. Essa è simmetrica e positiva definita per i modelli della famiglia esponenziale con link canonico. L'inverso della matrice di Informazione di Fisher fornisce un limite inferiore alla varianza di qualsiasi stimatore non distorto (Cramér-Rao lower bound) e, asintoticamente, alla varianza dell'MLE.