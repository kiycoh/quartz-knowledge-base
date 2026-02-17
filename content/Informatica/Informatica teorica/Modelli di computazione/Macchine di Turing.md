---
last modified: 2025-05-25T16:44:00.000Z
related:
  - '[[Informatica teorica]]'
  - '[[Test di Turing]]'
tags:
  - informatica-teorica
  - test-turing
  - algoritmo
---
# Il programma Hilbertiano
[[Informatica teorica]]

"*La matematica può essere resa completamente algoritmica o ci saranno sempre nuovi problemi che superano qualsiasi algoritmo dato, e quindi richiedono atti creativi della ente per essere risolti?*"

Nel 1920 il matematico e logico David Hilbert, preoccupato degli attacchi alla coerenza della matematica all'inizio del XX secolo, abbozza un programma di ricerca volta a fornire un nuovo fondamento alla disciplina. La sua speranza è che il programma possa consolidare le conquiste, ed al tempo stesso risolvere le preoccupazioni sulla coerenza della matematica, dimostrando che la matematica può essere riformulata utilizzando una base logica solida. Questo lavoro di ricerca prenderà il nome di "Programma di Hilbert"

> *Algoritmo = metodo di risoluzione automatico del problema*

## Godel e l'incompletezza
*Dato un qualsiasi sistema formale basato su assiomi e regole, esisteranno sempre in questo sistema delle proposizioni vere, ma la cui verità non può essere dimostrata facendo uso degli assiomi e delle regole*. ^Godel-incompletezza

Nel 1931 una risposta negativa al quesito posto da Hilbert arriva dal logico Austriaco Kurt Godel, sotto forma dei suoi teoremi di incompletezza
La dimostrazione dei teoremi di completezza, ancora oggi attuale e non facile da comprendere, si basa essenzialmente sulla finitezza dei sistemi formali.

## Turing e l'algoritmizzazione
Quello che manca nel lavoro di Godel è una caratterizzazione precisa e operazionalizzabile del concetto di algoritmo. Con il suo articolo del 1936, il matematico Turing fornisce una contemporaneamente una caratterizzazione funzionale del concetto di algoritmo, definisce un modello di computazione che risulterà essere il paradigma dei computer moderni, e di fatto costituisce il primo mattone per la costruzione dell'edificio e delle scienze dell'informazione.

*Le intuizioni di Turing sull'algoritmica intesa come...*
- **Manipolazione di simboli, non di numeri** (idea Hilbertiana): l'attenzione si sposta non sui numeri ma sui simboli che essi rappresentano e sulle regole utilizzate per operare sui simboli.

- **Procedura interamente deterministica** ("il salto nel buio" algoritmico, la proprietà di determinismo degli algoritmi). Gli algoritmi vengono eseguiti, dopo essere stati scritti, da una macchina completamente automatica e non supervisionata-

- **Sganciata dall'implementazione fisica**. Per quanto Turing costruisca una macchina ideale, gli elementi che la compongono sono astratti e possono essere implementati indipendentemente dall'hardware. (Una macchina di Turing è ideale ed immaginaria, irrealizzabile)

- **Basata sulle codifiche**. Turing dimostra che ogni calcolo simbolico può essere simulato utilizzando solo due simboli, tramite riscrittura.

# Cos'è una macchina di Turing

Turing affronta il problema di fornire un equivalente rigoroso del concetto intuitivo di algoritmo definendo **un modello dell'attività di un essere umano** che stia eseguendo un calcolo di tipo algoritmico.

Questo modello prende forma in una classe di dispostivi computazionali, di macchine calcolatrici astratte, nel senso che, nel caratterizzarle, non vengono presi in considerazione quei vincoli che sono fondamentali se si intende progettare una macchina calcolatrice reale e soprattutto nel senso che esse sono definite **a prescindere dalla loro realizzazione fisica**.

Un calcolo consiste nell'**operare su di un certo insieme di simboli** scritti su un supporto fisico, ad esempio un foglio di carta.

## Definizione formale di macchina di Turing

![[2.4 Macchine di Turing_image_1.png]]

## Caratteristiche della macchina di Turing

- La macchina di Turing utilizza per la "scrittura" un nastro monodimensionale di lunghezza virtualmente illimitata in entrambe le direzioni (per questo La MdT è ideale). Questo nastro è suddiviso in celle, ogni cella ospita un simbolo alla volta.

- Ogni MdT dispone di un insieme finito di simboli (il suo alfabeto). Il fatto che l'alfabeto sia limitato non è una limitazione.

- La macchina può esaminare soltanto una cella alla volta, osserva ad ogni passo al più un singolo simbolo. Ogni cella è disposta di un dispositivo di lettura.

- L'operatore può scrivere nuovi simboli, di cancellare quelli già scritti (da continuare dalle slide.)

- La MdT assume un certo numero finito di stati interni (uno e non più di uno alla volta), che corrispondono agli "stati mentali". Secondo Turing "se ammettessimo un'infinità di stati mentali, alcuni di essi sarebbero arbitrariamente prossimi e quindi confusi". Il numero finito di stati non costituisce un vincolo, in quanto "l'uso di stati mentali più complicati può essere evitato scrivendo più simboli sul nastro".

## Architettura della macchina di Turing

Si hanno dei dati in ingresso, dati in uscita e il programma. 
I dati in ingresso e in uscita **risiedono sullo stesso nastro** (che fa quindi da input e da output, quindi accetta o rifiuta). Ogni cella contiene un solo simbolo. 
Il programma è l'insieme di istruzioni (nelle limitazioni della macchina di Turing).

*Riassumendo le differenze tra* **automi finiti deterministici** *e macchine di Turing:*
1. Una macchina di Turing può sia scrivere che leggere sul nastro.
2. La testina di lettura-scrittura può muoversi sia verso sinistra che verso destra.
3. Il nastro è infinito.
4. Gli stati speciali di accettazione e rifiuto hanno effetto immediato.

## Qual è la potenza di calcolo di una macchina di Turing?
La stessa del più potente dei calcolatori. Mantenendo la struttura corrente dei calcolatori (inclusi quelli quantistici), la MdT è il più potente tra tutti i calcolatori.
## Funzionamento della macchina di Turing

1. Riceve l'input su *n* celle più a sinistra del nastro, mentre il resto del nastro è vuoto.
2. La testina di lettura parte dalla posizione più a sinistra del nastro e legge i simboli per ogni singola cella.
3. La macchina inizia la computazione secondo le regole descritte dalla funzione di transizione. La computazione prosegue fin quando la macchina raggiunge lo stato di accettazione o di rifiuto. Se nessuno dei due stati viene raggiunto la macchina va avanti per sempre.

Durante la computazione si verificano cambiamento dello *stato corrente*, del *contenuto corrente del nastro* e della *posizione corrente della testina*. Un'impostazione di questi 3 elementi è chiamata **configurazione**

# Linguaggio Turing Riconoscibile
Un linguaggio è decidibile quando il linguaggio è il suo complemento sono Turing riconoscibili.
