from random import randint
import time


class Sort():
    ''' Classe che permette di ordinare una lista di numeri random con diversi metodi di ordinamento (InsertionSort, BubbleSort, MergeSort, QuickSort) '''

    def __init__(self, string='4', n=10):
        self.string = string
        self.n = n
        self.array = [randint(0, n) for _ in range(n)]   # Creazione di una lista di n elementi random
        self.dict_metodi = {"1": self.__InsertionSort, "2": self.__BubbleSort, "3": self.__MergeSort, "4": self.__QuickSort, "5":self.__CoutingSort}   # Dizionario che associa ad ogni numero un metodo di ordinamento
        
    def fit(self):
        # Metodo che restituisce la lista non ordinata
        return self.array

    def transform(self):
        # Metodo che restituisce la lista ordinata
        self.curr = time.time()
        if self.string in self.dict_metodi:
            metodo = self.dict_metodi[self.string]   # Estrazione del metodo di ordinamento
            return metodo(self.array.copy())
        else:
            raise Exception("Scegliere un metodo valido")
        
    def fit_transform(self):
        # Metodo che restituisce la lista non ordinata e quella ordinata
        output = str(self.fit()) + '\n' + str(self.transform())
        end = time.time()
        tempo = end - self.curr
        return output + '\n Tempo trascorso: ' + str(tempo)
    
    def change_method(self):
        # Metodo che permette di cambiare il metodo di ordinamento
        self.string = input("Scegliere un metodo di ordinamento:\n 1) InsertionSort\n 2) BubbleSort\n 3) MergeSort\n 4) QuickSort\n")
        return self.fit_transform()

    def __InsertionSort(self, a):
        for i in range(1, len(a)):
            ele = a[i]
            j = i-1
            while j >= 0 and a[j]>ele :
                a[j + 1] = a[j]
                j =j-1
            a[j + 1] = ele
        return a

    def __BubbleSort(self, lista):
        n = len(lista)
        for i in range(n - 1):
            for j in range(n-1-i):
                if lista[j] > lista[j+1]:
                    tmp = lista[j+1]
                    lista[j+1] = lista[j]
                    lista[j] = tmp
        return lista

    def __MergeSort(self, list):
        list_length = len(list)
        if list_length == 1:
            return list
        q = list_length // 2 #calcoliamo il punto centrale
        left = self.__MergeSort(list[:q]) #lista di sinistra da 0 a q
        right = self.__MergeSort(list[q:]) #lista di destra da q alla fine
        return self.__Merge(left, right)
    def __Merge(self, left, right):
        ordered = []
        
        while left and right:
            ordered.append((left if left[0] <= right[0] else right).pop(0))
        return ordered + left + right

    def __QuickSort(self, numbers):
        length = len(numbers)
        if length <= 1:
            return numbers
        
        pivot = numbers.pop()
        high, low = [], []
        for number in numbers:
            if number > pivot:
                high.append(number)
            else:
                low.append(number)
        return self.__QuickSort(low) + [pivot] + self.__QuickSort(high)
    
    def __CoutingSort(self, arr):
        # The output character array that will have sorted arr
        output = [0 for i in range(256)]
    
        # Create a count array to store count of individual
        # characters and initialize count array as 0
        count = [0 for i in range(256)]
    
        # For storing the resulting answer since the 
        # string is immutable
        ans = ["" for _ in arr]
    
        # Store count of each character
        for i in arr:
            count[ord(i)] += 1
    
        # Change count[i] so that count[i] now contains actual
        # position of this character in output array
        for i in range(256):
            count[i] += count[i-1]
    
        # Build the output character array
        for i in range(len(arr)):
            output[count[ord(arr[i])]-1] = arr[i]
            count[ord(arr[i])] -= 1
    
        # Copy the output array to arr, so that arr now
        # contains sorted characters
        for i in range(len(arr)):
            ans[i] = output[i]
        return ans 

def __main__():
    try:
        metodo = input("Scegliere un numero a cui corrisponde il metodo da utilizzare:\n 1) InsertionSort\n 2) BubbleSort\n 3) MergeSort\n 4) QuickSort\n 5) CoutingSort\n")
        taglia = int(input("Scegliere la taglia della lunghezza della sequenza: "))
        ordina = Sort(metodo, taglia)
        print(ordina.fit_transform())
        choice = input("Vuoi cambiare metodo? (s/n)")
        while choice == 's':
            print(ordina.change_method())
            choice = input("Vuoi cambiare metodo? (s/n)")
    except Exception as error:
        print("Errore: %s" %(error))

__main__()