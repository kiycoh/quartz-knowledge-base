---
tags: [event-definition, indicator-function, teoria-probabilità]
last modified: 2025, 11, 24 22:11:40
---

# Evento (teoria della probabilità)
Nella [[Teoria della probabilità]], un **evento** è un'unità logica che può assumere valore "Vero" o "Falso".
Gli eventi si indicano sempre con le lettere maiuscole.

In astratto è l'insieme dei casi possibili di un esperimento aleatorio ( incerto) può essere rappresentato in uno spazio $\Omega$ e ogni caso elementare sarà rappresentato come un punto in questo spazio.

Fissato un sottoinsieme $E$ di $\Omega$ che rappresenta un evento, il risultato (V o F) e quindi il caso elementare che si verifica, corrisponde a un punto che appartiene a $E$. Distinguiamo due eventi particolari:

## Tipologie
* [[Evento certo]]: rappresentato dall'insieme $\Omega$, risulta **sempre vero** ($|\Omega| = 1$)
* [[Evento impossibile]]: rappresentato dall'insieme vuoto $\emptyset$, risulta sempre falso ($|\emptyset| = 0$)
* [[Evento complementare]]: 

# Indicatore
Dato un evento $E$ si definisce l'indicatore come:
$$
|E|=
\begin{cases}
1 \text{ se E è vero}\\
0 \text{ se E è falso}
\end{cases} 
$$
 
## Proprietà
* $|A \wedge B| = |A| \cdot |B| = \text{min}\{|A|, |B|\}$
* $|A \vee B| = |A| + |B| = \text{max}\{|A|, |B|\}$
* $|A| \leq |A \vee B| \Leftrightarrow |B| \leq |A \vee B$
