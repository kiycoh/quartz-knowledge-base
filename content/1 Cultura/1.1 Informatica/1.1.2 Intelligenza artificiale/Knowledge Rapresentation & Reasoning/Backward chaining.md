---
last modified: 24/10/2025 14:02
related:
  - '[[Forward chaining]]'
tags:
  - logic-matematica
  - backward-chaining
  - knowledge-representation
---
# Definizione di Forward chaining
Il Backward Chaining è una procedura deduttiva che opera "a ritroso" per dimostrare un obiettivo (goal) partendo da esso e risalendo ai fatti noti nella [[Base di conoscenza]] (KB). Il backward chaining è una procedura deduttiva che parte da un obiettivo da dimostrare e procede a ritroso, cercando fatti e regole nella base di conoscenza (KB) che possano giustificare tale obiettivo, fino a raggiungere fatti noti o risolvendo tutti i sotto-obiettivi. Funziona con un approccio "depth-first" (a profondità prima), tentando di risolvere immediatamente i nuovi sotto-obiettivi generati prima di tornare agli obiettivi precedenti.

**Principi Operativi**:
* [[Backtracking]]
- **Orientato all'obiettivo**: Parte da un'affermazione da dimostrare.
- **A catena all'indietro (Backward Chaining)**: Risale dalla conclusione ai presupposti, cercando regole e fatti che possano giustificare l'obiettivo.
- **Da sinistra a destra (Left-to-right)**: Affronta i sotto-obiettivi nell'ordine in cui compaiono.
- **A profondità prima (Depth-first)**: Tenta di risolvere immediatamente i nuovi sotto-obiettivi generati prima di tornare agli obiettivi precedenti.

**Processo (SLD Derivations)**:

1. **Input**: Un insieme di obiettivi {q1, q2, ..., qn}.
2. **Caso Base**: Se l'insieme degli obiettivi è vuoto, la procedura termina con successo.
3. **Passo Ricorsivo**:
    - Prende il primo obiettivo (q1) dall'elenco.
    - Cerca nella KB una clausola di Horn positiva che abbia q1 come letterale positivo (es. `p1 ∧ p2 ∧ ... ∧ pk ⊃ q1`).
    - Per ogni clausola trovata, aggiunge i letterali `p1, ..., pk` come nuovi sotto-obiettivi e richiama ricorsivamente la procedura con l'insieme di obiettivi aggiornato `{p1, ..., pk} ∪ {q2, ..., qn}`.

**Applicazioni**:

- È una tecnica fondamentale per il ragionamento con le clausole di Horn nei sistemi esperti.
- Può essere utilizzato nelle tassonomie per verificare l'appartenenza di un individuo a una categoria più generale, sfruttando la struttura gerarchica.

**Vantaggi**:

- Utile per obiettivi specifici.
- Approccio ricorsivo semplice.

**Svantaggi e Problemi**:

- **Rischio di cicli infiniti**: La procedura può entrare in loop, specialmente in presenza di tautologie nella KB.
- **Inefficienza**: Anche se termina, può ripetere la ricerca degli stessi obiettivi più volte, risultando computazionalmente costosa (complessità esponenziale).
- **Limiti**: Non è utile quando gli obiettivi non sono chiari o si vogliono conoscere tutte le conseguenze di una KB, caso in cui è preferibile il Forward Chaining. La sua efficienza dipende anche dall'ordine in cui i sotto-obiettivi sono risolti.


