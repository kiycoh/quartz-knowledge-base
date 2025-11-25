---
tags:
  - machine-learning
  - scienze-cognitive
  - intelligenza-artificiale
---

 **Determinare male l'insieme di definizione comporta l'annullamento dell'intero esercizio!**

Il dominio di una funzione $f(x)$ è l'insieme dei valori possibili che la variabile indipendente $x$ può assumere, in modo che la funzione sia definita in tali valori. Il dominio è il più ampio sott'insieme di R per cui ha senso l'espressione.

Il calcolo del dominio è il primo passo dello studio di una funzione nell'individuazione del dominio $x$ (**campo di esistenza**) in cui la funzione è definita.

Nel caso della funzione $f(x)= \frac {x}{x-1}$ l'intervallo di definizione sarà: 
$$D: \forall x \in \mathbb{R}, (- \infty,1) \cup (1, -\infty)$$

Questo ci permette di trovare anche i **punti per cui la funzione non è definita**. Ad esempio, la funzione $f(x)= \frac {x}{x-1}$ non è definita in $x=1$.
$$f(1)= \frac {1}{1-1} = \frac10: Indefinita$$
## Altri esempi
- Nel caso della funzione $f(x)= x^2- 3x^2+1$ l'intervallo di definizione sarà:
$$D:]-\infty,+\infty[$$
- Nel caso della funzione $f(x)= \frac {x^2} {2} + \sqrt 5x +\log3$ l'intervallo di definizione sarà: $$D:]-\infty,+\infty[$$
### Come trovare il dominio di una funzione
Se nell'equazione della funzione non compaiono le seguenti condizioni allora il dominio della funzione è sicuramente tutto $\mathbb{R}$ :
- la variabile dipendente $x$ a denominatore -> $f(x)=\frac{[...]}{x}$
- la variabile $x$ all'interno di radici con indice pari -> $f(x)=[...]+\sqrt[4]x+[...]$
- logaritmi contenenti la $x$ come base o argomento -> $f(x)=[...]+\log_xx+[...]$
- funzioni $\arccos$ o $\arcsin$ con argomento la $x$ -> $f(x)=\arccos x-\arcsin x$ 
- funzioni esponenziale a base variabile -> $f(x)=[...]+a^x+[...]$ 


### $x$ a denominatore

Consideriamo la funzione $f(x)=\frac{x}{x-3}$ 
- Dobbiamo porre il denominatore diverso da 0   ->  $x-3\neq 0$ 
- $x-3\neq0 \to x\neq3$ 
- Il dominio è sicuramente l'intervallo $\to\;\;]-\infty,3[\;\cup\;]3,+\infty[$ 

Consideriamo la funzione $f(x)=\frac{x+1}{x^2-3x+2}$ 
- Poniamo il denominatore diverso da 0   $\to\;\;x^2-3x+2\neq0$
- $x^2-3x+2\neq0 \;\;\to\;\;(x-1)(x-2)\neq0\;\;\to\;\;x\neq1,\;x\neq2$ 
- Il dominio è sicuramente l'intervallo $]-\infty,1[\;\cup\;]1,2[\;\cup\;]2,+\infty[$ 

Consideriamo la funzione $f(x)=\frac{3}{|x|-5}$
- Poniamo il denominatore diverso da 0   $\to \;\;|x|-5\neq0$
- $|x|-5\neq0 \;\;\to\;\;x\neq5,\;x\neq-5$ 
- Il dominio è sicuramente l'intervallo $]-\infty,-5[\;\cup\;]-5,5[\;\cup\;]5,+\infty[$ 

Consideriamo la funzione $f(x)=e^{\frac{1}{x-2}}+\frac{3x}{x+1}$ 
- Poniamo il denominatore dell'esponente di $e$ diverso da 0   $\to \;\; x-2\neq0$ 
- $x-2\neq0\;\;\to\;\;x\neq2$ 
- Ora poniamo il denominatore della funzione diverso da 0  $\to\;\;x+1\neq0$
- $x+1\neq0 \;\;\to\;\;x\neq-1$ 
- Il dominio è sicuramente l'intervallo $]-\infty,-1[\;\cup\;]-1,2[\;\cup\;]2,+\infty[$ 


### radici di $x$ con indice pari

Consideriamo la funzione $f(x)=\sqrt{1-x}$ 
- Poniamo il radicando strettamente maggiore di 0   $\to\;\; 1-x\ge 0$ 
- $1-x\ge0\;\;\to\;\;x\le-1$ 
- Il dominio è sicuramente l'intervallo $]-\infty,1[$ 

Consideriamo la funzione $f(x)=\sqrt[4]{9-x^2}$ 
- Poniamo il radicando strettamente maggiore di 0  $\to\;\;9-x^2\ge0$ 
- $9-x^2\ge0\;\;\to\;\;-3\le x \le 3$  
- Il domino è sicuramente l'intervallo $]-3,3[$ 

Consideriamo la funzione $f(x)=\sqrt{|x-3|+5}$ 
- Poniamo il radicando strettamente maggiore di 0   $\to\;\;|x-3|+5$