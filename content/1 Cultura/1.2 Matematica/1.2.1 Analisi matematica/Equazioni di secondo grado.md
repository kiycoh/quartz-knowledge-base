---
tags:
  - algebra-relazionale
  - equazioni-di-secondo-grado
  - risoluzione-equazioni
---


>[!definizione ]
> Un'**equazione di secondo grado** o **quadratica** ad un'incognita $x$ è un'equazione algebrica in cui il grado massimo con cui compare l'incognita è 2, ed è sempre riconducibile alla forma $$\displaystyle \Large ax^2+bx+c=0\;\;con \;a\neq0$$

## Processo risolutivo generale

1. Operazioni algebriche di base, quali moltiplicazioni, potenze, ecc.
2. Ricondurre l'equazione ad una forma del tipo $ax^2+bx+x=0$
3. Identificare le soluzioni tramite la formula $$\Delta = b^2-4ac \;\;\;\;\;\;\;\;\;\;\;x_{1,2}=\frac{-b\pm\sqrt{\Delta}}{2a}$$
>[!warning] Attenzione al $\Delta$ 
> - Se $\Delta > 0$ l'equazione ammette due soluzioni reali       $\to\;\;x_1,x_2\in\mathbb{R}:x_1\neq x_2$
> - Se $\Delta = 0$ l'equazione ammette una sola soluzione reale ($ma=2$)   $\to\;\;x_1\in\mathbb{R}$
> - Se $\Delta < 0$ l'equazione non ammette alcuna soluzione reale


## Equazioni di secondo grado monomie

>[!definizione] 
> Diciamo equazione di secondo grado monomia un'equazione di secondo grado in forma normale in cui appare solo il termine di secondo grado $$\Large ax^2=0 \;\;con \; a\neq0$$ 

Il metodo di risoluzione è immediato infatti queste equazioni ammettono due soluzioni reali e coincidenti, entrambe nulle


## Equazioni di secondo grado pure

>[!definizione]
>Diciamo equazione di secondo grado pura un'equazione di secondo grado in forma normale in cui il coefficiente del termine di primo grado è nullo e il termine noto è diverso da zero $$\Large ax^2+c=0\;\;con\;a\neq0,\;c\neq0$$ 

  Il metodo di risoluzione è molto semplice, infatti per calcolare le due soluzioni possiamo procedere con il seguente calcolo $$\displaystyle \Large x^2=\frac{-c}{a}$$
  >[!warning] Attenzione
  >- Se $a$ e $c$ sono concordi, allora $-\frac{c}{a}$ è negativo e l'equazione non ammette soluzioni reali
  >- Se $a$ e $c$ sono discorsi, allora $-\frac{c}{a}$ è positivo e l'equazione ammette due soluzioni reali distinte, date da $$\displaystyle \large x_{1,2}=\pm \sqrt{\frac{-c}{a}}$$
  

## Equazioni di secondo grado spurie

>[!definizione]
>Diciamo equazione di secondo grado spuria un'equazione di secondo grado in forma normale in cui il coefficiente del termine noto è nullo e il coefficiente del termine di primo grado è diverso da zero $$\Large ax^2+bx=0\;\;con\;a\neq0,\;b\neq0$$
>

Il metodo di risoluzione è immediato infatti basta effettuare un raccoglimento a fattor comune $$\Large ax^2+bx=0\;\;\to\;x(ax+b)=0$$
e per la legge di annullamento del prodotto possiamo porre separatamente i due fattori a zero $$\Large x=0,\;\;ax+b=0$$
trovando così le due soluzioni distinte $$\Large x_1=0,\;\;x_2=\frac{-b}{a}$$
## Metodo alternativo

Un ulteriore metodo di risoluzione prevede la scomposizione dell'equazione seguendo le tecniche di scomposizione utilizzando anche i [[Prodotti notevoli di polinomi|prodotti notevoli]] 

