---
last modified: 2025, 11, 15 22:11:27
related:
  - '[[Linguaggio di programmazione]]'
parent note: '[[Programmazione orientata agli oggetti (OOP)]]'
tags:
  - java
  - object-oriented-programming
  - linguaggi-programmazione
---
# Java
==**Java** è un [[Linguaggio orientato agli oggetti]]== inizialmente rilasciato da [Sun Microsystems](https://en.wikipedia.org/wiki/Sun_Microsystems) (acquisita da Oracle). Il principale vantaggio di Java è la sua portabilità: l'obiettivo del suo inventore [James Gosling](https://nighthacks.com/jag/bio/index.html), era quello di poter *"scrivere una volta, eseguire ovunque"* (computers, data centers, dispositivi mobili, console di gioco, dispositivi medici, ecc…).

![[Java program lifecycle.svg#center|600]]
* **[[Java syntax]]**: si basa su [[C (Linguaggio di programmazione)|C]] e [[C++]];
	* Java e [[JavaScript]] sono diversi tra loro: è necessario compilare Java, non lo è per JavaScript.
* [[Variabile Java]]:
* [[Java Type Casting]]

> [!NOTE] Ciclo di vita di un programma Java
> Il codice sorgente Java scritto in un file `.java` viene compilato dal compilatore Java (javac) in linguaggio *bytecode* conservato in files `.class`, per essere successivamente interpretato dalla [Java Virtual Machine (JVM)](https://en.wikipedia.org/wiki/Java_virtual_machine) in modo da essere eseguito su una piattaforma specifica. Quando un programma Java è eseguito, la JVM:
> 1. Carica queste classi compilate in memoria attraverso una serie di processi;
> 2. Verifica la compliance di sicurezza del bytecode
> 3. Performa compilazione Just-In-Time (JIT) per tradurre bytecode in machine code
> 4. Esegue il programma mentre gestisce le risorse di sistema
> 	- In esecuzione, la JVM gestisce anche la [[garbage collection]] riprendendo memoria da oggetti non più utilizzati
> 	- Finita l'esecuzione rilascia tutte le risorse 
>
>Questo meccanismo rende Java indipendente dalla piattaforma, buon equilibro portabilità prestazioni poiché il bytecode può essere eseguito su qualsiasi dispositivo compatibile con una JVM.