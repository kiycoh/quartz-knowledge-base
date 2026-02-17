---
tags:
  - machine-learning
  - scienze-cognitive
  - intelligenza-artificiale
---


>[!Teorema] 
>Sia $\large A$ un numero reale positivo e sia $\large n$ un numero intero positivo, esiste un unico numero reale positivo $\large x$ tale che $\large x^n=A$.
>$\large x$ prende il nome di **radice $\large n$-esima di $A$** e si indica con 
>
>![[Radicali 2024-03-25 18.56.39.excalidraw|center]]

Vediamo degli esempi di radicali:

$\displaystyle 8^{\frac{1}{3}}=\sqrt[3]{8}=2\;\;\;\;\;\;\;16^{\frac{1}{2}}=\sqrt{16}=4\;\;\;\;\;\;\; 4^{\frac{1}{2}}=\sqrt{\frac{4}{25}}=\frac{2}{5}\;\;\;\;\;\;\;10.000^{\frac{1}{4}}=\sqrt[4]{10.000}=10\;\;\;\;\;\;\;2^{\frac{1}{2}}=\sqrt{2}=1,414..$ 

Nell'ultimo esempio otteniamo come risultato un [[Insiemi numerici#$ mathbb{I} = { ; allineamento ; decimale ; illimitato ; non ; periodico ; con ; segno ; }$ 29a726|numero irrazionale]], quindi illimitato, non periodico

>[!tip] Nota bene
> Non sottovalutare la possibilità di esprimere un radicale sotto forma di potenza poiché ci permette di sfruttare le [[Proprietà delle potenze|proprietà delle potenze]] per poter fare ragionamenti del tipo: $$\displaystyle \Large A^{\frac{m}{n}}=(A^{\frac{1}{n}})^m=(A^m)^{\frac{1}{n}}=\sqrt[n]{A^m}$$ 

Facciamo due esempi:

- $\displaystyle \Large 27^{\frac{2}{3}}=\sqrt[3]{27^2}=3^2=9$ 
- $\displaystyle \large \left(\frac{9}{4}\right)^{\frac{3}{2}}=\sqrt[2]{\left(\frac{9}{4}\right)^{3}}=\left(\frac{3}{2}\right)^3=\frac{27}{8}$ 


>[!Teorema]
>È possibile definire la **radice n-esima** anche se $\large A$ è negativo ed $\large n$ è dispari:
>difatti possiamo definire $$\large \sqrt[n]{-A}=-\sqrt[n]{A}$$ 
>>[!warning] Attenzione
>>Non esiste la **radice n-esima** di un numero negativo per un indice pari, infatti $$\large \sqrt[2]{-4}\;non\;esiste\;in\;\mathbb{R}$$
>>


## Operazioni e principali proprietà

> Il primo passo per poter operare su un radicale, consiste nello studiare le **condizioni di esistenza** al variare della $x\in\mathbb{R}$ 

$\displaystyle \large \sqrt{x-3}$  esiste solo se  $\large x-3\ge0$  ovvero se  $\large x\ge3$ 


>[!prop] $\large \sqrt[n]{A^n}=\begin{cases}A\;se\;n\;e'\;dispari\\|A|\;se\;n\;e'\;pari\end{cases}$ 
$$\large \sqrt{2^3}=2\;\;\;\;\;\;\sqrt[3]{-2^3}=-2\;\;\;\;\;\;\sqrt[]{2^2}=|2|\;\;\;\;\;\;\sqrt[]{-2^2}=|2|$$

>[!prop] Proprietà invariantiva
>$\Large se \;A\ge0\;allora\;\sqrt[n]{A^m}=\sqrt[n\cdot k]{A^{m\cdot k}}$
$$\large \sqrt[3]{7^2}=\sqrt[3 \cdot 2]{7^{2\cdot 2}}=\sqrt[6]{7^4}\;\;\;\;\;\;\sqrt[4]{3}=\sqrt[4\cdot3]{3^{1\cdot3}}=\sqrt[12]{27}\;\;\;\;\;\;$$ 
$\Large se \;A\ge0\;allora\;\sqrt[n\cdot k]{A^{m\cdot k}}=\sqrt[n]{A^m}$
$$\large \sqrt[4]{9}=\sqrt[4]{3^2}=\sqrt[]{3}\;\;\;\;\;\;\sqrt[8]{16}=\sqrt[8]{4^2}=\sqrt[]{2}\;\;\;\;\;\;$$ 


