---
last modified: 2025-06-15T18:55:00.000Z
related:
  - '[[Payload]]'
tags:
  - intelligenza-artificiale
  - computer-vision
  - machine-learning
---
# Definizione di header
L'*header* indica quella parte di [[Pacchetto (Telecomunicazione)|pacchetto]] (più in generale, di [[Protocol Data Unit (PDU)|PDU]]) che ==contiene le [[Protocollo di rete|informazioni di protocollo]] necessarie affinché i dati utili che vengono trasportati efficacemente tra gli utilizzatori della rete, garantendo il corretto funzionamento della rete==

![[pacchetto_dati.svg#center|400]]
## Composizione standard di un header
* **ID:** identificatore 16 bit della query (per associare risposta → query).
* **Flags (bit):**
	* **QR:** 0 = query, 1 = reply.
	* **AA (Authoritative Answer):** = 1 se il server è autoritativo.
	* **RD (Recursion Desired):** client chiede ricorsione.
	* **RA (Recursion Available)**: server può fare ricorsione.
* **4 campi numerici:** indicano quanti record sono presenti nelle sezioni successive.