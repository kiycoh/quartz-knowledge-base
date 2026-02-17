---
last modified: 2025, 11, 24 22:11:24
related:
  - '[[Machine learning]]'
tags: [anomaly-detection, machine-learning, one-class-classification]
---
# Definizione di One-Class Classification
**One Class Classification (OCC)** è una tecnica di Apprendimento automatico usata quando **abbiamo dati solo di una classe**, e vogliamo costruire un modello che riconosca se un nuovo dato **appartiene o meno a quella classe**.

In altre parole, il modello **impara solo da esempi positivi**, e poi cerca di capire se un nuovo esempio è simile a quelli visti prima (quindi "normale") o è diverso (quindi "anomalo").

> [!NOTE] Come funziona?
> Il modello cerca di **imparare il "confine"** che racchiude tutti i dati normali. Se un nuovo dato cade **fuori da questo confine**, viene considerato anomalo.
## Quando usarlo?
È utile in situazioni dove:
- Abbiamo **molti esempi di una sola classe** e pochi o nessun esempio delle altre classi.
- Vogliamo **rilevare anomalie** o comportamenti sospetti.

> [!TIP] Algoritmi comuni
> - **One-Class SVM (Support Vector Machine)**: costruisce un "muro" (iperpiano) che separa i dati normali dal resto dello spazio.
> - **Autoencoder**: è una rete neurale che cerca di **ricostruire i dati normali**: se non riesce a ricostruire bene un nuovo dato, vuol dire che è anomalo. 
>- **Isolation Forest**: costruisce [[Decision tree|alberi decisionali]] che "isolano" punti: gli outlier si isolano più facilmente.
>- [[One-Class Support Vector Data Descriptor]]: serve a costruire un confine che racchiuda i **dati normali** e a identificare tutto ciò che sta **fuori** da questo confine come **anomalo**.

