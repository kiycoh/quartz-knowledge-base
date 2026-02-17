---
last modified: 2025, 11, 10 16:11:24
related:
  - '[[Token (Linguistica computazionale)]]'
parent note: null
tags:
  - linguistica-computazionale
  - analisi-lessicale
  - tokenizzazione
---
# Java token
==I **Java token** sono gli elementi lessicali di base, indivisibili e categorizzati, che il compilatore Java riconosce durante l'[[Analisi lessicale (Linguistica computazionale)|analisi lessicale]] del codice sorgente==, prima della fase di parsing e generazione del bytecode. I tokens possono essere pensati come il **vocabolario di base** del linguaggio: le "parole" e la "punteggiatura" che, combinate secondo le regole della **sintassi** (la grammatica), formano programmi validi.
- Quando si parla di tokens in Java (o in qualsiasi linguaggio di programmazione), 

| Tipo di tokens                       | Lessemi                                                      | Spiegazione                                                                               |
| :----------------------------------- | :----------------------------------------------------------- | :---------------------------------------------------------------------------------------- |
| **[[Java keyword\|Keywords]]**       | `class`, `public`, `static`, `void`, `if`, `for`, `while`    | Parole riservate con un significato fisso e immutabile nel linguaggio.                    |
| **[[Java identifier\|Identifiers]]** | `String`, `main`, `args`, `myVariable`, `calculateTotal`     | Nomi definiti dal programmatore per classi, metodi, variabili, ecc.                       |
| **[[Java literal\|Literals]]**       | `10`, `3.14`, `'A'`, `"Ciao Mondo"`, `true`, `false`, `null` | Valori costanti e fissi nel codice.                                                       |
| **[[Java separator\|Separators]]**   | `;` `,` `.` `()` `{}` `[]`                                   | Caratteri usati per delimitare e organizzare il codice.                                   |
| **[[Java Operator\|Operators]]**     | `=`, `+`, `-`, `*`, `/`, `==`, `!=`, `<`, `>`, `&&`, `++`    | Simboli che rappresentano operazioni.                                                     |
| **[[Java comment\|Comments]]**       | `// commento`, `/* commento */`, `/** doc */`                | Anche se spesso ignorati dal compilatore, sono elementi lessicali riconosciuti dal lexer. |
