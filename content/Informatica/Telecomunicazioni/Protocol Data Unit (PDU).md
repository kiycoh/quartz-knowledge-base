---
last modified: 2025-06-15T16:55:00.000Z
related:
  - '[[Commutazione dati (Rete informatica)]]'
tags:
  - protocolli-rete
  - computer-networking
  - packet-switching
---
# Definizione di Protocol Data Unit (PDU)
==Un *Protocol Data Unit* (*PDU*) è una sequenza finita di dati trasmessa su una rete, un canale o una linea di comunicazione che utilizzi un [[Commutazione dati (Rete informatica)|modo di trasferimento]] a [[Packet switching]].==

Un **Protocol Data Unit (PDU)** è un'unità di informazione atomica scambiata tra entità paritarie di una rete di computer che usano un determinato protocollo di comunicazione. Rappresenta il "blocco di dati" specifico per ogni livello del modello OSI.

>![[pacchetto_dati.svg#center|400]]
>Ogni pacchetto contiene il **payload** (l'informazione) e **l'[[Header (Telecomunicazione)|header]]** (l'intestazione) che include informazioni su come deve essere indirizzato e consegnato.

## Tipologie di PDU

| Livello OSI | Nome livello | PDU                                                       | Descrizione                                                                  |
| :---------- | :----------- | :-------------------------------------------------------- | :--------------------------------------------------------------------------- |
| 4           | Trasporto    | **Segmento** (per TCP) / **Datagramma** (per UDP)         | Contiene i dati e le informazioni sulle porte (es. porta 80 per HTTP).       |
| 3           | Rete         | **[[Pacchetto (Telecomunicazione)\|Pacchetto]] (Packet)** | Incapsula il segmento e aggiunge gli indirizzi IP di origine e destinazione. |
| 2           | Data Link    | **Frame** (o Trama)                                       | Incapsula il pacchetto e aggiunge gli indirizzi MAC per la rete locale.      |
| 1           | Fisico       | **Bit**                                                   | La sequenza di 1 e 0 che viaggia sul cavo o via radio.                       |

