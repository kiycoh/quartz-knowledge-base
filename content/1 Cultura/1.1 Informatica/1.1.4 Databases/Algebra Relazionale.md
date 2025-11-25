---
last modified: 2025-05-24T23:11:00.000Z
related: null
tags:
  - algebra-relazionale
  - database-design
  - informatica-teorica
---


# Definizione di algebra relazionale
L'algebra relazionale è un formalismo matematico utilizzato per definire e manipolare le query sui database relazionali. È un linguaggio di interrogazione teorico che fornisce un insieme di operazioni per estrarre e combinare dati da tabelle (o relazioni) in un [[database]]. È stata introdotta da Edgar F. Codd nel 1970 per promuovere l'indipendenza dei dati.

![[Pasted image 20241015150515.png|600]]

L'algebra relazionale è composta da un insieme di operatori che operano su relazioni e producono nuove relazioni come output. Questi operatori possono essere composti insieme per formare espressioni più complesse.
# Operazioni principali

L'algebra relazionale tratta le relazioni come insiemi, quindi sono applicabili [[Operatori insiemistici]] come unione, intersezione e differenza. Questi operatori possono essere applicati solo a relazioni definite sugli stessi attributi, il che significa che possono operare solo su tuple uniformi.

>[!WARNING]-
>Gli operatori insiemistici possono essere applicati solo a relazioni con schemi identici, il che significa che possono operare solo su tuple uniformi.

Gli operatori nell'algebra relazionale possono essere classificati come segue:
- Operatori insiemistici: unione, intersezione, differenza
## Selezione (σ)
L'operatore di selezione in algebra relazionale, denotato con $\sigma$ , è un operatore monadico (che ha un solo argomento) che estrae un sottoinsieme di tuple da una relazione in base a una condizione specificata. Questo operatore produce una nuova relazione che ha lo stesso schema dell'operando originale, ma contiene solo le tuple che soddisfano la condizione.

La condizione di selezione è un'espressione booleana che può combinare condizioni atomiche usando i [[Connettivi logici (Informatica Teorica)|connettivi logici]] AND ($∧$), OR ($∨$) e NOT ($¬$). Le condizioni atomiche confrontano i valori degli attributi con costanti o con altri attributi utilizzando [[Operatori di confronto]].

> [!EXAMPLE] Esempio pratico di applicazione dell'operatore 'Selezione'
Si consideri la seguente relazione Impiegati:
>
| Cognome | Filiale | Stipendio | Matricola |
| ------- | ------- | --------- | --------- |
| Neri    | Milano  | 645998    | 1         |
| Rossi   | Roma    | 357309    | 2         |
| Neri    | Napoli  | 645698    | 3         |
| Milano  | Milano  | 449553    | 4         |
>
> Per estrarre gli impiegati che guadagnano più di 500,000, si può utilizzare la seguente espressione di selezione:
>
>```
σ Stipendio > 500000 (Impiegati)
>```
>
>Il risultato di questa operazione sarebbe la seguente relazione:
>
| Cognome | Filiale | Stipendio | Matricola |
| ------- | ------- | --------- | --------- |
| Neri    | Milano  | 645998    | 1         |
| Neri    | Napoli  | 645698    | 3         |

## Proiezione (π)
L'operatore di proiezione, denotato con π (pi greco), estrae un sottoinsieme di colonne (attributi) da una relazione. In altre parole, esegue una "decomposizione verticale", mantenendo solo le colonne specificate.

Sintassi:

```
π ListaAttributi (Relazione)
```

Semantica:

Il risultato dell'operazione di proiezione è una nuova relazione che contiene solo gli attributi elencati nella ListaAttributi. Le tuple nella nuova relazione mantengono i valori corrispondenti agli attributi selezionati.

Esempio:

Riprendendo la relazione Impiegati precedente, per estrarre solo i cognomi e i salari degli impiegati, si può usare la seguente espressione:

```
π Cognome, Stipendio (Impiegati)
```

Il risultato sarebbe:

|         |           |
| ------- | --------- |
| Cognome | Stipendio |
| Neri    | 645998    |
| Rossi   | 557309    |
| Neri    | 645698    |
| Milano  | 449553    |
## Ridenominazione (ρ)
L'operatore di ridenominazione, $\rho$, è un **operatore monadico** e modifica lo schema di una relazione rinominando uno o più attributi.
- L'operatore di ridenominazione è utile per rendere tuple di dati (o colonne) omogenee tra loro.

> [!EXAMPLE] Applicazione pratica dell'operatore ridenominazione
> L'obiettivo è utilizzare l'operatore di ridenominazione affinché tutte le tuple risultino omogenee..
> 
>Database 'Impiegati':
>
| Cognome | Ufficio | Stipendio |
| ------- | ------- | --------- |
| Rossi   | Roma    | 55        |
| Neri    | Milano  | 64        |
>\- - -
>Database 'Operai':
>
| Cognome | Fabbrica | Salario |
| ------- | -------- | ------- |
| Bruni   | Monza    | 45      |
| Verdi   | Latina   | 55      |
>
> ..infine utilizzo l'operatore unione per ottenere un unico database omogeneo che contiene tutte le informazioni contenute nelle basi principali:
>`P Sede,Retribuzione ← Ufficio, Stipendio(Impiegati) ∪ P Sede,Retribuzione ← Fabbrica, Salario(Impiegati)`
>
| Cognome | Sede   | Retribuzione |
| ------- | ------ | ------------ |
| Rossi   | Roma   | 55           |
| Neri    | Milano | 64           |
| Bruni   | Monza  | 45           |
| Verdi   | Latina | 55           |

