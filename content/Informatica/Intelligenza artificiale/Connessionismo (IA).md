---
last modified: 2025, 11, 25 18:11:26
related:
  - '[[Connessionismo (Psicologia)]]'
tags: [connessionismo-ia, intelligenza-artificiale, reti-neurali]
---
> [!WARNING]- IA Connessionista *vs* IA Simbolica
> Immagina di dover insegnare a distinguere un gatto da un cane:
> - **Approccio [[Simbolismo|simbolico]]:** Creeresti una [[base di conoscenza]] con regole come: "Se ha baffi lunghi E fa le fusa ALLORA è un gatto"; "Se abbaia E scodinzola ALLORA è un cane".
> - **Approccio Connessionista:** Mostreresti alla rete migliaia di foto di gatti e cani, e lei "imparerebbe" da sola le caratteristiche distintive, anche quelle che tu non sapresti descrivere a parole facilmente.
>
> | Caratteristica         | IA Simbolica (GOFAI)                                  | IA Connessionista                                      |
| :--------------------- | :---------------------------------------------------- | :----------------------------------------------------- |
| **Ispirazione** | Logica formale, filosofia della mente, linguistica    | Neuroscienze, struttura del cervello                   |
| **Unità base** | Simboli, regole, fatti (es. "Socrate è un uomo")      | Neuroni artificiali, pesi delle connessioni           |
| **Rappresentazione della conoscenza** | Esplicita, strutturata (es. alberi logici, reti semantiche) | Distribuita, implicita nei pesi delle connessioni     |
| **Processo decisionale** | Inferenza logica, ricerca attraverso spazi di stati | Propagazione di attivazioni attraverso la rete        |
| **Apprendimento** | Principalmente basato su regole predefinite, aggiunta di nuova conoscenza simbolica | Apprendimento dai dati (es. backpropagation), aggiustamento dei pesi |
| **Trasparenza** | Generalmente alta ("**[[White box]]**"), i passaggi logici sono tracciabili | Generalmente bassa ("**[[Black box]]**"), difficile interpretare i pesi |
| **Gestione dell'incertezza e del rumore** | Può essere difficile, richiede logiche specializzate (es. logica fuzzy) | Generalmente più robusta, intrinsecamente capace di gestire dati rumorosi |
| **Necessità di dati** | Meno dipendente da grandi dataset per l'apprendimento di base (più dalla conoscenza pre-programmata) | **Richiede grandi quantità di dati per l'addestramento** |
| **Esempi di task** | Sistemi esperti, problem solving, pianificazione, comprensione del linguaggio naturale (inizialmente) | Riconoscimento di pattern (immagini, voce), traduzione automatica, veicoli a guida autonoma |
| **Punti di forza** | Ragionamento esplicito, spiegabilità, gestione di conoscenza astratta | Apprendimento da dati complessi, robustezza al rumore, generalizzazione |
| **Debolezze** | Fragilità di fronte a input imprevisti, difficoltà ad apprendere da dati grezzi, "collo di bottiglia della conoscenza" (difficoltà a codificare tutta la conoscenza umana) | Opacità, necessità di grandi dataset, a volte può dare risposte "strane" o inaspettate |

# Definizione di Connessionismo (IA)
Il **Connessionismo** è un approccio all'[[Intelligenza artificiale]] che propone un nuovo modello per la costruzione e programmazione hardware e software atti a iper-semplificare il funzionamento del cervello biologico. ==Il principio connessionista centrale è che i fenomeni mentali possono essere descritti da reti interconnesse di [[Neurone artificiale|unità semplici]]== e spesso uniformi.

I suoi punti fondamentali sono:
* Basato su [[Rete neurale artificiale|reti neurali artificiali]] che si ispirano alla struttura e al funzionamento del cervello umano.
* La memoria e l'apprendimento emergono in modo automatico dall'addestramento della rete modificando i "pesi" delle connessioni tra le unità neurali, generalmente rappresentate come una [[Matrice (Matematica)|matrice]] $n×m$. 
	* I pesi vengono regolati in base a una [regola di apprendimento](https://en.wikipedia.org/wiki/Learning_rule "Learning rule") o a un algoritmo come come [l'apprendimento hebbiano](https://en.wikipedia.org/wiki/Hebbian_theory "Hebbian theory"). **No regole predefinite.**
* L'informazione è distribuita in tutta la rete.

> Molti sistemi moderni combinano elementi simbolici e connessionisti, utilizzando reti neurali per l'apprendimento e modelli simbolici per la spiegazione e il ragionamento ad esempio integrando deep learning con [[Base di conoscenza|basi di conoscenza strutturate]].