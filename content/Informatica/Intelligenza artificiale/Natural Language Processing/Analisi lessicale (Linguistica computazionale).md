---
last modified: 2025, 11, 10 16:11:11
related: null
parent note: '[['
tags:
  - linguistica-computazionale
  - analisi-lessicale
  - tokenizzazione
---
# Analisi lessicale (Linguistica computazionale)
L'analisi lessicale è la **prima fase** che un compilatore o un interprete (come quello di Java) esegue sul codice sorgente. Il suo compito è trasformare una semplice sequenza di caratteri (il file di testo del tuo codice) in una sequenza più strutturata di "elementi significativi", chiamati **Token**.

Pensa a questo processo come a come il tuo cervello legge una frase in una lingua naturale:
*   **Input:** "Ilcanecorreveloce" (una sequenza di caratteri senza spazi)
*   **Output del Lexer:** "Il" - "cane" - "corre" - "veloce" (parole distinte con un significato)