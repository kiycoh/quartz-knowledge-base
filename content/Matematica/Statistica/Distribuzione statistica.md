---
last modified: 2025-03-06T09:35:00.000Z
related: null
tags:
  - statistica-informatica
  - statistica-descrittiva
  - distribuzione-statistica
---
# Definizione di distribuzione statistica
==Una **distribuzione statistica** è una rappresentazione del modo in cui diverse [[Modalità (Statistica)|modalità]] di un [[Variabile statistica|carattere]] si distribuiscono nelle [[Popolazione statistica#Definizione di unità statistica|unità statistiche]].== In altre parole è la "tabella", "grafico" o "lista".
Distinguiamo:
* *[[Distribuzione unitaria semplice (Statistica)|Distribuzione unitaria semplice]]*: se si rileva un solo carattere.
* *[[Distribuzione unitaria multipla (Statistica)|Distribuzione unitaria multipla]]*: se si rilevano più caratteri sullo stesso collettivo.

## [[Distribuzioni di frequenza]]

## [[Misure di posizione statistica]]
### Distribuzione di frequenze relative


![[Tabella a doppia entrata.svg]]

## Distribuzione di quantità

## [[Distribuzione statistica congiunta]]
La **distribuzione congiunta** descrive come due (o più) variabili casuali si comportano insieme, cioè definisce la probabilità che ciascuna possibile coppia (o insieme) di valori si verifichi contemporaneamente.

### Distribuzione Congiunta per Variabili Discrete

- **Definizione:**  
  Se abbiamo due variabili discrete $X$ e $Y$, la distribuzione congiunta è data dalla funzione di probabilità $p_{X,Y}(x, y)$ che associa a ciascuna coppia $(x, y)$ la probabilità che $X=x$ e $Y=y$ accadano insieme:
  $$
  p_{X,Y}(x, y) = P(X = x \text{ e } Y = y)
  $$
- **Proprietà:**  
  La somma di tutte le probabilità per tutte le possibili coppie deve essere uguale a 1:
  $$
  \sum_{x}\sum_{y} p_{X,Y}(x, y) = 1
  $$
- **Esempio:**  
  Immagina di lanciare due dadi. Se $X$ è il risultato del primo dado e $Y$ quello del secondo, la distribuzione congiunta mostra la probabilità di ottenere, ad esempio, $X=3$ e $Y=5$ simultaneamente.

### Distribuzione Congiunta per Variabili Continue

- **Definizione:**  
  Per variabili continue $X$ e $Y$, la distribuzione congiunta è descritta da una funzione di densità $f_{X,Y}(x, y)$ tale che la probabilità che $(X, Y)$ cada in una regione $A$ del piano è data dall'integrale doppio:
  $$
  P((X,Y) \in A) = \int\!\!\int_A f_{X,Y}(x, y)\,dx\,dy
  $$
- **Proprietà:**  
  Anche in questo caso, l'integrale su tutto lo spazio deve essere uguale a 1:
  $$
  \int_{-\infty}^{\infty} \int_{-\infty}^{\infty} f_{X,Y}(x, y)\,dx\,dy = 1
  $$

### Utilità della Distribuzione Congiunta

- **Marginali:**  
  Dalla distribuzione congiunta, si possono ricavare le distribuzioni marginali (cioè le distribuzioni di $X$ e $Y$ prese singolarmente) sommando (o integrando) rispetto all'altra variabile.
- **Condizionate:**  
  Si possono inoltre calcolare le distribuzioni condizionate, che indicano la probabilità che una variabile assuma un certo valore dato un valore fisso dell'altra variabile.
- **Applicazioni Pratiche:**  
  Ad esempio, in uno studio statistico potresti voler analizzare la relazione tra il numero di ore di studio ($X$) e il voto ottenuto in un esame ($Y$); la distribuzione congiunta ti aiuterebbe a capire come queste due variabili sono correlate.

## Distribuzione di frequenza relativa condizionata
## Distribuzione condizionata
## Distribuzione marginali
La **distribuzione di frequenza marginale** rappresenta le frequenze (assolute o relative) di una singola variabile, ottenute **sommando le frequenze** della distribuzione doppia (congiunta) rispetto all’altra variabile.

### Distribuzione marginale assoluta
Supponiamo di avere due variabili categoriche $X$ e $Y$, e una tabella di contingenza che rappresenta le **frequenze congiunte** $f_{ij}$ (cioè il numero di osservazioni per cui $X = x_i$ e $Y = y_j$).

Allora la **frequenza marginale assoluta** di $X = x_i$ è:

$$
f_{i\cdot} = \sum_j f_{ij}
$$

E analogamente, la **frequenza marginale assoluta** di $Y = y_j$ è:

$$
f_{\cdot j} = \sum_i f_{ij}
$$

---

### Formula (frequenze relative marginali)

Se $n$ è il totale delle osservazioni, la **frequenza relativa congiunta** è:

$$
p_{ij} = \frac{f_{ij}}{n}
$$

Le **frequenze relative marginali** si ottengono sommando su righe o colonne:

- Per la variabile $X$:

$$
p_{i\cdot} = \sum_j p_{ij}
$$

- Per la variabile $Y$:

$$
p_{\cdot j} = \sum_i p_{ij}
$$
