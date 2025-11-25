---
last modified: 24/10/2025 14:02
related:
  - '[[Machine learning]]'
  - '[[Analisi della regressione]]'
tags:
  - machine-learning
  - linear-regression
  - statistical-modeling
---
# Definizione di regressione lineare
La **regressione lineare** è un modello di [[Apprendimento supervisionato|apprendimento supervisionato]] utilizzato per compiti di **regressione**. Il suo obiettivo è predire il valore di una variabile di risposta **numerica continua**, modellando la relazione lineare tra questa e una o più variabili predittorie.

$$
Y = \alpha + \beta X + \varepsilon
$$

> ![[linear_regression.svg|500]]
> - I modelli di regressione sono utili per scoprire le relazioni tra i dati.
> - Un caso speciale di regressione lineare è quando è presente **solo una variabile esplicativa**: Questo è chiamato regressione lineare semplice.
> - Quando ci sono **più variabili esplicative**, il processo è chiamato regressione lineare multipla.

> [!QUESTION]- Approfondimento sulla linea di regressione
> ![[Pasted image 20250523182303.png#center]]
> Regressione lineare è sinonimo di **linea di regressione**, *cioè è la linea di migliore adattamento tracciata attraverso un grafico a dispersione dei dati*. Le linee verticali dalla linea di regressione ai punti del campione sono chiamate **[[Residui statistici|residui]] (o offsets)** e rappresentano gli errori nella previsione del modello di regressione.
## Tipi di regressione lineare
* [[Regressione lineare semplice]]
* [[Regressione lineare multipla]]
## Tipi di assunzioni
## Assunzioni deboli
Le **assunzioni deboli del modello di regressione** (o **ipotesi deboli**) sono condizioni fondamentali che permettono di **stimare i parametri** del modello (cioè $\alpha$ e $\beta$) in modo **corretto e affidabile**, **ma senza pretendere troppo**.  
Sono chiamate “deboli” perché **non richiedono condizioni forti** come la normalità degli errori.
## Assunzioni forti
Le **assunzioni forti** in un modello di **regressione lineare** sono le **condizioni teoriche** che devono essere rispettate affinché le **stime dei parametri** siano affidabili e le **inferenze statistiche** (come test e intervalli di confidenza) siano valide.

La **regressione lineare** è una tecnica di modellazione statistica utilizzata per descrivere una [[Variabile quantitativa statistica|variabile quantitativa statistica continua]] in funzione di una o più variabili. 
* La regressione lineare classica *funziona al meglio quando la variabile che stai cercando di prevedere (la variabile risposta) ha una distribuzione normale, o almeno i suoi errori ce l'hanno.*
	* si assume che l'effetto delle variabili esplicative sulla variabile risposta sia lineare (se una aumenta, l'altra aumenta o diminuisce in modo costante).

> [!NOTE]- Regressione lineare vs [[Regressione logistica]]
> | Aspetto                   | Regressione lineare             | Regressione logistica                              |
> | ------------------------- | ------------------------------- | -------------------------------------------------- |
> | **Tipo di output**        | Continuo (numerico)             | Categorico (probabilità)                           |
> | **Funzione obiettivo**    | Minimizzare l'errore quadratico | Massimizzare la probabilità (max. verosimiglianza) |
> | **Metriche comuni**       | MSE, $R^2$, MAE                 | Accuratezza, precisione, recall, F1-score, AUC-ROC |
> | **Tipologia di problema** | Regressione                     | Classificazione                                    |
>
