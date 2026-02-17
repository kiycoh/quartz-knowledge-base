---
tags:
  - algoritmi-ordinamento
  - lista-concatenata-semplice
  - algoritmi-greedy
---

# Cos'è una lista concatenata semplice?

![[Lista concatenata semplice_image_1.png]]

Ha un solo collegamento per nodo. Questo collegamento punta al nodo successivo della lista o ad un valore nullo o ad una lista vuota se è il valore finale.

## Operazioni su lista concatenata semplice

### Insertion all'inizio della lista
1. Colleghiamo l'Head al nuovo nodo;
2. Rimuoviamo il collegamento tra Head e primo nodo originale;
3. Rendiamo il nuovo nodo l'Head della lista concatenata.

![[Lista concatenata semplice_image_2.webp]]

``` python
# This function is in LinkedList class
# Function to insert a new node at the beginning
def push(self, new_data):

	# 1 & 2: Allocate the Node & Put in the data
	new_node = Node(new_data)

	# 3. Make next of new Node as head
	new_node.next = self.head

	# 4. Move the head to point to new Node
	self.head = new_node
```
#### Analisi della complessità
- Complessità temporale: *$O(1)$*, Si ha un puntatore alla testa ed è possibile collegare direttamente un nodo e cambiare il puntatore. Il lavoro è costante.
- Spazio ausiliario: *$O(1)$*
### Insertion dopo un determinato nodo
1. Verificare se il nodo specificato esiste o meno:
	2. Se non esiste;
		3. Terminare il processo,

	2. Se esiste:
		3. Inserire l'elemento nella lista come un nuovo nodo;
		4. Direzionare il puntatore del nodo specificato verso il nuovo nodo inserito;
		5. Direzionare il puntatore del nuovo nodo verso il suo nodo successivo.

![[Lista concatenata semplice_image_3.webp]]

``` python
# This function is in LinkedList class.
# Inserts a new node after the given prev_node. This method is
# defined inside LinkedList class shown above */
def insertAfter(self, prev_node, new_data):

	# 1. check if the given prev_node exists
	if prev_node is None:
		print("The given previous node must inLinkedList.")
		return

	# 2. Create new node &
	# 3. Put in the data
	new_node = Node(new_data)

	# 4. Make next of new Node as next of prev_node
	new_node.next = prev_node.next

	# 5. make next of prev_node as new_node
	prev_node.next = new_node

```
#### Analisi della complessità
- Complessità temporale: *$O(1)$*, poiché `prev_node` è già dato come argomento in un metodo, non c'è bisogno di iterare sulla lista per trovare `prev_node`
- Spazio ausiliario: *$O(1)$*, poiché si utilizza uno spazio costante per modificare i puntatori.
### Insertion alla fine della lista
1. Direziona il puntatore dell'ultimo nodo da `NULL` al nuovo nodo;
2. Direziona il puntatore del nuovo nodo verso `NULL`.

![[Lista concatenata semplice_image_4.webp]]

``` python
# This function is defined in Linked List class
# Appends a new node at the end. This method is
# defined inside LinkedList class shown above
def append(self, new_data):

		# 1. Create a new node
		# 2. Put in the data
		# 3. Set next as None
		new_node = Node(new_data)

		# 4. If the Linked List is empty, then make the
		# new node as head
		if self.head is None:
			self.head = new_node
			return

		# 5. Else traverse till the last node
		last = self.head
		while (last.next):
			last = last.next

		# 6. Change the next of last node
		last.next = new_node
```

#### Analisi della complessità
- Complessità temporale: *$O(n)$*, dove $n$ è il numero di nodi dell'elenco collegato. Poiché c'è un ciclo dalla testa alla fine, la funzione svolge un lavoro $O(n)$.  *Questo metodo può essere ottimizzato* per lavorare in $O(1)$ mantenendo un puntatore extra alla coda dell'elenco collegato.
- Spazio ausiliario: $O(1)$

### Deletetion
