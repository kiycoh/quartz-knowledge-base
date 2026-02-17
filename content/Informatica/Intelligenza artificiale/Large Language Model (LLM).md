---
tags:
  - intelligenza-artificiale
  - rete-neurale
  - machine-learning
---

# Definizione di Large Language Model
Un **Large Language Model** (abbreviato **LLM**, in italiano **Modello Linguistico di Grandi Dimensioni**) è un tipo di modello di [[Intelligenza artificiale]] basato su [[Rete neurale artificiale|reti neurali]] (solitamente con architettura [[Transformer]]) addestrato su enorme quantità di dati testuali.

> [!WARNING] ChatBot *vs* LLM
> A differenza di un [[chatbot]], un LLM è un modello linguistico nettamente più potente e versatile:ù
> 
> | Caratteristica | Chatbot (Tradizionale) | Large Language Model (LLM) |
| :--- | :--- | :--- |
| **Scopo Principale** | Applicazione per un compito specifico (es. prenotare un volo, rispondere a FAQ). | Motore di linguaggio per scopi generali. |
| **Architettura** | Spesso basato su regole, script o modelli di recupero. | Rete neurale di grandi dimensioni (es. Transformer). |
| **Flessibilità** | Limitata al suo dominio e agli script predefiniti. | Estremamente flessibile; può affrontare compiti nuovi tramite il prompting. |
| **Generazione Testo**| Solitamente recupera risposte da un database o segue uno script. | Genera testo nuovo e originale in modo dinamico. |
| **Dati di Addestramento**| Addestrato (se basato su ML) su un dataset specifico per il suo compito. | Addestrato su un corpus massivo e diversificato di testo e codice. |
| **Esempio** | Un assistente bancario automatico che risponde a domande sul saldo del conto. | Il modello GPT-3, LaMDA, o Gemini. |

## Caratteristiche di un LLM
- **Generalità**: è addestrato su un corpus vasto e generico (come gran parte di Internet), il che gli consente di comprendere e generare testo su una gamma quasi illimitata di argomenti.
- **Capacità Generative**: può generare testo nuovo e coerente, non solo recuperare risposte predefinite. Questo gli permette di riassumere, tradurre, scrivere codice, rispondere a domande complesse e persino scrivere poesie.
- **Apprendimento Contestuale (In-context Learning)**: può adattare il suo comportamento in base agli esempi e alle istruzioni fornite nel prompt, senza necessità di ri-addestramento.