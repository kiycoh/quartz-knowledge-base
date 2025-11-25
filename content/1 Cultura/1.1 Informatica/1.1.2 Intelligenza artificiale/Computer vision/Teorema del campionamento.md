---
last modified: 2025, 11, 11 19:11:01
tags:
  - campionamento-statistico
  - teoria-probabilità
  - statistica-inferenziale
---
# Teorema del campionamento
Il [[Teorema del campionamento]] (noto anche come **teorema di Nyquist-Shannon**) ==afferma che per ricostruire perfettamente un segnale analogico a banda limitata, è necessario campionarlo a una frequenza (frequenza di campionamento) che sia almeno il doppio della frequenza più alta presente nel segnale==. Introduce vincoli sulla quantità di informazione che può essere fedelmente catturata durante il [[Campionamento di un segnale]].

> Una funzione continua e limitata in banda (la cui trasformata di Fourier è zero oltre un intervallo finito di frequenze) può essere recuperata completamente dai suoi campioni se la frequenza di campionamento **supera il doppio della sua frequenza massima** (frequenza di Nyquist).

- **Campionamento 2D:** per le immagini (funzioni 2D), il campionamento deve soddisfare questa condizione in entrambe le direzioni ($m$ e $n$).
- **Aliasing spaziale:** se si utilizza un tasso di campionamento troppo grossolano (sotto-campionamento), si verifica l'[[aliasing]], in cui segnali continui diversi diventano indistinguibili. Nelle immagini, questo si manifesta come artefatti, tra cui bordi frastagliati, falsi riflessi e l'apparizione di pattern di frequenza non presenti nell'originale, come il **Moiré pattern**.


