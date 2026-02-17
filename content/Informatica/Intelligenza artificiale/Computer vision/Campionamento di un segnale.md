---
last modified: 2025, 11, 12 14:11:10
related:
  - '[[Quantizzazione di un segnale]]'
parent note: '[[Immagine digitale]]'
tags:
  - campionamento-spaziale
  - campionamento-temporale
  - signal-processing
---
# Campionamento di un segnale
==Il **campionamento di un segnale** è una tecnica che consiste nel convertire un segnale continuo (nel tempo o nello spazio) del tipo $f(s,t)$ in un [[segnale discreto]] del tipo $f(x,y)$,== valutandone l'ampiezza a intervalli temporali o spaziali solitamente regolari. Formalmente, il campionamento partiziona il piano $xy$ in una griglia, con coordinate appartenenti a $\mathbb{Z}^2$. Riconosciamo:
- [[Campionamento spaziale]]
- [[Campionamento temporale]]

> [!QUESTION] Che tipo di campionamento utilizzare in base al formato?
> - **Immagini Fisse (Foto):** Usano principalmente il **campionamento spaziale**. Il segnale (la luce) viene campionato su una griglia (i pixel) per creare l'immagine statica.
> - **Audio:** Usa principalmente il **campionamento temporale**. Il segnale (l'onda sonora) viene campionato migliaia di volte al secondo per registrarne l'evoluzione nel tempo.
> - **Video:** Usano **entrambi** i tipi di campionamento.
>     1. **Campionamento Spaziale:** Ogni singolo *fotogramma* del video è un'immagine, creata campionando lo spazio (dividendolo in pixel).
>     2. **Campionamento Temporale:** La sequenza di questi fotogrammi viene catturata a intervalli di tempo regolari (ad esempio 24, 30 o 60 fotogrammi al secondo) per creare l'illusione del movimento.