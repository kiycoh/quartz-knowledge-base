---
last modified: 27/10/2025 18:51
related:
  - '[[Classi di complessità (P, NP, NP-completi)]]'
tags:
  - algoritmi-ordinamento
  - complessita-computazionale
  - algoritmi-greedy
---
# Cos'è un problema computazionale?
==Un **problema computazionale** definisce la relazione formale tra un input e l'output desiderato.== Esso può essere un **problema astratto**, ovvero una relazione binaria tra un insieme di istanze e un insieme di soluzioni. In base alla natura della sua soluzione, un problema astratto si classifica in:
- **Problema di Decisione**: L'insieme delle soluzioni è binario (vero/falso, 1/0). Ad esempio, "Il numero X è primo?".
- **Problema di Ottimizzazione**: Si cerca una soluzione che minimizzi o massimizzi una certa misura (es. costo o guadagno). Ad esempio, "Trovare il percorso più breve". È importante notare che un problema di ottimizzazione può essere trasformato in un problema di decisione senza che diventi più difficile da risolvere.

Per essere gestito da un calcolatore, un problema astratto deve essere convertito in un **problema concreto** attraverso una **codifica**, che è una funzione che mappa oggetti astratti (es. numeri, grafi) a stringhe binarie. Il calcolatore opera direttamente su queste stringhe. L'insieme delle istanze di un problema di decisione, in termini di linguaggi formali, è rappresentato dall'insieme di tutte le stringhe binarie ($\Sigma^_$). Un problema di decisione $Q$ viene quindi definito da un linguaggio $L = {x \in \Sigma^_ : Q(x) = 1}$.

La scelta della codifica è cruciale, ma se due codifiche sono **correlate polinomialmente** (cioè, la lunghezza dell'output di una codifica è polinomiale rispetto alla lunghezza dell'input dell'altra), l'appartenenza del problema alla classe P non cambia. Per convenzione, si utilizzano codifiche standard (es. binaria per interi, ASCII per insiemi) e si ci riferisce ai problemi astratti, indicando una codifica standard di un oggetto $O$.

Un linguaggio $L$ è **accettato** da un algoritmo $A$ se $A(x)$ ritorna 1 per ogni stringa $x \in L$. Non è detto che $A(x)$ ritorni 0 per le stringhe non in $L$. Un linguaggio $L$ è **deciso** da un algoritmo $A$ se $A(x)$ accetta ogni stringa in $L$ e rifiuta ogni stringa non in $L$. Per la classe P, si può dimostrare che le due definizioni sono equivalenti.

Un algoritmo deve essere corretto, ovvero deve risolvere ogni possibile istanza di un dato problema computazionale e può essere 
N.B. Vedremo che un algoritmo non corretto può aiutare nell’ambito dell’IA trovando delle soluzioni non errate ma accettabili a problemi non facilmente risolvibili.
[[Algoritmo di ordinamento]]

# Come risolvere un problema computazionale?
Gli [[Algoritmo (Informatica)|algoritmi]] e le [[Struttura dati (Informatica teorica)|strutture dati]] consentono di risolvere [[Problema computazionale|problemi computazionali]] definendo in termini formali e generali la relazione che deve sussistere tra un input e un output.
- Esistono diverse soluzioni ad un problema: *il compito difficile è scegliere la più efficiente* (vedi [[Algoritmo di ordinamento|Il problema dell'ordinamento]]).
	- Esistono problemi per i quali non si conosce una soluzione efficiente ([[Problemi NP-completi|problemi NP-completi]]).