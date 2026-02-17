---
last modified: 2025, 11, 24 22:11:38
related:
  - '[[Immagine analogica]]'
parent note: '[[Computer Vision (CV)]]'
tags: [computer-vision, digital-image-processing, immagine-raster]
---
# Immagine digitale
In [[Digital Image processing (DIP)]], un'**immagine digitale** è definita come una funzione bidimensionale $f(x,y)$, dove $x$ e $y$ sono *coordinate spaziali (cartesiane)* che definiscono la posizione del pixel sul piano. L'ampiezza di $f$ per ogni paio di coordinate $(x,y)$ è il range del c.d. *punto grigio*. Un'immagine digitale è formata per:
1. [[Campionamento spaziale]]: discretizza *valori di coordinate* continui $f(s,t)$ in una funzione bidimensionale $f(x,y)$.
2. [[Quantizzazione di un segnale]]: discretizza i *valori di ampiezza* (livelli di intensità o grigio) di un'immagine continua (analogica).

> ![[Pasted image 20251111213151.png]]
> Un'immagine immagine digitale: un generico piano cartesiano segmentato in quadrati al cui interno sono rappresentati con livelli di intensità i pixel.

> [!NOTE] Tipi di immagine digitale
> - **[[Immagine raster]]** (o **Bitmap**): una griglia di pixel (abbreviazione per Picture Elements), in altre parole un mosaico di quadretti con colori specifici
> - **[[Immagine vettoriale]]**: una serie di istruzioni matematiche. Il file memorizza formule che descrivono forme geometriche basilari (punti, linee, curve, …)
