---
tags:
  - machine-learning
  - scienze-cognitive
  - limiti-funzioni
---


>[!definizione]
>Per ogni $\delta > 0$ deve esistere un intorno del punto $c$  tale che, scelto un qualunque numero reale appartenente all'intorno bucato di $c$, $|f(x)-l|<\delta$
>$$\forall \;\delta > 0 \; \exists \; I (c) : \forall x \in I(c), x\neq c \rightarrow l-\delta < f(x) < l+\delta$$

Calcolare il $\displaystyle \lim_{x\to c}$ non vuol dire andare a calcolare la funzione nel punto $c$, nel quale potrebbe anche non esistere, vuol dire calcolare la funzione in un intorno del punto $c$ dove assumerà valori molto ma molto vicini ad $l$

![[Limiti di funzioni 2024-03-13 22.50.53.excalidraw|80%]]
>[!teorema] Attenzione
>Come si può notare, preso un qualunque $\epsilon > 0$, esiste un intorno del punto $c$, tale che preso un qualunque valore di $x \in I(c)$ distinto da $c$, l'immagine del punto $x$ della funzione rientra tra $l+\epsilon$ e $l-\epsilon$ 

[[0 Cultura/0.3 Matematica/0.3.1 Analisi matematica/Esempio verifica limite di funzione]]

# Limite infinito in un punto

>[!definizione]
>Per ogni $M > 0$, deve esistere sempre un intorno bucato del punto $c$, tale che scegliendo un qualsiasi $x$ reale dell'intorno bucato del punto $c$, la funzione valutata in $|x|$ deve essere maggiore di $M$ 
$$\forall\; M>0\;\; \exists \;I(c):\forall x \in I(c)\;\rightarrow|f(x)|>M$$


![[Limiti di funzioni 2024-03-13 22.50.53.excalidraw 1|80%]]


>[!teorema] Attenzione
>Come si può notare, preso un qualunque $M > 0$, esiste un intorno del punto $c$, tale che preso un qualunque valore di $x \in I(c)$ distinto da $c$, l'immagine del punto $x$ della funzione risulta maggiore di $M$ 

[[0 Cultura/0.3 Matematica/0.3.1 Analisi matematica/Esempio verifica limite di funzione infinita]]

## Teorema di unicità del limite
Il [[0 Cultura/0.3 Matematica/0.3.1 Analisi matematica/Teorema di unicità del limite]] è un principio fondamentale nell'ambito dell'analisi matematica, che svolge un ruolo cruciale nella definizione di limiti e nella comprensione del comportamento delle funzioni. Questo teorema stabilisce che se una funzione si avvicina a un determinato valore mentre la sua variabile indipendente si avvicina a un punto specifico, allora tale valore è unico; in altre parole, una funzione non può avere più di un limite in un punto dato.
