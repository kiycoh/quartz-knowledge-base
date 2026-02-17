---
last modified: 2025-05-02T17:34:00.000Z
related:
  - '[[Regressione lineare]]'
tags:
  - statistical-relation
  - dependent-variable
  - independent-variable
---
# Definizione di relazione statistica
Una **relazione statistica** si verifica quando **i valori di una [[Variabile statistica|variabile]] dipendono in qualche modo dai valori di un’altra variabile**. In altre parole esiste una correlazione tra comportamento di una variabile e l'altra in quanto il valore di $X$ influenza $Y$. Il risultato è una tendenza (che comprende un termine di errore) il più vicino possibile ai veri valori di $Y$.

> La *relazione statistica* si distingue dalla [[Relazione deterministica|relazione deterministica]] (che ha dipendenza "perfetta") per via della [[#Variabilità|variabilità (o rumore)]].

$$
Y = \underbrace{f(X;\theta)}_{\text{Componente deterministica}} + \underbrace{\varepsilon}_{\text{Componente stocastica}}
$$ 
* $Y$ è la **variabile risposta** (quella che vogliamo **prevedere**).
* $f$ è una qualsiasi funzione di $X$
* $\theta$ sono i parametri che caratterizzano $f$
* **$\varepsilon$** (epsilon) è il **termine di errore**: rappresenta **le variazioni casuali** o **fattori non spiegati dal modello**.
## Variabili dipendenti e indipendenti
Quando si analizza una relazione tra due variabili, si cerca di capire **se e come una variabile influenza un’altra**. Riconosciamo: 

- **Variabile indipendente (o esplicativa)  ($X$)**:
  - È la variabile che **spiega** o **predice**.
  - Viene **manipolata o osservata** per vedere l’effetto sull’altra variabile.

- **Variabile dipendente (o di risposta) ($Y$)**:
  - È la variabile che **risponde** o **dipende** dalla X.
  - È quella che si vuole **prevedere** o **studiare**.

> [!EXAMPLE] Esempi
> | Dose (X) | Riduzione febbre (Y) |
> |----------|----------------------|
> | 0        | 0.1°C                |
> | 1        | 0.8°C                |
> | 2        | 1.5°C                |
> | 3        | 2.0°C                |
> 
> Dove **X = dose del farmaco** (variabile esplicativa) e **Y = riduzione della febbre** (variabile risposta).
> 
> *Altri esempi:*
> * Il numero di bambini che soffre d’asma; 
> * Il livello di inquinamento dell’aria;
> * La probabilità di sviluppare un cancro e il numero di sigarette fumate in un giorno.

