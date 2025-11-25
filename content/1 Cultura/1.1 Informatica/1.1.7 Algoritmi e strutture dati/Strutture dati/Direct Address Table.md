---
last modified: 2025, 11, 22 17:11:43
related: null
parent note: null
tags:
  - data-science
  - database-management
  - indexing-slicing
---
# Direct Address Table
- **Descrizione**: Strutture dati che permettono l'indirizzamento diretto degli elementi tramite la loro chiave, utilizzata come indice (come negli array).
    - **Operazioni**: `INDEX` in **O(1)**.
    - **Limiti**:
        - Spreco di spazio se l'universo di chiavi `U` è molto più grande delle chiavi effettivamente utilizzate.
        - Non possono memorizzare tutti gli elementi se il loro numero supera la dimensione di `U`.
    - **Utilizzo Pratico**: Quando l'universo delle chiavi è piccolo e denso.