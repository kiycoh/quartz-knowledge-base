---
last modified: 2025, 11, 24 16:11:47
tags:
  - intelligenza-artificiale
  - ragionamento-deduttivo
  - ragionamento-non-monotono
---
# Definizione di Ragionamento

Il **ragionamento** è il processo di manipolazione di simboli che rappresentano la conoscenza, al fine di dedurre nuove informazioni o prendere decisioni. È un componente fondamentale per i sistemi di Intelligenza Artificiale (IA) in quanto permette di spiegare e prevedere il comportamento di un agente intelligente, consentendo decisioni basate sulle informazioni disponibili piuttosto che mere reazioni a input predefiniti.

Esistono diverse forme di ragionamento:

1. **[[Ragionamento deduttivo (KRR)]]**:
2. **[[Ragionamento non-monotono (KRR)]] **:
3. **[[Ragionamento Abduttivo (KRR)]]**:
4. **Ragionamento sulle Azioni e Pianificazione ([[Situation Calculus]])**:
    - **Definizione**: Una variante della FOL che rappresenta azioni e situazioni come oggetti, utile per modellare un mondo che cambia nel tempo. Utilizza "fluendi" per descrivere cosa è vero in una situazione specifica.
    - **Assiomi**: Richiede assiomi di precondizione (quando un'azione è possibile) e di effetto (cosa cambia dopo un'azione).
    - **Frame Problem**: Il problema di dover specificare esplicitamente tutti gli assiomi di frame, che indicano cosa *non* cambia a seguito di un'azione. Questo porta a un numero enorme di assiomi.
    - **Soluzione al Frame Problem**: Si mira a generare automaticamente gli assiomi di frame dagli assiomi di effetto, utilizzando assiomi di chiusura esplicativa e assiomi di stato successivo, che unificano gli effetti positivi e negativi di un fluente in un'unica formula compatta.
    - **Compiti**: Proiezione (cosa sarà vero dopo una sequenza di azioni) e verifica di legalità (se una sequenza di azioni può essere eseguita).

## Definizione e Approfondimento del [[Controllo Procedurale]]

