---
tags:
  - reinforcement-learning
  - intelligenza-artificiale
  - machine-learning
---

**[Gymnasium](https://gymnasium.farama.org/)** è ambiente per implementazione di *Reinforcement Learning Agents*, per singolo agente (per ambienti multi-agenti vedi [[PettingZoo (Python)|PettingZoo]]).

I metodi API principali sono:
* `step()`: aggiorna l'ambiente con azioni ritornando *l'agente osservante* seguente, la ricompensa per l'azione compiuta.
* `reset()`: resetta l'ambiente allo stato iniziale.
* `render()`: presenta l'ambiente di visualizzazione dell'agente.
* `close()`: chiude l'ambiente.
	* *Importante quando si utilizzano software esterni come [[PyGame (Python)|PyGame]]*