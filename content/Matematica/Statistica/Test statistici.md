---
tags:
  - statistica-inferenziale
  - statistica-descrittiva
  - test-statistici
---

# Definizione di test statistico
![[Pasted image 20250414194619.png]]
###  Test sulle medie
Quando analizzi variabili quantitative
* [[Test T di Student]]
* [[ANOVA]]

| Test                                            | Quando si usa                                                                          |
| ----------------------------------------------- | -------------------------------------------------------------------------------------- |
| **Test t per 1 campione**                       | Confronti la media di un campione con un valore teorico (es. $\mu$ = 1)                |
| **Test t per 2 campioni indipendenti**          | Confronti le medie di due gruppi distinti (es. uomini vs donne)                        |
| **Test t per campioni appaiati (o dipendenti)** | Confronti due misure fatte **sugli stessi soggetti** (es. prima e dopo un trattamento) |
| **ANOVA (Analisi della Varianza)**              | Confronti le medie tra **più di due gruppi**                                           |

---
###  Test sulle proporzioni
Quando analizzi variabili categoriche
* [[Test Z]]

| Test                                      | Quando si usa                                                                                 |
| ----------------------------------------- | --------------------------------------------------------------------------------------------- |
| **Test z per 1 proporzione**              | Vuoi sapere se la proporzione osservata è diversa da un valore atteso                         |
| **Test z per 2 proporzioni**              | Confronti la proporzione tra due gruppi                                                       |
| **Test chi-quadro (χ²) per indipendenza** | Verifichi se due variabili categoriche sono associate (es. sesso e preferenza di un prodotto) |
| **Test chi-quadro (χ²) per adattamento**  | Verifichi se una distribuzione osservata segue una distribuzione attesa                       |

---
### Test sulle varianze
Dispersione dei dati
* [[Test F di Fisher]]

| Test                  | Quando si usa                                                                                  |
| --------------------- | ---------------------------------------------------------------------------------------------- |
| **Test F di Fisher**  | Confronti due varianze                                                                         |
| **Levene o Bartlett** | Verifichi se più gruppi hanno **varianze uguali** (soprattutto come precondizione per l’ANOVA) |

---
###  Altri test utili

| Test                                                                 | Quando si usa                                                                 |
| -------------------------------------------------------------------- | ----------------------------------------------------------------------------- |
| **Test di normalità (es. Shapiro-Wilk, Kolmogorov-Smirnov)**         | Per vedere se i tuoi dati seguono una distribuzione normale                   |
| **Test non parametrici (Mann-Whitney, Wilcoxon, Kruskal-Wallis...)** | Da usare **quando i dati non sono normali** o non soddisfano certe condizioni |

---
### Come scegliere il test giusto?
1. **Che tipo di variabile hai?** (quantitativa o categorica?)
2. **Quanti gruppi stai confrontando?**    
3. **I gruppi sono indipendenti o dipendenti?**
4. **Conosci la varianza della popolazione?**
5. **I dati sono distribuiti normalmente?**