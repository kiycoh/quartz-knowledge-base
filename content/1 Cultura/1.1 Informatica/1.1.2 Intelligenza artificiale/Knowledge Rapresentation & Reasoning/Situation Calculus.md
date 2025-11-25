---
last modified: 24/10/2025 14:02
related:
  - '[[Frame Problem]]'
tags:
  - situation-calculus
  - frame-problem
  - logica-primo-ordine
---
# Definizione di Situation Calculus
Il **Situation Calculus** è una variante della logica del primo ordine (FOL) specificamente progettata per rappresentare e ragionare su un mondo che cambia nel tempo, distinguendosi dalla revisione delle credenze che modifica le credenze del sistema.

### Componenti Fondamentali

Il Situation Calculus tratta azioni e situazioni come oggetti nel dominio:

- **Azioni**: Rappresentano eventi che modificano lo stato del mondo, come `jump`, `kick(x)` o `put(r,x,y)`. Sono contestuali all'applicazione.
- **Situazioni**: Denotano sequenze di azioni o "storie del mondo". `S0` è la situazione iniziale. `do(a, s)` rappresenta la nuova situazione che si ottiene eseguendo l'azione `a` nella situazione `s`. L'ordine delle azioni è rilevante (es. `do(pickup(b2), do(pickup(b1), S0))` è diversa da `do(pickup(b1), do(pickup(b2), S0))`).
- **Fluenti**: Sono predicati o funzioni il cui valore può variare tra le situazioni. Descrivono ciò che è vero in una data situazione, con la situazione sempre come ultimo argomento (es. `Holding(r, x, s)` indica che il robot `r` tiene l'oggetto `x` nella situazione `s`). Nel Situation Calculus, non esiste una situazione "attuale" fissa, e le formule possono riferirsi a situazioni passate, presenti o future.
- **`Poss(a, s)`**: Un predicato speciale che indica se un'azione `a` può essere eseguita in una situazione `s`.

### Rappresentazione del Cambiamento

Per modellare i cambiamenti, il Situation Calculus utilizza diversi tipi di assiomi:

1. **Assiomi di Precondizione**: Specificano le condizioni che devono essere vere affinché un'azione possa essere eseguita. Sono espressioni della forma `Poss(Azione, Situazione) ≡ Condizioni`.
2. **Assiomi di Effetto**: Descrivono come le azioni modificano i fluenti. Possono essere positivi (rendono un fluente vero) o negativi (lo rendono falso). Hanno forme come `F(argomenti, do(Azione, Situazione))` o `Poss(Azione, S) ⊃ F(argomenti, do(Azione, S))`.
3. **Assiomi di Frame**: Delineano ciò che _non_ cambia quando un'azione viene eseguita, specificando gli effetti nulli delle azioni sui fluenti non direttamente modificati.

* Il [[Frame Problem]] e la sua Soluzione

