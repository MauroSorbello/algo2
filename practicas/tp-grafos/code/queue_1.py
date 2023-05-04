
def dequeue(Q):
  if Q[0] != None:
    element = Q[len(Q) - 1]
    Q.pop(len(Q) - 1)
    return element
  else:
    return None 
  


