---
last modified: 2025-09-25T00:41:00.000Z
related: null
tags:
  - algoritmi-ordinamento
  - complessita-computazionale
  - efficienza-algoritmica
---


# Cos'è il selection sort?
Il Selection Sort è un [[Algoritmo di ordinamento|algoritmo di ordinamento]] che trova il minimo elemento dalla lista non ordinata e lo scambia con il primo elemento della stessa lista. Poi trova il minimo tra i restanti e lo scambia con il secondo, e così via.


![[Selection Sort_image_1.png|400]]

## Caratteristiche
- **Stabilità**
- **Complessità di Tempo:** O($N^2$) qualunque sia l'input perché l'algoritmo consiste in due cicli annidati: 
	- Il primo ciclo scorre attraverso l'intera lista e seleziona l'elemento minimo tra quelli non ordinati.
	- Il secondo ciclo scambia l'elemento con quello iniziale del sub-array.
- **In-place** in quanto non richiede spazio aggiuntivo significativo.