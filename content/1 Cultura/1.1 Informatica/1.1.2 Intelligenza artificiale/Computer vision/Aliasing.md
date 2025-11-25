---
last modified: 2025, 11, 11 21:11:45
related: null
parent note: null
tags:
  - campionamento-statistico
  - teorema-del-campionamento
  - anti-aliasing
---
# Aliasing
L'**aliasing** è un errore di campionamento. Si verifica quando un segnale viene [[Campionamento di un segnale|campionato]] (misurato) a una frequenza troppo bassa, violando il Teorema del Campionamento. Di conseguenza, le componenti ad alta frequenza del segnale originale vengono erroneamente interpretate come componenti a bassa frequenza, creando distorsione.
![[Pasted image 20251111194808.png]]

Per evitare l'aliasing, è necessario applicare un processo chiamato **[[Anti-aliasing]]**, che consiste nello smussare (filtrare passa-basso) la funzione di ingresso per attenuare le sue frequenze più alte, e ciò deve essere fatto *prima* del campionamento.