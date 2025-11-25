---
last modified: 2025, 11, 10 15:11:43
related: null
parent note: '[[Diagramma UML]]'
tags:
  - machine-learning
  - uml
  - software-design
---
# Diagramma UML comportamentale
- **[[Use Case Diagram]]**: descrive le funzionalità (casi d'uso) offerte dal sistema dal punto di vista degli attori (utenti o sistemi esterni). È ottimo per raccogliere i requisiti.
- **[[Sequence Diagram]]**: *molto comune*, mostra le interazioni tra oggetti in una sequenza temporale, evidenziando l'ordine dei messaggi scambiati. È ideale per modellare la logica di un singolo caso d'uso.
- **[[Communication Diagram]]**: simile al diagramma di sequenza, si concentra più sulle relazioni strutturali tra gli oggetti che sull'ordine temporale dei messaggi. (Era noto come "Diagramma di Collaborazione" in UML 1.x).
- **[[Activity Diagram]]**: modella il flusso di controllo o il flusso di dati da un'attività all'altra. È simile a un diagramma di flusso (flowchart) e può essere usato per modellare processi business o algoritmi complessi.
- **[[State Machine Diagram]]**: mostra come un singolo oggetto risponde agli eventi durante la sua vita, descrivendo la sequenza di stati in cui si trova e le transizioni che causano il cambiamento di stato.
- **[[Timing Diagram]]**: un tipo specializzato di diagramma di sequenza che si concentra specificamente sui vincoli temporali, mostrando come lo stato di un oggetto cambia in un preciso arco di tempo.
- **[[Interaction Overview Diagram]]**: fornisce una panoramica ad alto livello di un flusso di controllo, combinando elementi dei diagrammi di attività e di sequenza. Mostra come diverse interazioni (sequence diagram) sono collegate tra loro.