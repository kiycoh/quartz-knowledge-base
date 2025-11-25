---
tags:
  - machine-learning
  - k-nearest-neighbors
  - regression
---

Il **K-Nearest Neighbors (KNN)** è un **metodo non parametrico estremamente semplice e intuitivo** per l'**apprendimento supervisionato**, applicabile sia alla **classificazione** che alla **regressione** [Query]. La sua forza risiede nella capacità di operare senza fare assunzioni preliminari sulla distribuzione sottostante dei dati, distinguendosi così dai modelli parametrici.

L'essenza del KNN si fonda sul principio che le osservazioni simili esistono in prossimità l'una dell'altra in uno spazio di caratteristiche. Per classificare o prevedere il valore di un nuovo punto di dati, il KNN esamina i **'k' punti di dati più vicini** nel set di training [Query, 238].

**Processo e Applicazioni:**

1. **Identificazione dei vicini**: Quando si presenta un nuovo punto (detto "istanza di test") da classificare o per il quale si vuole prevedere un valore, il KNN calcola la sua **distanza** rispetto a tutti i punti presenti nel **set di training**. La **distanza euclidea** è una metrica comune per questo calcolo.
2. **Selezione dei 'k' più vicini**: Vengono poi identificati i **'k' punti nel training set che presentano la distanza minore** dall'istanza di test [Query, 157, 238]. Il valore di 'k' è un iperparametro che deve essere scelto dall'utente.
3. **Classificazione**:
    - Se utilizzato per la classificazione, il nuovo punto viene assegnato alla **classe che è più frequentemente rappresentata tra i suoi 'k' vicini**. Questo meccanismo è assimilabile a un "voto di maggioranza".
    - È stato suggerito che un **classificatore k-nearest neighbor** è strettamente correlato a un **classificatore di Bayes** che utilizza stime di densità del kernel per dati continui.
    - Un approccio "t-nearest neighbor" può essere applicato dopo la proiezione dei dati lungo una direzione discriminante (ad esempio, derivata dall'analisi discriminante), dove viene riportata l'etichetta dominante tra i _t_ punti più vicini. Il KNN può essere utilizzato anche come passo successivo ad altre tecniche di pre-elaborazione, come la **Linear Discriminant Analysis (LDA)**, per la classificazione.
4. **Regressione**:
    - Nel caso della regressione, il valore della variabile risposta (regressand) per il nuovo punto viene calcolato come la **media dei valori delle variabili risposta dei suoi 'k' vicini**. Questo è ciò che un **regressore k-nearest neighbor** produce come output.

**Generalizzazione tramite Stima della Densità del Kernel (KDE):**

Un'interpretazione più sofisticata estende il KNN attraverso la **Stimazione della Densità del Kernel (KDE)**. Un **regressore k-nearest neighbor** può essere visto come una **versione generalizzata** in cui una **funzione kernel**, derivata dalla KDE con una specifica **ampiezza di banda (_h_)**, è utilizzata per ponderare il contributo dei punti vicini. In questo modello generalizzato, l'**ampiezza di banda _h_ gioca un ruolo simile a quello del numero di vicini _k_**.

La KDE è un **metodo non parametrico** fondamentale per la **ricostruzione di distribuzioni di probabilità**. Non richiede assunzioni predefinite sulla forma della distribuzione dei dati. Il suo principio consiste nel sostituire ogni punto di dati con un "**bump**" (o kernel) liscio, centrato su quel punto, e nell'aggregare questi "bump" per formare una stima continua della densità. Questo approccio permette di modellare distribuzioni di **forma arbitraria**.

La scelta dell'ampiezza di banda _h_ in KDE è cruciale e riflette il **trade-off bias-varianza**:

- **Valori piccoli di _h_** producono stime con **alta varianza** ma basso bias, tendendo a catturare troppo rumore e potenzialmente causando **overfitting** ai dati di training.
- **Valori grandi di _h_** generano stime con **alto bias** ma bassa varianza, che possono **sovrassimplificare** la struttura sottostante della distribuzione.

La funzione di predizione della regressione kernel è una versione generalizzata della regressione k-nearest neighbor, che si basa sulla similarità tra i dati di training e tra i dati di training e test.

**Altri Contesti del Concetto di "Vicino più Prossimo":**

Il principio del "vicino più prossimo" si estende anche oltre la classificazione e la regressione diretta. Ad esempio, può essere utilizzato per calcolare un punteggio di **"outlierness"** per un punto, misurando la sua distanza euclidea dal suo vicino più prossimo, indicando quanto un'osservazione devia dalle altre.

In sintesi, il KNN è un algoritmo versatile e robusto grazie alla sua natura **non parametrica**, che lo rende applicabile in contesti dove le ipotesi distributive sono difficili o impossibili da fare. La sua efficacia pratica, sia in forma base che generalizzata tramite le funzioni kernel, lo rende uno strumento prezioso in vari ambiti dell'analisi dei dati e del machine learning.