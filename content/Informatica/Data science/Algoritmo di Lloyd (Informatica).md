---
tags:
  - algoritmo-di-lloyd
  - clustering
  - machine-learning
---

> Prende il nome da Stuart P. Lloyd

==L'algoritmo di Lloyd (o rilassamento di Voroni) è un algoritmo utile per trovare insiemi di punti equidistanti in sottoinsiemi di spazi euclidei e partizioni di questi sottoinsiemi in celle.==
- Come il [[Clustering K-Means]] questo algoritmo trova ripetutamente il baricentro di ciascun insieme nella partizione e quindi ripartiziona l'insieme dei punti in base a quale di questi baricentri è più vicino.
- L'operazione media è un integrale su una ragione di spazio e l'operazione del centroide (o baricentro) più vicino risulta nei [[Diagrammi di Voroni (Matematica)]].
- L'algoritmo può essere applicato nello smussamento delle mesh triangolari del [[Metodo degli elementi finiti]].

![[Algoritmo di Lloyd (Informatica)_image_1.png|400]]


> [!note] Algoritmo è applicabile su più dimensioni
> L'algoritmo può essere applicato più direttamente al piano euclideo ma anche a spazi di dimensioni superiori o a spazi con altre metriche non euclidee.

# Come viene applicato?
L'algoritmo di Lloyd inizia con un posizionamento iniziale di un certo numero k di siti del dominio di input. Quindi viene eseguita ripetutamente la seguente fase di rilassamento:
- Viene calcolato il [[Diagrammi di Voroni (Matematica)|Diagramma di Voroni]] dei k siti.
- Ogni cella del diagramma di Voroni viene integrata e viene calcolato il baricentro.
- Ogni sito viene quindi spostato dal baricentro della sua cella di Voroni.

>[!warning] L'approssimazione è fondamentale.
>Poiché gli algoritmi per la costruzione dei diagrammi di Voroni possono essere complessi, i passaggi per calcolarli e trovare i baricentri delle celle possono essere sostituiti da un'approssimazione.