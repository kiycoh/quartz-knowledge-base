---
last modified: 2025, 11, 24 22:11:57
related: null
parent note: null
tags: [ethical-hacking, penetration-testing, web-application-security]
---
# Penetration testing
Un **penetration test (o pen test)** ha come obiettivo valutare la sicurezza dell'intera "superficie di attacco" di un'organizzazione o sistema. Un hacker reale cerca il punto d'ingresso più debole, e un "ethical hacker" (il penetration tester) fa lo stesso.

Le aree di applicazione principali includono:
- **[[Network Pen testing]]:**
    - **Esterna:** Si simula un attacco da Internet, cercando di violare le difese perimetrali (firewall, server esposti).
    - **Interna:** Si simula un utente malintenzionato che è *già* all'interno della rete aziendale (ad esempio, un dipendente scontento o un dispositivo compromesso) per vedere quali danni può fare.
- **[[Web Application Pen testing]]:** questa è l'area a cui ti riferivi. Si cercano vulnerabilità specifiche dei siti web come SQL Injection, Cross-Site Scripting (XSS), problemi di autenticazione, ecc.
- **[[Mobile Pen Testing]]:** si analizza la sicurezza delle app su iOS e Android, controllando come salvano i dati, come comunicano con i server e se possono essere manipolate.
- **[[Cloud Pen testing]]:** si valuta la configurazione della sicurezza su piattaforme come AWS, Azure o Google Cloud, cercando errori di configurazione che potrebbero esporre dati.
- **[[Social Engineering]]:** si testa la preparazione dei dipendenti simulando attacchi di **phishing** (email ingannevoli), **vishing** (truffe telefoniche) o persino tentativi di accesso fisico per ottenere credenziali o accesso a zone riservate.
- **[[IoT Pen test]]:** si testano dispositivi connessi come telecamere di sicurezza, stampanti, sensori industriali, ecc., che sono spesso un punto debole trascurato. 
- **Sicurezza fisica:** in alcuni casi, il test può includere tentativi di eludere la sicurezza fisica (es. scassinare serrature, scavalcare recinzioni, clonare badge) per ottenere l'accesso fisico ai server.