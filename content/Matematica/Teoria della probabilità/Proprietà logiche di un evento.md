---
tags:
  - logica-matematica
  - teoria-probabilità
  - principi-di-inclusione-esclusione
---

# Proprietà logiche di un evento (Teoria della probabilità)
## Implicazione

L'**implicazione** ($\subseteq$) è una relazione logica.

$$
\begin{aligned}
A \subseteq B &\Rightarrow \text{ Se A è vero, B è vero} \\
A \subseteq B &\nRightarrow B \subseteq A 
\end{aligned}
$$
## Uguaglianza
Se $A \subseteq B$ e $B \subseteq A$, allora $A$ e $B$ si dicono equivalenti (uguali).

## Principio di inclusione - esclusione
Il principio di inclusione ed esclusione permette di calcolare la probabilità dell'unione di più eventi attraverso le loro intersezioni.
$$
P(E_1 \cup E_2 \cup \dots \cup E_m) = P\left(\bigcup_{\lambda=1}^{m} E_{\lambda}\right) =
\sum_{\lambda=1}^{m} P(E_{\lambda}) - \sum_{\lambda_1 < \lambda_2} P(E_{\lambda_1} E_{\lambda_2}) +
\sum_{\lambda_1 < \lambda_2 < \lambda_3} P(E_{\lambda_1} E_{\lambda_2} E_{\lambda_3}) -
\sum_{\lambda_1 < \lambda_2 < \lambda_3 < \lambda_4} P(E_{\lambda_1} E_{\lambda_2} E_{\lambda_3} E_{\lambda_4}) +
\cdots + (-1)^{k+1} \sum_{\lambda_1 < \dots < \lambda_k} P(E_{\lambda_1} E_{\lambda_2} \dots E_{\lambda_k}) +
\cdots + (-1)^{m+1} P(E_1 E_2 \dots E_m)
$$
* $\sum_{i=1}^{m} P(E_i)$: somma delle probabilità di ciascun evento;
* $\sum_{i_1<i_2} P(E_i1 E_i2)$: somma delle probabilità delle intersezioni di ogni coppia di eventi
	* a 3 a 3
	* a 1 a 1
	* ecc..

* $(-1)^{k+1} \sum_{i_1<\dots i_k} P(E_{i_1} \dots E_{i_k})$: somme delle probabilità delle intersezioni di ogni gruppo di k eventi. 
	* Il termine $(-1)^{k+1}$ determina il segno:
		* $k \text{ pari } \Rightarrow \text{ segno positivo}$
		* $k \text{ dispari } \Rightarrow \text{ segno negativo}$

* $(-1)^{m+1} P(E_1, \dots, E_m)$: intersezione di tutti gli eventi. 
	* Il termine $(-1)^{m+1}$ determina il segno: 
		* $m \text{ pari} \Rightarrow \text{ negativo}$
		* $m \text{ dispari} \Rightarrow \text{ positivo}$

Se gli eventi sono a 2 a 2 $\varnothing$ allora $P( {\Large \cup}_{i=1}^m E_i) = \sum_{i=1}^m P(E_i) + \dots + P(E_m)$
