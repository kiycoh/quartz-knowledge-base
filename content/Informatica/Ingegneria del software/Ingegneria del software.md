---
last modified: 2025, 11, 25 17:11:58
related:
  - '[[Industria 4.0]]'
  - '[[Java]]'
  - '[[Legge di Eagleson]]'
  - '[[Refactoring (Ingegneria del software)]]'
  - '[[Unified Modeling Language (UML)]]'
tags: [agile-development, ingegneria-software, software-development]
---
# Ingegneria del software
==L'**Ingegneria del software** è una disciplina ingegneristica [[Informatica]] che caratterizza l'intero processo di produzione di un *[[software]]*==: dalla sua ideazione iniziale all'operatività fino al suo mantenimento. 

Distinguiamo i seguenti principali approcci ingegneristici allo sviluppo software:
* **[[Plan-driven development (PDD)]]** incentrato sull' [[Anticipazione del cambiamento (Software)|Anticipazione del cambiamento]]
* **[[Agile development]]** incentrato sulla [[Tolleranza al cambiamento (Software)|Tolleranza al cambiamento]]

> [!QUESTION] Cosa fa un software ben ingegnerizzato?
> Un software ben ingegnerizzato restituisce le funzionalità aspettate, è [[Performance software|performante]], [[Manuntenibilità software|manuntenibile]], affidabile e utilizzabile dall'utente finale. Ad esempio:
> 
> ```mermaid
> graph LR
>     A[Utente] -- Interagisce con --> B(Frontend / UI);
>     B -- Invia Richiesta HTTP (API Call) --> C{Backend / Server};
>     C -- Legge/Scrive Dati --> D[(Database)];
>     D -- Restituisce Dati --> C;
>     C -- Invia Risposta --> B;
>     B -- Mostra il Risultato --> A;
> 
>     subgraph "Lato Client (Browser/App)"
>         A
>         B
>     end
> 
>     subgraph "Lato Server"
>         C
>         D
>     end
> ```
> 

- [[Software#Ciclo di vita generico di un software]]

- [[Modelli di sviluppo software]]