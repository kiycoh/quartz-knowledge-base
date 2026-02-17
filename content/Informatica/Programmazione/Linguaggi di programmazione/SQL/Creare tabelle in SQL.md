---
last modified: 2024-11-26T10:07:00.000Z
related:
  - '[[Database]]'
tags:
  - database-design
  - sql
  - database-management-system
---
La sintassi generica per creare una tabella in SQL è:
```SQL
CREATE TABLE nome_tabella (
	nome_attributo1 tipo_dato [vincoli]
	nome_attributo2 tipo_dato [vincoli]
);
```
## Gli attributi (SQL)
Per attributo si intende una colonna della tabella. Ogni attributo ha un nome e un tipo di dato associato, ad esempio:
- `Nome varchar(20)`
- `Età integer`

Ogni attributo può avere dei **[[Vincoli (SQL)|vincoli]]** che definiscono le regole specifiche sui valori che possono essere inseriti. Alcuni vincoli comuni includono:
- `NOT NULL`: impedisce che l'attributo assuma valore nullo.
- `UNIQUE`: Garantisce che i valori siano unici all'interno della colonna
- `PRIMARY KEY`: Identifica univocamente ogni riga della tabella.
[[Tipi di dati (SQL)]]
[[Modificatori (SQL)]]
[[Gestione tabelle (SQL)]]
### Altri attributi

| **Attributo**   | **Descrizione**                                                          |
| --------------- | ------------------------------------------------------------------------ |
| `COLLATE`       | Specifica il confronto di caratteri (case-sensitive o case-insensitive). |
| `CHARACTER SET` | Specifica la codifica dei caratteri per una colonna.                     |
| `COMMENT`       | Aggiunge un commento descrittivo alla colonna.                           |
# Domini
Un **dominio** può essere visto come un 'tipo di dato personalizzato con vincoli specifici'. Sono utili per riutilizzare una definizione di tipo e vincoli.
I domini sono particolarmente utili nei seguenti casi:
- Quando più colonne in tabelle diverse devono rispettare gli stessi vincoli.
- Quando si vuole semplificare la manutenzione del database centralizzando regole e vincoli.
- Quando si desidera rendere più leggibile e auto-documentato lo schema del database.

> [!EXAMPLE]
> La sintassi per creare un dominio varia leggermente tra i sistemi di database. Ecco un esempio in **PostgreSQL**:
> ```SQL
> CREATE DOMAIN email_address AS VARCHAR(255)
> CHECK (VALUE ~* '^[A-Za-z0-0._%+-])+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$');
> ```
> - **`email_address`** è il nome del dominio.
> - **`AS VARCHAR(255)`** specifica il tipo di dato sottostante.
> - **`CHECK`** definisce un vincolo per assicurare che il valore sia un indirizzo email valido.
> 

***MySQL non supporta nativamente i domini  (2024)***

# Valori di Default
==Il **Valore Default** (`DEFAULT`) è utilizzato per specificare un valore predefinito per un attributo nel caso in cui non venga fornito nel momento dell'inserimento==. Un esempio:

```SQL
NumeroDipendenti smallint DEFAULT 0
```
- Se non viene fornito alcun valore per `NumeroDipendenti`, verrà automaticamente impostato a 0.

# Vincoli di integrità
I **vincoli di integrità** in SQL sono 'regole' applicate ai dati in una tabella, ==vengono utilizzati per limitare il tipo di dati che possono essere inseriti, aggiornati o eliminati.==
- I vincoli possono essere definiti per una singola colonna o anche per un'intera tabella.

| **Attributo** | **Descrizione**                                            |
| ------------- | ---------------------------------------------------------- |
| `PRIMARY KEY` | Definisce una chiave primaria univoca per la tabella.      |
| `FOREIGN KEY` | Vincolo che crea una relazione con un'altra tabella.       |
| `UNIQUE`      | Impone l'unicità dei valori nella colonna.                 |
| `NOT NULL`    | Impedisce che una colonna abbia valori nulli.              |
| `DEFAULT`     | Specifica un valore predefinito per la colonna.            |
| `CHECK`       | Impone una condizione sui valori accettati in una colonna. |
| `INDEX`       | Crea un indice per velocizzare le query.                   |
## Vincoli di integrità referenziale
Questi vincoli stabiliscono relazioni tra le colonne di due tabelle, garantendo che i dati in una tabella (chiamata **tabella figlia**) corrispondano ai dati in un'altra tabella (chiamata **tabella padre**).
- I vincoli di integrità referenziale sono regole utilizzate nei database relazionali per mantenere la coerenza e l'integrità dei dati tra tabelle diverse.
- Il vincolo di integrità referenziale è implementato tramite il **FOREIGN KEY** (chiave esterna). Questo vincolo assicura che il valore di una colonna nella tabella figlia esista come valore in una colonna della tabella padre. Ciò impedisce l'inserimento di dati non validi che potrebbero compromettere la relazione tra le tabelle.

> [!EXAMPLE]
> 
> ```SQL
> CREATE TABLE Persone ( PersonID INT PRIMARY KEY, Nome VARCHAR(50), Età INT ); CREATE TABLE Ordini ( OrderID INT PRIMARY KEY, OrderNumber INT, PersonID INT, FOREIGN KEY (PersonID) REFERENCES Persone(PersonID) );
> ```

