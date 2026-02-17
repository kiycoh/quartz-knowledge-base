---
last modified: 24/10/2025 14:04
tags:
  - nlp
  - chatbot
  - intelligenza-artificiale
---
# Cos'è il chatbot ELIZA
Il [[chatbot]] **ELIZA** è un *caso studio* fondamentale nella sfera del [[Natural Language Processing (NLP)]]. È considerato il primo [[Conversational agent]] della storia. La sua iterazione più famosa DOCTOR fù progettato per impersonificare uno *psicoterapeuta rogeriano* (terapia basata sul riflettere le domande) e simulare una conversazione umana.

![[Pasted image 20251007113417.png]]
## Caratteristiche di ELIZA
La peculiarità di ELIZA non risiedeva in una vera intelligenza, ma in un trucco algoritmico relativamente semplice. Il suo funzionamento si basava su due principi chiave:

- **Pattern Matching (Corrispondenza di modelli)**: ELIZA analizzava l'input dell'utente alla ricerca di parole chiave o frasi specifiche (pattern). Ad esempio, se un utente scriveva "Mi sento triste", ELIZA riconosceva il pattern `Mi sento [EMOZIONE]`.
- **Risposte basate su template**: Una volta identificato un pattern, il programma applicava una regola di trasformazione per generare una risposta. Seguendo l'esempio precedente, la regola poteva essere: "Perché dice di sentirsi [EMOZIONE]?" oppure "Da quanto tempo si sente [EMOZIONE]?". Se non trovava nessun pattern conosciuto, ricorreva a frasi generiche come "Mi parli della sua famiglia" o "Continui".

> [!NOTE] Effetto ELIZA
> L' **effetto ELIZA** fù la tendenza delle persone ad attribuire comprensione, intelligenza ed empatia a un programma anche quando sanno che si tratta di una macchina che segue semplici regole. Molti utenti si sentivano sinceramente "ascoltati" da ELIZA, nonostante la sua totale mancanza di comprensione.

## Critiche ad ELIZA
Le critiche a ELIZA furono importanti e provennero principalmente dal suo stesso creatore:

1. La critica fondamentale è che **ELIZA non capiva assolutamente nulla del significato delle parole.** Era un abile manipolatore di simboli, ma non possedeva alcuna conoscenza del mondo, memoria contestuale della conversazione o capacità di ragionamento.
2. *Joseph Weizenbaum* rimase sconcertato e allarmato nel vedere quanto facilmente ==le persone==, inclusa la sua segretaria, ==si lasciassero ingannare dal programma, confidandogli problemi personali e credendo che li capisse davvero.== Questo lo portò a diventare un forte critico dell'intelligenza artificiale, avvertendo del pericolo di **confondere la simulazione dell'intelligenza con l'intelligenza stessa.**