---
last modified: 27/10/2025 18:51
related:
  - '[[Struttura dati (Informatica teorica)]]'
tags:
  - algoritmi-ordinamento
  - informatica-teorica
  - algoritmi-greedy
---
# Perché algoritmi e strutture dati?
Gli [[Algoritmo (Informatica)|algoritmi]] e le [[Struttura dati (Informatica teorica)|strutture dati]] consentono di risolvere [[Problema computazionale|problemi computazionali]] definendo in termini formali e generali la relazione che deve sussistere tra un input e un output.
- Esistono diverse soluzioni ad un problema: *il compito difficile è scegliere la più efficiente* (vedi [[Algoritmo di ordinamento|Il problema dell'ordinamento]]).
	- Esistono problemi per i quali non si conosce una soluzione efficiente ([[Problemi NP-completi|problemi NP-completi]]).
## Cos'è un algoritmo?
Un [[Algoritmo (Informatica)]] è una sequenza di passi computazionali che trasforma l'input in output in un tempo definito. Bisogna che funzionino su *una gamma* di input possibili in una determinata istanza di problema.
- Un algoritmo ambisce ad essere **efficiente** e **corretto**.
	- Un algoritmo efficiente e corretto utilizza il minor numero di risorse computazionali (potenza di calcolo e spazio).
## [[Struttura dati (Informatica teorica)]]
E' un modo per arrangiare informazioni su di un computer affinché queste possano essere accessibili e modificabili efficacemente.

- Non esiste un'unica struttura dati che vada bene per qualsiasi compito (è importante valutare vantaggi e svantaggi di ognuna).

## [[Programmazione dinamica]]
Una lista concatenata ha una *struttura dati dinamica* le cui operazioni permesse sono `insertion` e `delete`
# [[Equazione di ricorrenza]]

# [[Albero (Struttura dati)|Gli alberi]]
# [[Alberi binari di ricerca]]

# [[Classi di complessità (P, NP, NP-completi)]]
Problemi verificabili in tempo polinomiale, la soluzione potrebbe essere esponenziale.
- Problemi P
- Problemi NP
- Problemi NP-completi
# [[Agenti (IA)]]
# Analisi algoritmica
Analizzare un algoritmo significa prevedere le risorse che l'algoritmo richiede (tempo di elaborazione).
# To-do
Pesi positivi, pesi negativi, cammino, cicli, grafi, archi positivi e negativi, ordinamento topologico, l'algoritmo Dijkstra, Minheap. albero di fibonacci, Bellan Ford, algoritmi avidi, algoritmi dinamici
# Agenti
https://www.okpedia.it/temp/agente_intelligente
## Esempi tipi di ambiente

| Ambiente operativo   | Osservabile     | Agenti   | Deterministico | Episodico | Statico | Discreto               |
| -------------------- | --------------- | -------- | -------------- | --------- | ------- | ---------------------- |
| Cruciverba           | ✅ Completamente | Singolo  | ✅              | ❌         | ✅       | ✅                      |
| Scacchi              | ✅ Completamente | Multipli | ✅              | ❌         | ✅       | ✅                      |
| Scacchi con orologio | ✅ Completamente | Multipli | ✅              | ❌         | 🟨 Semi | 🟨 Discreto e continuo |
| Poker                | ❌ Parzialmente  | Multipli | 🟨 Stocastico  | ❌         | ✅       | ✅                      |
| Autista di taxi      | ❌ Parzialmente  | Multipli | ❌              | ❌         | ❌       | ❌ Continuo             |
| Diagnosi medica      | ❌ Parzialmente  | Singolo  | 🟨 Stocastico  | ❌         | ❌       | ❌ Continuo             |

# Appunti vari
Formula consistenza di un euristica == disuguaglianza triangolare

# Funzioni euristiche
## Come progettare un'euristica
- Rilassamento del problema
- Database pattern
- Uso dei punti di riferimento
- Apprendimento tramite esperienza