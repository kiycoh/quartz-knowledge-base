---
last modified: 28/10/2025 15:44
related:
  - '[[Natural Language Processing (NLP)]]'
parent note: '[[Tokenization (NLP)]]'
tags:
  - nlp-pre-processing
  - tokenization
  - sub-word-tokenization
---
# Metodi di tokenization
Non esiste un unico approccio alla [[Tokenization (NLP)|tokenizzazione]] ma a seconda dello scopo e della lingua usata possono essere distinti:
- *[[Approccio Bottom-Up]] (aggregativo)* a partire dalle proprietà del linguaggio.
	- [[Byte-Pair Encoding (BPE)]] ([[Sub-word Tokenization]]): la strategia è spandere il vocabolario aggiungendo dei token ottenuti dalle coppie di vocaboli ricorrenti.
- *[[Approccio Top-Down]] (disgregativo)*, a partire dai dati del corpus.
	* **[[Word Tokenization]]**;
	* [[Character Tokenization]]; 
	* [[WordPiece]] ([[Sub-word Tokenization]])
	* [[Unigram]] ([[Sub-word Tokenization]])
