---
last modified: 2025-10-14T15:32:00.000Z
related: null
links: >-
  https://www.youtube.com/watch?v=LQQbW3Pve5U&list=PLS1QulWo1RIZDws-_0Bfw5FZFmQJWtMl1
tags:
  - nlp-pre-processing
  - natural-language-toolkit
  - machine-learning
---
# Cos'è NLTK?
**NLTK (Natural Language ToolKit)** è una suite [[Python]] creata nel 2001 che mette a disposizioni diversi moduli per l'[[Natural Language Processing (NLP)|analisi del linguaggio naturale]] simbolico e statistico.  
Riconosciamo i seguenti moduli rilevanti:
* `tokenize` suddivide il testo in parole (`word_tokenize`) o frasi (`sent_tokenize`);
* `corpus` permette di accedere ai diversi corpus e liste di [[Stop words (NLP)]];
* `stem` applica algoritmi di *[[Stemming (NLP)|stemming]]* come *PorterStemmer* o *SnowballStemmer* per ridurre parole alla radice;
* `lemmatize` si riferisce alla *lemmatizzazione*, cioè normalizza le parole alla loro forma base usando *WordNetLemmatizer*;
* `tag` applica automaticamente ad ogni parola la sua specifica etichetta grammaticale (sostantivo, verbo, aggettivo, ecc..);
* `probability` calcola la [[Distribuzione di frequenza semplice (Statistica)|distribuzione di frequenze]] (FreqDist) delle parole;
* `chunck` e `parse` per l'analisi sintattica e la suddivisione in costituenti (chunking, parsing);
* `classification`utile per attività di [[Apprendimento supervisionato]] (*sentiment analysis* o *classificazione anti-spam*).

> [!NOTE] Supporto e compatibilità NLTK
> * Supporta l'integrazione con [[scikit-learn]] e [[TensorFlow]] (chatbot, sistemi di analisi dati).
> * Fornisce accesso a risorse linguistiche come WordNet, liste di stopword per molte lingue e numerosi corpus testuali
