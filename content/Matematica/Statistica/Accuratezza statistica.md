---
tags:
  - machine-learning
  - classificazione-statistica
  - statistica-inferenziale
---

Per confrontare dei Modelli Lineari Generalizzati (GLM), è essenziale valutare la loro capacità di adattamento ai dati, la loro complessità e la loro performance predittiva su osservazioni non viste, tenendo conto del trade-off tra bias e varianza. Un modello _ottimale_ minimizza l'errore su nuovi dati, non necessariamente quello sui dati di addestramento.

> [!EXAMPLE] Esempio pratico di accuratezza nella regressione logistica
> Ad esempio, in un modello di regressione logistica per prevedere i movimenti giornalieri del mercato azionario, un'accuratezza del 56% indica che il 56% dei movimenti giornalieri è stato correttamente previsto.

Due metriche fondamentali nel confronto dei modelli, in particolare in problemi di classificazione, sono l'**Accuratezza** e la **Sensibilità**.

### 1. Accuratezza (Accuracy)
L'**Accuratezza** è una metrica di valutazione della performance del modello, specialmente nel contesto della classificazione, che quantifica la proporzione di previsioni corrette rispetto al totale delle previsioni.

- **Definizione**: Nel contesto della classificazione, l'accuratezza è calcolata come: $\text{Accuratezza} = \frac{\text{TP} + \text{TN}}{\text{TP} + \text{TN} + \text{FP} + \text{FN}}$ dove:
    
    - **TP** (True Positives): osservazioni positive correttamente classificate come positive.
    - **TN** (True Negatives): osservazioni negative correttamente classificate come negative.
    - **FP** (False Positives): osservazioni negative erroneamente classificate come positive (errore di I tipo).
    - **FN** (False Negatives): osservazioni positive erroneamente classificate come negative (errore di II tipo).
- **Contesto e Interpretazione**:
    - **Regressione**: In un contesto di regressione, la "qualità di adattamento" (accuracy) è spesso misurata tramite l'[[Errore quadratico medio (MSE)]]. Si distingue tra **MSE di training** (calcolato sui dati usati per addestrare il modello) e **MSE di test** (calcolato su dati non visti). L'obiettivo è minimizzare il MSE di test, non quello di training, poiché un modello con un MSE di training basso ma un MSE di test alto indica _overfitting_. Un esempio pratico riguarda la previsione del prezzo di un'azione o del rischio di diabete, dove l'accuratezza su dati futuri è l'obiettivo primario.
    - **Limiti**: L'accuratezza può essere fuorviante in presenza di dataset molto sbilanciati. Ad esempio, in un problema di diagnosi di una malattia rara (prevalenza 1%), un modello che predice sempre "negativo" avrebbe un'accuratezza del 99%, ma sarebbe inutile per identificare i casi positivi. Per questo motivo, sono necessarie metriche più dettagliate come la Precisione, il Richiamo (Sensitivity) e l'F1-Score.
    - **Misura della Variabilità/Complessità**: In alcuni algoritmi come Random Forest, l'accuratezza può essere usata per misurare l'importanza delle variabili. La "Gini decrease" è un sottoprodotto dell'algoritmo, mentre la "accuracy decrease" (riduzione dell'accuratezza) è una metrica più affidabile per l'importanza delle variabili, sebbene richieda calcoli aggiuntivi.
    - **Overfitting**: L'accuratezza sui dati di training è spesso troppo ottimistica e tende a sottostimare l'errore su dati di test. Metodi più flessibili possono raggiungere un'accuratezza del training molto alta, ma la loro performance sui dati di test potrebbe peggiorare a causa dell'overfitting.
### 2. Sensibilità (Sensitivity o Richiamo / Recall)
La **Sensibilità**, o Richiamo (Recall), è una metrica cruciale in contesti di classificazione, particolarmente quando il costo dei Falsi Negativi (FN) è elevato. Caratterizza la performance di un classificatore o di un test di screening.

