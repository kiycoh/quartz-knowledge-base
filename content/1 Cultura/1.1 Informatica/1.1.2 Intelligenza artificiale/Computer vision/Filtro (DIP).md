---
last modified: 2025, 11, 11 21:11:55
related: null
tags:
  - digital-image-processing
  - spatial-filtering
  - frequency-domain-filtering
---
# Filtro digitale
Nell'[[Digital Image processing (DIP)|elaborazione delle immagini]], un filtro elabora nel dominio della frequenza e si il tuo compito è **passare, modificare o rigettare componenti di frequenza specifiche** di un'[[immagine digitale]]. Può essere matematicamente concettualizzato come una funzione del tipo
![[Pasted image 20251009172222.png]]
## Tipi di filtro
I filtri si suddividono in base al dominio in cui operano:
## Filtri spaziali
Il dominio spaziale (**spatial filtering** si riferisce al piano dell'immagine stessa, dove i metodi di elaborazione sono basati sulla manipolazione diretta dei pixel.
1. **Meccanica:** il filtraggio spaziale modifica un'immagine **sostituendo il valore di ciascun pixel con una funzione dei valori di quel pixel e dei suoi vicini**. L'operazione viene eseguita su un'area ristretta (spesso rettangolare) chiamata **vicinato** o *neighborhood*.
2. **Nucleo del Filtro (Filter Kernel):** In questo dominio, il filtro è rappresentato da una matrice chiamata **nucleo del filtro** (*filter kernel*), o anche **maschera** (*mask*), *template* o **finestra**.
3. **Filtri Lineari:** Se l'operazione sui pixel è lineare, il filtro è detto **filtro spaziale lineare**. Un filtro spaziale lineare esegue un'operazione di **somma dei prodotti** (*sum-of-products*) tra l'immagine e il nucleo del filtro. Questa operazione è sinonimo di **convoluzione spaziale** (*spatial convolution*).
4. **Filtri Non Lineari:** Altrimenti, il filtro è non lineare. Un esempio importante è il **[[Filtro mediano]]** (un **filtro statistico d'ordine**), la cui risposta si basa sull'ordinamento dei pixel nel vicinato; esso sostituisce il valore del pixel centrale con la mediana dei valori di intensità vicini. I filtri mediani sono particolarmente efficaci nel ridurre il rumore impulsivo (sale e pepe).

B. Filtri nel Dominio della Frequenza (Frequency Domain Filtering)
Il filtraggio nel dominio della frequenza è una tecnica di elaborazione che richiede di eseguire una **trasformata** (come la Trasformata di Fourier Discreta, DFT) sull'immagine, eseguire l'elaborazione su tale dominio e, infine, calcolare la trasformata inversa per tornare al dominio spaziale.
1. **Funzione di Trasferimento del Filtro ($H(u, v)$):** Nel dominio della frequenza, il filtro è chiamato **funzione di trasferimento del filtro**.
2. **Operazione Fondamentale:** Il filtraggio in questo dominio si basa sulla **moltiplicazione elemento per elemento** della funzione di trasferimento del filtro $H(u, v)$ con la Trasformata di Fourier $F(u, v)$ dell'immagine in ingresso, seguita dalla trasformata inversa per ottenere l'immagine filtrata $g(x, y)$.
3. **Equivalenza Spazio-Frequenza:** Il **teorema di convoluzione** stabilisce un'equivalenza tra il filtraggio nel dominio spaziale (convoluzione) e il filtraggio nel dominio della frequenza (moltiplicazione). Il nucleo spaziale $h(x, y)$ e la funzione di trasferimento nel dominio della frequenza $H(u, v)$ formano una coppia di trasformate di Fourier.
]]