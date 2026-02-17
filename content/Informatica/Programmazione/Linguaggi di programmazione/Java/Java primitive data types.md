---
last modified: 2025, 11, 10 19:11:58
related: null
parent note: '[[Java data types]]'
tags:
  - java-data-types
  - linguaggi-programmazione
  - computer-science
---
# Java primitive data types
I **tipi di dato primitivi** in [[Java]] sono delle [[Java keyword|keywords]], rappresentano "valori grezzi".

| Tipo                                      | Dimensione | Intervallo min        | Intervallo max       | Descrizione                                                                          |
| ----------------------------------------- | ---------- | --------------------- | -------------------- | ------------------------------------------------------------------------------------ |
| **[[byte (Java data type)\|byte]]**       | 8 bit      | $-128$                | $+127$               | Tipo intero a 8 bit con segno. Usato per risparmiare memoria in array o dati binari. |
| **[[short (Java data type)\|short]]**     | 16 bit     | $-32.768$             | $+32.767$            | Tipo intero a 16 bit con segno. Usato per compatibilità o ottimizzazione memoria.    |
| **[[int (Java data type)\|int]]**         | 32 bit     | $-2^{31}$             | $2^{31}-1$           | Tipo predefinito per interi, utilizzato nella maggior parte dei casi.                |
| **[[long (Java data type)\|long]]**       | 64 bit     | $-2^{63}$             | $2^{63}-1$           | Tipo intero a 64 bit per intervalli estesi. Suffisso `L` (es. `123L`).               |
| **[[float (Java data type)\|float]]**     | 32 bit     | $\sim{ 1.4×10^{-45}}$ | $\sim{3.4×10^{38}}$  | Virgola mobile a precisione singola. Suffisso `f` (es. `3.14f`).                     |
| **[[double (Java data type)\|double]]**   | 64 bit     | $\sim{4.9×10^{-324}}$ | $\sim{1.7×10^{308}}$ | Virgola mobile a precisione doppia. Tipo predefinito per decimali.                   |
| **[[boolean (Java data type)\|boolean]]** | -          | `false`               | `true`               | Tipo logico per condizioni e controlli. Non convertibile in numeri.                  |
| **[[char (Java data type)\|char]]**       | 16 bit     | `\u0000` (0)          | `\uffff` (65.535)    | Carattere Unicode singolo. Usato per lettere, simboli e caratteri speciali.          |

> [!EXAMPLE] Esempio di primitive in Java
> ```java
> class DataTypes {
>     public static void main(String[] args) {
>         // Integer data types
>         byte byteVar = 100; // -128 to 127
>         short shortVar = 10000; // -32,768 to 32,767
>         int intVar = 100000; // -2147483648 to 2147483647
>         long longVar = 100000L; // -9223372036854775808 to 9223372036854775807
> 
>         // Floating-point data types
>         float floatVar = 10.5f; // 1.4E-45 to 3.4028235E38
>         double doubleVar = 20.99; // 4.9E-324 to 1.7976931348623157E308
> 
>         // Character data type
>         char CopyrightSymbol = '\u00A9';
> 
>         // Boolean data type
>         boolean boolVar = true;
>     }
> } 
> ```