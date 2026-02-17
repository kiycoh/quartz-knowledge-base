---
last modified: 2025, 11, 24 1:11:20
related:
  - '[[Digital Image processing (DIP)]]'
parent note: '[[Intelligenza artificiale]]'
tags:
  - computer-vision
  - intelligenza-artificiale
  - image-processing
---
# Computer Vision 
In ambito [[Intelligenza artificiale]], la **computer vision** (**CV**, **visione artificiale** in italiano) si riferisce all'estrazione dimensionale di informazioni da un'[[immagine digitale]]. Più in generale è l'insieme dei processi atti a simulare la realtà (3D) da immagini (2D), al fine di ==simulare la vista umana (ad esempio la capacità di interpretare il contenuto di una determinata area della foto) ed eventualmente implicare una decisione automatica.==
- La [[Digital Image processing (DIP)]] è tipicamente la fase iniziale (basso livello) di qualunque processo di CV: la maggior parte delle tecniche DIP servono per preparare ed elaborare successivamente un'immagine in ambito CV.

![[AI branches.svg#center|600]]

> [!NOTE] Artificial Vision *vs* Human Vision
> Le immagini giocano un ruolo fondamentale nella percezione umana: la visione sfrutta dei [[Gestalt|meccanismi propri per risolvere l'ambiguità]] (che possono essere sfruttati per creare [[Illusioni ottiche]]) ma a differenza di questi, le macchine possono percepire più del limitato [[Spettro elettromagnetico (EM)]] naturalmente percepibile dall'uomo (vedi [[Occhio (Biologia)|Occhio]]).
> * Ultrasuoni
> * Microscopio elettronico

## Artificial vision tasks
* [[Image Classification (CV)]]: l'obiettivo è assegnare una **singola etichetta** (una classe) a un'intera immagine.
- [[Object Detection (CV)]]: l'obiettivo è localizzare e rilevare l'oggetto in un'immagine (inquadrandolo con un *bounding-box*).
- [[Image Segmentation (CV)]]: l'obiettivo è classificare **ogni singolo pixel** dell'immagine in modo da individuare precisamente i contorni dell'oggetto focus.
	- [[Instance Segmentation (CV)]]: ibrido tra object detection e segmentazione semantica. Identifica e delinea *ogni istanza* di un oggetto
	- [[Panoptic Segmentation (CV)]]: combina le due precedenti: assegna a ogni pixel sia un'etichetta di classe (come la semantica) sia un ID di istanza (come la segmentazione d'istanza).
- [[Facial Recognition (CV)]]: task specializzato per il rilevamento di volti
	- [[Facial Analysis (CV)]]: task specializzato per riconoscere determinate caratteristiche da un volto (umore, età..)
- [[Image generation (CV)]]: permette la creazione di immagini digitali sintetiche
	- [[Style transfer (CV)]]: permette di trasferire lo stile di un'immagine ad un'altra.

## Applicazioni
- Riconoscimento difetti e rispetto delle tolleranze
- Orientamento, posizionamento e guida robot
- Misure non a contatto
- Verifiche su nastri in continuo (*Web Inspection*)
- Classificazione e scelta
- Lettura di caratteri e codici