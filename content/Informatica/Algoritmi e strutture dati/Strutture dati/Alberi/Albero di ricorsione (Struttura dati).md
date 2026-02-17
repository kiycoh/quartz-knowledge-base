---
last modified: null
related:
  - '[[Equazione di ricorrenza]]'
tags:
  - algoritmi-ordinamento
  - algoritmi-greedy
  - analisi-lessicale
---
# Definizione di albero di ricorsione
Un **albero di ricorsione** è una **rappresentazione grafica** del processo di un algoritmo ricorsivo e del costo associato ad ogni sua invocazione. È un metodo potente per visualizzare e analizzare le ricorrenze, in particolare per quelle della forma $T(n) = aT(n/b) + f(n)$, dove:
- $T(n)$ è il tempo di esecuzione per un problema di dimensione $n$.
- $a$ è il numero di sottoproblemi generati da ciascuna chiamata ricorsiva.
- $n/b$ è la dimensione di ciascun sottoproblema.
- $f(n)$ rappresenta il costo delle operazioni non ricorsive: la fase di "Divide" (suddivisione del problema) e la fase di "Combina" (unione delle soluzioni dei sottoproblemi).
- Il **caso base** $T(n) = \Theta(1)$ per $n$ sufficientemente piccolo (spesso $n=1$) funge da condizione di arresto della ricorsione.

## Struttura dell'albero 
In un albero di ricorsione:
1. **Ogni nodo** contiene il **costo per la risoluzione di un singolo sottoproblema ricorsivo** in quel punto dell'esecuzione.
2. **La radice** rappresenta il problema originale di dimensione $n$ e il costo $f(n)$ delle operazioni non ricorsive a quel livello.
3. **I figli di un nodo** corrispondono ai sottoproblemi in cui il problema del nodo padre viene suddiviso. Il numero di figli è $a$, e la dimensione dei sottoproblemi è $n/b$.
4. L'albero si estende verso il basso fino a raggiungere i **nodi foglia**, che rappresentano i casi base della ricorsione (problemi di dimensione $n$ sufficientemente piccola da essere risolti in tempo costante $\Theta(1)$).

## Analisi della complessità tramite albero di ricorsione
L'obiettivo dell'analisi con un albero di ricorsione è sommare i costi di tutti i nodi per ottenere il costo totale dell'algoritmo. Questo si fa tipicamente calcolando il costo totale di ogni livello dell'albero e poi sommando i costi di tutti i livelli.

***Passi per l'analisi:***
1. **Determinare l'altezza dell'albero (numero di livelli)**: Per una ricorrenza $T(n) = aT(n/b) + f(n)$, l'altezza $h$ di un albero ricorsivo bilanciato è data da $h = \log_b n$ (escludendo il livello delle foglie). Questo rappresenta il numero di volte che l'input viene diviso per $b$ fino a raggiungere la dimensione del caso base.
2. **Calcolare il costo per ogni livello**: A ogni livello $i$ (partendo da $i=0$ per la radice), il costo totale è dato dal numero di nodi a quel livello moltiplicato per il costo di ciascun nodo a quel livello.
3. **Calcolare il numero di foglie**: Il numero di nodi al livello più profondo (le foglie) è $a^h = a^{\log_b n} = n^{\log_b a}$. Il costo totale delle foglie è questo numero moltiplicato per $\Theta(1)$.
4. **Sommare i costi di tutti i livelli**: Il tempo di esecuzione complessivo $T(n)$ è la somma dei costi di tutti i livelli, inclusi i costi dei nodi foglia. Questa somma può spesso essere espressa come una serie geometrica o un'altra forma chiusa.

Esempio Pratico: $T(n) = 3T(n/4) + \Theta(n^2)$

Consideriamo la ricorrenza $T(n) = 3T(n/4) + \Theta(n^2)$. Qui abbiamo:

