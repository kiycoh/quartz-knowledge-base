---
last modified: 2025-10-31T13:10:57.000Z
related: null
parent note: null
tags:
  - java
  - linguaggi-programmazione
  - object-oriented-programming
---
# Metodi Java predefiniti
I metodi Java predefiniti sono [[Java method|metodi]] già scritti e inclusi in Java API, possono essere richiamati direttamente perché definiti a priori.


### Metodi Fondamentali (dalla classe `Object`)

Questi metodi sono disponibili su _qualsiasi_ oggetto in Java, poiché tutti gli oggetti ereditano (direttamente o indirettamente) dalla classe `Object`.

- `equals(Object obj)`: Controlla se due oggetti sono "uguali" (la definizione di "uguale" dipende da come il metodo è implementato nella classe).
    
- `toString()`: Restituisce una rappresentazione in formato stringa dell'oggetto. È utilissimo per il debug (es. quando stampi un oggetto in console).
    
- `hashCode()`: Restituisce un numero intero (hash) che rappresenta l'oggetto. È fondamentale per il funzionamento di `HashMap` e `HashSet`.
    
- `getClass()`: Restituisce la classe dell'oggetto a runtime.
    

---

### 📄 Metodi della classe `String`

Probabilmente la classe più usata in assoluto. Le stringhe sono immutabili, quindi questi metodi **restituiscono sempre una nuova stringa** senza modificare l'originale.

- `length()`: Restituisce il numero di caratteri nella stringa.
    
- `charAt(int index)`: Restituisce il carattere (tipo `char`) all'indice specificato.
    
- `substring(int beginIndex, int endIndex)`: Estrae una nuova stringa da quella originale, partendo dall'indice `beginIndex` (incluso) fino a `endIndex` (escluso).
    
- `equals(Object anotherObject)`: Confronta questa stringa con un altro oggetto (case-sensitive).
    
- `equalsIgnoreCase(String anotherString)`: Confronta due stringhe ignorando le differenze tra maiuscole e minuscole.
    
- `indexOf(String str)`: Trova l'indice della prima occorrenza di una sotto-stringa.
    
- `toLowerCase()` / `toUpperCase()`: Converte l'intera stringa in minuscolo o maiuscolo.
    
- `trim()`: Rimuove gli spazi bianchi all'inizio e alla fine della stringa.
    
- `split(String regex)`: Divide la stringa in un array di stringhe (`String[]`) basandosi su un delimitatore (spesso uno spazio `" "`, una virgola `","` o un'espressione regolare).
    
- `replace(CharSequence target, CharSequence replacement)`: Sostituisce tutte le occorrenze di una sotto-stringa con un'altra.
    
- `isEmpty()`: Restituisce `true` se la stringa ha lunghezza 0.
    
- `isBlank()` (da Java 11): Restituisce `true` se la stringa è vuota o contiene solo spazi bianchi.
    
- `String.format(String format, Object... args)`: (Come discusso prima!) Crea una stringa formattata.
    
- `String.valueOf(Object obj)`: Metodo _statico_ che converte qualsiasi tipo (primitivo o oggetto) in una stringa.
    

---

### 🗃️ Metodi delle Collezioni (Interfacce `List`, `Map`, `Set`)

Questi sono i cavalli di battaglia per gestire gruppi di dati.

#### `List` (es. `ArrayList`)

- `add(E element)`: Aggiunge un elemento alla fine della lista.
    
- `get(int index)`: Recupera l'elemento all'indice specificato.
    
- `set(int index, E element)`: Sostituisce l'elemento all'indice specificato.
    
- `remove(int index)` / `remove(Object o)`: Rimuove un elemento (per indice o per oggetto).
    
- `size()`: Restituisce il numero di elementi nella lista.
    
- `isEmpty()`: Controlla se la lista è vuota.
    
- `contains(Object o)`: Controlla se la lista contiene un determinato elemento.
    

#### `Map` (es. `HashMap`)

- `put(K key, V value)`: Associa un valore a una chiave (se la chiave esiste, aggiorna il valore).
    
- `get(Object key)`: Recupera il valore associato a una chiave (restituisce `null` se la chiave non esiste).
    
- `remove(Object key)`: Rimuove la coppia chiave-valore associata alla chiave.
    
- `containsKey(Object key)`: Controlla se la mappa contiene la chiave specificata.
    
- `size()`: Restituisce il numero di coppie chiave-valore.
    
- `keySet()`: Restituisce un `Set` contenente tutte le chiavi.
    
- `values()`: Restituisce una `Collection` contenente tutti i valori.
    
- `entrySet()`: Restituisce un `Set` di coppie (`Map.Entry`) (usatissimo per iterare sulle mappe).
    

---

### 🌊 Metodi della Stream API (da Java 8)

Questi metodi vengono usati per l'elaborazione "funzionale" delle collezioni. Sono estremamente potenti e molto comuni nel codice moderno.

- `stream()`: (Chiamato su una collezione, es. `miaLista.stream()`) Converte la collezione in uno "stream" per l'elaborazione.
    
- `filter(Predicate p)`: Filtra gli elementi dello stream, tenendo solo quelli che soddisfano una condizione.
    
- `map(Function f)`: Trasforma ogni elemento dello stream in qualcos'altro (es. da un oggetto `Utente` al suo `nome`).
    
- `forEach(Consumer c)`: Esegue un'azione su ogni elemento (spesso usato come passo finale, es. `forEach(System.out::println)`).
    
- `collect(Collector c)`: Raccoglie i risultati dello stream in una nuova collezione (es. `Collectors.toList()` per rimetterli in una lista).
    
- `findFirst()` / `findAny()`: Trova il primo (o uno qualsiasi) elemento che corrisponde ai filtri.
    

---

### 🧮 Metodi Matematici (Classe `Math`)

Questi sono tutti metodi _statici_, quindi li chiami direttamente sulla classe `Math`.

- `Math.max(a, b)`: Restituisce il più grande tra due numeri.
    
- `Math.min(a, b)`: Restituisce il più piccolo tra due numeri.
    
- `Math.abs(num)`: Restituisce il valore assoluto.
    
- `Math.round(double num)`: Arrotonda un numero decimale all'intero più vicino.
    
- `Math.ceil(double num)`: Arrotonda per eccesso (all'intero superiore).
    
- `Math.floor(double num)`: Arrotonda per difetto (all'intero inferiore).
    
- `Math.random()`: Restituisce un numero `double` casuale tra 0.0 (incluso) e 1.0 (escluso).
    
- `Math.pow(double base, double exponent)`: Calcola la potenza.
    

---

### 🖥️ Metodi di Utility e Stampa

- `System.out.println(Object o)`: Il metodo più usato in assoluto per il debug. Stampa l'oggetto (chiamando il suo `toString()`) sulla console e va a capo.
    
- `System.out.print(Object o)`: Come `println` ma non va a capo.
    
- `Arrays.toString(array[])`: Metodo _statico_ utilissimo per stampare il contenuto di un array in modo leggibile (es. `[1, 2, 3]`).
    
- `Arrays.asList(T... items)`: Metodo _statico_ che crea rapidamente una lista (di dimensione fissa) a partire da un elenco di elementi.
    
- `Collections.sort(List list)`: Metodo _statico_ per ordinare una lista.
    

Vuoi approfondire una di queste categorie, ad esempio come funzionano i metodi delle collezioni o gli Stream?