>**Attenzione**
>
>Applicare la proprietà invariantiva ad un radicando letterale potrebbe farci incappare in problemi relativi al campo di esistenza, vediamo alcuni esempi
>
>
>$\large \sqrt[6]{a^8}=\sqrt[3]{a^4}$ in questo caso l'uguaglianza è corretta infatti il primo radicale esiste $\large \forall a \in \mathbb{R}$, proprio come il secondo e sono sempre $\large \ge0$ poiché elevati ad una potenza pari
>
>$\large \sqrt[15]{a^5}=\sqrt[3]{a}$ in questo caso i due radicali esistono $\large\forall a \in \mathbb{R}$ e mantengono il segno di $\large a$
>
>$\large \sqrt[8]{a^4}\neq\sqrt[]{a}$ in questo caso il primo radicale esiste $\large \forall a \in \mathbb{R}$ in quanto il radicale anche per valori negativi di $\large a$ sarà maggiore di 0, il secondo invece non esiste per valori negativi di $\large a$ quindi bisogna utilizzare il valore assoluto $$\large \sqrt[8]{a^4}=\sqrt[]{|a|}$$
>$\large \sqrt[6]{a^2}\neq\sqrt[3]{a}$ in questo caso, sia il primo radicale che il secondo, esistono $\large \forall a \in \mathbb{R}$, il primo però è sempre maggiore di 0, mentre il secondo solo per valori positivi di $\large a$, quindi possiamo correggere la scrittura così $$\large \sqrt[6]{a^2}=\sqrt[3]{|a|}$$


>[!prop] Prodotto di radicali con lo stesso indice
>$$\;\;\Large se\;A\ge0,\;e\;B\ge0\;\;allora\;\;\sqrt[n]{A}\cdot\sqrt[n]{A}=\sqrt[n]{A\cdot B}$$ 

>[!prop] Quoziente di due radicali con lo stesso indice
>$$\;\;\Large se\;A\ge0,\;e\;B\gt0\;\;allora\;\;\sqrt[n]{A}:\sqrt[n]{A}=\sqrt[n]{A: B}$$ 
>

>[!prop] Riduzione di due radicali allo stesso indice
>$$\large \sqrt[n]{a}, \sqrt[m]{b}\;\;\to\;\;\sqrt[c]{a^{\frac{c}{n}}},\sqrt[c]{a^{\frac{c}{m}}}\;\;\;con\;c\;=\;mcm(n,m)$$

>[!prop] Moltiplicazione e divisione di radicali con indici diversi
>$$\large\displaystyle \sqrt[n]{a}\cdot\sqrt[m]{b}\;\;\to\;\;\sqrt[c]{a^{\frac{c}{n}}}\cdot\sqrt[c]{b^{\frac{c}{m}}}\;\;\to\;\;\sqrt[c]{a^{\frac{c}{n}}\cdot b^{\frac{c}{m}}}\;\;\;con\;c\;=\;mcm(n,m)$$

>[!prop] Radice di radice
>$$\Large \sqrt[m]{\sqrt[n]{a}}=\sqrt[m\cdot n]{a}\;\;con\;a\ge0$$

>[!prop] Trasportare un fattore sotto il segno di radice
>$$\large a\sqrt[n]{b}=\sqrt[n]{a^n\cdot b}\;\;\;oppure\;\;\;-a\sqrt[n]{b}=-\sqrt[n]{a^n\cdot b}$$ 

>[!prop] Trasportare un fattore fuori dal segno di radice
>$$\large \sqrt[n]{a^n\cdot b}=a\sqrt[n]{b}$$




