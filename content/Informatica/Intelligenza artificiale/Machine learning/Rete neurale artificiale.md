---
last modified: 24/10/2025 14:02
related:
  - '[[Connessionismo (IA)]]'
  - '[[Regressione lineare]]'
tags:
  - machine-learning
  - intelligenza-artificiale
  - neural-networks
---
# Definizione di rete neurale artificiale
Nel [[Machine learning]], ==una **neural network** (anche chiamata **rete neurale artificiale** o **ANN** o **NN**) è un modello di apprendimento che mima la struttura biologica delle reti neurali biologiche.== 
* Gli *ANN* sono caratterizzati da una struttura a più livelli: ogni neurone riceve segnali in ingresso, li elabora e trasmette un segnale in uscita.
	* **Input layer:** strato di input;
	* **Hidden layers:** strato di elaborazione;
	* **Output layer:** strato di ritorno del risultato.
* L'unità più piccola è il *[[Neurone artificiale|neurone artificiale]]* (o *nodo*).
	* I *nodi* sono interconnessi tra loro tramite associazioni numeriche, c.d. *weights* ($w$).

> ![[Simple neural network.drawio.png#center]]
> *Qualsiasi stato mentale può essere descritto come un vettore n-dimensionale di valori di attivazione numerica su unità neurali in una rete.*

> [!QUESTION] Come apprendono le reti neurali?
> Le reti neurali non hanno regole predefinite, ma **apprendono dai dati**.
> * L'apprendimento avviene attraverso l’aggiustamento dei pesi sinaptici, spesso tramite l'algoritmo di [[Backpropagation|backpropagation]].
> * Possono apprendere schemi complessi e generalizzare da dati mai visti prima.
> * L’informazione non è immagazzinata in unità simboliche discrete, ma è distribuita su tutta la rete.
