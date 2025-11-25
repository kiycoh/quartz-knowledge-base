---
last modified: 2025, 11, 24 22:11:46
related:
  - '[[SQL]]'
tags: [database-design, database-management, sql]
---
# Operatori [[DML (Data Manipulation Language)|DML]]

| ***Categoria***                  | ***Descrizione***                                                                             | ***Esempi di Operatori***                                                    |
| -------------------------------- | --------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------- |
| **Operatori di confronto**       | Permettono di confrontare valori all'interno delle clausole `WHERE` per filtrare i dati.      | `=`, `<>`, `<`, `>`, `<=`, `>=`                                              |
| **Operatori aritmetici**         | Si usano per eseguire operazioni matematiche sui valori numerici.                             | `+`, `-`, `*`, `/`, `%`                                                      |
| **Operatore di concatenazione**  | Permette di unire stringhe di testo.                                                          | \| \|                                                                        |
| **Operatori logici**             | Si usano per combinare più condizioni nelle clausole `WHERE`.                                 | `AND`, `OR`, `NOT`                                                           |
| **Operatore `IN`**               | Verifica se un valore è presente in un insieme di valori.                                     | `IN (val1, val2, …)` <br>`NOT IN (val1, val2, …)`                        |
| **Operatore `BETWEEN`**          | Verifica se un valore è compreso tra due estremi.                                             | `BETWEEN val1 AND val2` <br>`NOT BETWEEN val1 AND val2`                      |
| **Operatore `LIKE`**             | Permette di cercare valorio che corrispondono a un pattern specificato, usando `%` e `_`.     | `LIKE 'pattern%'`, `LIKE 'pattern_'` <br>`NOT LIKE…`                       |
| **Operatori di quantificazione** | Confrontano un valore scalare con i valori in un insieme derivato da una sottoquery.          | `EXISTS`, `NOT EXISTS`, `ALL`, `ANY`                                         |
| **Operatori di insieme**         | Combinano i risultati di due o più `SELECT` in un unico risultato.                            | `UNION`, `INTERSECT`, `EXCEPT`                                               |
| **Operatori di join**            | Combinano dati da più tabelle in base a una condizione di join.                               | `JOIN`, `NATURAL JOIN`, `LEFT JOIN`, `RIGHT JOIN`, `FULL JOIN`, `CROSS JOIN` |
| **Operatori di aggregazione**    | Calcolano valori aggregati da un insieme di dati.                                             | `SUM`, `AVG`, `MIN`, `MAX`, `COUNT`                                          |
| **Operatore `GROUP BY`**         | Raggruppa i dati in base a uno o più attributi e applica operatori di aggregazione ai gruppi. | `GROUP BY`                                                                   |
| **Operatore `HAVING`**           | Filtra i gruppi risultanti da un `GROUP BY` in base a una condizione.                         | `HAVING`                                                                     |
| **Operatore `ORDER BY`**         | Ordina i dati in base a uno o più attributi.                                                  | `ORDER BY`                                                                   |