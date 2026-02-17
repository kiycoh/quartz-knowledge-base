---
last modified: 24/10/2025 14:02
related:
  - '[[Closed World Assumption (CWA)]]'
  - '[[Ragionamento non-monotono (KRR)]]'
tags:
  - machine-learning
  - scienze-cognitive
  - intelligenza-artificiale
---



La Circumscription è  un approccio fondamentale al **[[Ragionamento non-monotono (KRR)]]**, che permette di trarre conclusioni plausibili in presenza di conoscenza incompleta, a differenza del ragionamento deduttivo classico che è monotono.
### Circumscription

La Circumscription è un approccio più generale al ragionamento per default, introdotto per affrontare le limitazioni della CWA e modellare le eccezioni in modo più flessibile.

- **Principio**: Invece di assumere che tutti i fatti non dichiarati siano falsi, la circumscription assume che **il numero di eccezioni (rappresentate da un predicato speciale `Ab(x)`, "x è anormale") sia il più basso possibile**. Si cercano cioè i "modelli più normali" della KB, dove le eccezioni sono minimizzate.
- **Contesto**: Se una frase non è vera in tutti i modelli della KB, può essere accettabile se è vera nei modelli più normali.
- **Esempio**: Invece di dire "tutti gli uccelli volano", si dice "tutti gli uccelli normali volano": `∀x [Bird(x) ∧ ¬Ab(x) ⊃ Flies(x)]`. Se Tweety è un uccello e non si sa che sia anomalo, si conclude che vola, perché si minimizzano le anomalie.
- **Vantaggi**: È più flessibile della CWA, poiché permette di decidere quali predicati minimizzare. Consente un ragionamento più realistico, dove non tutto ciò che non è noto è falso, ma solo ciò che può essere ragionevolmente escluso come eccezione. È più prudente della CWA, ma più decisa della GCWA.
- **Formalizzazione**: A differenza della CWA che può essere simulata aggiungendo frasi negative (logica del primo ordine), la circumscription, per la sua finezza, richiede l'uso della **logica del secondo ordine**, che permette di quantificare sui predicati stessi (come `Ab`) tramite un assioma di circumscription (`τ`). Questo assioma seleziona i modelli in cui l'estensione dei predicati `Ab` è la più piccola possibile.
- **Problemi e Limiti**:
    - Può essere troppo drastica ed eliminare classi intere (es. concludere che i pinguini non esistono se sono sempre anormali per il volo).
    - **Soluzione ai problemi**: Si può distinguere tra **predicati da minimizzare** (es. `Ab`) e **predicati da mantenere fissi** (es. `Penguin`), evitando così l'esclusione di intere categorie.
    - Nonostante i miglioramenti, il metodo ha comunque dei limiti: richiede conoscenze esplicite sulle individualità (es. `Tweety ≠ Chilly`) e resta complesso decidere a priori cosa minimizzare e cosa no.