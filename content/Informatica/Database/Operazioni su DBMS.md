---
last modified: 2025, 11, 24 22:11:49
related:
  - '[[Operatori insiemistici]]'
tags: [data-definition-language-These-tags-are-chosen-based-on-the-content-of-the-document, database-design, database-management]
---
# Operazioni su DBMS
Le operazioni sui dati in un database possono essere classificate in due categorie principali: **operazioni di scrittura**, che modificano i dati, e **operazioni di lettura**, che accedono ai dati senza modificarli.

Le operazioni di scrittura, specialmente in contesti di accesso concorrente al database, vengono gestite all'interno di **transazioni**. Le transazioni garantiscono l'integrità e la coerenza dei dati anche in situazioni complesse, anche in caso di malfunzionamenti *(backup & recovery)*.

==Una **transazione** è un'unità logica di lavoro che raggruppa una o più operazioni sui dati== garantendo che queste vengano eseguite tutte con successo oppure, in caso di errore, che nessuna di esse abbia effetto sul database. Le transazioni godono delle proprietà **ACID** (Atomicità, Consistenza, Isolamento, Durabilità)

>[!ERROR]- Problemi derivati da una gestione inadeguata dei dati
>- **Ridondanza e inconsistenza dei dati e difficoltà di aggiornamento e manutenzione:** Senza una gestione organica, i dati tendono ad essere duplicati in diversi punti del sistema, con il rischio di creare inconsistenza quando le informazioni vengono aggiornate solo in alcune copie. Apportare modifiche o aggiornamenti ai dati diventa un'operazione complessa e rischiosa
>	- Ad esempio, se i dati di un cliente sono memorizzati in più sistemi non integrati, un cambiamento di indirizzo potrebbe essere registrato solo in uno di essi, creando confusione e potenziali errori nelle comunicazioni successive.
>- **Difficoltà di accesso e interrogazione e problemi di sicurezza** La mancanza di un sistema di gestione centralizzato rende difficile l'accesso ai dati da parte di utenti e applicazioni. Se i dati sono sparsi in diversi file e formati, recuperare informazioni specifiche può diventare un processo complesso per via dell'eventuale capacità di integrare manualmente i dati dalla molteplicità delle fonti.
>	- Inoltre, diventa difficile implementare misure di sicurezza efficaci per controllare l'accesso ai dati sensibili.

## Operazioni di Scrittura
- **Inserimento (`INSERT`):** Questa operazione permette di aggiungere nuove informazioni al database. L'istruzione `INSERT` in SQL consente di specificare la tabella in cui inserire i dati e i valori per ogni attributo. Ad esempio, per aggiungere un nuovo studente in una tabella "Studenti", si indicherebbe la tabella "Studenti", i valori per "Matricola", "Nome", "Cognome", ecc.
- **Cancellazione (`DELETE`):** Questa operazione permette di rimuovere informazioni dal database. L'istruzione DELETE in SQL consente di specificare la tabella da cui eliminare i dati e una condizione per selezionare le righe da eliminare. Ad esempio, per eliminare uno studente dalla tabella "Studenti", si indicherebbe la tabella "Studenti" e la condizione "Matricola = 12345".
- **Modifica (`UPDATE`):** Questa operazione permette di cambiare informazioni esistenti nel database. L'istruzione UPDATE in SQL consente di specificare la tabella, i nuovi valori per gli attributi da modificare e una condizione per selezionare le righe da aggiornare. Ad esempio, per modificare il "Cognome" di uno studente nella tabella "Studenti", si indicherebbe la tabella "Studenti", il nuovo "Cognome" e la condizione "Matricola = 12345".

## Operazioni di Lettura
- **Ricerca (`SELECT`):** Questa operazione permette di accedere e recuperare informazioni dal database. L'istruzione SELECT in SQL è la più potente e flessibile, consentendo di specificare la tabella da cui estrarre i dati, le colonne da visualizzare, le condizioni per filtrare i risultati, l'ordinamento desiderato e molto altro. Ad esempio, per trovare tutti gli studenti con "Cognome = Rossi" nella tabella "Studenti", si utilizzerebbe l'istruzione SELECT, specificando la tabella "Studenti", le colonne desiderate (ad esempio, "Matricola", "Nome") e la condizione "Cognome = Rossi".