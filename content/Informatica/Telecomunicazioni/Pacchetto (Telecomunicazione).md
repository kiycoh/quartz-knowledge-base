---
last modified: 2025-06-15T21:51:00.000Z
related:
  - '[[Packet switching]]'
tags:
  - protocolli-rete
  - packet-switching
  - telecomunicazioni
---
# Definizione di pacchetto
Un *pacchetto* è un [[Protocol Data Unit (PDU)]] nel livello 3 OSI

## Composizione pacchetto
**La forma esatta di ogni pacchetto dipende quindi dal protocollo utilizzato**, ma in genere sono presenti tre parti:
* [[Header (Telecomunicazione)]]: contiene tutte le informazioni di [[Overhead (Informatica)]] necessarie alla trasmissione come l'*indirizzo del trasmettitore e del ricevitore*, *la vita del pacchetto*, i *dati che riguardano l'assemblaggio* con gli altri pacchetti.
* [[Payload]]: i *data* utili trasmessi.
* [[Checksum (Informatica)]]: codice di controllo per verificare la corretta ricezione dei pacchetti (e quindi l'eventuale presenza di errori).