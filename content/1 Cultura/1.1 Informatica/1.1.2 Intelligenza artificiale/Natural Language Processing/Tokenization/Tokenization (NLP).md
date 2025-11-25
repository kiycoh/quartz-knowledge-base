---
last modified: 28/10/2025 15:06
related: null
tags:
  - nlp-pre-processing
  - tokenization
  - natural-language-processing
---
# Tokenization
In [[Natural Language Processing (NLP)|NLP]], ==la **tokenization**== (o **tokenizzazione** in italiano) è un processo che consiste nel suddividere un testo grezzo in [[Token (NLP)|token]] il più velocemente possibile. Nello specifico ==trasforma un testo non strutturato in una sequenza di token che può essere interpretata da una macchina.==
- [[Metodi di tokenizzazione]]

Formalmente la tokenization può essere rappresentata come una funzione matematica
$$f:S\to T$$
 che trasforma una stringa di testo $S$ in una sequenza ordinata di token $T=t_1,t_2,\dots,t_n$ dove ogni token è una sotto-sequenza di caratteri consecutivi estratti da $S$ del tipo: $$S=\underbrace{(c_1,c_2,\dots,c_n)}_{\text{caratteri del testo originale}}$$
  $T$ è una partizione ordinata di $S$ tale che $$t_i=(c_{k_i},c_{k_{i+1}},\dots c_{k_{+1}-1})$$con $1=k_1<k_2<\dots<k_{n+1}=m+1$ dove $k_2, k_3, \dots, k_n$ sono i punti di separazione stabiliti dall'algoritmo di tokenizzazione.
> ![[Pasted image 20251023155135.png|600]]
> Un testo tokenizzato.

> [!WARNING] Problemi della tokenizzazione
> * Mergere o non mergere più token? Vedi ([[Chinese Tokenization]])
> * Problemi che possono essere risolti attraverso l'uso di [[Espressione regolare (Informatica teorica)|espressioni regolari]]
> 	* Rimozione di punteggiatura e caratteri che contribuiscono al senso.
> 	* Presenza di clitici (*we're*, *j'ai*)