---
last modified: 24/10/2025 14:02
tags:
  - machine-learning
  - overfitting
  - inductive-bias
---
# Definizione di rischio induttivo
Nel **[[Machine learning|machine learning (ML)]]**, il **rischio induttivo** è un concetto centrale e si riferisce al fatto che qualsiasi modello di apprendimento automatico, quando impara da un insieme limitato di dati di addestramento, deve fare delle **assunzioni implicite** per poter **generalizzare** ciò che ha appreso a nuovi dati mai visti prima. 
==Il **"rischio"** sta nel fatto che queste assunzioni (o preferenze) potrebbero non essere corrette per il problema reale che si sta cercando di risolvere.==

In sostanza:
1.  Il modello ML vede solo un **campione** dei dati possibili (i dati di addestramento).
2.  Da questo campione, deve **indurre** una regola o un pattern generale.
3.  Esistono potenzialmente **infinite regole** che potrebbero spiegare perfettamente i dati di addestramento, ma che darebbero risultati diversi su nuovi dati.
4.  L'algoritmo di apprendimento e la sua configurazione (spesso chiamati collettivamente "inductive bias" o "bias di apprendimento") lo portano a **preferire certe tipologie di regole/pattern** rispetto ad altre.

## Fattori di rischio induttivo
1.  **Dati di addestramento:**
    * **Dati di addestramento limitati** costringono il modello a fare "scommesse" più audaci (e quindi aumentano il rischio induttivo).
    * **Dati di addestramento distorti (biased data)** possono ingannare il modello, portandolo a fare generalizzazioni errate e potenzialmente discriminatorie (bias nel riconoscimento facciale).
2.  **Overfitting e Underfitting**
    * L'**overfitting** si ha quando il modello impara così bene i dati di addestramento (incluso il rumore e le coincidenze) che fallisce nel generalizzare a nuovi dati. È una classica manifestazione di un rischio induttivo gestito male.
    * L'**underfitting** si ha quando il modello è troppo semplice.
3.  **Cambiamento del dominio (Domain Shift):**
    * Quando i dati su cui il modello viene testato o utilizzato nel mondo reale differiscono significativamente dai dati su cui è stato addestrato.