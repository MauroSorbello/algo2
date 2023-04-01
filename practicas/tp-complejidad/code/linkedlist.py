from algo1 import *

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

def search (L, element):
  currentNode = L.head
  posicion1 = 0
  check = False
  while (currentNode != None):
    if currentNode.value == element:
      check = True
      posicion = posicion1
    posicion1 = posicion1 + 1
    currentNode = currentNode.nextNode
  if check:
    return posicion
  else:
    return None

def insert(L, element, position):
    long = length(L)
    class Node:
      value=None
      nextNode=None
    newNode = Node()
    newNode.value = element
    if (position <= long):
      if long == 0:
        L.head = newNode
      elif (position == 0):
        newNode.nextNode = L.head
        L.head = newNode
      else:  
        currentNode = L.head  
        i = 0
        while i < position - 1:
          currentNode = currentNode.nextNode
          i = i + 1
        newNode.nextNode = currentNode.nextNode
        currentNode.nextNode = newNode
      return position
    else:
        return None


def delete(L, element):
  position = search(L, element)
  if position != None: 
    if position == 0:
      L.head = L.head.nextNode  
      return position
    else:
      currentNode = L.head    
      i = 0  
      while i < (position - 1): 
        currentNode = currentNode.nextNode 
        i = i + 1  
      currentNode.nextNode = currentNode.nextNode.nextNode 
      return position
  else:
    return None


def length(L):
    cantidad = 0
    currentNode = L.head
    while currentNode != None:
        currentNode = currentNode.nextNode
        cantidad = cantidad + 1
    return cantidad

def access(L, position):
    long = length(L)
    if position < length(L):
        currentNode = L.head
        i = 0
        while i < position:
            currentNode = currentNode.nextNode
            i = i + 1
        return currentNode.value
    else:
        return None

def update(L, element, position):
    long = length(L)
    if position < length(L):
        currentNode = L.head
        i = 0
        while i < position:
            currentNode = currentNode.nextNode
            i = i + 1
        currentNode.value = element
        return position
    else:
        return None

  