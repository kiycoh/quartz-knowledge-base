---
last modified: 2025-09-08T01:08:00.000Z
related: null
tags:
  - machine-learning
  - statistical-inference
  - maximum-likelihood-estimator
---
# Definizione di stimatore di massima verosimiglianza
==Lo stimatore di massima verosimiglianza (in inglese **Maximum Likelihood Estimator (MLE)**) è un metodo per stimare i parametri di un modello probabilistico che si basa sull'idea di trovare i valori dei parametri che massimizzano la probabilità di osservare i dati ottenuti==. In altre parole, si cerca il parametro che rende i dati osservati "più probabili" rispetto a tutti gli altri valori possibili del parametro.

> [!EXAMPLE]- Esempio pratico sullo stimatore di massima verosimiglianza
> **Scenario:** si supponga di avere un'urna contenente biglie nere e bianche. Si sa che il rapporto tra biglie nere e bianche è 3:1, ma non si sa quale colore sia il più numeroso. Si estraggono 10 biglie dall'urna, una alla volta, rimettendo ogni volta la biglia estratta nell'urna. Si osserva che vengono estratte 7 biglie nere e 3 biglie bianche.
> 
> ---
> 
> **Obiettivo:** stimare la probabilità di estrarre una biglia nera, ovvero il parametro "$p$" della distribuzione binomiale.
> 
> ---
> 
> **Procedimento:** si definisce la funzione di verosimiglianza, che rappresenta la probabilità di osservare i dati ottenuti (7 nere e 3 bianche) in funzione del parametro p (probabilità di estrarre una biglia nera). In questo caso, la funzione di verosimiglianza è: $$L(p)=\binom{7}{10}p^7(1−p)^3,$$
> Dove $\binom{7}{10}$ è il coefficiente binomiale, che rappresenta il numero di modi per scegliere 7 biglie nere da 10 estrazioni. Per semplificare i calcoli, spesso si utilizza la log-verosimiglianza, che è il
> logaritmo naturale della funzione di verosimiglianza. La massimizzazione della log-verosimiglianza è equivalente alla massimizzazione della verosimiglianza stessa. In questo caso: $$logL(p)=\log(\binom{7}{10}​)+7\log(p)+3\log(1−p)$$
> 
> ---
> 
**Derivata e azzeramento:** si calcola la derivata della log-verosimiglianza rispetto a $p$ e la si pone uguale a zero per trovare il punto di massimo: $$\text{d}\frac{(\log L(p))}{\text{dp}} = \frac{7}{p}​−\frac{3}{1-p} =0$$
Risolvendo l'equazione, si ottiene: $$p=\binom{7}{10}​$$
## Proprietà dello stimatore di massima verosimiglianza
**Gli stimatori di massima verosimiglianza (MLE)** godono di proprietà che li rendono desiderabili nella [[Statistica inferenziale|statistica inferenziale]]:
* **Invarianza:** se $\hat{\theta}{MLE}$ è lo stimatore di massima verosimiglianza per $\theta$, allora $g(\hat{\theta}{MLE})$ è lo stimatore di massima verosimiglianza per $g(\theta)$, per qualsiasi funzione biunivoca $g(\cdot)$.
* **Sufficienza:** se esiste una statistica sufficiente per $\theta$, lo stimatore $\hat{\theta}_{MLE}$, se esiste, è una funzione di tale statistica. Una statistica sufficiente è una funzione del campione che contiene tutte le informazioni rilevanti per il parametro $\theta$.
* **Efficienza:** se esiste uno stimatore non distorto ed efficiente per $\theta$, questo coincide con lo stimatore di massima verosimiglianza. L'efficienza si riferisce alla proprietà di avere la varianza più bassa possibile tra tutti gli stimatori non distorti.
### Proprietà asintotiche dello stimatore di massima verosimiglianza
Per grandi campioni (ovvero, all'aumentare di $n$):
* Sono asintoticamente non distorti: $\lim_{n\to\infty} E[\hat{\theta}_{MLE}] = \theta$.
* Sono asintoticamente efficienti: raggiungono il limite inferiore di Cramer-Rao per la varianza.
* Sono consistenti: la probabilità che lo stimatore differisca dal vero valore del parametro di una quantità arbitrariamente piccola tende a 1 al crescere della dimensione campionaria. Questo deriva dalla loro asintotica non distorsione e dalla riduzione della varianza al crescere di $n$.
* Si distribuiscono asintoticamente come una Normale: $\hat{\theta}_{MLE} \stackrel{D}{\to} N(\theta, [I(\theta)]^{-1})$, dove $I(\theta)$ è la matrice di informazione di Fisher.
## Applicazioni dello stimatore di massima verosimiglianza
Il metodo della massima verosimiglianza è un approccio molto generale e potente per la stima dei parametri. Viene ampiamente utilizzato in vari modelli statistici, inclusi i Modelli Lineari Generalizzati (GLM) come la regressione logistica, dove i parametri sono stimati tramite la massimizzazione della log-verosimiglianza. Esempi specifici di applicazione includono la stima dei parametri per distribuzioni come la Binomiale e Poisson.