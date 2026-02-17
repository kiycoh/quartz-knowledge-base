---
last modified: 2025, 11, 24 2:11:33
tags:
  - statistica-informatica
  - statistica-descrittiva
  - distribuzione-condizionata
---

# Definizione di distribuzione marginale
La **distribuzione marginale** di una variabile è la distribuzione di frequenza (assoluta o relativa) di quella variabile quando si ignora, o si "margina", l'informazione relativa alle altre variabili presenti in una distribuzione congiunta. In pratica, permette di concentrarsi su un singolo carattere rilevato su un collettivo, come se fosse l'unica variabile di interesse, senza considerare la sua associazione con altre variabili.

**Contesto e Derivazione:** Una distribuzione marginale si ottiene a partire da una **distribuzione congiunta** (o doppia), che rappresenta l'associazione tra due o più caratteri e ne elenca le frequenze per ogni combinazione di modalità. Se si considera una tabella a doppia entrata (o tabella di contingenza) che riassume una distribuzione congiunta di due caratteri X e Y, le distribuzioni marginali si trovano nei "margini" della tabella, ovvero nelle righe e colonne che riassumono i totali per ciascuna modalità di un singolo carattere.

Formalmente:

- Per variabili discrete, la frequenza marginale di una modalità di X si ottiene sommando le frequenze congiunte su tutte le modalità di Y. Analogamente, per Y, si sommano le frequenze congiunte su tutte le modalità di X.
    - Sia $n_{ij}$ la frequenza congiunta della modalità $x_i$ di X e $y_j$ di Y.
    - La frequenza marginale per la modalità $x_i$ è $n_{i.} = \sum_{j=1}^{C} n_{ij}$.
    - La frequenza marginale per la modalità $y_j$ è $n_{.j} = \sum_{i=1}^{R} n_{ij}$.
- Per variabili continue, la distribuzione marginale di una variabile (es. X) si ricava dalla funzione di densità di probabilità congiunta $f(x,y)$ tramite integrazione rispetto all'altra variabile (Y): $f_X(x) = \int_{-\infty}^{\infty} f(x,y)dy$.

**Esempio Pratico:** Consideriamo la distribuzione congiunta (tabella a doppia entrata) di "Diploma" e "Sesso" da un campione di 50 studenti:

|Diploma \ Sesso|M|F|Totale|
|---|---|---|---|
|LC|6|9|15|
|LS|6|6|12|
|ITC|5|4|9|
|ITI|3|3|6|
|Altro|4|4|8|
|Totale|24|26|50|

- **Distribuzione marginale della variabile "Diploma"**: Si ottiene leggendo la colonna "Totale" più a destra.
    - LC: 15
    - LS: 12
    - ITC: 9
    - ITI: 6
    - Altro: 8
    - Totale: 50 Questa distribuzione mostra quanti studenti hanno ciascun tipo di diploma, indipendentemente dal loro sesso.
- **Distribuzione marginale della variabile "Sesso"**: Si ottiene leggendo la riga "Totale" più in basso.
    - M: 24
    - F: 26
    - Totale: 50 Questa distribuzione mostra la ripartizione dei sessi nel campione, indipendentemente dal tipo di diploma.

**Utilità e Importanza:** Le distribuzioni marginali sono il punto di partenza per comprendere le caratteristiche individuali di ciascuna variabile in un dataset multivariato. Esse precedono l'analisi delle **distribuzioni condizionate**, che, al contrario, esaminano la distribuzione di una variabile dato un valore specifico dell'altra. Permettono di ottenere misure di sintesi e variabilità per ogni singola variabile (come media, mediana, varianza) senza la necessità di considerare le interazioni o dipendenze con altre variabili, le quali saranno poi oggetto di studi più approfonditi (es. indipendenza in distribuzione, dipendenza in media, correlazione).