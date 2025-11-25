---
last modified: 2025, 11, 10 16:11:29
related: null
tags:
  - nlp-pre-processing
  - chinese-tokenization
  - tokenization
---
# Chinese Tokenization
In [[Natural Language Processing (NLP)]], la **Tokenizzazione del Cinese** è un caso particolare di [[Tokenization (NLP)|tokenization]] perché il [[Cinese]] non usa spazi per separare le parole.
* L'approccio più semplice è tokenizzare ogni singolo *hanzi (漢字)* ma approcci moderni hanno cambiato questo paradigma. 
* La taglia del vocabolario Cinese è decisamente ridotta, il 95% delle parole sono composte da 1 o 2 hanzi.
* In altre lingue come il Giapponese o il Thai i singoli caratteri sono unità troppo piccole e tecniche di segmentazione in parole

> ![[Pasted image 20251023210659.png|900]]
> Diversi tipi di tokenizer restituiscono [[Token (NLP)|token]] di lunghezza diversa. La frase tradotta: "Lui è un tipo che crede alla scienza, lui non crede alle questioni misteriose"