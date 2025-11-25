---
last modified: 27/10/2025 18:51
related:
  - '[[Struttura dati (Informatica teorica)]]'
tags:
  - algoritmi-ordinamento
  - informatica-teorica
  - ricorsione
---
# "Divide et impera" in strutture dati
La famosa frase latina "Divide et impera" nel contesto dell'informatica e delle strutture dati,  indica una metodologia di progettazione che permette di formulare algoritmi [[Analisi asintotica (Matematica)|asintoticamente]][[Efficienza algoritmica| efficienti]].

Si basa su 3 fasi principali (caso ricorsivo):
1. **Divide**: il problema viene suddiviso in uno o più sotto-problemi più semplici.
2. **Impera**: i sotto-problemi vengono risolti ricorsivamente
3. **Combina**: le soluzioni dei sotto-problemi vengono combinate per formare la soluzione di un problema.

La ricorsione si arresta quando si arriva ad un problema abbastanza piccolo (**caso base**) da poter essere risolto in modo semplice.