- $a = 3$ (ogni problema si suddivide in 3 sottoproblemi).
- $b = 4$ (la dimensione di ciascun sottoproblema è $n/4$).
- $f(n) = \Theta(n^2)$ (il costo delle operazioni non ricorsive a ogni livello).

Visualizziamo l'albero di ricorsione:

- **Livello 0 (Radice)**:
    
    - Problema di dimensione $n$.
    - Costo: $c \cdot n^2$.
- **Livello 1**:
    
    - Vengono generati $a=3$ sottoproblemi, ciascuno di dimensione $n/b = n/4$.
    - Costo per ogni sottoproblema: $c \cdot (n/4)^2 = c \cdot n^2 / 16$.
    - Costo totale del livello: $3 \cdot c \cdot (n/4)^2 = 3/16 \cdot c \cdot n^2$.
- **Livello 2**:
    
    - Vengono generati $a^2 = 3^2 = 9$ sottoproblemi, ciascuno di dimensione $n/b^2 = n/16$.
    - Costo per ogni sottoproblema: $c \cdot (n/16)^2 = c \cdot n^2 / 256$.
    - Costo totale del livello: $9 \cdot c \cdot (n/16)^2 = 9/256 \cdot c \cdot n^2 = (3/16)^2 \cdot c \cdot n^2$.
- **Livello $i$ (generico)**:
    
    - Vengono generati $a^i = 3^i$ sottoproblemi, ciascuno di dimensione $n/b^i = n/4^i$.
    - Costo totale del livello: $3^i \cdot c \cdot (n/4^i)^2 = 3^i \cdot c \cdot n^2 / (4^i)^2 = 3^i \cdot c \cdot n^2 / 16^i = (3/16)^i \cdot c \cdot n^2$.
- **Altezza dell'albero**: L'altezza è $h = \log_b n = \log_4 n$. L'albero ha $\log_4 n + 1$ livelli (dalla radice al livello prima delle foglie).
    
- **Costo totale (somma dei livelli)**: Il costo totale dell'algoritmo è la somma dei costi di ogni livello, più il costo dei nodi foglia. La somma dei costi dai livelli $i=0$ a $h-1$ (escluse le foglie) è: $\sum_{i=0}^{\log_4 n - 1} (3/16)^i \cdot c \cdot n^2$. Questa è una serie geometrica con ragione $r = 3/16$. Poiché $|r| < 1$, la serie converge a $1/(1-r) = 1/(1 - 3/16) = 1/(13/16) = 16/13$. Quindi la somma dei costi dei livelli superiori è $c \cdot n^2 \cdot (16/13) = \Theta(n^2)$.
    
- **Costo dei nodi foglia**: Il numero di nodi foglia è $a^{\log_b n} = 3^{\log_4 n} = n^{\log_4 3}$. Poiché $\log_4 3 \approx 0.79 < 2$, il costo delle foglie, $n^{\log_4 3} \cdot \Theta(1)$, è asintoticamente inferiore al costo $\Theta(n^2)$ dei livelli superiori.
    
- **Conclusione**: Il costo dominante è quello della radice e dei livelli più vicini ad essa, che sommano a $\Theta(n^2)$. Pertanto, la soluzione asintotica della ricorrenza è $T(n) = \Theta(n^2)$.
    

### Relazione con altri Metodi di Risoluzione

L'albero di ricorsione è un metodo **grafico** che fornisce un'intuizione chiara sul comportamento della ricorrenza. Spesso, l'intuizione ottenuta dall'albero di ricorsione può essere usata per formulare un'ipotesi nel **metodo di sostituzione**, che richiede una dimostrazione formale per induzione matematica. Per ricorrenze di forma standard, il **Master Theorem** (o Metodo Principale) offre una soluzione più rapida, classificando le ricorrenze in base al confronto tra $f(n)$ e la funzione "spartiacque" $n^{\log_b a}$. L'albero di ricorsione aiuta a comprendere perché il Master Theorem funziona, mostrando visivamente il contributo relativo della radice, dei livelli intermedi e delle foglie al costo totale.