- **Definizione**: La Sensibilità misura la proporzione di veri positivi (casi reali positivi) che sono stati correttamente identificati dal modello: $\text{Sensibilità} = \text{Richiamo} = \frac{\text{TP}}{\text{TP} + \text{FN}}$
    
- **Contesto e Interpretazione**:
    
    - **Diagnosi Mediche**: In campo medico, è fondamentale avere un'alta sensibilità per evitare di perdere casi positivi (es. malati). Ad esempio, se un paziente è affetto da una malattia grave, un modello con alta sensibilità minimizzerà la probabilità di un falso negativo, cioè di non diagnosticare la malattia.
    - **Rilevamento Frodi**: Similmente, nel rilevamento delle frodi finanziarie, un'alta sensibilità assicura che un gran numero di transazioni fraudolente venga identificato.
    - **Relazione con Specificità**: La sensibilità è spesso messa in relazione con la **Specificità**, che misura la proporzione di veri negativi correttamente identificati. Esiste un trade-off tra sensibilità e specificità: aumentare una di solito comporta la diminuzione dell'altra.
    - **Curva ROC**: La relazione tra sensibilità e specificità per tutte le possibili soglie di decisione di un classificatore viene visualizzata tramite la **Curva ROC (Receiver Operating Characteristic)**. L'asse Y della curva ROC rappresenta il Tasso di Veri Positivi (che è la sensibilità), mentre l'asse X rappresenta il Tasso di Falsi Positivi (1 - Specificità). Un classificatore ottimale "abbraccia" l'angolo in alto a sinistra del grafico ROC, indicando alta sensibilità e bassa specificità (o alto tasso di veri positivi e basso tasso di falsi positivi). L'Area Sotto la Curva (AUC) della ROC è una misura sintetica della capacità discriminatoria del modello.
    - **Soglia di Decisione**: Nei classificatori che producono probabilità, la sensibilità può essere influenzata modificando la soglia di decisione. Abbassare la soglia aumenta la sensibilità (e riduce i falsi negativi), ma può ridurre la precisione (aumentando i falsi positivi). La scelta della soglia ottimale dipende dal problema specifico e dai costi relativi degli errori.
- **Pagine di riferimento per "Sensitivity"**:,,,,,,,,,,,,,,,,,,.
    

### 3. Altri Criteri per Confrontare i GLM

Oltre ad Accuratezza e Sensibilità, il confronto dei GLM si avvale di altri strumenti:

- **Test del Rapporto di Verosimiglianza (LRT)**: Usato per confrontare modelli annidati (dove un modello è un sottoinsieme dell'altro). La statistica test si basa sulla differenza delle devianze e segue una distribuzione chi-quadrato.
- **Criteri Informativi (AIC, BIC)**: Utilizzati quando i modelli non sono annidati o per la selezione del modello. Bilanciano la bontà di adattamento (log-verosimiglianza) con la complessità (numero di parametri), penalizzando i modelli più complessi. Valori più bassi indicano modelli preferibili.
- **Pseudo-$R^2$**: Tentativi di estendere il concetto di $R^2$ della regressione lineare ai GLM (es. McFadden, Nagelkerke). Misurano la proporzione di variabilità spiegata dal modello, ma la loro interpretazione non è diretta come nell'$R^2$ classico e non sono confrontabili tra diverse famiglie di distribuzione.
- **Cross-Validation**: Tecnica fondamentale per stimare la capacità di generalizzazione di un modello su dati non visti e prevenire l'overfitting. Consiste nel suddividere i dati in training e test set ripetutamente, fornendo una stima robusta dell'errore di test. È cruciale per la selezione di iperparametri.
- **Analisi Diagnostica dei Residui**: Permette di verificare l'adeguatezza del modello in termini di scelta della famiglia di distribuzione, funzione di link e forma funzionale del predittore lineare, oltre a identificare outlier e punti influenti. Plot di residui, leve e distanze di Cook sono strumenti chiave.

In sintesi, la valutazione dei GLM è un processo multi-criterio che considera accuratezza predittiva, interpretabilità del modello e robustezza dei risultati, usando un mix di test statistici, metriche di performance e tecniche di validazione incrociata.