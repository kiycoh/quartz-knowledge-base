---
tags:
  - algoritmi-ordinamento
  - automi-finiti-non-deterministici
  - cognitivismo
---

Gli **automi a pila (PDA - Pushdown Automata)** sono modelli di automi che estendono gli automi a stati finiti ([[Automa finito deterministico (DFA)]]) introducendo una pila, una struttura dati a cui si può accedere o inserire simboli solo all'estremità superiore. I PDA sono più potenti degli automi a stati finiti e possono riconoscere linguaggi più complessi, come i linguaggi context-free. 

Gli automi a pila sono come gli automi finiti non deterministici ma hanno una componente in più chiamata **pila** (stack). 

*La **pila** fornisce memoria aggiuntiva oltre alla quantità finita di essa disponibile nel controllo, perciò la pila consente agli automi di riconoscere alcuni linguaggi non regolari.

Gli automi a pila sono **computazionalmente equivalenti** alla grammatica context-free. Questa equivalenza ci dà 2 alternative per provare che un linguaggio è context-free: possiamo dare una grammatica context-free che lo genera oppure un automa a pila che lo riconosce.

Gli automi a pila possono essere non deterministici. Automi a pila deterministici e non deterministici non sono computazionalmente equivalenti.