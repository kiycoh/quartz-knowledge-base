---
last modified: 24/10/2025 02:56
related:
  - '[[Modello lineare classico]]'
  - '[[Statistica]]'
tags:
  - machine-learning
  - statistical-modeling
  - linear-regression
---
# Definizione di modello lineare generalizzato
Un **modello lineare generalizzato (GLM)** è una generalizzazione (o estensione) del [[modello lineare classico]] nell'ambito della [[Regressione lineare]] che consente di modellare relazioni tra i predittori (le variabili indipendenti) e la variabile di risposta (la variabile dipendente).quando:
* La variabile risposta non segue la distribuzione normale;
* La relazione tra variabile risposta e le esplicative NON è necessariamente lineare ([[#Funzione di legame]])

![[Pasted image 20250531195406.png#center|400]]
**Il piano orizzontale (la base):** Rappresenta lo spazio definito da due variabili predittrici, chiamiamole $X_1$ e $X_2$. Ogni punto su questo piano è una combinazione di valori di $X_1$ e $X_2$.
* **I punti rossi:** Sono i **dati osservati**. Ogni punto ha tre coordinate $(x_1, x_2, y)$, dove $y$ è il valore reale della variabile di risposta che hai misurato. Nota che i punti non giacciono su una superficie piana, ma sono sparsi.
    * **Il piano giallo inclinato:** Questo è il cuore del modello. Rappresenta il **valore atteso (la media) della variabile di risposta**, predetto dal modello per ogni combinazione dei predittori. In un GLM, questa superficie è ottenuta tramite due passaggi:
        1.  Un **predittore lineare**: $η = β_0 + β_1x_1 + β_2x_2$. Questa è una combinazione lineare dei predittori, che di per sé definirebbe un piano.
        2.  Una **funzione di legame (link function)**: Questa funzione $g(\cdot)$ collega la media della risposta al predittore lineare. Il piano giallo che vediamo è quindi la rappresentazione di $E[Y] = g^{-1}(η)$, cioè la media della risposta trasformata per tornare alla sua scala originale.
    * **Le curve a campana blu:** Questa è la parte "Generalizzata". A differenza di un modello lineare classico (che assume che i punti si disperdano secondo una distribuzione Normale con varianza costante attorno al piano), un GLM permette che la distribuzione della risposta appartenga ad altre famiglie (es. Poisson, Binomiale, Gamma). Le curve blu mostrano che per un dato valore dei predittori, il modello non predice un singolo punto sul piano giallo, ma una **distribuzione di probabilità** di cui il piano giallo rappresenta solo la **media**. I punti rossi (i dati reali) sono visti come un campione estratto da queste distribuzioni.

> [!EXAMPLE] Esempi di applicazioni pratiche tramite GLM
> I GLM possono gestire variabili risposta che seguono altre distribuzioni oltre quella normale:
> - **Conteggi**: numero di clienti, numero di errori (distribuzione di Poisson).
> - **Proporzioni/Probabilità**: successo/fallimento, sì/no (distribuzione Binomiale, come nella regressione logistica).
> - **Tempi di attesa**: (distribuzione Gamma o Esponenziale).
> Di seguito alcuni esempi di GLM specifici:
> * la [[Regressione lineare]]: la variabile risposta è continua e positiva, spesso asimmetrica. Assume che $Y$ segua una distribuzione Gamma. Un legame comune è la funzione log: $\log(\mu) = \beta_0 + \beta_1x_1 + \ldots + \beta_px_p$. Similmente alla regressione di Poisson, $e^{\beta_i}$ è il fattore moltiplicativo per la media $\mu$. Applicazioni includono tempi, costi, e redditi.
> * la [[Regressione logistica]]: la variabile risposta è binaria (es. 0 o 1). Assume che $Y$ segua una distribuzione Bernoulli (o Binomiale con $n=1$). Il legame canonico è la funzione logit: $\log(\frac{p}{1-p}) = \beta_0 + \beta_1x_1 + \ldots + \beta_px_p$. $e^{\beta_i}$ rappresenta l'odds ratio per l'aumento di un'unità in $x_i$. È ampiamente usata per la classificazione binaria.
> * la [[Regressione di Poisson]]: la variabile risposta è un conteggio (numeri interi non negativi). Assume che $Y$ segua una distribuzione Poisson. Il legame canonico è la funzione log: $\log(\lambda) = \beta_0 + \beta_1x_1 + \ldots + \beta_px_p$. $e^{\beta_i}$ rappresenta il fattore moltiplicativo per la media $\lambda$ quando $x_i$ aumenta di un'unità. È usata per modellare eventi rari o tassi di incidenza.

## [[Funzione di legame (Statistica)]]
La **funzione di legame ("*link function*" in inglese)** permette di trasformare la relazioni tra le variabili: anche se i predittori sono combinati linearmente, questa combinazione lineare è poi collegata alla media della variabile risposta attraverso questa funzione di legame, permettendo di modellare relazioni che non sono una linea retta sulla scala originale della variabile risposta.
# Definizione di modello lineare generalizzato (GLM)
I **modelli Lineari Generalizzati (GLM)** (o Generalized Linear Models in inglese) sono un *framework statistico* che estende il [[Modello lineare classico]]. ==Essi consentono di modellare relazioni tra una variabile risposta e variabili esplicative anche quando la risposta non segue una distribuzione normale o la relazione non è necessariamente lineare==. 
## Componenti di un GLM
Un GLM è costituito da *tre componenti fondamentali*:
1. **Componente casuale (o stocastica)**: specifica la distribuzione di probabilità della variabile risposta $Y$. Si assume che $Y$ segua una distribuzione appartenente alla [[Famiglia naturale esponenziale (NEF)]].
    - **Proprietà fondamentali**: Per una variabile della famiglia esponenziale, il valore atteso e la varianza sono dati da:
        - $E[Y] = \mu = b'(\theta)$
        - $Var[Y] = b''(\theta)a(\phi)$ dove $b'(\theta)$ e $b''(\theta)$ sono la prima e la seconda derivata di $b(\theta)$ rispetto a $\theta$. La funzione $b''(\theta)$ è nota come **funzione di varianza**, $V(\mu)$, quindi $Var[Y] = a(\phi)V(\mu)$.
    - **Esempi di distribuzioni**: Rientrano in questa famiglia le distribuzioni Normale, Binomiale, Poisson e Gamma.
2. **Componente sistematica**: Le variabili esplicative $X_1, \ldots, X_p$ producono un **predittore lineare** $\eta$: $\eta = \beta_0 + \beta_1X_1 + \ldots + \beta_pX_p$. In notazione matriciale, si esprime come $\mathbf{y} = \mathbf{X}\boldsymbol{\beta} + \boldsymbol{\varepsilon}$.
    - Le variabili in $\mathbf{X}$ possono essere quantitative, categoriali o un mix. Possono essere originali o derivate tramite trasformazioni (es. logaritmi, potenze, funzioni trigonometriche) o interazioni (combinazioni di più variabili, tipicamente tramite prodotto).
    - La dimensione del modello è data dal numero di parametri $k$ nel vettore $\boldsymbol{\beta}$. Si distinguono modelli saturi ($k=n$), ridotti ($k<n$) e nulli ($k=1$, con $\mathbf{X}$ come vettore di 1).

**GLM vs. Trasformazione Diretta della Variabile Risposta**: Una differenza cruciale tra i GLM e altri approcci (es. trasformazione di una variabile $Y$) è che nei GLM non si trasforma direttamente la variabile risposta $Y$, ma il suo valore atteso $\mu$: $g(\mu) = \eta$. Applicare una trasformazione direttamente a $Y$ (es. $\log(Y) = X\boldsymbol{\beta} + \boldsymbol{\varepsilon}$) può portare a incoerenze, poiché in generale $E[g(Y)] \neq g(E[Y])$. La funzione legame nei GLM mantiene la coerenza statistica, evitando errori sistematici.

**Stima dei Parametri nei GLM**: I parametri $\beta$ nei GLM sono stimati tramite il metodo della **[[Massima verosimiglianza]]**. Poiché le equazioni di verosimiglianza non ammettono generalmente una soluzione esplicita, è necessario ricorrere a metodi iterativi. L'algoritmo standard è l'**Iterative Weighted Least Squares (IWLS)**, basato sul metodo di Newton-Raphson. L'IWLS risolve un problema di minimi quadrati pesati ad ogni iterazione, aggiornando iterativamente i pesi.

**Diagnostica nei GLM**: La diagnostica è fondamentale per valutare l'adeguatezza del modello, verificando la scelta della famiglia di distribuzione e della funzione legame, la forma funzionale del predittore lineare e la presenza di outlier o punti influenti. Si utilizzano diversi tipi di residui:

- **Residui Ordinari (o di Risposta)**: $r_i = y_i - \hat{\mu}_i$. Hanno utilità limitata nei GLM poiché non tengono conto della funzione di link.
- **Residui di Lavoro (Working Residuals)**: $r_W = \mathbf{z}(\hat{\boldsymbol{\beta}}) - \hat{\boldsymbol{\eta}}(\hat{\boldsymbol{\beta}}) = \mathbf{D}(\hat{\boldsymbol{\beta}})^{-1}[\mathbf{y} - \hat{\boldsymbol{\mu}}(\hat{\boldsymbol{\beta}})]$. Sono più informativi dei residui ordinari in quanto considerano la struttura del modello.
- **Residui di Pearson**: $r_{Pi} = \frac{y_i - \hat{\mu}_i}{\sqrt{a(\hat{\phi})V(\hat{\mu}_i)}}$. Sono residui standardizzati che stimano il contributo di ogni osservazione all'adeguatezza complessiva del modello.
- **Residui di Devianza**: $r_{Di} = \text{sign}(y_i - \hat{\mu}_i) \sqrt{\frac{2}{a(\hat{\phi})} [ y_i(\tilde{\theta}_i - \hat{\theta}_i) - b(\tilde{\theta}_i) + b(\hat{\theta}_i) ]}$. Rappresentano il contributo individuale alla devianza complessiva del modello e tengono conto della famiglia esponenziale e del link.
- **Residui Jackknife (o Predittivi)**: Non sono un nuovo tipo di residui, ma un modo diverso di calcolare quelli già noti, escludendo ogni osservazione a turno durante la stima per ottenere una previsione "leave-one-out".
- **Elementi di Leva (Leverages)**: Elementi diagonali della hat matrix $\mathbf{H}$, misurano quanto l'i-esima osservazione è distante dal centro dello spazio delle esplicative e il suo potenziale di influenza.
- **Distanza di Cook**: Misura l'influenza complessiva di un'osservazione, combinando informazioni sui residui e sui leverages.

I GLM sono strumenti versatili per l'analisi dei dati, offrendo una grande flessibilità nel modellare diversi tipi di variabili risposta e relazioni, pur mantenendo un solido fondamento statistico e interpretativo.