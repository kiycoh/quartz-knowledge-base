---
last modified: 24/10/2025 02:56
related:
  - '[[Famiglia esponenziale (Statistica)]]'
tags:
  - statistica
  - famiglia-esponenziale
  - statistica-descrittiva
---
# Definizione di Famiglia esponenziale naturale (NEF)
La **Famiglia esponenziale** è un concetto fondamentale in statistica che raggruppa una vasta classe di distribuzioni di probabilità, sia discrete che continue, accomunate da una specifica forma matematica.

> [!IMPORTANT] Forma canonica standard della formuila utilizzata nel contesto dei [[Modello lineare generalizzato (GLM)]]
> La **Famiglia esponenziale naturale (NEF)**: una variabile casuale $Y$ appartiene a questa famiglia se la sua funzione di densità (o di probabilità) può essere scritta nella forma:
> $$f(y|\theta, \phi) = \exp { \frac{y\theta - b(\theta)}{a(\phi)} + c(y, \phi)}$$
> 
> dove:
> - $\theta$ è il **parametro naturale (o canonico)**, che determina la forma della distribuzione ed è legato al valore atteso $\mu$.
> - $\phi$ è il **parametro di dispersione**, che controlla la varianza della distribuzione e influenza la varianza.
> - $a(\phi)$, $b(\theta)$, e $c(y, \phi)$ sono funzioni specifiche. $a(\phi)$ è spesso della forma $\phi/w$, dove $w$ è un peso noto. $b(\theta)$ è la funzione cumulante (o di normalizzazione), che garantisce che la densità integri a 1 e fornisce informazioni sul valore atteso e la varianza di $Y$.
