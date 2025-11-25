---
last modified: 2025, 11, 23 19:11:17
tags:
  - machine-learning
  - intelligenza-artificiale
  - scienze-cognitive
---
# Controllo Procedurale
Il **controllo procedurale** si riferisce alla guida mirata del processo di ragionamento in un sistema di IA per renderlo più efficiente e gestibile, evitando percorsi inferenziali inutili. Data la complessità computazionale delle procedure automatiche di dimostrazione dei teoremi (come la Risoluzione in FOL), il controllo procedurale è essenziale per ottimizzare le performance, specialmente in domini complessi.

**Necessità e Obiettivi:**

- Le procedure di ragionamento generale sono computazionalmente costose.
- Conoscere la struttura del dominio può guidare il ragionamento in modo più mirato.
- Obiettivo è migliorare l'efficienza e la gestibilità del processo inferenziale.

**Strategie e Applicazioni:**

1. **Forme Logiche Orientate**:
    
    - Una strategia consiste nell'usare implicazioni unidirezionali, che limitano l'inferenza in una sola direzione.
    - Un esempio pratico è la suddivisione della base di conoscenza (KB) in "fatti" (verità di base, atomi istanziati) e "regole" (nuove relazioni, implicazioni universali). Questo permette di distinguere tra conoscenza di base e conoscenza derivabile.
2. **Definizione delle Regole e Ordine degli Obiettivi**:
    
    - La formulazione delle regole in una KB ha un impatto significativo sull'efficienza del ragionamento. Si consideri la definizione della relazione `Ancestor(x, y)` (x è antenato di y) basata su `Parent(x, y)` (x è genitore di y):
        - **Definizione 1 (Ricerca Discendente/Dall'alto verso il basso)**: `Parent(x, y) ⊃ Ancestor(x, y)` e `Parent(x, z) $\land$ Ancestor(z, y) ⊃ Ancestor(x, y)`. Per dimostrare `Ancestor(a, e)`, si cerca un figlio `b` di `a` (`Parent(a,b)`) e poi si verifica se `b` è antenato di `e` (`Ancestor(b,e)`). Questa soluzione è efficiente se ogni individuo nella catena ha pochi figli, e la sua complessità dipende dalla profondità dell'albero.
        - **Definizione 2 (Ricerca Ascendente/Dal basso verso l'alto)**: `Parent(x, y) ⊃ Ancestor(x, y)` e `Ancestor(x, z) $\land$ Parent(z, y) ⊃ Ancestor(x, y)`. Per dimostrare `Ancestor(a, e)`, si risale l'albero partendo da `e`: si cerca un genitore `d` di `e` (`Parent(d,e)`) e poi si controlla se `a` è antenato di `d` (`Ancestor(a,d)`). Questa soluzione è più efficiente della prima se ogni individuo ha molti figli (rispetto a pochi genitori).
        - **Definizione 3 (Ricerca Bidirezionale/Mista)**: `Parent(x, y) ⊃ Ancestor(x, y)` e `Ancestor(x, z) $\land$ Ancestor(z, y) ⊃ Ancestor(x, y)`. Questa opzione suggerisce una ricerca in entrambe le direzioni contemporaneamente.
    - L'**ordine degli obiettivi** nella concatenazione all'indietro (backward chaining) è logicamente irrilevante, ma può influenzare drasticamente l'efficienza computazionale. Ad esempio, per dimostrare `AmericanCusin(x)` dalla regola `America(x) $\land$ Cusin(x) ⊃ AmericanCusin(x)`, se si valuta prima `America(x)` si potrebbe dover iterare su milioni di americani per trovare il cugino, mentre valutando prima `Cusin(x)` si itererebbe su un numero molto minore di cugini, rendendo la ricerca più efficiente.

**Ruolo nel [[Backward Chaining]]**: Il controllo procedurale è cruciale per mitigare gli svantaggi del backward chaining, come il rischio di cicli infiniti (specialmente con tautologie) e l'inefficienza dovuta alla ripetizione di ricerche per gli stessi obiettivi. Le considerazioni sul controllo procedurale sono quindi necessarie per evitare "tranelli" e rendere il backward chaining utilizzabile in pratica.