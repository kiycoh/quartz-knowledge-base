---
last modified: 24/10/2025 02:56
related:
  - '[[Misure di posizione statistica]]'
tags:
  - statistica-informatica
  - teoria-probabilità
  - funzione-di-ripartizione
---
# Definizione di funzione di ripartizione empirica
In statistica e teoria della probabilità, la **funzione di ripartizione empirica** (o **funzione di distribuzione cumulata**) è una [[Funzione di variabile reale]] che racchiude le informazioni su un fenomeno (insieme di dati, evento casuale) riguardanti la sua presenza o la sua distribuzione *prima* o *dopo* un certo punto.

> [!IMPORTANT] Formula della funzione di ripartizione
> 
> $$F_X(x)=P(X\leq x)$$
> dove:
> * $F_X(x)$ è la funzione di $X$
> * $X$ è la variabile reale, le probabilità che $X$ avrà
> * $P$ è un valore minimo o  uguale a $x$

> ![[Pasted image 20250629160227.png]]
> Grafico della funzione di ripartizione relativa alla distribuzione uniforme
## Proprietà della funzione di ripartizione
La **funzione di ripartizione** gode delle seguenti proprietà:
* È definita per qualunque valore di $X$.
* È non decrescente.
* È pari a $0$ quando $x$ è minore o uguale dell’estremo inferiore della prima classe.
* È pari a $1$ quando $x$ è maggiore o uguale dell’estremo superiore dell’ultima classe.