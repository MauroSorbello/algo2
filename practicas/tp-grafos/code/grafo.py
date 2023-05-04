import math
from queue_1 import *

"""
Donde Graph es una representación de un grafo simple mediante listas de adyacencia resolver los siguiente ejercicios
Ejercicio 1
Implementar la función crear grafo que dada una lista de vértices y una lista de aristas cree un grafo con la representación por Lista de Adyacencia.

def createGraph(List, List) 
Descripción: Implementa la operación crear grafo
Entrada: LinkedList con la lista de vértices y LinkedList con la lista de aristas donde por cada par de elementos representa una conexión entre dos vértices.
Salida: retorna el nuevo grafo
"""

#REALIZADO POR LISTA DE ADYACENCIA

def createGraph(V, A):
    graph = []
    for i in range(0, len(V)):
        graph.append([])
    for j in range(0, len(A)):
        graph[A[j][0]].append(A[j][1])
        if graph[A[j][0]] != graph[A[j][1]]:
            graph[A[j][1]].append(A[j][0])
    return graph


V1 = [0,1,2,3]
A1 = ((0,1), (0,2), (1,3), (0,0), (2,0))
G = createGraph(V1, A1) 
print(G)


"""
def existPath(Grafo, v1, v2): 
Descripción: Implementa la operación existe camino que busca si existe un camino entre los vértices v1 y v2 
Entrada: Grafo con la representación de Lista de Adyacencia, v1 y v2 vértices en el grafo.
Salida: retorna True si existe camino entre v1 y v2, False en caso contrario.
"""

def existPath(Grafo, v1, v2):
    #CASO 1: ALGUNO DE LOS DOS VERTICES NO SE ENCUENTRAN EN EL GRAFO
    if Grafo[v1] == None:
        return False
    elif Grafo[v2] == None:
        return False
    #CASO 2: SI ALGUNO NO TIENE ADYACENCIA
    if (len(Grafo[v1]) == 0) or (len(Grafo[v2]) == 0):
        return False
    #CASO 3: SE ENCUENTRAN EN LA LISTA DE ADYACENCIA
    for i in range(0, len(Grafo[v1])):
        if Grafo[v1][i] == v2:
            return True
    for j in range(0, len(Grafo[v2])):
        if Grafo[v2][j] == v1:
            return True
    #CASO 4: ESTAN CONECTADOS POR UN NODO EN COMUN
    if len(Grafo[v1]) == 0:
        v1New = v2
        return existPathRec(Grafo, v2, v1New, v1)
    else:
        v1New = v1
        return existPathRec(Grafo, v1, v1New, v2)

def existPathRec(Grafo, v1, v1New, v2): 
    for i in range(0, len(Grafo[v1New])):
        check = existPath(Grafo, Grafo[v1New][i], v2)
        if check == True:
            return True
    """
    i = 0
    while i < len(Grafo):
        if len(Grafo[v1New]) == 0:
            i += 1
            v1New = v1
        if len(Grafo[v1New]) > i + 1:
            i +=1
        if Grafo[v1New][i] != v2: 
            return existPathRec(Grafo, v1 ,Grafo[v1New][i], v2)

        else:
            return True
    return None
    """
VI = 0
VF = 3
print(existPath(G, VI, VF))

"""
Ejercicio 3
Implementar la función que responde a la siguiente especificación.
def isConnected(Grafo): 
Descripción: Implementa la operación es conexo 
Entrada: Grafo con la representación de Lista de Adyacencia.
Salida: retorna True si existe camino entre todo par de vértices, False en caso contrario.
"""    

def isConnected(Grafo): 
    List = []
    for i in range (0, len(Grafo)):
        for j in range (0, len(Grafo)):
            v1 = i
            if i != j:
                v2 = j
                try:
                    List.index([v2,v1])
                except ValueError:
                    indice = None
                else:
                    indice = List.index([v2,v1])
                if indice == None:
                    check = existPath(Grafo, v1, v2)
                    if check == False:
                        return False
                    if check == True:
                        List.append([v1,v2])
    return True

#El método list.index() en Python tiene una complejidad de tiempo promedio de O(n), 
# donde n es el número de elementos en la lista. 
# Esto se debe a que el método realiza una búsqueda secuencial en la lista para encontrar el índice del elemento especificado.

print(isConnected(G))

"""
Ejercicio 4
Implementar la función que responde a la siguiente especificación.
def isTree(Grafo): 
Descripción: Implementa la operación es árbol 
Entrada: Grafo con la representación de Lista de Adyacencia.
Salida: retorna True si el grafo es un árbol.
"""

#Es un arbol si no tiene loop y es conexo

def isTree(Grafo): 
    #Comprobamos si tiene un loop
    valoresUnicos = []
    for j in range(0, len(Grafo)):
        valoresUnicos.append([])
    #Borramos las aristas que generen loops
    for k in range(0, len(Grafo)):
        for elem in Grafo[k]:
            if elem in valoresUnicos[k]:
                return False
            if elem not in valoresUnicos:
                valoresUnicos[k].append(elem)
    for i in range(0, len(Grafo)):
        try:
            Grafo[i].index(i)
        except ValueError:
            indice = None
        else:
            indice = Grafo[i].index(i)
        if indice != None:
            return False
    #Comprobamos si es conexo
    conexo = isConnected(Grafo)
    if conexo == True:
        return True
    else:
        return False
#El método list.index() en Python tiene una complejidad de tiempo promedio de O(n), 
# donde n es el número de elementos en la lista. 
# Esto se debe a que el método realiza una búsqueda secuencial en la lista para encontrar el índice del elemento especificado.

print(isTree(G))

