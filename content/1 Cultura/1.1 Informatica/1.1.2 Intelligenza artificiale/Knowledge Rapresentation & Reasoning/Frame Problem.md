---
last modified: 24/10/2025 14:02
tags:
  - krr
  - knowledge-representation
  - intelligenza-artificiale
---
Il problema principale degli assiomi di [[Frames (KRR)]] è la loro numerosità: sono necessari in gran quantità perché per ogni fluente e per ogni azione che non lo modifica, bisognerebbe esplicitare l'assenza di effetto. La soluzione desiderata è un metodo automatico e compatto per generare questi assiomi. La risoluzione si basa sulla riscrittura degli assiomi di effetto in forme normali e sull'introduzione di nuovi tipi di assiomi:

- **Assiomi di chiusura esplicativa**: Completano la descrizione degli effetti di un fluente affermando che un fluente cambia valore _solo se_ si verificano le condizioni specificate dagli assiomi di effetto.
- **Assiomi di stato successivo**: Se si assumono la coerenza degli effetti (un fluente non può essere reso contemporaneamente vero e falso dalla stessa azione) e l'unicità dei nomi delle azioni, è possibile unificare tutti gli assiomi di effetto e di frame per un dato fluente in una singola formula compatta. Questa formula descrive esattamente quando un fluente sarà vero dopo un'azione.

### Tipi di Ragionamento

Una volta strutturata una base di conoscenza nel Situation Calculus, è possibile eseguire vari tipi di ragionamento:

- **Proiezione**: Determinare cosa sarà vero dopo una data sequenza di azioni a partire da una situazione iniziale.
- **Verifica di Legalità**: Controllare se una sequenza di azioni può essere effettivamente eseguita, verificando che le precondizioni di ogni azione siano soddisfatte nella situazione precedente.

### Limitazioni
Nonostante la sua utilità, il Situation Calculus ha delle limitazioni:

- Gestisce un solo agente.
- Non rappresenta il tempo esplicito (durata delle azioni).
- Non gestisce la concorrenza (le azioni sono sequenziali).
- Modella solo azioni discrete.
- Permette solo ipotesi, non afferma che un'azione sia realmente accaduta.
- Lavora solo con azioni primitive, non azioni complesse con cicli o condizioni.