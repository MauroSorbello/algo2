"""
Implementar un algoritmo Contiene-Suma(A,n) que recibe una lista de enteros A y un entero n y devuelve True si existen en A un par de elementos que sumados den n. Analice el costo computacional.
"""

def ContieneSumaAux(A, n, current):
    if current != None:
        newCurrent = current
        check = False
        while check == False:
            suma = current.value + newCurrent.value
            if suma == n:
                return True
            else:
                if newCurrent.nextNode != None:
                    newCurrent = newCurrent.nextNode
                else:
                    check = True
    if current.nextNode != None:
        return ContieneSumaAux(A, n, current.nextNode)

def ContieneSuma(A, n):
    if A.head != None:
        return ContieneSumaAux(A, n, A.head)
    
class LinkedList:
  head=None

class Node:
  value=None
  nextNode=None

def add(L,element):
  nodeNew = Node()
  nodeNew.value = element
  nodeNew.nextNode = L.head
  L.head = nodeNew

A = LinkedList()
add(A, 3)
add(A, 2)
add(A, 4)
add(A, 5)
add(A, 6)
add(A, 7)
add(A, 8)

print(ContieneSuma(A, 5))