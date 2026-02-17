---
last modified: 2025, 11, 10 21:11:36
related: null
parent note: '[[Java modifier]]'
tags:
  - java-modifiers
  - access-modifiers
  - object-oriented-programming
---
# Java non-access modifiers
- [[static (Modificatore di non accesso)]]: un metodo che appartiene ad una classe, non ad un oggetto.
- [[final (Modificatore di non accesso)]]: metodo che vieta la riassegnazione di una variabile in un secondo momento;

- [[abstract (Modificatore di non accesso)]]: un metodo astratto appartiene ad una classe astratta


## Tips and Best Practices

- **Use Access Modifiers Wisely**: Restrict access as much as possible to protect your data. Use `private` for fields unless they need to be accessed outside the class.
- **Static Usage**: Use `static` for utility methods and constants that do not require object state.
- **Final for Constants**: Declare constants using `final` and `static` to prevent modification.
- **Abstract Classes**: Use `abstract` classes as base classes that should not be instantiated directly.
- **Synchronized for Thread Safety**: Use `synchronized` to ensure thread safety when necessary, but be aware of potential performance impacts.
- **Volatile for Visibility**: Use `volatile` for variables shared between threads to ensure visibility of changes.
- **Transient for Serialization**: Use `transient` to exclude fields from serialization when they should not be part of the serialized object.