### Sintassi:
```
ρ NuovoNomeRelazione (Relazione) 
```

oppure
```
ρ VecchioAttributo->NuovoAttributo (Relazione)
```
## Join (⨝)
### Join Naturale
Il join naturale è un caso speciale del theta-join dove la condizione θ è l'uguaglianza tra tutti gli attributi con lo stesso nome nelle due relazioni.

Sintassi:

```
Relazione1 ⋈ Relazione2
```

Semantica:

Il risultato del join naturale contiene tutte le combinazioni di tuple dalle due relazioni di input dove i valori degli attributi con lo stesso nome sono uguali.

Esempio:

Supponiamo che la relazione Impiegati abbia un attributo Reparto e la relazione Reparti abbia un attributo NomeReparto. Il join naturale Impiegati ⋈ Reparti combinerà le tuple dove Impiegati.Reparto = Reparti.NomeReparto.
### Theta-join
Il theta-join è una generalizzazione del join naturale che consente di specificare una condizione arbitraria (θ) per combinare le tuple delle due relazioni. La condizione θ può essere un qualsiasi predicato booleano.

Sintassi:

```
Relazione1 ⋈<sub>θ</sub> Relazione2
```

Semantica:

Il risultato del theta-join contiene tutte le combinazioni di tuple dalle due relazioni di input che soddisfano la condizione θ.

Esempio:

Per estrarre tutte le coppie di impiegati e reparti dove l'impiegato lavora in quel reparto, si potrebbe usare un theta-join con la condizione Impiegati.Reparto = Reparti.CodiceReparto.
### Semi join
Il semi-join restituisce le tuple della prima relazione che partecipano al join naturale con la seconda relazione.

Sintassi:

```
Relazione1 ⋉ Relazione2
```

Semantica:

Il risultato del semi-join contiene tutte le tuple di Relazione1 per le quali esiste una tupla in Relazione2 che soddisfa la condizione di join naturale.

Esempio:

Per ottenere una relazione contenente solo gli impiegati che lavorano in un reparto presente nella relazione Reparti, si può usare:

```
Impiegati ⋉ Reparti
```
## Prodotto Cartesiano (×)
Il prodotto cartesiano è un'operazione fondamentale in matematica che consente di costruire insiemi di coppie ordinate a partire da due insiemi. Se abbiamo due insiemi $A$ e $B$, il prodotto cartesiano di $A$ e $B$ è l'insieme di tutte le coppie ordinate $(a, b)$ dove $a \in A$ e $b \in B$.

>[!definizione] 
>Il prodotto cartesiano di due insiemi $A$ e $B$, indicato con $A \times B$, è l'insieme di tutte le coppie ordinate $(a, b)$ tali che $a \in A$ e $b \in B$. Matematicamente, $A \times B = {(a, b) | a \in A, b \in B}$.

- **Notazione**: Se $A = {1, 2}$ e $B = {x, y}$, allora $A \times B = {(1, x), (1, y), (2, x), (2, y)}$.
    
- **Proprietà**:
    - **Non Commutatività**: In generale, $A \times B \neq B \times A$. Ad esempio, se $A = {1}$ e $B = {x}$, allora $A \times B = {(1, x)}$, mentre $B \times A = {(x, 1)}$.
    - **Cardinalità**: Se $|A|$ è la cardinalità di $A$ (il numero di elementi in $A$) e $|B|$ è la cardinalità di $B$, allora la cardinalità di $A \times B$ è $|A| \times |B|$.

- **Estensioni**: Il concetto di prodotto cartesiano può essere esteso a più di due insiemi. Per esempio, il prodotto cartesiano di tre insiemi $A$, $B$, e $C$ è l'insieme delle triple ordinate $(a, b, c)$ con $a \in A$, $b \in B$, e $c \in C$.

#### NEW
Prodotto Cartesiano (×): L'operatore di prodotto cartesiano combina ogni tupla della prima relazione con ogni tupla della seconda relazione. Il risultato è una relazione con un numero di attributi pari alla somma degli attributi delle due relazioni di input.

Sintassi:

```
Relazione1 × Relazione2
```

Semantica:

Il risultato del prodotto cartesiano è una relazione che contiene tutte le possibili combinazioni di tuple dalle due relazioni di input.

Esempio:

Se la relazione Impiegati ha 4 tuple e la relazione Reparti ha 3 tuple, il prodotto cartesiano Impiegati × Reparti produrrà una relazione con 12 tuple (4 * 3).

> [!TIP]- Il modello relazionale
>  - Le relazioni sono insiemi e i risultati prodotti sono anch'essi relazioni. L'algebra relazionale può essere utilizzata solo con il modello di dati relazionale.
>  - Gli operatori possono essere combinati tra loro per creare espressioni complesse che consentono di estrarre informazioni specifiche dai dati relazionali.
>  - Tra questi, gli operatori *unione, differenza, selezione, proiezione e join naturale* sono considerati **operatori primitivi**.


## [[Operatori insiemistici]]

# Esempi
πTreno(σNome='Roma-Milano'∧ OrarioArrivo='')


proiezione Codice (selezione nomePartito=Partitodemocratico(partito)) join codicePart=codice proiezione percFavorevoli(sondaggi)

dobbiamo fare una relazione tra partiti e sondaggi attraverso una rinominazione tra codice (in partito) e CodPart (in sondaggi)

πNomeFarmaco, Prezzo(σCategoria="Antibiotico"((πCategoria, ID NomeFarmaco(sostanze))⨝(πNomeFarmaco, Prezzo , ρPrincipioAttivo=ID(Farmaci))))