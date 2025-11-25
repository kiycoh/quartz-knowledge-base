---
last modified: 24/10/2025 14:02
related:
  - '[[Backward chaining]]'
tags:
  - intelligenza-artificiale
  - scienze-cognitive
  - machine-learning
---
# Definizione di Forward chaining

Il Forward Chaining è una procedura deduttiva che opera "in avanti", partendo dai fatti noti nella base di conoscenza (KB) e applicando iterativamente le regole per derivare nuove conclusioni, fino a raggiungere un obiettivo o esaurire le deduzioni possibili.

**Principi Operativi**:

- **Orientato ai dati**: Inizia dai fatti e procede per inferenze.
- **A catena in avanti (Forward Chaining)**: Si deduce da premesse note a nuove conclusioni.
- **Iterativo**: Applica le regole più volte finché non si possono derivare nuovi fatti.

**Processo (Sistemi di Produzione)**:

1. **Input**: Un insieme di fatti noti e, opzionalmente, un insieme di obiettivi da verificare.
2. **Fase di ricerca**: Esplora la KB per trovare clausole (regole) del tipo `¬q1, ¬q2, ..., ¬qn, p` (equivalente a `q1 ∧ q2 ∧ ... ∧ qn ⊃ p`) per le quali tutti i letterali nel corpo (`q1, ..., qn`) sono già fatti noti nella memoria di lavoro.
3. **Risoluzione**: Se una regola è attivabile, la clausola `p` viene risolta e aggiunta alla KB come nuovo fatto.
4. **Ripetizione**: Il ciclo di ricerca e applicazione delle regole continua.
5. **Terminazione**: La procedura termina quando non ci sono più regole applicabili, o quando tutti gli obiettivi specificati sono stati dedotti.

**Caratteristiche e Vantaggi**:

- **Completezza ed efficienza**: È in grado di trovare tutte le conseguenze logiche dei fatti iniziali in modo sistematico ed efficiente, particolarmente per le clausole di Horn.
- **Terminazione garantita**: La procedura è finita, poiché ogni clausola può essere attivata al massimo una volta.
- **Efficienza computazionale**: Può essere implementata con complessità in tempo lineare, utilizzando strutture dati adeguate come contatori e code.
- **Modularità e Trasparenza**: Le regole sono indipendenti e facilmente interpretabili.
- **Flessibilità**: Adattabile a diversi tipi di problemi.

**Applicazioni**:

- Comunemente impiegato nei **Sistemi Esperti**, che sono modelli computazionali basati su regole "SE... ALLORA..." e utilizzano una memoria di lavoro per i fatti noti. Esempi includono sistemi medici o di configurazione automatica.
- Utilizzato per il ragionamento in **Tassonomie** e sistemi orientati agli oggetti (come i frame), consentendo di dedurre nuove informazioni sfruttando la struttura gerarchica dei concetti e l'ereditarietà.