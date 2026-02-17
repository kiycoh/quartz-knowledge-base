---
last modified: 27/10/2025 18:51
related:
  - '[[Analisi algoritmica]]'
tags:
  - algoritmi-ordinamento
  - programmazione-dinamica
  - complessita-computazionale
---
==La **programmazione dinamica (DP)** è una metodologia algoritmica di progettazione che si distingue per la sua efficienza nella risoluzione di problemi di ottimizzazione, in particolare quelli che possono essere scomposti in sotto-problemi correlati.== Il suo obiettivo è trovare la soluzione migliore (massimizzando un guadagno o minimizzando un costo) tra tutte quelle possibili.

> [!IMPORTANT] DP vs Divide et impera
> La DP emerge come soluzione ai limiti della classica metodologia "[[Divide et impera]]" quando i sotto-problemi non sono indipendenti ma "dipendenti". In un approccio puramente ricorsivo, senza ottimizzazioni, ri-calcolare ripetutamente gli stessi sotto-problemi porta a uno spreco di risorse e a un'[[Complessità temporale algoritmica#Tipi di complessità temporale|inefficienza esponenziale]].

> [!EXAMPLE]- Esempio di programmazione dinamica con [[Sequenza di Fibonacci]]
> Consideriamo il calcolo dell'n-esimo numero di Fibonacci, definito da $F(n) = F(n-1) + F(n-2)$, con $F(0)=1$ e $F(1)=1$. Un'implementazione ricorsiva diretta `Fibonacci(n)`:
> 
> ```
> PROCEDURE Fibonacci(n)
> 1. If (n==1) return 1
> 2. If (n==0) return 1
> 3. Return Fibonacci(n-1) + Fibonacci(n-2)
> ```
> 
> Si notano molteplici chiamate per gli stessi valori (`F(2)` viene calcolato più volte). Questo porta a una complessità temporale di $O(2^n)$.

## Caratteristiche di un algoritmo di programmazione dinamica
Un [[Algoritmo (Informatica)]] di programmazione dinamica deve soddisfare e implementare i seguenti punti per essere efficace:
1. **Suddivisione ricorsiva:** il problema deve essere ricorsivamente suddivisibile in sotto-problemi.
2. **Calcolo unico:** ogni sotto-problema deve essere calcolato una sola volta.
3. **Struttura ausiliaria efficiente:** deve utilizzare una [[Struttura dati (Informatica teorica)|struttura dati]] ausiliaria (es. array o matrice) per memorizzare i risultati dei sotto-problemi, garantendo un accesso in tempo costante (es. `INDEX` in $O(1)$).
## Metodologie di risoluzione
Esistono due approcci principali per implementare la programmazione dinamica:
1. **Approccio Top-Down (con Memorizzazione):** Questo approccio mantiene la struttura ricorsiva, ma aggiunge un meccanismo di "memorizzazione" (annotazione) per memorizzare i risultati dei sotto-problemi già calcolati in una tabella (es. un array `R`). Prima di calcolare un sotto-problema, si verifica se il risultato è già presente nella tabella; in tal caso, lo si recupera direttamente, altrimenti lo si calcola e lo si memorizza.
    

