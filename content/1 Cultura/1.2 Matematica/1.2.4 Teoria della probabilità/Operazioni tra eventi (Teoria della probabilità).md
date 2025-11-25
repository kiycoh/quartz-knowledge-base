---
tags:
  - algebra-relazionale
  - algoritmi-ordinamento
  - statistica-inferenziale
---

# Operazioni (Teoria della probabilità)
## Negazione 
La **negazione** ($\neg$), o evento contrario, è l'evento che è vero quando $E$ è falso e viceversa.  È un operazione unaria.

$$
\begin{aligned}
\text{Dato }E^C=1-|E| \\
\ \\
|E^C| = 
\begin{cases}
1 \text{ se } |E|=0 \\
0 \text{ se } |E|=1 \\
\end{cases}
\end{aligned}
$$

### Proprietà
* $(E^C)^C = E$


## Unione
L'**unione** ($\cup$, $\vee$ o $\text{OR}$ logico )
$A \cup B = A \vee B \Rightarrow \text{Vero}$ quando almeno uno dei due eventi è vero. Implica "Falso" quando sia $A$ che $B$ sono falsi.

L'unione tra due eventi è anch'essa un evento (operazione binaria).

| $\|A\|$ | $\|B\|$ | $\|A \cup B\|$ |
| ------- | ------- | -------------- |
| 1       | 1       | 1              |
| 1       | 0       | 1              |
| 0       | 1       | 1              |
| 0       | 0       | 0              |
### Proprietà
* $(A \cup B) \cup C = A \cup(B \cup C) = A \cup B \cup C$
* $A \cup B = B \cup A$
* $A \cup \Omega = \Omega$
* $A \cup \varnothing = A$
* $A \cup A^C = \Omega$
* Proprietà distributiva rispetto all'intersezione: $C \cup (A \cup B) = (C \cup A) \cup (C \cup B)$

## Intersezione
L'**intersezione** ($\wedge$, $\cap$ o $\text{AND}$ logico) è un'operazione binaria.
$A \cap B = A \wedge B \Rightarrow \text{Vero}$ quando entrambi gli eventi sono veri. Implica "Falso" se almeno uno dei due eventi è "Falso".


| $\|A\|$ | $\|B\|$ | $\|A \cap B\|$ |
| ------- | ------- | -------------- |
| 1       | 1       | 1              |
| 1       | 0       | 0              |
| 0       | 1       | 0              |
| 0       | 0       | 0              |

### Proprietà
* $(A \cap B) \cap C = A \cap (B \cap C) = A \cap B \cap C$
* $A \cap B = B \cap A$
* $A \cap A = A$
* $A \cap A^C = \varnothing$
* $A \cap \Omega = A$
* $A \cap \varnothing = \varnothing$
* Proprietà distributiva rispetto all'unione: $C \cup (A \cup B) = (C \cup A) \cap (C \cup B) = CA \cup CB$

# Incompatibilità
Due eventi $A$ e $B$ si dicono incompatibili se non si possono verificare contemporaneamente.
$$
AA^C = \varnothing
$$
