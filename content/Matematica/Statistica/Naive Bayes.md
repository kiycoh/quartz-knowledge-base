---
last modified: 2025-06-23T16:32:00.000Z
related:
  - '[[Machine learning]]'
  - '[[Teorema di Bayes]]'
tags:
  - machine-learning
  - naive-bayes
  - bayesian-statistics
---
# Definizione di *Naive Bayes*
Il *Naive Bayes* è un [[Classificatore probabilistico]] basato sul [[Teorema di Bayes]]. 
* ==È definito "ingenuo" (naive) per via della sua **assunzione fondamentale di indipendenza condizionale tra le caratteristiche** (o [[Predittore (Statistica)|predittori]]) dato un certo valore della classe.== 
	* Nonostante questa semplificazione, spesso non vera nel mondo reale, il *Naive Bayes* si dimostra efficace in molte applicazioni pratiche e **richiede relativamente pochi dati per l'addestramento.**

> [!IMPORTANT] Formula di un classificatore bayesiano
> Il classificatore si fonda sulla seguente espressione del Teorema di Bayes: 
> $$P(Y|X) = \frac{P(X|Y) \cdot P(Y)}{P(X)}$$ 
> Dove:   
> - $P(Y|X)$ è la **probabilità a posteriori** della classe $Y$ dato il vettore di caratteristiche $X$.
> - $P(X|Y)$ è la **verosimiglianza**, ovvero la probabilità di osservare $X$ data la classe $Y$.
> - $P(Y)$ è la **probabilità a priori** della classe $Y$.
> - $P(X)$ è la probabilità marginale di $X$.> 
## Come funziona il *Naive Bayes*
Il classificatore *Naive Bayes* assegna a una nuova osservazione la classe ($y$) che massimizza la probabilità a posteriori, calcolata come: $\hat{y} = \text{argmax}_{y \in {1,\ldots,k}} P(Y=y) \prod_{i=1}^{n} P(X_i|Y=y)$ Non è necessario calcolare $P(X)$ perché è una costante per tutte le classi e non influenza la decisione di massima. Spesso si usa il logaritmo di questa espressione (log-verosimiglianza) per evitare problemi numerici con prodotti di piccole probabilità. L'algoritmo si articola in tre passaggi principali:
- Calcolare le probabilità a priori delle classi e le probabilità condizionate delle caratteristiche dai dati di training.
- Per ogni nuovo dato, calcolare la probabilità di ciascuna classe usando il Teorema di Bayes e l'assunzione di indipendenza ingenua.
- Assegnare la classe con la probabilità a posteriori maggiore.

> [!WARNING] Punti di forza e limitazione:
> - **Punti di forza**: è semplice (computazionalmente efficiente), richiede pochi dati di addestramento, gestisce bene le caratteristiche irrilevanti e funziona efficacemente in domini con molte caratteristiche. Se l'obiettivo è classificare i record in base alla loro probabilità (ranking), può dare buoni risultati anche con stime di probabilità biasate.
> - **Limitazioni**: la sua performance può degradare quando l'assunzione di indipendenza è fortemente violata. Le stime di probabilità prodotte dal classificatore *Naive Bayes* possono essere distorte (biased).
## L'Assunzione "Naive"
L'assunzione chiave è che, data la classe $Y$, tutte le caratteristiche $X_i$ sono indipendenti tra loro. Matematicamente, ciò significa che la verosimiglianza $P(X|Y)$ può essere scomposta nel prodotto delle probabilità condizionate di ciascuna caratteristica: $P(X|Y) = P(X_1, X_2, \ldots, X_n|Y) = \prod_{i=1}^{n} P(X_i|Y)$

Questa assunzione semplifica notevolmente il modello e riduce i requisiti computazionali, rendendolo una buona scelta in situazioni dove la dimensione del campione ($n$) non è grande a sufficienza rispetto al numero di predittori ($p$) per stimare efficacemente la distribuzione congiunta. Tale semplificazione introduce un certo [[Bias (Statistica)|bias]], ma riduce significativamente la varianza, portando spesso a buone performance pratiche.
## Varianti di *Naive Bayes*
- **[[Gaussian Naive Bayes]]**: per caratteristiche continue, assume che i valori seguano una distribuzione normale all'interno di ogni classe. 
- **[[Multinomial Naive Bayes]]**: per dati discreti che rappresentano conteggi (es. frequenza di parole nell'analisi del testo, o "bag-of-words").
- **[[Bernoulli Naive Bayes]]**: per caratteristiche binarie che indicano presenza o assenza (es. una parola è presente o meno in un documento).
### Relazione con Altri Classificatori
Il *Naive Bayes*, [[Linear Discriminant Analysis (LDA)]] e [[Quadratic Discriminant Analysis (QDA)]] sono tutti classificatori che utilizzano il Teorema di Bayes stimando la funzione di densità $f_k(x)$. In particolare, LDA può essere visto come un caso speciale di *Naive Bayes* quando le distribuzioni delle caratteristiche sono modellate come Gaussiane unidimensionali e la matrice di covarianza è ristretta a essere diagonale. Né QDA né *Naive Bayes* sono casi speciali l'uno dell'altro; il *Naive Bayes* può produrre un adattamento più flessibile per modelli puramente additivi, mentre QDA può gestire meglio le interazioni tra predittori.