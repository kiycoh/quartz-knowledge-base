---
last modified: 24/10/2025 14:02
tags:
  - logica-classica
  - risoluzione
  - backward-chaining
---
- **Definizione**: Partendo da una base di conoscenza (KB) contenente affermazioni esplicite, si derivano altre informazioni implicite. Questo approccio è tipico della logica classica, delle logiche descrittive e dei sistemi procedurali. In un sistema basato sulla conoscenza, il compito principale è calcolare le implicazioni della KB. Un sistema di ragionamento deduttivo è considerato "corretto" se produce solo affermazioni logicamente garantite e "completo" se è in grado di derivare tutte le conseguenze logiche della KB.
    - **Strumenti e Limiti**:
        - **Logica del Primo Ordine (FOL)**: Fornisce un quadro formale per esprimere e manipolare la conoscenza. Sebbene potente, il ragionamento in FOL può essere computazionalmente intrattabile, e il problema della validità è indecidibile. Non esiste una procedura computazionale che possa sempre determinare se una formula è logicamente conseguente da una KB. Inoltre, la FOL è corretta ma non può essere contemporaneamente completa se è sufficientemente espressiva da includere l'aritmetica, come dimostrato dai teoremi di incompletezza di Gödel.
        - **Risoluzione**: Una procedura per determinare la soddisfacibilità di insiemi di clausole. Richiede che le formule siano convertite in Forma Normale Congiuntiva (CNF). La risoluzione per refutazione dimostra che KB $\models$ $\alpha$ se KB $\cup$ {$\neg \alpha$} è insoddisfacibile.
        - **Clausole di Horn**: Un sottoinsieme della FOL in cui la Risoluzione diventa più efficiente.
        - **Derivazione SLD**: Un tipo di derivazione per Risoluzione, particolarmente rilevante per le clausole di Horn.
        - **Backward Chaining**: Una procedura SLD che parte da un obiettivo da dimostrare e risale a ritroso nella KB. Caratteristiche: "left-to-right" (ordina gli obiettivi), "backward chaining" (parte dagli obiettivi), "depth-first" (approfondisce una linea di deduzione). Tuttavia, presenta svantaggi come il rischio di cicli infiniti e inefficienza.
        - **Forward Chaining**: Una procedura deduttiva che parte dai fatti noti e applica iterativamente le regole per derivare nuove conclusioni. È completa ed efficiente per le clausole di Horn, con terminazione garantita e implementabile in tempo lineare.