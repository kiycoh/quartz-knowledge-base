---
last modified: 2025, 11, 24 22:11:24
related: []
tags: [intelligenza-artificiale, machine-learning, reti-neurali]
---
# Intelligenza artificiale
![[AI branches.svg#center]]

## Branche dell'intelligenza artificlae
* [[Sistemi esperti (IA)]]
* [[Rappresentazione della conoscenza e del ragionamento (KRR)]]
[[Algoritmi di ricerca euristica]]
[[Agenti singoli semplici (IA)]]
[video](https://youtu.be/PZ30zva-r4I):

[[Agenti (IA)]]

Basi e Architetture:
 * Intelligenza Artificiale (AI): Sistemi che risolvono problemi che richiedono l'intelletto umano [02:02].
 * Task: Il problema specifico che un sistema di intelligenza artificiale è progettato per risolvere [02:42].
 * Algoritmo: La serie di passaggi che un sistema di intelligenza artificiale utilizza per risolvere un task [02:52].
 * Machine Learning: Un approccio allo sviluppo di algoritmi di intelligenza artificiale che consente ai sistemi di apprendere dai dati [04:15].
 * Reti Neurali: Un tipo specifico di algoritmo di machine learning, ampiamente utilizzato nell'intelligenza artificiale [05:34].
 * Parametri: Numeri all'interno di una rete neurale che vengono regolati per influenzare l'output del modello [05:58].
 * Large Language Model (LLM): Un tipo di modello di intelligenza artificiale basato su reti neurali, addestrato su testo per comprendere e generare testo [07:42].
 * Transformer: Un'architettura di rete neurale che costituisce la base di molti LLM moderni [08:12].
 * Next Token Prediction: Il task di base che gli LLM sono progettati per risolvere, ovvero prevedere la parola successiva in una sequenza di testo [09:45].
 * Meccanismo dell'Attenzione: Una tecnica utilizzata nelle architetture [[Transformer]] per consentire al modello di concentrarsi su parti specifiche dell'input [11:38].
 * Mixture of Experts: Architettura che migliora l'efficienza della rete, attivando pezzi specifici a seconda delle richieste [14:34].
Allenamento e Ottimizzazione:
 * Training Set: L'insieme di dati utilizzato per addestrare un modello di machine learning [16:37].
 * Pretraining: La fase iniziale dell'addestramento di un LLM, in cui impara a prevedere il token successivo [17:09].
 * Supervised Fine-Tuning: Una fase di addestramento in cui i parametri di un LLM vengono perfezionati per compiti specifici [17:39].
 * Alignment: Fase in cui vengono scelte le risposte migliori, non tanto in termini di performance, quanto di allineamento nel comportamento [18:38].
 * Distillation: Una tecnica per comprimere un modello di intelligenza artificiale di grandi dimensioni in uno più piccolo [21:01].
 * Quantization: Una tecnica per ridurre la dimensione di un modello di intelligenza artificiale riducendo la precisione dei suoi parametri [24:41].
Prompt e Sistemi:
 * Prompting: L'atto di progettare input efficaci per i modelli di intelligenza artificiale per ottenere i risultati desiderati [27:21].
 * In-context Learning: La capacità di un modello di intelligenza artificiale di utilizzare il contesto fornito nel prompt per migliorare le sue prestazioni [33:43].
 * Zero-shot: Non fornire esempi al modello [34:40].
 * Few-shot: Fornire pochi esempi al modello [34:40].
 * Chain of Thought (CoT): Tecnica che migliora il ragionamento del modello, facendogli snocciolare i token [37:49].
 * Retrieval Augmented Generation (RAG): Un sistema che recupera informazioni rilevanti da una base di conoscenza esterna e le incorpora nel prompt per migliorare la risposta del modello [40:28].
 * Agenti: Modelli in grado di interagire con il mondo [42:05].
 * Open Source: Modelli di cui si conoscono i parametri [30:55].
Valutazione:
 * Benchmarking: Il processo di confronto sistematico delle prestazioni di diversi sistemi di intelligenza artificiale [44:18].
 * Benchmark: Una verifica per confrontare le performance dei sistemi di intelligenza artificiale [44:18].
 * Training Set: Dati che diamo alla rete in fase di allenamento [44:53].
 * Test Set: L'esame vero e proprio che il modello non deve aver mai visto prima [44:53].
 * Data Leaking: Quando il test set finisce nei dati di allenamento [50:40].
Safety:
 * Preparedness Framework: Framework di Star pronti, se non si tiene d'occhio i modelli, sfuggono di mano [55:43].
 * System Card: Documento che descrive i rischi e le limitazioni di un modello di intelligenza artificiale [57:09].
 * Jailbreak: Saltare da parte dell'utente i blocchi che sono stati messi in fase di allineamento per censurare il modello a fare cose che non dovrebbe fare [58:00].
 * Mitigation: Sviluppare dei pezzi apposta nei modelli per impedire che succedano determinate cose [58:28].