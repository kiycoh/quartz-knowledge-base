---
last modified: 24/10/2025 14:02
related:
  - '[[Ragionamento non-monotono (KRR)]]'
tags:
  - closed-world-assumption
  - krr
  - non-monotonic-reasoning
---


# Definizione di Closed World Assumption (CWA)
La Closed World Assumption (CWA) è un approccio fondamentale al **[[Ragionamento non-monotono (KRR)]]**, che permette di trarre conclusioni plausibili in presenza di conoscenza incompleta, a differenza del [[Ragionamento deduttivo]] classico che è monotono.

La Closed World Assumption (Assunzione del Mondo Chiuso) è la forma più semplice di ragionamento per default.

- **Principio**: Si basa sull'idea che, quando si rappresentano fatti sul mondo, ci si aspetta che solo una piccola parte delle possibili affermazioni atomiche sia vera. Pertanto, **si assume che tutte le frasi atomiche non dichiarate esplicitamente nella base di conoscenza (KB) siano false**.
- **Applicazioni**: Questa convenzione è usata in contesti come enciclopedie, dizionari, mappe e banche dati informatiche, dove l'assenza di un'informazione implica la sua inesistenza o falsità.
- **Formalizzazione**: Si introduce una nuova forma di conseguenza logica (`KB ⊨C α`) che è definita come `KB+ ⊨ α`. `KB+` è la KB originale arricchita con le negazioni (`¬p`) di tutte le frasi atomiche `p` che non possono essere dimostrate dalla KB stessa.
- **Effetto**: La CWA rende la KB **completa**, nel senso che per ogni frase atomica, la KB estesa (`KB+`) può determinarne la verità o falsità. Ciò permette una valutazione diretta e ricorsiva delle query.
- **Problemi**: La CWA può portare a **incoerenze** se la KB contiene disgiunzioni positive (es. `p ∨ q`). In tal caso, assumere la falsità di `p` e `q` porta a una contraddizione con la disgiunzione stessa.
- **Soluzione parziale**: La Generalized Closed World Assumption (GCWA) è una versione più cauta che mantiene la consistenza anche con le disgiunzioni, assumendo falso un atomo solo se la sua assenza non compromette altre disgiunzioni implicate dalla KB.
- **Quantificatori**: Per gestire le frasi con quantificatori, la CWA richiede un'assunzione più forte, la **Chiusura del Dominio**, che postula che gli unici individui esistenti siano quelli esplicitamente nominati nella KB.