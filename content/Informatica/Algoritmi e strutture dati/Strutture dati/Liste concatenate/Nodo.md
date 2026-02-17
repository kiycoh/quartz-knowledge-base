---
tags:
  - algoritmi-ordinamento
  - linked-list
  - data-science
---

Un nodo contiene informazioni:
- Data
- Pointer

``` python
# Node class 
class Node: 

	# Function to initialize the node object 
	def __init__(self, data): 
		self.data = data # Assign data 
		self.next = None # Initialize next as null 
```
# Head Pointer
L'Head punta al primo elemento della lista. Se la lista è vuota punta direttamente NULL o nulla.

``` python
# Linked List class 
class LinkedList: 

	# Function to initialize the Linked List object 
	def __init__(self): 
		self.head = None
```

> [!warning] L'Head è una variabile!
> L'Head non è di per sé un nodo, bensì una variabile che viene associata al nodo che rappresenta la 'testa' della lista, cioè il primo.