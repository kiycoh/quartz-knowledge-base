---
tags:
  - machine-learning
  - statistica-inferenziale
  - regressione-lineare
---

# Definizione di funzione legame
La funzione legame (o _link function_, $g(\cdot)$) è una componente fondamentale dei Modelli Lineari Generalizzati (GLM). Essa stabilisce la relazione tra il valore atteso della variabile risposta $\mu = E[Y|\mathbf{X}]$ e il [[predittore lineare]] $\eta = \beta_0 + \beta_1X_1 + \dots + \beta_pX_p$. Matematicamente, si esprime come $g(\mu) = \eta$.

### Scopo e Necessità
Il principale scopo della funzione legame è permettere di modellare variabili risposta che non seguono una distribuzione normale e per le quali la relazione tra la risposta e i predittori non è necessariamente lineare. In particolare, consente di mappare il range del valore atteso della variabile risposta, che spesso è limitato (ad esempio, le probabilità sono confinate tra 0 e 1), all'intero asse dei numeri reali, su cui opera il predittore lineare.

Le proprietà desiderate per $g(\cdot)$ includono la differenziabilità e la monotonicità (strettamente crescente o decrescente), con un'inversa ben definita $g^{-1}$.

### Ruolo nei Modelli Lineari Generalizzati (GLM)

All'interno di un GLM, la funzione legame è uno dei tre elementi costitutivi, insieme alla componente casuale (la distribuzione della variabile risposta, appartenente alla famiglia esponenziale naturale) e alla componente sistematica (il predittore lineare).

La relazione fondamentale per la famiglia esponenziale è $E[Y] = \mu = b'(\theta)$ e $Var[Y] = b''(\theta)a(\phi)$, dove $\theta$ è il parametro naturale e $b''(\theta)$ è la funzione di varianza $V(\mu)$. La funzione legame canonica $g(\mu) = \theta$ connette direttamente il valore atteso $\mu$ al parametro naturale $\theta$. Questo tipo di legame offre vantaggi significativi in termini di semplificazione della stima dei parametri e proprietà statistiche ottimali.

### Esempi Pratici di Funzioni Legame
La scelta della funzione legame dipende dalla distribuzione assunta per la variabile risposta:

1. **Regressione Lineare (Distribuzione Normale)**:
    
    - **Funzione Legame:** Identità $g(\mu) = \mu$.
    - **Esempio Immaginifico:** Si vuole prevedere l'altezza media ($\mu$) di una popolazione in base all'età (X). Si assume che l'altezza sia normalmente distribuita. Il modello sarà semplicemente $\mu = \beta_0 + \beta_1 \cdot Età$, cioè l'identità tra il valore atteso e il predittore lineare.
2. **Regressione Logistica (Distribuzione Bernoulli/Binomiale)**:
    
    - **Funzione Legame:** Logit $g(\mu) = \log\left(\frac{\mu}{1-\mu}\right)$. Qui, $\mu$ è la probabilità di "successo" $P(Y=1)$, che varia tra 0 e 1. La funzione logit mappa questo intervallo a $(-\infty, +\infty)$.
    - **Esempio Immaginifico:** Prevedere la probabilità di default di un cliente ($\mu$) in base al suo saldo del conto (X). Poiché $\mu$ è una probabilità, il suo valore è tra 0 e 1. La funzione logit trasforma questa probabilità in log-odds, che possono variare su tutto l'asse reale: $\log\left(\frac{P(Default=Sì|Saldo)}{1-P(Default=Sì|Saldo)}\right) = \beta_0 + \beta_1 \cdot Saldo$.
3. **Regressione di Poisson (Distribuzione Poisson)**:
    
    - **Funzione Legame:** Log $g(\mu) = \log(\mu)$. Qui, $\mu$ è il tasso di eventi o il conteggio atteso, che deve essere non negativo. La funzione logaritmo garantisce che il valore atteso $\mu = e^\eta$ sia sempre positivo.
    - **Esempio Immaginifico:** Modellare il numero di incidenti stradali in un incrocio ($\mu$) in base al volume di traffico (X). Il numero di incidenti è un conteggio, quindi $\mu \ge 0$. La funzione logaritmica assicura che il valore atteso sia sempre coerente: $\log(\mu) = \beta_0 + \beta_1 \cdot Traffico$.
4. **Regressione Gamma (Distribuzione Gamma)**:
    
    - **Funzione Legame:** Log $g(\mu) = \log(\mu)$ (più comune) o Inversa $g(\mu) = -1/\mu$. Utilizzata per variabili continue positive e spesso asimmetriche, come tempi o costi.
    - **Esempio Immaginifico:** Stimare il costo medio dei sinistri assicurativi auto ($\mu$) in base all'età del conducente (X). I costi sono valori positivi, e la distribuzione Gamma è adatta per variabili continue positive con asimmetria. Il modello con link logaritmico sarebbe $\log(\mu) = \beta_0 + \beta_1 \cdot Età$.

### Stima dei Parametri

Nei GLM, i parametri del modello ($\beta$) vengono stimati tramite il metodo della massima verosimiglianza. Poiché le equazioni di verosimiglianza dipendono non linearmente da $\beta$ attraverso la funzione legame, la soluzione non è esplicita e richiede metodi iterativi. L'algoritmo standard è l'Iterative Weighted Least Squares (IWLS), che ad ogni iterazione risolve un problema di minimi quadrati ponderati, aggiornando dinamicamente i pesi che derivano dalla funzione legame e di varianza. Le derivate della funzione legame sono cruciali nella costruzione del vettore score e della matrice di informazione di Fisher utilizzati nell'IWLS.

### [[Diagnostica GLM]]
### Distinzione Cruciale: $g(\mu)$ vs. $g(Y)$
È fondamentale notare che nei GLM la trasformazione ($g(\cdot)$) viene applicata al _valore atteso_ della variabile risposta ($\mu$), non direttamente alla variabile risposta osservata $Y$. Questa distinzione è cruciale perché, in generale, $E[g(Y)] \neq g(E[Y])$. Trasformare direttamente $Y$ potrebbe portare a stime incoerenti e errori sistematici, mentre la funzione legame nei GLM mantiene la coerenza dell'interpretazione statistica.