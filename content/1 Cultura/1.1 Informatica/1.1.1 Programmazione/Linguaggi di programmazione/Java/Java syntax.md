---
last modified: 2025, 11, 10 18:11:52
related: null
parent note: '[[Java]]'
tags:
  - java
  - linguaggi-programmazione
  - software-development
---
# Java syntax
La **sintassi Java** è tutto ciò che scrivi in un file `.java` che il compilatore deve ricompilerà in bytecode. In altre parole è la sequenza di caratteri che dà significato al codice. Riconosciamo i seguenti componenti principali:
- [[Java token]]: gli elementi più basilari che il compilatore riconosce;
- [[Java data types]]: come dichiarare ed usare variabili;
- [[Java hierarchy]]: definisce la gerarchia e organizzazione del codice;
- [[Java instructions]]: le azioni che il programma può eseguire e controllo dell'ordine di esecuzione.


> [!EXAMPLE] Hello World in Java
> ```java
> public class Main {
>   public static void main(String[] args) {
>     System.out.println("Hello World");
>   }
> }
> ```

> [!NOTE] Consigli generali sulla sintassi Java
> - Ogni applicazione Java inizia con una classe il cui nome deve essere lo stesso del file perché [[Java]] usa il nome della classe per trovare ed eseguire il codice.
> - Ogni linea di codice deve essere inserita in una [[Java class]], il cui nome deve iniziare sempre con una maiuscola;
> - *Java è case sensitivity* quindi `MyClass` e `myclass` verranno trattati in maniere diverse