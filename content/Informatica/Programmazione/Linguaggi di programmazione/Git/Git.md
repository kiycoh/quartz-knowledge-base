---
last modified: 2025, 11, 20 15:11:38
related: null
links: https://github.com/
tags:
  - machine-learning
  - software-development
  - version-control
---
# Git
**Git**, creato da [Linus Torvalds](https://it.wikipedia.org/wiki/Linus_Torvalds) nel 2005, ==è un **sistema di controllo di versione distribuito** per tracciare modifiche al codice sorgente== durante lo [[sviluppo software]]. Permette di collaborare con altri sviluppatori e mantenere un log dettagliato di tutte le modifiche, da un file all'intera codebase. Git implementa un modello distribuito: ogni sviluppatore possiede una **copia completa del repository** con l'intera cronologia del progetto, a differenza dei sistemi centralizzati come Subversion (SVN).
* [[Oggetti Git]]

> [!IMPORTANT] Git nello specifico
> Nello specifico, Git è un **[[filesystem content-addressable]]**: ==al suo nucleo c'è un semplice database chiave-valore dove il contenuto determina la chiave==: Gli oggetti sono identificati da [[hash SHA-1]] (Secure Hash Algorithm 1), una stringa esadecimale di 40 caratteri che funge da fingerprint crittografico.
​

## Architettura Interna e Strutture Dati

## Sistema Content-Addressable e Object Database

Git è fondamentalmente un **filesystem content-addressable**: al suo nucleo c'è un semplice database chiave-valore dove il contenuto determina la chiave. Gli oggetti sono identificati da **hash SHA-1** (Secure Hash Algorithm 1), una stringa esadecimale di 40 caratteri che funge da fingerprint crittografico.[wikipedia+4](https://en.wikipedia.org/wiki/Git)​

```bash
# Calcolo dell'hash SHA-1 di un file echo "Hello Git"

>>> git hash-object --stdin

# Output: 8cf2d8a03c123f8824ac46aa20a6b924ad44f0c8
```
Gli oggetti Git sono **immutabili**: una volta creati, non possono essere modificati. Questa immutabilità garantisce l'integrità del repository. Ogni modifica genera un nuovo oggetto con un nuovo hash, prevenendo corruzioni e alterazioni non autorizzate.[graphapp+3](https://www.graphapp.ai/engineering-glossary/git/git-internals-objects-refs-etc)​


## Le Tre Aree Fondamentali di Git​

## 1. Working Directory (Working Tree)

La **directory di lavoro** contiene i file effettivi in formato normale del filesystem, dove gli sviluppatori modificano attivamente il codice. È essenzialmente una "sandbox" dove puoi sperimentare modifiche prima di renderle permanenti.​

bash

`# Visualizzazione dello stato del working directory git status # Output mostra file modificati, non tracciati, ecc.`

## 2. Staging Area (Index)
L'**area di staging** (anche chiamata **index** o **cache**) è uno strato intermedio tra il working directory e il repository. Funziona come un'area di preparazione dove assembli il prossimo commit:​

- Contiene una copia dei file estratti dal repository, pronti per essere committati
- Permette di selezionare granularmente quali modifiche includere nel prossimo commit
- Memorizza lo **snapshot proposto** del prossimo commit

bash

`# Aggiunta di file alla staging area git add file.txt # Aggiunta di tutti i file modificati git add . # Visualizzazione delle modifiche staged git diff --cached # Rimozione di file dalla staging area git reset HEAD file.txt`

## 3. Repository (Object Database)

Il **repository** (`.git/objects`) memorizza in modo permanente gli snapshot completi di ogni commit in formato compresso Git. Ogni commit cattura lo stato completo del progetto al momento del commit.[graphapp+3](https://www.graphapp.ai/engineering-glossary/git/git-internals-objects-refs-etc)​

bash

`# Commit dei file staged nel repository git commit -m "Descrizione delle modifiche" # Visualizzazione della storia dei commit git log --oneline --graph --all`

## Git Workflow
Il workflow base di Git segue questo pattern:
``` bash
# 1. Modifica file nel working directory
echo "nuovo contenuto" >> file.txt 
# 2. Staging delle modifiche 
git add file.txt 
# 3. Commit dello snapshot 
git commit -m "Descrizione commit"`
```

Concettualmente:
- **Working Directory → Staging Area**: `git add` (preparazione)
- **Staging Area → Repository**: `git commit` (permanenza)
- **Repository → Working Directory**: `git checkout` (estrazione)
## Gestione dei Branch e Strategie di Branching

## Concetto di Branch

Un **branch** in Git è essenzialmente un puntatore mobile a un commit. Il branch di default è chiamato `main` (precedentemente `master`). I branch permettono sviluppo parallelo e isolato di feature senza disturbare il codice principale.[atlassian+2](https://www.atlassian.com/git/tutorials/comparing-workflows/feature-branch-workflow)​

bash

``` bash
# Creazione di un nuovo branch
git branch feature-login

# Switch al nuovo branch
git checkout feature-login 
# oppure (Git 2.23+)
git switch feature-login

# Creazione e switch combinati
git checkout -b feature-login
# oppure
git switch -c feature-login

# Visualizzazione di tutti i branch
git branch -a
# Eliminazione di un branch
git branch -d feature-login
```

## Strategie di Merge
Git offre diverse strategie di merge per integrare modifiche tra branch:​

**1. Fast-Forward Merge**

Quando il branch target è un diretto antenato, Git semplicemente muove il puntatore in avanti:[git-scm](https://git-scm.com/book/en/v2/Git-Branching-Basic-Branching-and-Merging)​

bash

`git checkout main git merge feature-branch # Fast-forward merge se non ci sono commit divergenti`

**2. Three-Way Merge (Recursive)**

La strategia di default quando le storie divergono. Git crea un **merge commit** con due parent:[git-scm+1](https://git-scm.com/docs/merge-strategies)​

bash

`git checkout main git merge feature-branch # Merge commit: "Merge branch 'feature-branch' into main"`

**3. Octopus Merge**

Utilizzata automaticamente per mergiare più di due branch contemporaneamente:[atlassian+1](https://www.atlassian.com/git/tutorials/using-branches/merge-strategy)​

bash

`git merge branch1 branch2 branch3 # Crea un merge commit con multipli parent`

**4. Squash Merge**

Combina tutti i commit di un branch in un singolo commit:[atlassian](https://www.atlassian.com/git/tutorials/using-branches/merge-strategy)​

bash

`git merge --squash feature-branch git commit -m "Feature completa in un unico commit"`

## Gitflow Workflow

**Gitflow** è una strategia di branching strutturata per progetti complessi:[aws.amazon+2](https://docs.aws.amazon.com/prescriptive-guidance/latest/choosing-git-branch-approach/branches-in-a-gitflow-strategy.html)​

**Branch Principali:**
- **main**: codice in produzione stabile
- **develop**: branch di integrazione per nuove feature

**Branch di Supporto:**
- **feature/**: sviluppo di singole funzionalità (da `develop`)
- **release/**: preparazione per release (da `develop` a `main`)
- **hotfix/**: fix urgenti in produzione (da `main`)

bash

`# Creazione di un feature branch git checkout develop git checkout -b feature/user-auth # Lavoro sulla feature… git add . git commit -m "Implementata autenticazione utente" # Merge in develop git checkout develop git merge feature/user-auth # Creazione di release branch git checkout -b release/1.0.0 develop # Dopo testing, merge in main e develop git checkout main git merge release/1.0.0 git tag -a v1.0.0 -m "Release versione 1.0.0" git checkout develop git merge release/1.0.0`

## Feature Branch Workflow
Strategia più semplice e flessibile: ogni feature ha il proprio branch dedicato:[about.gitlab+1](https://about.gitlab.com/topics/version-control/what-is-git-workflow/)​

bash

`# Creazione feature branch da main git checkout main git pull origin main git checkout -b feature/payment-integration # Sviluppo… git add . git commit -m "Implementato gateway di pagamento" # Push per collaborazione/backup git push -u origin feature/payment-integration # Merge tramite pull request o direttamente git checkout main git merge feature/payment-integration git push origin main # Pulizia git branch -d feature/payment-integration git push origin --delete feature/payment-integration`

## Repository Remoti e Collaborazione

## Configurazione dei Remote
I **remote** sono riferimenti a repository ospitati altrove (GitHub, GitLab, server privati):[git-scm+1](https://git-scm.com/book/ms/v2/Git-Basics-Working-with-Remotes)​

bash

`# Visualizzazione dei remote configurati git remote -v # Aggiunta di un remote git remote add origin https://github.com/user/repo.git # Modifica URL remote git remote set-url origin git@github.com:user/repo.git # Rimozione remote git remote remove origin`

## Operazioni di Sincronizzazione

**Fetch vs Pull vs Push**:[theserverside+2](https://www.theserverside.com/blog/Coffee-Talk-Java-News-Stories-and-Opinions/Git-pull-vs-fetch-Whats-the-difference)​

**Git Fetch**: scarica dati dal remote nel repository locale senza modificare il working directory:[github+2](https://docs.github.com/en/get-started/using-git/getting-changes-from-a-remote-repository)​

bash

`# Fetch da origin git fetch origin # Fetch di un branch specifico git fetch origin main # Fetch di tutti i remote git fetch --all`

**Git Pull**: esegue `fetch` + `merge` automaticamente:[theserverside+2](https://www.theserverside.com/blog/Coffee-Talk-Java-News-Stories-and-Opinions/Git-pull-vs-fetch-Whats-the-difference)​

bash

`# Pull con merge (default) git pull origin main # Pull con rebase (mantiene storia lineare) git pull --rebase origin main # Equivalente manuale git fetch origin git merge origin/main`

**Git Push**: carica commit locali sul repository remoto:[git-scm+1](https://git-scm.com/book/ms/v2/Git-Basics-Working-with-Remotes)​

bash

`# Push del branch corrente git push origin feature-branch # Push e impostazione upstream git push -u origin feature-branch # Push di tutti i branch git push --all origin # Push forzato (ATTENZIONE: riscrive storia remota) git push --force origin feature-branch # Alternativa più sicura git push --force-with-lease origin feature-branch`

## Clone e Repository Inizializzazione

bash

`# Clone di un repository remoto git clone https://github.com/user/repo.git # Clone con submoduli (vedi sezione avanzata) git clone --recurse-submodules https://github.com/user/repo.git # Inizializzazione di un nuovo repository mkdir my-project cd my-project git init git remote add origin https://github.com/user/my-project.git`

## Comandi Avanzati: Rebase, Reset, Cherry-Pick

## Git Rebase

**Rebase** riscrive la storia dei commit riapplicandoli sopra un'altra base:[stackoverflow+2](https://stackoverflow.com/questions/68095467/git-interactive-rebase-squash-commits-any-shortcuts)​

bash

`# Rebase del branch corrente su main git checkout feature-branch git rebase main # Rebase interattivo (ultimi 5 commit) git rebase -i HEAD~5 # Durante rebase interattivo, opzioni disponibili: # pick = usa commit # reword = modifica messaggio # edit = ferma per ammending # squash = unisci con commit precedente mantenendo messaggi # fixup = come squash ma scarta messaggio # drop = elimina commit`

**Esempio di Interactive Rebase per Squash**:[dmcinfo+2](https://www.dmcinfo.com/blog/19251/git-as-fast-as-possible-reword-and-squash/)​

bash

`# Visualizza ultimi 4 commit git log --oneline # a1b2c3d Fix typo # e4f5g6h Add feature # i7j8k9l Update docs # m0n1o2p Initial commit # Rebase interattivo git rebase -i HEAD~3 # Editor mostra: pick e4f5g6h Add feature pick i7j8k9l Update docs pick a1b2c3d Fix typo  # Modifica in: pick e4f5g6h Add feature squash i7j8k9l Update docs squash a1b2c3d Fix typo  # Salva: Git combinerà i 3 commit in uno solo`

**Alternative veloci per squash**:[stackoverflow](https://stackoverflow.com/questions/68095467/git-interactive-rebase-squash-commits-any-shortcuts)​

bash

`# Reset soft + commit git reset --soft HEAD~3 git commit -m "Implementata feature completa"`

## Git Reset: Soft, Mixed, Hard

`git reset` muove HEAD e il branch corrente a un commit specificato, con tre modalità che influenzano working directory e staging area:[geeksforgeeks+2](https://www.geeksforgeeks.org/git/whats-the-difference-between-git-reset-mixed-soft-and-hard/)​

**Reset Soft**: muove HEAD ma preserva staging area e working directory:[gitkraken+1](https://www.gitkraken.com/learn/git/git-reset)​

bash

`git reset --soft HEAD~2 # Commit annullati, modifiche rimangono staged # Utile per riorganizzare commit mantenendo tutte le modifiche`

**Reset Mixed** (default): muove HEAD, resetta staging area, preserva working directory:[geeksforgeeks+1](https://www.geeksforgeeks.org/git/whats-the-difference-between-git-reset-mixed-soft-and-hard/)​

bash

`git reset HEAD~2 # oppure git reset --mixed HEAD~2 # Commit annullati, modifiche in working directory ma unstaged`

**Reset Hard**: muove HEAD, resetta staging area E working directory:[gitkraken+1](https://www.gitkraken.com/learn/git/git-reset)​

bash

`git reset --hard HEAD~2 # ATTENZIONE: distrugge permanentemente le modifiche non committate # Riporta tutto allo stato del commit specificato`

**Esempi pratici**:[geeksforgeeks+1](https://www.geeksforgeeks.org/git/whats-the-difference-between-git-reset-mixed-soft-and-hard/)​

bash

`# Annullare ultimo commit mantenendo modifiche staged git reset --soft HEAD~1 # Unstage tutti i file git reset HEAD # Scartare tutte le modifiche locali git reset --hard HEAD # Tornare a un commit specifico git reset --hard abc123`

## Git Cherry-Pick

**Cherry-pick** applica un commit specifico dal branch corrente a un altro branch:[stackoverflow+1](https://stackoverflow.com/questions/30986376/how-to-undo-a-successful-git-cherry-pick)​

bash

`# Checkout del branch target git checkout main # Applica commit specifico git cherry-pick abc123 # Cherry-pick multipli commit git cherry-pick abc123 def456 ghi789 # Cherry-pick senza commit automatico (per revisione) git cherry-pick --no-commit abc123 # Cherry-pick con modifica messaggio git cherry-pick -e abc123`

**Undo di cherry-pick**:[stackoverflow](https://stackoverflow.com/questions/30986376/how-to-undo-a-successful-git-cherry-pick)​

bash

`# Con modifiche locali: stash prima git stash git reset --hard HEAD^ git stash pop # Senza modifiche locali git reset --hard HEAD^`

## Comandi di Utilità Avanzata

## Git Stash

**Stash** salva temporaneamente modifiche non committate per un recupero successivo:[jwiegley.github+2](https://jwiegley.github.io/git-from-the-bottom-up/4-Stashing-and-the-reflog.html)​

bash

`# Stash delle modifiche correnti git stash # oppure con messaggio git stash save "WIP: feature parziale" # Lista degli stash git stash list # Output: # stash@{0}: WIP on main: abc123 Last commit # stash@{1}: On feature: def456 Another stash # Applica ultimo stash (mantiene in lista) git stash apply # Applica e rimuovi ultimo stash git stash pop # Applica stash specifico git stash apply stash@{1} # Stash include file untracked git stash -u # Eliminazione di uno stash git stash drop stash@{0} # Eliminazione di tutti gli stash git stash clear`

## Git Reflog

**Reflog** (reference log) traccia ogni modifica ai riferimenti del repository, fornendo una rete di sicurezza per recuperare commit "persi":[wanago+3](https://wanago.io/2020/09/14/geeky-with-git-cherry-pick-reflog/)​

bash

`# Visualizza reflog git reflog # Output esempio: # abc123 (HEAD -> main) HEAD@{0}: commit: Feature completa # def456 HEAD@{1}: commit: Work in progress # ghi789 HEAD@{2}: reset: moving to HEAD~1 # Recupera commit dopo reset accidentale git reset --hard abc123 # Reflog per branch specifico git reflog show main # Cherry-pick da reflog git cherry-pick HEAD@{2} # Reflog per stash git reflog stash`

## Git Diff

Analisi dettagliata delle differenze tra versioni:[graphite+1](https://graphite.dev/guides/git-staging-area)​

bash

`# Differenze tra working directory e staging area git diff # Differenze tra staging area e ultimo commit git diff --cached # oppure git diff --staged # Differenze tra working directory e ultimo commit git diff HEAD # Differenze tra due commit git diff abc123 def456 # Differenze per file specifico git diff main feature-branch -- file.txt # Statistiche delle modifiche git diff --stat # Diff inline più compatto git diff --word-diff`

## Git Hooks: Automazione del Workflow

**Git hooks** sono script eseguiti automaticamente prima o dopo eventi Git specifici:[gitguardian+3](https://www.gitguardian.com/glossary/git-hooks)​

## Hook Lato Client

Localizzati in `.git/hooks/`, eseguiti sulla macchina locale:[graphite+1](https://graphite.dev/guides/git-hooks)​

**pre-commit**: eseguito prima di finalizzare un commit:[atlassian+1](https://www.atlassian.com/git/tutorials/git-hooks)​

bash

`#!/bin/sh # .git/hooks/pre-commit # Linting del codice if ! flake8 .; then     echo "Errori di linting trovati. Commit annullato."     exit 1 fi # Esecuzione test if ! npm test; then     echo "Test falliti. Commit annullato."     exit 1 fi exit 0`

**commit-msg**: valida il messaggio di commit:[pre-commit+1](https://pre-commit.com/)​

bash

`#!/bin/sh # .git/hooks/commit-msg commit_msg_file=$1 commit_msg=$(cat "$commit_msg_file") # Pattern: "TYPE: Descrizione" if ! echo "$commit_msg" | grep -qE "^(feat|fix|docs|style|refactor|test|chore): "; then     echo "Formato messaggio non valido."     echo "Usa: TYPE: Descrizione"     echo "TYPE: feat, fix, docs, style, refactor, test, chore"     exit 1 fi`

**pre-push**: eseguito prima di push su remote:[graphite+1](https://graphite.dev/guides/git-hooks)​

bash

`#!/bin/sh # .git/hooks/pre-push echo "Esecuzione test prima del push…" if ! npm test; then     echo "Test falliti. Push annullato."     exit 1 fi`

## Hook Lato Server

Eseguiti sul server Git remoto:[gitguardian+2](https://www.gitguardian.com/glossary/git-hooks)​

**pre-receive**: eseguito sul server prima di accettare push:[gitguardian+1](https://www.gitguardian.com/glossary/git-hooks)​

bash

`#!/bin/sh # hooks/pre-receive (sul server) while read oldrev newrev refname; do     if [ "$refname" = "refs/heads/main" ]; then         # Impedisci push diretti a main         echo "Push diretti a main non consentiti. Usa pull request."         exit 1     fi done`

**post-receive**: eseguito dopo accettazione push, utile per CI/CD:[graphite+1](https://graphite.dev/guides/git-hooks)​

bash

`#!/bin/sh # hooks/post-receive while read oldrev newrev refname; do     if [ "$refname" = "refs/heads/main" ]; then         echo "Deploying to production…"         cd /var/www/app        git pull origin main        npm install         pm2 restart app     fi done`

**Rendere hook eseguibili**:

bash

`chmod +x .git/hooks/pre-commit`

**Framework per Gestione Hook**:[pre-commit](https://pre-commit.com/)​

bash

`# Installazione di pre-commit framework pip install pre-commit # File .pre-commit-config.yaml repos:   - repo: https://github.com/pre-commit/pre-commit-hooks     rev: v4.4.0     hooks:       - id: trailing-whitespace       - id: end-of-file-fixer       - id: check-yaml       - id: check-json  # Installazione hooks pre-commit install # Esecuzione manuale su tutti i file pre-commit run --all-files`

## Concetti Avanzati: Submodules, Subtrees, Monorepo

## Git Submodules

I **submodules** permettono di includere un repository Git come sottodirectory di un altro repository:[thebottleneckdev+2](https://thebottleneckdev.com/blog/monorepo-git-submodules)​

bash

`# Aggiunta di un submodule git submodule add https://github.com/user/lib.git libs/external-lib # Clonazione repository con submodules git clone --recurse-submodules https://github.com/user/main-project.git # Inizializzazione submodules dopo clone normale git submodule init git submodule update # Update di tutti i submodules alla versione più recente git submodule update --remote # Rimozione di un submodule git submodule deinit libs/external-lib git rm libs/external-lib rm -rf .git/modules/libs/external-lib`

**Limitazioni dei Submodules**:[timhutt](https://blog.timhutt.co.uk/against-submodules/)​

- Non compatibili con git worktrees
    
- Richiedono `git submodule update` manuale dopo switch branch
    
- Complessità nel sincronizzare modifiche tra repo principale e submodule
    

## Git Subtree

**Subtree** è un'alternativa ai submodules, incorpora un repository esterno come sottodirectory mantenendo una storia unificata:[apollographql+1](https://www.apollographql.com/blog/how-apollo-manages-swift-packages-in-a-monorepo-with-git-subtrees)​

bash

`# Aggiunta di un subtree git subtree add --prefix=libs/external-lib https://github.com/user/lib.git main --squash # Pull di aggiornamenti dal repository esterno git subtree pull --prefix=libs/external-lib https://github.com/user/lib.git main --squash # Push di modifiche locali al repository esterno git subtree push --prefix=libs/external-lib https://github.com/user/lib.git feature-branch`

**Vantaggi**: storia unificata, più semplice per contribuire modifiche upstream.[timhutt](https://blog.timhutt.co.uk/against-submodules/)​

## Monorepo vs Polyrepo

**Monorepo**: singolo repository contenente multipli progetti:[reddit+2](https://www.reddit.com/r/git/comments/zgct19/monorepo_multirepo_and_git_submodules/)​

**Vantaggi**:

- Visibilità unificata del codebase
    
- Refactoring cross-project semplificato
    
- Condivisione di codice immediata
    
- Atomic changes cross-project
    

**Svantaggi**:

- Repository di grandi dimensioni
    
- Clonazione e operazioni più lente
    
- Controllo accessi granulare limitato
    

**Gestione Monorepo con Submodules**:[thebottleneckdev+1](https://thebottleneckdev.com/blog/monorepo-git-submodules)​

bash

`# Repository monorepo con submodules per progetti individuali mkdir monorepo && cd monorepo git init git submodule add https://github.com/org/project-one.git packages/project-one git submodule add https://github.com/org/project-two.git packages/project-two # Workflow sviluppo: lavoro su submodule cd packages/project-one git checkout -b feature-x # modifiche… git commit -am "Feature X" git push origin feature-x # Update riferimento nel monorepo cd ../.. git add packages/project-one git commit -m "Update project-one to feature-x"`

## Garbage Collection e Ottimizzazione Repository

## Git Garbage Collection (GC)

Git accumula oggetti "orfani" e ridondanti nel tempo. **git gc** pulisce e ottimizza il repository:[atlassian+2](https://www.atlassian.com/git/tutorials/git-gc)​

bash

`# GC automatico (eseguito periodicamente) git gc --auto # GC manuale git gc # GC aggressivo (ricompressione completa, più lento ma più efficace) git gc --aggressive # Prune objects più vecchi di 2 settimane git gc --prune=2.weeks.ago # Forzare prune immediato git gc --prune=now`

**Cosa fa GC**:[graphite+2](https://graphite.dev/guides/git-garbage-collection)​

1. **Rimozione oggetti irraggiungibili**: elimina commit orfani non referenziati
    
2. **Packing**: combina oggetti in packfile compressi
    
3. **Delta compression**: memorizza solo differenze tra oggetti simili
    
4. **Repack**: ottimizza packfile esistenti
    

**Packfiles e Delta Compression**:[geeksforgeeks+2](https://www.geeksforgeeks.org/git/git-packfiles/)​

bash

`# Manuale repacking git repack -a -d # Verifica packfile git verify-pack -v .git/objects/pack/pack-*.idx`

Git usa **delta compression** per ridurre storage: invece di salvare copie complete di file simili, memorizza solo le differenze. Ad esempio, se `file-v1.txt` (10 MB) e `file-v2.txt` differiscono solo per 100 KB, Git può salvare v1 completo e v2 come delta (+100 KB, -50 KB), risparmiando circa 9.95 MB.[geeksforgeeks+1](https://www.geeksforgeeks.org/git/git-packfiles/)​

## Configurazione GC Automatico

bash

`# Configura soglia per GC automatico git config --global gc.auto 6700 # Tempo di retention per reflog git config --global gc.reflogExpire "90 days" # Logging verboso git config --global gc.verbose true`

## Esempi Pratici Integrati

## Scenario 1: Feature Development con Rebase

bash

`# Setup iniziale git checkout main git pull origin main git checkout -b feature/user-profile # Sviluppo feature echo "Profile page" > profile.html git add profile.html git commit -m "feat: Add user profile page" echo "Profile CSS" > profile.css git add profile.css git commit -m "style: Add profile styling" # Main è avanzato nel frattempo git fetch origin main # Rebase per mantenere storia lineare git rebase origin/main # Risoluzione conflitti (se presenti) # … modifica file conflittuali … git add . git rebase --continue # Push con force (storia riscritta) git push -f origin feature/user-profile # Merge tramite pull request o locale git checkout main git merge --no-ff feature/user-profile git push origin main`

## Scenario 2: Hotfix Urgente in Produzione

bash

`# Identificazione bug in produzione (main) git checkout main git pull origin main # Creazione hotfix branch git checkout -b hotfix/critical-security-fix # Fix del bug echo "Fixed vulnerability" >> security.patch git add security.patch git commit -m "fix: Patch critical security vulnerability" # Test rapido npm test # Merge in main git checkout main git merge hotfix/critical-security-fix git tag -a v1.0.1 -m "Security hotfix v1.0.1" git push origin main --tags # Merge anche in develop per mantenere sincronizzazione git checkout develop git merge hotfix/critical-security-fix git push origin develop # Pulizia git branch -d hotfix/critical-security-fix`

## Scenario 3: Collaborazione con Stash e Cherry-Pick

bash

`# Lavoro in corso su feature-A git checkout feature-A # … modifiche non committate … # Richiesta urgente di lavorare su feature-B git stash save "WIP: feature-A - authentication logic" # Switch a feature-B git checkout feature-B # … lavoro su feature-B … git commit -am "Complete feature-B implementation" # Identifico commit utile per feature-A git log --oneline # abc123 Add validation utility # Torno a feature-A git checkout feature-A # Cherry-pick del commit utile git cherry-pick abc123 # Recupero lavoro precedente git stash pop # Risoluzione conflitti stash (se presenti) # … modifica file … git add . # Continuo sviluppo feature-A git commit -am "Complete feature-A with validation"`

## Scenario 4: Recupero da Errore con Reflog

bash

`# Reset accidentale troppo indietro git log --oneline # 123abc Feature X # 456def Feature Y # 789ghi Feature Z git reset --hard 789ghi # Ops! Volevo tornare a 456def, non 789ghi # Reflog salva tutto git reflog # 789ghi HEAD@{0}: reset: moving to 789ghi # 456def HEAD@{1}: commit: Feature Y # 123abc HEAD@{2}: commit: Feature X # Recupero posizione corretta git reset --hard HEAD@{1} # Alternativa: reset a commit specifico git reset --hard 456def`

## Scenario 5: Pulizia Storia con Interactive Rebase

bash

`# Visualizza ultimi 5 commit git log --oneline -5 # abc123 Fix typo in docs # def456 Update tests # ghi789 Implement feature X # jkl012 WIP: partial implementation # mno345 Start feature X # Interactive rebase per pulire storia git rebase -i HEAD~5 # Editor mostra: pick mno345 Start feature X pick jkl012 WIP: partial implementation pick ghi789 Implement feature X pick def456 Update tests pick abc123 Fix typo in docs # Riorganizza e squash: pick mno345 Start feature X squash jkl012 WIP: partial implementation squash ghi789 Implement feature X reword def456 Update tests fixup abc123 Fix typo in docs # Risultato: 2 commit puliti invece di 5 frammentati`

## Configurazione Git Avanzata

## Configurazione Globale e Locale

bash

`# Identità utente git config --global user.name "Mario Rossi" git config --global user.email "mario@example.com" # Editor predefinito git config --global core.editor "vim" # Diff e merge tool git config --global diff.tool vimdiff git config --global merge.tool meld # Colorazione output git config --global color.ui auto # Alias utili git config --global alias.co checkout git config --global alias.br branch git config --global alias.ci commit git config --global alias.st status git config --global alias.unstage 'reset HEAD --' git config --global alias.last 'log -1 HEAD' git config --global alias.lg "log --graph --oneline --decorate --all" # Configurazione locale (per repository specifico) git config --local user.email "work@company.com" # Visualizzazione configurazione git config --list git config --global --list git config user.name`

## File .gitignore

bash

`# .gitignore esempi # Dipendenze node_modules/ vendor/  # File build dist/ build/ *.o *.pyc __pycache__/  # IDE .vscode/ .idea/ *.swp *.swo  # Sistema operativo .DS_Store Thumbs.db  # Secrets .env *.pem config/secrets.yml  # Logs *.log logs/  # Pattern avanzati # Ignora tutti i .txt tranne important.txt *.txt !important.txt # Ignora files in qualsiasi directory temp **/temp/`

## Gitattributes per Gestione Fine-Grained

bash

`# .gitattributes # Normalizzazione line endings * text=auto *.sh text eol=lf *.bat text eol=crlf # File binari *.png binary *.jpg binary *.pdf binary  # Diff personalizzati *.json diff=json *.md diff=markdown # Merge strategies personalizzate database.lock merge=ours`

## Comandi di Debug e Diagnostica

## Git Bisect: Ricerca Binaria di Bug

bash

`# Inizia bisect git bisect start # Marca commit corrente come bad git bisect bad # Marca ultimo commit funzionante come good git bisect good v1.0.0 # Git checkout automaticamente commit intermedio # Testa e marca: # - Se funziona: git bisect good # - Se bug presente: git bisect bad # Git continua ricerca binaria automaticamente # Ripeti fino a identificazione commit problematico # Automazione con script git bisect run npm test # Fine bisect git bisect reset`

## Git Blame: Annotazioni Riga per Riga

bash

`# Mostra autore per ogni riga git blame file.txt # Limita a righe specifiche git blame -L 10,20 file.txt # Ignora whitespace changes git blame -w file.txt # Mostra email invece di nome git blame -e file.txt`

## Git Log Avanzato

bash
```bash
# Log grafico compatto
git log --graph --oneline --decorate --all 

# Log con statistiche modifiche 
git log --stat 

# Log con diff complete 
git log -p 

# Filtro per autore 
git log --author="Mario Rossi" 

# Filtro per data 
git log --since="2 weeks ago" --until="yesterday" 

# Filtro per messaggio commit 
git log --grep="fix" 

# Log per file specifico 
git log -- path/to/file.txt

# Log con formato personalizzato 
git log --pretty=format:"%h - %an, %ar : %s"

# Trova commit che modificano una stringa specifica (pickaxe) 
git log -S"function_name" 

# Conta commit per autore 
git shortlog -sn
```
## Conclusione

Git rappresenta uno strumento fondamentale per lo sviluppo software moderno, combinando potenza tecnica con flessibilità operativa. La comprensione profonda della sua architettura interna—dall'object database content-addressable basato su SHA-1, alle tre aree fondamentali (working directory, staging area, repository), passando per le strategie di branching, merge e collaborazione distribuita—permette agli sviluppatori di sfruttare appieno le sue capacità.

I concetti avanzati come rebase interattivo, cherry-pick, hooks, submodules, delta compression e garbage collection offrono strumenti potenti per ottimizzare workflow complessi, mantenere repository efficienti e automatizzare processi ripetitivi. La padronanza di Git non si limita alla conoscenza dei comandi, ma richiede la comprensione dei principi sottostanti che guidano il suo design distribuito e content-addressable.

Attraverso una pratica costante e l'applicazione dei pattern illustrati—dal semplice feature branch workflow fino alle strategie articolate come Gitflow—gli sviluppatori possono collaborare efficacemente in team di qualsiasi dimensione, mantenendo codebasi pulite, tracciabili e resilienti.