> [!NOTE] Esempio di metodologica [[Bottom-Up]] tramite Fibonacci con memorizzazione
>    ```
>    PROCEDURE Memoized-Fibonacci(A, n)
>     1. If (n==1) return 1
>     2. If (n==0) return 1
>     3. If(A[n-1] != NIL)
>     4. a = A[n-1]
>     5. Else
>     6. a = Memoized-Fibonacci(A, n-1)
>     7. If(A[n-2] != NIL)
>     8. b = A[n-2]
>     9. Else
>     10. b = Memoized-Fibonacci(A, n-2)
>     11. A[n] = a+b // Annotazione della soluzione
>     12. Return a+b
>    ```
>     
>     L'array `A` viene inizializzato con `NIL` o `-∞` per indicare i valori non ancora calcolati. L'efficienza migliora drasticamente, passando a $O(n^2)$ per il taglio dell'asta e $O(n)$ per Fibonacci.

    
1. **Approccio Bottom-Up (Iterativo):** questa metodologia costruisce la soluzione partendo dai sotto-problemi più piccoli e noti, procedendo iterativamente verso i problemi di dimensione maggiore. Non utilizza la ricorsione, ma un ciclo che popola la tabella dei risultati in un ordine che garantisce che ogni volta che un sotto-problema è necessario, la sua soluzione sia già stata calcolata e memorizzata.
    
    **Esempio: Problema del Taglio dell'Asta (Rod Cutting)** Dato un'asta di lunghezza `n` e un array `p` di prezzi per diverse lunghezze di taglio, si vuole massimizzare il guadagno tagliando l'asta in pezzi. La relazione ricorsiva è $r_n = \max { p_j + r_{n-j} : 1 \le j \le n }$.
    
    Un algoritmo Bottom-Up per il taglio dell'asta:
    
    ```
    PROCEDURE Bottom-Up-Cut-Rod(p, n)
    1. r[0:n] nuovo array
    2. r = 0 // Caso base: asta di lunghezza 0 ha ricavo 0
    3. for i = 1 to n
    4. q = -∞
    5. for j = 1 to i
    6. q = max{q, p[j] + r[i-j]} // r[i-j] è già noto
    7. r[i] = q // Memorizza il massimo ricavo per asta di lunghezza i
    8. return r[n]
    ```
    
    Questo approccio ha una complessità temporale di $O(n^2)$.
    
### Ricostruzione della Soluzione Ottima
Spesso, oltre al valore ottimo, è necessario conoscere la sequenza di scelte che ha portato a tale soluzione. La Programmazione Dinamica permette anche questo, estendendo la procedura per memorizzare non solo il valore ottimo ma anche la "prima scelta" che ha contribuito a raggiungerlo. Questo si fa solitamente con un'ulteriore matrice `s` (ad esempio, in `s[j]` si memorizza il primo taglio da effettuare per un'asta di lunghezza `j`). La soluzione finale può essere ricostruita tramite un processo di **[[Backtracking]]**, ripercorrendo a ritroso le scelte memorizzate.

**Esempio: Ricostruzione per il Taglio dell'Asta**
```
PROCEDURE Extended-Bottom-Up-Cut-Rod(p, n) // Estende il precedente per memorizzare le scelte
1. r[0:n] nuovo array
2. s[0:n] nuovo array
3. r = 0
4. for i = 1 to n
5. q = -∞
6. for j = 1 to i
7. if(q < p[j] + r[i-j]) // Correzione: deve essere p[j] + r[i-j]
8. q = p[j] + r[i-j]
9. s[i] = j // Memorizza la lunghezza del primo pezzo tagliato
10. r[i] = q
11. return r, s

PROCEDURE Print-Cut-Rod-Solution(p, n)
1. (r,s) = Extended-Bottom-Up-Cut-Rod(p, n)
2. Stampa "Migliore Ricavo " + r[n]
3. While n > 0
4. stampa "Taglio a " + s[n]
5. n = n - s[n]
```

Per un'asta di lunghezza $n=6$ e prezzi $p = {1:1, 2:5, 3:8, 4:9, 5:10, 6:14}$, la procedura `Extended-Bottom-Up-Cut-Rod` calcola i valori `r` e `s`. Ad esempio, `s=3` indica che il primo taglio da fare per un'asta di lunghezza 6 è di lunghezza 3. Successivamente, `Print-Cut-Rod-Solution` stamperà "Taglio a 3", e ricalcolerà per la parte restante dell'asta (lunghezza $6-3=3$), ottenendo un ricavo totale di 16.

### Applicazioni della programmazione dinamica
La programmazione dinamica si applica efficacemente a una vasta gamma di problemi, molti dei quali non sono trattabili con approcci esaustivi:

