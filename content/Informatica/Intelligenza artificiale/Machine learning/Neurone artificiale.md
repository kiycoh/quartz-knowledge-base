---
last modified: 2025, 11, 24 22:11:38
related:
  - '[[Machine learning]]'
tags: [intelligenza-artificiale, machine-learning, neural-networks]
---
Un **neurone artificiale** è identificabile nel **percettrone** (o **perceptron**, **nodo**): un modello matematico ispirato al [[Neurone biologico|neurone biologico]] sviluppato inizialmente da Frank Rosenblatt ([[Percettrone di Rosenblatt]]) nel 1957, nello specifico: ==è un algoritmo per l'apprendimento di un classificatore lineare a soglia, con dati binari multipli in entrata e un singolo dato binario in uscita==. Un numero opportuno di *nodi*, connessi tra loro formano una [[Rete neurale artificiale|rete neurale]] in grado di calcolare funzioni booleane.
# Struttura
1. Il *neurone* riceve dei segnali in input $x_1, x_2, \dots, x_n$.
2. Ogni input è moltiplicato per un peso $w_1, w_2, \dots, w_n$
3. La somma ponderata degli input viene calcolata aggiungendo un termine di bias $b$: $$z = \sum_{i=1}^{n} w_i x_i + b.$$
4. Il risultato $z$ viene passato attraverso una funzione di attivazione **non lineare** (*[[Funzione sigmoidea|sigmoide]]*, *ReLU*, ecc..) per ottenere l'output finale del neurone.

![[neurone_artificiale.svg#center]]
# Funzionamento
