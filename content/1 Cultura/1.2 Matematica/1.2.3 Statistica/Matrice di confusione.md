---
tags:
  - machine-learning
  - classificazione-statistica
  - matrice-di-confusione
---

# Definizione di matrice di confusione
==La **matrice di confusione** è una **tabella** che visualizza le **prestazioni** di un modello di classificazione,== confrontando le **classi vere** con quelle **previste**, capendo *dove* il modello commette errori. 

Supponiamo di avere un **problema di classificazione binaria**, cioè con **due classi**: **positivo** (1) e **negativo** (0):

|                   | Predetto Positivo | Predetto Negativo |
| ----------------- | ----------------- | ----------------- |
| **Vero positivo** | TP                | FN                |
| **Vero negativo** | FP                | TN                |
* Le righe della matrice rappresentano le **classi reali (o effettive)**;
* le colonne rappresentano le **classi predette dal modello**.

> [!NOTE] Significato dei termini:
> - **Veri Positivi (TP - True Positives):** Casi in cui il modello ha predetto correttamente la classe Positiva.
> - **Veri Negativi (TN - True Negatives):** Casi in cui il modello ha predetto correttamente la classe Negativa.
> - **Falsi Positivi (FP - False Positives):** Casi in cui il modello ha predetto la classe Positiva, ma la classe reale era Negativa (Errore di Tipo I). Esempio: un'email non spam classificata come spam.
> - **Falsi Negativi (FN - False Negatives):** Casi in cui il modello ha predetto la classe Negativa, ma la classe reale era Positiva (Errore di Tipo II). Esempio: un paziente malato diagnosticato come sano.

# Utilizzare la matrice di confusione
La *matrice di confusione* non è solo una tabella di conteggi, ma la base per calcolare metriche di valutazione più sofisticate e informative rispetto alla semplice accuratezza:

- **Accuratezza ([[Accuratezza statistica]]):** $\frac{TP + TN}{TP + TN + FP + FN}$    
    - Proporzione di predizioni corrette sul totale. Può essere fuorviante in caso di dataset sbilanciati (cioè, con molte più istanze di una classe rispetto all'altra).
- **Precisione (Precision o Positive Predictive Value):** TP / (TP + FP)
    - Di tutti i casi che il modello ha predetto come Positivi, quanti erano effettivamente Positivi? Utile quando il costo dei Falsi Positivi è alto (es. marcare email importanti come spam).
- **Sensibilità (Recall o True Positive Rate, TPR):** TP / (TP + FN)
    - Di tutti i casi che erano realmente Positivi, quanti ne ha identificati correttamente il modello? Utile quando il costo dei Falsi Negativi è alto (es. mancare una diagnosi di malattia grave).
        
- **Specificità (Specificity o True Negative Rate, TNR):** TN / (TN + FP)
    - Di tutti i casi che erano realmente Negativi, quanti ne ha identificati correttamente il modello?
- **F1-Score:** 2 * (Precisione * Sensibilità) / (Precisione + Sensibilità)
    - Media armonica di Precisione e Sensibilità, utile per bilanciare le due metriche.