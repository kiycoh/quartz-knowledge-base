---
last modified: 2025-05-24T23:14:00.000Z
related:
  - '[[SQL]]'
tags:
  - sql
  - database-management-system
  - database-design
---


- Le parole chiave DDL non sono operatori nel senso matematico del termine, ma comandi che il DBMS esegue per modificare lo schema del database.
- La sintassi esatta e le funzionalità specifiche dei comandi DDL possono variare leggermente a seconda del DBMS utilizzato.

Ecco una tabella con le parole chiave DDL più comuni in SQL e i vincoli di integrità associati:

| ***Parola Chiave DDL*** | ***Funzionalità***                                                                                                             | ***Esempio***                                                   |
| ----------------------- | ------------------------------------------------------------------------------------------------------------------------------ | --------------------------------------------------------------- |
| **CREATE**              | Crea nuovi oggetti del database (tabelle, viste, indici, procedure, trigger, ecc.).                                            | `CREATE TABLE Clienti (ID INT PRIMARY KEY, Nome VARCHAR(255));` |
| **ALTER**               | Modifica oggetti del database esistenti, aggiungendo, modificando o rimuovendo colonne, o cambiando nomi di tabelle o colonne. | `ALTER TABLE Clienti ADD Email VARCHAR(255);`                   |
| **DROP**                | Elimina oggetti del database, come tabelle o viste.                                                                            | `DROP TABLE Clienti;`                                           |
| **TRUNCATE**            | Elimina tutti i dati da una tabella mantenendo la struttura.                                                                   | `TRUNCATE TABLE Clienti;`                                       |
| **RENAME**              | Rinomina una tabella o una colonna tramite `ALTER TABLE`.                                                                      | `ALTER TABLE Clienti RENAME TO Utenti;`                         |
### Vincoli di Integrità

| ***Vincolo di Integrità*** | ***Descrizione***                                                                                                               | ***Esempio***                                   |
| -------------------------- | ------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------- |
| **PRIMARY KEY**            | Definisce una chiave primaria, garantendo l'unicità e che non siano ammessi valori NULL.                                        | `PRIMARY KEY (ID)`                              |
| **FOREIGN KEY**            | Definisce un vincolo referenziale tra tabelle, garantendo che i valori corrispondano a una chiave primaria in un'altra tabella. | `FOREIGN KEY (ID_Ordine) REFERENCES Ordini(ID)` |
| **UNIQUE**                 | Assicura che i valori di una colonna (o gruppo di colonne) siano unici.                                                         | `UNIQUE (Email)`                                |
| **NOT NULL**               | Impedisce l'inserimento di valori NULL in una colonna.                                                                          | `Nome VARCHAR(255) NOT NULL`                    |
| **CHECK**                  | Definisce una condizione che i dati in una colonna devono soddisfare.                                                           | `CHECK (Età >= 18)`                             |
