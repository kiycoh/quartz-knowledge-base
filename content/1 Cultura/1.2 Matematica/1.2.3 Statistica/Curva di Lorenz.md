---
last modified: 24/10/2025 02:56
related:
  - '[[Indici di concentrazione (Statistica)]]'
  - '[[Coefficiente di Gini]]'
tags:
  - statistica-descrittiva
  - statistica-inferenziale
  - indice-di-concentrazione-gini
---
# Definizione di curva di Lorenz
La **curva di Lorenz** è un ==grafico che mostra come è distribuita una variabile statistica, come il reddito o la ricchezza.== In altre parole viene usata per rappresentare graficamente il grado di concentrazione di una [[Variabile statistica|variabile]].
* Vengono disposti i valori della variabile in ordine non decrescente;
* La curva si ottiene ponendo su un piano cartesiano le frequenze.


La curva di Lorenz è la rappresentazione grafica della concentrazione. Essa si costruisce su un piano cartesiano in cui l'asse delle ascisse rappresenta le frazioni cumulate di unità ($F_i$) e l'asse delle ordinate rappresenta le proporzioni cumulate dell'ammontare del carattere ($Q_i$). I punti $(F_i, Q_i)$ vengono congiunti da una spezzata.

•

La bisettrice (la retta $y=x$) rappresenta la perfetta equidistribuzione, dove $Q_i = F_i$ per ogni $i$.

•

Maggiore è l'area compresa tra la bisettrice e la curva di Lorenz, maggiore è la concentrazione. Questa area è direttamente proporzionale al rapporto di Gini.

•

In condizioni di massima concentrazione, la curva di Lorenz coincide con l'asse delle ascisse per le prime $n-1$ unità (poiché $Q_i = 0$ per $i < n$) e poi sale verticalmente al punto $(1,1)$ (l'ultima unità possiede l'intero ammontare).

![[Pasted image 20250407183824.png]]
> [!info]- Codice Python plot curva di Lorenz
> 
> ```Python
> data = sns.load_dataset("diamonds")
> 
> af_price = data['price'].value_counts().sort_values()   # Frequenza assoluta di 'price'
> 
> # Frequenze relative e cumulate
> rel_freq = af_price / len(data)
> cum_rel_freq = rel_freq.cumsum()
> price_proportion = np.arange(1, len(af_price) + 1) / len(af_price)   # Proporzione cumulata del prezzo
> 
> # Indice di concentrazione di Gini
> x_lorenz = np.insert(price_proportion, 1, 0)   # Aggiungo 0,0 come punto iniziale
> y_lorenz = np.insert(cum_rel_freq.values, 0, 0)
> 
> # Area sotto la curva di Lorenz
> area_lorenz = np.trapezoid(y_lorenz, x_lorenz)
> 
> # Area sotto la retta di equidistribuzione
> area_equi = 0.5
> 
> # Indice di Gini
> gini = (area_equi - area_lorenz) / area_equi
> 
> # 4. Disegno della curva di Lorenz
> fig, ax = plt.subplots(figsize=(10, 8))
> ax.plot(x_lorenz, y_lorenz, 'b-', linewidth=2, label='Curva di Lorenz')
> plt.plot([0, 1], [0, 1], 'r--', linewidth=2, label='Equidistribuzione')
> plt.xlabel('Proporzione cumulata delle isole')
> plt.ylabel('Proporzione cumulata dei pinguini')
> plt.title(f'Curva di Lorenz per la distribuzione dei pinguini sulle isole\nIndice di Gini = {gini:.4f}')
> plt.grid(True)
> plt.legend()
> 
> # Tabella riepilogativa
> table = pd.DataFrame({
>     'Island': af_price.index,
>     'Frequenza assoluta': af_price.values,
>     'Frequenza relativa': rel_freq.values,
>     'Frequenza cumulata': cum_rel_freq.values
> })
> 
> print("Tabella di distribuzione dei pinguini per isola:")
> print(table) 
> print(f"\nIndice di concentrazione di Gini: {gini:.4f}")
> 
> plt.show()
> ```
> 



> [!EXAMPLE] Esempio
> La curva di Lorenz è spesso usata per misurare la disuguaglianza nella distribuzione del reddito o della ricchezza


