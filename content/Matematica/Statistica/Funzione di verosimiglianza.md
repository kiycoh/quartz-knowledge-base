---
last modified: 2025-06-02T17:30:00.000Z
related:
  - '[[Stimatore di massima verosimiglianza]]'
tags:
  - machine-learning
  - statistical-inference
  - likelihood-function
---
# Definizione di funzione di verosimiglianza
La **funzione di verosimiglianza** (in inglese **likelihood function**) è una funzione di [[Probabilità condizionata]] che può essere pensata come uno strumento di un'[[indagine statistica]]: misura **quanto è probabile osservare un certo insieme di dati**, dato un modello con dei parametri.

In altre parole per un dato campione osservato $x = (x1, \dots, x_n)$, la funzione di verosimiglianza associa a ogni possibile valore di $\theta$ la probabilità (o densità) di osservare quel campione.

> [!IMPORTANT] Formula dello stimatore di massima verosimiglianza
> 
> $$
> L(\theta) = \prod_{i=1}^{n} f(x_i; \theta), \quad \text{(Con osservazioni indipendenti)}
> $$
> dove:
> - $f(x_i; \theta)$ è la funzione di densità (o massa di probabilità) per il dato $x_i$
> - $\theta$ è il vettore dei parametri da stimare
> - La produttoria $\prod$ indica che le osservazioni che stiamo moltiplicando **sono indipendenti**.
## Funzione di log-verosimiglianza
La **funzione di log-verosimiglianza** è *preferita rispetto alla standard per semplificare la massimizzazione* e si usa per stimare $\theta$ tramite il metodo della **massima verosimiglianza (MLE)**.
$$
\ell(\theta) = \log L(\theta) = \sum_{i=1}^{n} \log f(x_i; \theta)
$$
## Stima di massima verosimiglianza
È il **valore di $\theta$** che massimizza la funzione di verosimiglianza.
$$
\hat{\theta} = \arg\max_{\theta} L(\theta)

$$

> [!EXAMPLE]- Esempio
> Hai lanciato una moneta 10 volte e hai ottenuto:
> - 7 teste
> - 3 croci
> 
> Vuoi stimare la probabilità $p$ di ottenere testa.
> 1. Modello: ogni lancio è una **[[Variabile aleatoria di Bernoulli|Bernoulli]]** (testa=1, croce=0)
> 2. La verosimiglianza è:
> 
> $$
> L(p) = p^7 (1-p)^3
> $$
> 
> 3. Vuoi trovare il valore di $p$ che **massimizza** questa funzione.
> 
> Per farlo, puoi [[Derivata di funzione (Analisi matematica)|derivare]] $\log L(p) = 7\log(p) + 3\log(1-p)$ e risolvere l'equazione per trovare il massimo.
> 
> Risultato: $\hat{p} = \frac{7}{10} = 0.7$ (quindi la stima di massima verosimiglianza è 0.7)