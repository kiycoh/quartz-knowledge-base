---
last modified: 2024-10-02T03:38:00.000Z
related: '[[Python]]'
tags:
  - machine-learning
  - data-science
  - dictionary
---


> Vedi [[Hash table|le Hash Tables]]

==Un dictionary== ==è una collezione disordinata strutturata per duplice associazione utilizzando i parametri "**key:value"**==. I valori "**key:value**" sono separati tra loro da "," e sono inseriti tra {}. **Un valore può essere associato a più chiavi, le keys sono univoche**.

``` python
capitals = {"Italy":"Rome","France":"Paris"}
>>> capitals
>>> {"France","Paris","Italy":"Rome"}
```

*Possiamo manipolare i dictionaries*:
1. Accedendo al "**value**" (come un index) attraverso la "**key**":
``` python
for k in capitals:
print(capitals[k]," is the capital of ", k)
>>> print(capitals[k]," is the capital of ", k)
>>> "Paris is the capital of France"
>>> "Rome is the capital of Rome"
```

2. Aggiungendo un nuovo elemento "**key:value**":
``` python
capitals['Utah']='SaltLakeCity'
>>> capitals {"Utah":"SaltLakeCity","France":"Paris","Italy":"Rome"}
```

### Operatori su dictionary
| **Operatore** | **Uso** | **Spiegazione** |
| ---------- | --------- | --------- |
| \[] | dict\[k] | Ritorna il valore associato con *k*, altrimenti errore |
| in | key **in** dict | Ritorna *True* se "key" in dictionary, altrimenti *False* |
| del | del dict\[key] | Rimuove la chiave dal dictionary |

### Metodi su dictionary
| **Metodo** | **Uso** | **Spiegazione** |
| ---- | ---- | ---- |
| clear | dict.clear() | Rimuove tutti gli elementi dal dizionario. |
| copy | dict.copy() | Ritorna una copia del dizionario. |
| fromkeys | dict.fromkeys(x,y) | Ritorna un dizionario con le chiavi e i valori specificati. |
| keys | dict.keys() | Ritorna una lista contenente una tupla per ogni coppia chiave/valore. |
| values | dict.values() | Ritorna una lista di tutti i valori del dizionario. |
| items | dict.items | Ritorna i valori "key-value" in un dict_items object |
| ==get== | dict.get(k) | Ritorna elemento "value"  associato a *k*, altrimenti *None* |
| get | dict.get(k,alt) | Ritorna elemento "value" associato a *k*, altrimenti *alt* |
| ==pop== | dict.pop(k, def) | Rimuove il valore *k*, se la chiave non esiste ritorna *def* (parametro opzionale) |
| popitem | dict.popitem() | Rimuove l'ultimo elemento dal dizionario. |
| update | dict.update() | Aggiorna il dizionario con una coppia chiave/valore. |
#### Esempi
``` python
dict_keys(['brad', 'david'])
>>> list(phone_ext.keys())
['brad', 'david']

>>> "brad" in phone_ext
True

>>> 1137 in phone_ext
False    # 1137 is not a key in phone_ext
>>> phone_ext.values() # Returns the values of the dictionary
phone_ext
dict_values([1137, 1410])
>>> list(phone_ext.values())
[1137, 1410]
>>> phone_ext.items()
dict_items([('brad', 1137), ('david', 1410)])
>>> list(phone_ext.items())
[('brad', 1137), ('david', 1410)]
>>> phone_ext.get("kent")
>>> phone_ext.get("kent","NO ENTRY")
'NO ENTRY'
>>> del phone_ext["david"]
>>> phone_ext
{'brad': 1137}
```
---