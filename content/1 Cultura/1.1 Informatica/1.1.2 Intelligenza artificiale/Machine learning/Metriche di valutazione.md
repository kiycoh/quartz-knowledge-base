---
last modified: 2025, 11, 24 22:11:25
tags: [intelligenza-artificiale, machine-learning, scienze-cognitive]
---
# Metriche di valutazione
## Comprendere la metrica chiave: mAP
Prima di scrivere il codice, assicuriamoci di aver compreso la nostra metrica più importante.
- **Che cos'è la precisione?** Risponde alla domanda: "Di tutte le previsioni effettuate dal modello, quante erano corrette?"

- **Che cos'è il richiamo?** Risponde alla domanda: "Di tutti i gioielli effettivamente presenti nelle immagini, quanti ne ha trovati il modello?"

- **Precisione media (AP)**: per una singola classe (ad esempio "anello"), l'AP è la media dei valori di precisione calcolati a diversi livelli di richiamo. Ci offre una visione più olistica rispetto alla semplice osservazione di un singolo valore di precisione o richiamo.

- **Precisione media (mAP)**: è semplicemente la media dei valori AP di tutte le nostre classi (anello, collana, diamante, oro, ecc.). Ci fornisce un unico numero che riassume l'accuratezza complessiva del modello sia nell'individuazione che nella classificazione corretta dei gioielli.
Un mAP più alto è migliore. Un punteggio di `mAP@.50` significa che stiamo calcolando la precisione media in cui una previsione è considerata "corretta" se il suo riquadro di delimitazione ha un Intersection over Union (IoU) di almeno il 50% con il riquadro di riferimento.

  

*Tradotto con [DeepL.com](https://www.deepl.com/?utm_campaign=product&utm_source=web_translator&utm_medium=web&utm_content=copy_free_translation) (versione gratuita)*