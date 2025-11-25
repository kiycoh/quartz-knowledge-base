---
last modified: 2025, 11, 24 21:11:42
related: null
tags: [backtracking, backward-chaining, intelligenza-artificiale]
---

# Definizione di backtracking
Nel contesto del **backward chaining**, il **backtracking** è una tecnica fondamentale di gestione delle alternative durante il processo di dimostrazione di un obiettivo.

**Ruolo del backtracking**: Quando la procedura di backward chaining prende il primo obiettivo dall'elenco e cerca nella KB una clausola che abbia tale obiettivo come letterale positivo, possono esserci più regole o fatti che potenzialmente lo soddisfano. Il backtracking interviene quando una strada intrapresa non porta al successo (cioè non si riesce a dimostrare un sotto-obiettivo o si incontra una contraddizione). In questi casi, il sistema "torna indietro" (backtracks) e prova un'alternativa precedentemente scartata, esplorando un percorso di derivazione diverso. Questo consente di esplorare tutte le possibili combinazioni di regole e fatti per trovare una dimostrazione dell'obiettivo iniziale.

**Svantaggi del backtracking nel backward chaining**: Nonostante la sua utilità, il backtracking può portare a problematiche:

- **Cicli infiniti**: La procedura può entrare in loop infiniti, specialmente se la KB contiene tautologie o regole ricorsive definite in modo non ottimale, dove la dimostrazione di un obiettivo può generare se stessa come sotto-obiettivo indefinitamente.
- **Inefficienza**: Anche se termina, il processo può essere molto inefficiente, ripetendo la ricerca degli stessi obiettivi più volte e sprecando risorse computazionali.

Per gestire questi "tranelli" del backward chaining e ottimizzare l'efficienza, è necessario implementare strategie di controllo procedurale.