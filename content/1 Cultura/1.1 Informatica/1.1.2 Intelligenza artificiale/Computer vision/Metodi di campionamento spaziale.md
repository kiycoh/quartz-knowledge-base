---
last modified: 2025, 11, 11 19:11:09
related: null
parent note: null
tags:
  - machine-learning
  - spatial-sampling
  - image-processing
---
# Metodi di campionamento spaziale
Il modo in cui viene eseguito il campionamento spaziale è **determinato dalla disposizione fisica del sensore**:

1. **Elemento sensore singolo:** ottenuto selezionando il numero di incrementi meccanici individuali a cui il sensore raccoglie i dati, spesso combinato con il movimento meccanico.
2. **Striscia di sensori In-line (1D):** usata in scanner piani e imaging aereo. Il numero di sensori nella striscia stabilisce i campioni in una direzione, mentre il movimento meccanico stabilisce il numero di campioni nell'altra.
3. **Array di Sensori 2D (Array CCD):** l'assetto predominante nelle fotocamere digitali. Non è richiesto alcun movimento, e il numero di sensori nell'array definisce i limiti del campionamento in entrambe le direzioni spaziali.

La **risoluzione spaziale** è la misura del più piccolo dettaglio discernibile in un'immagine, spesso espressa quantitativamente in coppie di linee per unità di distanza o in punti (pixel) per unità di distanza (es. dpi).