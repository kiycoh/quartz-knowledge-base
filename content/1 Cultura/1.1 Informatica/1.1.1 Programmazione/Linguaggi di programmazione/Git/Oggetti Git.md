---
last modified: 2025, 11, 18 18:11:46
related: null
tags:
  - machine-learning
  - scienze-cognitive
  - intelligenza-artificiale
---
# Oggetti Git
Gli **Oggetti Git** (`.git/objects`) sono dei file (oggetti) immutabili, una volta creati non possono essere modificati. Questa proprietà garantisce l'integrità del repository. Ogni modifica genera un nuovo oggetto con un nuovo *hash*, prevenendo corruzioni e alterazioni non autorizzate. DIstinguiamo:
- [[Blob (Binary Large Object)]]
- [[Tree]]
- [[Commit]]
- [[Tag]]
- [[Packfile]]
```bash
$ echo "Git" | git hash-object --stdin
7c89aff95cd31a65842650dce92a028e3e3b30f0
```


Git memorizza i dati attraverso quattro tipi fondamentali di oggetti nella directory `.git/objects`:[geeksforgeeks+3](https://www.geeksforgeeks.org/git/git-internals/)​

**1. Blob (Binary Large Object)**

Rappresenta il contenuto di un file senza metadata come nome, path o permessi. Un blob è identificato dall'hash SHA-1 del suo contenuto:[graphapp+1](https://www.graphapp.ai/engineering-glossary/git/git-internals-objects-refs-etc)​

bash

`# Creazione di un blob object echo "test content" | git hash-object -w --stdin # Output: d670460b4b4aece5915caf5c68d12f560a9fe3e4 # Visualizzazione del contenuto di un blob git cat-file -p d670460b4b4aece5915caf5c68d12f560a9fe3e4 # Output: test content`

**2. Tree**

Rappresenta una directory e contiene una lista di blob e altri tree (sottodirectory), insieme ai loro nomi e permessi. I tree permettono a Git di ricostruire l'intera struttura gerarchica del progetto:[geeksforgeeks+1](https://www.geeksforgeeks.org/git/git-internals/)​

bash

`# Visualizzazione di un tree object git cat-file -p <tree-sha> # Output esempio: # 100644 blob a906cb2a4a904a152… README # 040000 tree 47c6340d6459e0578… lib`

**3. Commit**

Contiene i metadata di un commit: riferimento al tree dell'oggetto di primo livello, l'autore, il committer, timestamp, messaggio di commit e riferimenti ai commit parent (zero per il primo commit, uno per commit normali, multipli per merge):[wikipedia+2](https://en.wikipedia.org/wiki/Git)​

bash

`# Visualizzazione di un commit object git cat-file -p 9fceb02 # Output: # tree 36b74b3b8f6a… # parent cf23df2207d9… # author John Doe <john@example.com> 1234567890 +0100 # committer John Doe <john@example.com> 1234567890 +0100 # # Commit message here`

**4. Tag**

Un contenitore che referenzia un altro oggetto (tipicamente un commit) e può contenere metadata aggiuntivi. Utilizzato principalmente per memorizzare firme digitali che certificano release specifiche.[wikipedia+1](https://en.wikipedia.org/wiki/Git)​

**5. Packfile**

Per ottimizzare storage e trasferimento, Git raggruppa multipli oggetti in **packfile** compressi usando zlib e **delta compression**. Invece di salvare copie complete, Git memorizza solo le differenze (delta) tra oggetti simili:[linkedin+3](https://www.linkedin.com/pulse/gits-delta-compression-algorithm-technical-deep-dive-maheshwari)​

bash

`# Verifica dello stato dei packfile git verify-pack -v .git/objects/pack/pack-*.idx # Output esempio: # c8a5f71ad9e8539e blob 4593 3071 13431 1 b4e52f… # f6234a99bcf6a8e6 blob 6583 4210 137383`

L'algoritmo utilizza tecniche come **Longest Common Subsequence (LCS)** per identificare similarità tra versioni. Se un file di 10 MB subisce 100 modifiche minori da 100 KB, invece di occupare 1 GB (10 MB × 100), i delta compressi possono ridurre lo spazio a circa 10-20 MB.[linkedin](https://www.linkedin.com/pulse/gits-delta-compression-algorithm-technical-deep-dive-maheshwari)​
