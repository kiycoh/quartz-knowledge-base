---
last modified: 2025-06-15T21:39:00.000Z
related:
  - '[[Rete informatica]]'
tags:
  - protocolli-rete
  - packet-switching
  - communication
---
# Definizione di commutazione dati
Con *commutazione dati* (o *trasferimento dati*) si indica ==l'insieme delle modalità adottate da una [[Rete di telecomunicazione]] per trasferire efficacemente (con host [[Interoperabilità|interoperabili]]) le [[Protocol Data Unit (PDU)|informazioni]] attraverso la rete stessa.== Nello specifico è un'operazione all'interno di un nodo che tratta l'informazione e la trasmette sotto forma di segnale, affinché sia indirizzata verso il destinatario.
## Implementare un trasferimento
Fissare un modo di trasferimento vuol dire fissare:
* Uno schema di multiplazione (accesso multiplo) per il trasferimento dell'informazioni sui collegamenti fisici:
* Un meccanismo di *commutazione* sui nodi di transito elaborativi:
	* [[Circuit Switching]]
	* [[Packet switching]]
	* [[Virtual Circuit Switching]]
* L'architettura [[Protocollo di rete|protocollare]] per le funzioni di trasporto.

> [!NOTE] Approfondimento sui protocolli
> I protocolli di trasporto utilizzati per l'implementazione di queste funzioni sono progettati e realizzati specificatamente secondo le esigenze o tipologie di servizi che la rete o parte di essa deve supportare.
### Fasi standard di un trasferimento
1. **Segmentazione dati**: i dati inviati vengono suddivisi in [[Protocol Data Unit (PDU)|pacchetti]] (header e payload)
2. **Invio e instradamento**: i pacchetti vengono instradati in rete verso la loro destinazione da *[[Switch (Telecomunicazione)|switch di pacchetti]]* che decidono la rotta migliore sulla base delle informazioni nell'header.
3. **Ricomposizione dei pacchetti**: una volta raggiunta la destinazione i pacchetti vengono ri-assemblati per ricostruire i dati.