1. **Problema della Moltiplicazione a Catena di Matrici (Matrix Chain Multiplication):** Dato una sequenza di matrici $A_1, A_2, \dots, A_n$, l'obiettivo è determinare l'ordine di moltiplicazione che minimizzi il numero di moltiplicazioni scalari. L'operazione di moltiplicazione matriciale è associativa, quindi l'ordine non cambia il risultato ma influenza il costo. Un esempio con tre matrici $A_1(10 \times 100), A_2(100 \times 5), A_3(5 \times 50)$ mostra che l'ordine $(A_1 \times A_2) \times A_3$ costa $7500$ moltiplicazioni scalari, mentre $A_1 \times (A_2 \times A_3)$ costa $75000$. Il numero di parentesizzazioni possibili è esponenziale (similmente al taglio dell'asta, $O(2^n)$).
    
    La soluzione DP si articola in quattro fasi:
    - **Caratterizzazione della soluzione ottima:** Se $A_{i..j}$ è una parentesizzazione ottima, allora anche le sue sottomatrici $A_{i..k}$ e $A_{k+1..j}$ devono essere ottime.
    - **Definizione ricorsiva:** Si definisce $m[i,j]$ come il costo minimo per calcolare $A_{i..j}$. La formula ricorsiva è $m[i,j] = \min_{i \le k < j} {m[i,k] + m[k+1,j] + p_{i-1}p_k p_j }$, con $m[i,i]=0$ per il caso base. $p$ rappresenta le dimensioni delle matrici.
    - **Calcolo del valore ottimo:** Si utilizzano due matrici `m` e `s` (per memorizzare il costo e la scelta ottima di `k`) riempiendole "dal basso verso l'alto e da sinistra verso destra".
    - **Costruzione della soluzione:** La matrice `s` viene usata per ricostruire la parentesizzazione ottimale tramite backtracking ricorsivo.
    
    La complessità temporale è $O(n^3)$.
    
2. **Problema della Sottosequenza Comune Massima (Longest Common Subsequence - LCS):** Date due sequenze $X$ e $Y$, si vuole trovare la sottosequenza $Z$ comune a $X$ e $Y$ che abbia la lunghezza massima. Una sottosequenza non richiede che gli elementi siano contigui, ma mantengano l'ordine. Questo problema ha applicazioni in genetica per valutare la similarità tra sequenze di DNA.
    
    L'approccio DP si basa su un teorema che definisce la struttura ricorsiva della LCS:
    
    - Se l'ultimo carattere di $X$ e $Y$ è uguale ($x_m = y_n$), allora questo carattere fa parte della LCS, e la LCS residua è quella di $X_{1..m-1}$ e $Y_{1..n-1}$.
    - Se gli ultimi caratteri sono diversi ($x_m \neq y_n$), allora la LCS è la più lunga tra la LCS di $X_{1..m-1}$ e $Y$, o la LCS di $X$ e $Y_{1..n-1}$.
    
    Si usano due matrici: `c` per memorizzare le lunghezze delle LCS dei prefissi, e `b` per tracciare le scelte (indicando se si proviene da una diagonale, su, o a sinistra). La soluzione finale $c[m,n]$ si trova nella cella in basso a destra della matrice. La ricostruzione della LCS avviene tramite backtracking ricorsivo sulla matrice `b`.
    
    La complessità temporale è $O(mn)$, dove $m$ e $n$ sono le lunghezze delle sequenze.
    

> [!NOTE] DP vs Algoritmi greedy
> La Programmazione Dinamica è distinta dagli **[[Algoritmo greedy|Algoritmi greedy]]**. Mentre la DP analizza tutti i sotto-problemi e salva le soluzioni ottime, un algoritmo Greedy fa una scelta localmente ottima ad ogni passo, sperando che questa porti a una soluzione globalmente ottima. Questa ipotesi non è sempre vera.
> 
> - **Problema di Selezione Attività (Activity Selection Problem):** un problema in cui gli algoritmi Greedy funzionano in modo ottimale. Se le attività sono ordinate per tempo di fine, la scelta avida di selezionare l'attività che termina prima e poi la successiva compatibile porta alla soluzione ottima. La complessità è $O(n)$ dopo l'ordinamento.
> - **Problema dello Zaino (Knapsack Problem):** un esempio in cui un approccio Greedy semplice (es. massimizzare il valore o il rapporto valore/volume) non garantisce la soluzione ottima. Questo problema è tipicamente risolto con la Programmazione Dinamica per trovare la soluzione globale ottimale.