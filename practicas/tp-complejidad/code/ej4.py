from algo1 import *
from advancedsort import *
from linkedlist import*

A = LinkedList()

class Node:
  value=None
  nextNode=None

def val (L):
    currentNodeL1 = L.head
    print("Lista")
    for i in range(0, length(L)):
        print(currentNodeL1.value, end = "")
        currentNodeL1 = currentNodeL1.nextNode
        print(" ", end = "")
    print("")
    print("------------------------------------------------------------------")

add(A, 1)
add(A, 5)
add(A, 2)
add(A, 7)

add(A, 6)
add(A, 9)
add(A, 23)
add(A, 10)

#O(n²)

def ordenar(L):
  #ORDENO LA LISTA
  QuickSort(L)
  mitad = int(length(L)/2)
  print(mitad)
  current = L.head
  for i in range(0, mitad - 1):
    current = current.nextNode
  print(current.value)
  start = L.head
  for i in range(0, int((mitad -1) /2)):
    valS = start.value
    start.value = current.nextNode.value
    current.nextNode.value = valS
    current = current.nextNode
    start = start.nextNode
  print("LISTA A")
  val(A)
ordenar(A)

