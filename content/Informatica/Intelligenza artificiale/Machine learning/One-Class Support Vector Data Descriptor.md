---
last modified: 2025, 11, 24 2:11:53
related: null
parent note: null
tags:
  - one-class-svm
  - svdd
  - anomaly-detection
---
# Definizione di One-Class Support Vector Data Descriptor
Il **One-Class Support Vector Data Descriptor (SVDD)** è una tecnica molto simile alla **One-Class SVM**, ma con un'intuizione leggermente diversa e molto utile soprattutto per problemi di **rilevamento anomalie**.

In altre parole, il **SVDD** cerca di **racchiudere i dati normali all'interno di una sfera (o di una forma simile a una sfera)** nello spazio delle caratteristiche.  
Poi, se un nuovo dato **cade fuori da questa sfera**, viene considerato **anomalo**.

![[Pasted image 20250331102123.png]]


> [!EXAMPLE] Esempio
> Immaginiamo di avere punti dati distribuiti in modo circolare su un piano (es: dati di temperatura + pressione di una macchina in buone condizioni). Il **SVDD** proverà a **racchiudere questi punti in un cerchio** (in 2D) o una sfera (in 3D+). Un nuovo dato che si trova molto lontano da questa "nuvola" verrà considerato anomalo.


Supponiamo che:
- I tuoi dati siano $x_1, x_2, \ldots, x_n \in \mathbb{R}^d$
- Vuoi trovare una sfera di centro $a$ e raggio $R$

Allora il problema è:

$$
\min_{R, a} \quad R^2 + C \sum_{i=1}^n \xi_i
$$

Soggetto a:

$$
\|x_i - a\|^2 \leq R^2 + \xi_i,\quad \xi_i \geq 0
$$

Dove:
- $\xi_i$ sono delle variabili di slack (cioè permettono a qualche punto di stare fuori dalla sfera).
- $C$ è un parametro che controlla quanto sei disposto a **tollerare errori** (punti fuori dalla sfera).