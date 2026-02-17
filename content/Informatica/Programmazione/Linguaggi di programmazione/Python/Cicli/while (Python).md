---
last modified: 2025, 11, 10 18:11:57
tags:
  - python
  - machine-learning
  - programming
---
# while (Python)
Quando la condizione di continuazione del ciclo è più complessa e non è basata su un numero fisso di iterazioni noto in anticipo, un ciclo `while` può essere più flessibile.
``` python
# Prints out 0,1,2,3,4

count = 0
while count < 5:
    print(count)
    count += 1  # This is the same as count = count + 1
```