"""
Ejercicio 5 
Implementar la función que responde a la siguiente especificación.
def isComplete(Grafo): 
Descripción: Implementa la operación es completo 
Entrada: Grafo con la representación de Lista de Adyacencia.
Salida: retorna True si el grafo es completo.

Nota: Tener en cuenta que  un grafo es completo cuando existe una arista entre todo par de vértices.
"""

def isComplete(Grafo): 
    for i in range (0, len(Grafo)):
        for j in range (0, len(Grafo)):
            if i != j:
                try:
                    Grafo[i].index(j)
                except ValueError:
                    return False
    return True

print(isComplete(G))

"""
Ejercicio 6
Implementar una función que dado un grafo devuelva una lista de aristas que si se eliminan el grafo se convierte en un árbol. Respetar la siguiente especificación. 

def convertTree(Grafo)
Descripción: Implementa la operación es convertir a árbol 
Entrada: Grafo con la representación de Lista de Adyacencia.
Salida: LinkedList de las aristas que se pueden eliminar y el grafo resultante se convierte en un árbol.
"""

def convertTree(Grafo):
    #Comprobamos que sea conexo
    conexo = isConnected(Grafo)
    if conexo == True:
        L = []
        valoresUnicos = []
        for j in range(0, len(Grafo)):
            valoresUnicos.append([])
        #Borramos las aristas que generen loops
        for i in range(0, len(Grafo)):
            for elem in Grafo[i]:
                if elem in valoresUnicos[i]:
                    L.append([i, elem])
                    Grafo[i].remove(elem)
                if elem not in valoresUnicos:
                    valoresUnicos[i].append(elem)
        for k in range(0, len(Grafo)):
            try:
                Grafo[k].index(k)
            except ValueError:
                indice = None
            else:
                indice = Grafo[k].index(k)
                Grafo[k].pop(indice)
                L.append([k,k])
        return L
    else:
        return False

#print(convertTree(G))

"""
Ejercicio 7
Implementar la función que responde a la siguiente especificación.
def countConnections(Grafo):
Descripción: Implementa la operación cantidad de componentes conexas 
Entrada: Grafo con la representación de Lista de Adyacencia.
Salida: retorna el número de componentes conexas que componen el grafo.
"""

def countConnections(Grafo):
    valoresUnicos = []
    #Borramos las aristas que generen loops
    for i in range(0, len(Grafo)):
        for elem in Grafo[i]:
            if elem not in valoresUnicos:
                valoresUnicos.append(elem)
    compConnect = len(valoresUnicos)
    return compConnect

print(countConnections(G))

"""
Ejercicio 8
Implementar la función que responde a la siguiente especificación.
def convertToBFSTree(Grafo, v):
Descripción: Convierte un grafo en un árbol BFS
Entrada: Grafo con la representación de Lista de Adyacencia, v vértice que representa la raíz del árbol
Salida: Devuelve una Lista de Adyacencia con la representación BFS del grafo recibido usando v como raíz.
"""

def convertToBFSTree(Grafo, v):
    vertex = []
    BFS = []
    for i in range(0, len(Grafo)):
        vertex.append(["white", math.inf, None])
        BFS.append([])
    vertex[v] = ["Gray", 0, None]
    Q = []
    Q.append(v)
    d = 0
    ind = 0
    BFS[v] = ([v, d])
    while Q != []:
        u = dequeue(Q)
        d = vertex[u][1] + 1
        for i in range(0, len(Grafo[u])):
            vertice = Grafo[u][i]
            if vertex[vertice][0] == "white":
                vertex[vertice][0] = "Gray"
                vertex[vertice][1] = d
                vertex[vertice][2] = u
                Q.append(vertice)
                BFS[u].append([vertice, d])
        vertex[u] = "Black"
    BFSfin = []
    for j in range (0, len(BFS)):
        if BFS[j] != []:
            BFSfin.append(BFS[j])
    return BFSfin

print(convertToBFSTree(G, 0))

"""
Ejercicio 9
Implementar la función que responde a la siguiente especificación.
def convertToDFSTree(Grafo, v):
Descripción: Convierte un grafo en un árbol DFS
Entrada: Grafo con la representación de Lista de Adyacencia, v vértice que representa la raíz del árbol
Salida: Devuelve una Lista de Adyacencia con la representación DFS del grafo recibido usando v como raíz.
"""

def convertToDFSTree(Grafo, v):
    vertex = []
    BFS = []
    for i in range(0, len(Grafo)):
        vertex.append(["white", math.inf, math.inf, None])
        BFS.append([])
    time = 0
    for j in range(0, len(Grafo)):
            vertice = j
            if vertex[vertice][0] == "white":
                convertToDFSTreeRec(Grafo, vertex, vertice, time, BFS)
    BFSfin = []
    for j in range (0, len(BFS)):
        if BFS[j] != []:
            BFSfin.append(BFS[j])
    return BFSfin
    

def convertToDFSTreeRec(Grafo, vertex, u, time, BFS):
    time = time + 1
    vertex[u][1] = time
    vertex[u][0] = "Gray"
    for i in range(0, len(Grafo[u])):
        vertice = Grafo[u][i]
        if vertex[vertice][0] == "white":
            vertex[vertice][3] = u
            convertToDFSTreeRec(Grafo, vertex, vertice, time, BFS)
    time += 1
    vertex[u][2] = time
    vertex[u][0] = "Black"
    try: BFS[vertex[u][3]]
    except:
        TypeError
        BFS[u].append([u, vertex[u][1], vertex[u][2]])
    else:BFS[vertex[u][3]].append([u, vertex[u][1], vertex[u][2]])

    


print(convertToDFSTree(G, 0))
