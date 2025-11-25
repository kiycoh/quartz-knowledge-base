---
last modified: 2025, 11, 24 22:11:24
related: null
tags: [natural-language-processing, nlp, tokenization]
---

# Definizione di Delimiter-based tokenization
In [[Natural Language Processing (NLP)]], la **Delimiter-based tokenization**è un approccio alla [[Tokenization (NLP)|tokenizzazione]] che considera i *whitespaces*, punteggiatura e caratteri speciali come separatori per individuare i token.

> [!WARNING] Problema 
> Questo approccio è molto banale, in quanto non considera come questi elementi contribuiscano al significato di parole o frasi. Ad esempio:
> * Rimozione di [[Clitici (Linguistica)]] come "We're, j'ai, c'ho".
> * Espressioni su più parole "New York, rock'n'roll"
> Questi problemi possono essere risolti in maniera deterministica con l'uso di [[Espressione regolare (Informatica teorica)|espressioni regolari]].
