---
last modified: 2025-07-12T19:00:00.000Z
related:
  - '[[Hash table]]'
tags:
  - database-design
  - database-management-system
  - indexing-slicing
---
# Definizione di tabelle a indirizzamento diretto
Nelle **tabelle a indirizzamento diretto**, la chiave di un elemento corrisponde direttamente alla sua posizione nella tabella. Tuttavia, questo approccio è efficiente solo se il numero di chiavi effettivamente utilizzate è paragonabile alla dimensione dell'universo di chiavi (`|U|`), altrimenti si incorre in spreco di spazio.