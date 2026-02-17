---
tags:
  - machine-learning
  - string-manipulation
  - data-science
---

==Una stringa== ==è una collezione sequenziale di zero o più caratteri (codificati in **extended ASCII**== (*lettere, numeri o altri simboli*).
La differenza più importante tra una *stringa* e una *lista* è che la lista può essere modificata mentre la stringa no. Questa è chiamata **mutabilità**.
	*Esempio*: è possibile cambiare l'item in una lista usando gli indici e le assegnazioni. Ciò non è possibile in una stringa.
## Operatori su stringhe
| **Nome** | **Operatore** | **Spiegazione** |
| ---------- | --------- | --------- |
| Indicizzatore | \[ ] | Accedi ad un elemento della sequenza |
| Concatenatore | + | Combina più sequenze |
| Ripetitore | * | Concatena un determinato numero di volte |
| Appartenenza | **in** | Interroga sull'appartenenza di un elemento alla lista |
| Lunghezza | **len()** | Interroga sul numero di elementi nella sequenza |
| Slicing | \[ : ] | Estrai una parte della sequenza nel modo \[start:stop:step] |
## Metodi su stringhe
| **Nome** | **Operatore** | **Spiegazione** |
| ---- | ---- | ---- |
| center | string.center(w) | Ritorna una stringa centrata in un campo di grandezza *w* |
| ==count== | string.count(item) | Ritorna il numero di occorrenze di un item nella stringa |
| endswith | string.endswith(k) | Ritorna *True* se la stringa finisce con l'elemento k, *False* altrimenti |
| find | string.find(item) | Ritorna l'indice della prima ricorrenza dell'item |
| ==index== | string.index(char) | Ritorna l'indice dell'elemento "char". |
| isalnum | string.isalnum() | Ritorna _True_ se la stringa ha almeno un carattere ed è composta solo da lettere o numeri. Altrimenti *False* |
| isalpha | string.isalpha() | Ritorna *True* se la stringa ha almeno un carattere ed è composta solo da lettere. Altrimenti *False* |
| isdigit | string.isdigit() | Ritorna *True* se la stringa ha almeno un carattere ed è composta solo da numeri. Altrimenti *False* |
| islower | string.islower() | Ritorna *True* se la stringa ha almeno un carattere ed è composta da lettere minuscole. Altrimenti *False* |
| isspace | string.isspace() | Ritorna *True* se la stringa ha almeno un carattere vuoto (spazio, tab, newline). Altrimenti *False*. |
| isupper | string.isupper() | Ritorna *True* se la stringa ha almeno un carattere ed è composta da lettere maiuscole. Altrimenti *False*. |
| ==join== | string.join(tuple) | Unisce tutti gli elementi di una sequenza in una stringa unica, in questo caso separati da una string. |
| l just | string.l just(w) | Ritorna una stringa allineata a sinistra in un campo di grandezza *w* |
| lower | string.lower() | Ritorna una stringa in minuscolo |
| r just | string. r just(w) | Ritorna una stringa allineata a destra in un campo di grandezza *w* |
| ==replace== | string.replace(b,a) | Ritorna una stringa dove il valore specificato b è rimpiazzato dal valore a. |
| ==split== | string.split(char) | Divide la stringa in sotto-stringhe al carattere "*char*". Se non specificato divide la stringa in corrispondenza degli spazi vuoti. |
| startswith | string.startswith(k) | Ritorna *True* se la stringa inizia con l'elemento k, *False* altrimenti. |
| ==strip== | string.strip(char) | Rimuove il "*char*" in prima e ultima posizione dalla stringa. Se non specificato rimuove gli spazi vuoti. |
| upper | string.upper() | Ritorna una stringa in maiuscolo |
| ==zfill== | string.zfill(len) | Aggiunge all'inizio della stringa tanti 0 finché non raggiunge la lunghezza dichiarata. |
## Formattazione su stringhe
L'operatore *%* è usato per formattare un set di variabili in una lista limitata (tuple), in una "format string", che contiene testo normale con specificatori di argomento:

| **Operatore** | **Spiegazione** |
| ---- | ---- |
| %s | Formatta stringa |
| %d | Formatta un numero intero |
| %5d | Formatta un numero intero in modo che abbia larghezza 5 (aggiungendo spazi vuoti). |
| %f | Formatta un float |
| %.2f | Formatta un float a due  |
| %x | Formatta interi in rappresentazione hex (minuscolo) |
| %X | Formatta interi in rappresentazione hex (maiuscolo) |
