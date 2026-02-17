---
last modified: 2025-06-09T11:29:00.000Z
related:
  - '[[Modello lineare generalizzato (GLM)]]'
  - '[[Apprendimento supervisionato]]'
tags:
  - machine-learning
  - classificazione-statistica
  - regressione-logistica
---


# Definizione di Regressione logistica
La regressione logistica è un [[Modello lineare generalizzato (GLM)]] impiegato per modellare la relazione tra un insieme di [[Predittori statistici]] ($X$) e una [[Variabile risposta]] binaria ($Y$), che assume tipicamente valori 0 o 1 (ad esempio, successo/fallimento, malato/sano).

La **regressione logistica** è quindi una tecnica di [[Classificazione statistica|classificazione statistica]], in particolare per [[Problemi binari|problemi binari]].

> [!IM]
> A differenza della regressione lineare, che predice un output numerico continuo, la regressione logistica non modella direttamente la risposta $Y$, ma piuttosto la probabilità che $Y$ sia 1, $P(Y=1|X)$, che indichiamo con $p(X)$. Tentare di modellare $p(X)$ linearmente ($p(X) = \beta_0 + \beta_1X$) sarebbe problematico, poiché le probabilità devono essere comprese tra 0 e 1, mentre un modello lineare può produrre valori al di fuori di questo intervallo.
> 

> Usa la **regressione logistica** quando il risultato da predire è categorico (*o dicotomica*) (es: sì/no, sano/malato, cliente/non-cliente).

Ritorna la probabilità di successo