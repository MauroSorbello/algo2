from algo1 import *
from linkedlist import *
import random
from mystack import *

class LinkedList:
  head=None

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

####QuickSort####

def QuickSortAux1(L, menor, mayor):
  pivote = L.head
  for i in range(0, menor):
    pivote = pivote.nextNode
  pivVal = pivote.value
  #NODO INDICE 1
  left = L.head 
  for j in range(0, menor + 1):
    left =left.nextNode
  #NODO INDICE MAYOR
    right = L.head
  for j in range(0, mayor) :
    right = right.nextNode
  indMenor = menor + 1
  indMayor = mayor
  while True:
    while (indMenor <= indMayor) and (left.value <= pivVal):
      indMenor += 1
      left = left.nextNode
    while (indMenor <= indMayor) and (right.value >= pivVal):
      indMayor -= 1
      right = L.head
      for i in range(0, indMayor):
        right = right.nextNode
    if indMayor < indMenor:
      break
    else:
      valRight = right.value
      right.value = left.value
      left.value = valRight
  valRight = right.value
  right.value = pivVal
  pivote.value = valRight
  val(L)
  return indMayor

def QuickSortAux2(L, menor, mayor):
  if menor < mayor:
    #DEVOLVEMOS EL PIVOT
    pivot = QuickSortAux1(L, menor, mayor)
    #ORDENA PARTE IZQUIERDA
    QuickSortAux2(L, menor, pivot - 1)
    #ORDENA PARTE DERECHA
    QuickSortAux2(L, pivot + 1, mayor)

def QuickSort(L):
  QuickSortAux2(L, 0, length(L) - 1)

####MERGE SORT####
def dividir(L1, L2):
  List = LinkedList()
  List.head = None
  if L1 != None:
    curL1 = L1.head
  if L2 != None:
    curL2 = L2.head
  i = 0
  j = 0
  if L1 != None:
    if L2 != None:
      while curL1 != None and curL2 != None:
        if curL1.value < curL2.value:
          insert(List, curL1.value, j)
          curL1 = curL1.nextNode
        else: 
          insert(List, curL2.value, j)
          curL2 = curL1.nextNode
        j += 1
      while curL1 != None and curL2 == None:
        insert(List, curL1.value, j)
        curL1 = curL1.nextNode
      while curL1 == None and curL2 != None:
        insert(List, curL2.value, j)
        curL2 = curL2.nextNode
      return List
    
def MergeSort(L):
  L1 = LinkedList()
  L2 = LinkedList()
  largo = length(L)
  mitadLargo = int(largo / 2)
  current = L.head

  if largo > 1:
    j = 0
    for i in range(0, largo):
      if i < mitadLargo:
        value = current.value
        insert(L1, value, i)
      else:
        value = current.value
        insert(L2, value, j)
        j += 1
      current = current.nextNode
      
    L1 = MergeSort(L1)
    L2 = MergeSort(L2)
    return dividir(L1, L2)
    
  else:
    return L
