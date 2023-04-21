import numpy as np
import math

"""
A partir de una definición de diccionario como la siguiente:

dictionary = Array(m,0)

Crear un módulo de nombre dictionary.py que implemente las siguientes especificaciones de las operaciones elementales para el TAD diccionario .

"""

# Utilizare el Array de numpy que es O(1), esta función simplemente reserva la memoria necesaria para el array sin inicializar los elementos. Por lo tanto, la complejidad temporal de np.empty es O(1) para reservar la memoria.

# Ademas cumple con direccionamiento directo

# El método len() simplemente devuelve el tamaño del array que ya se ha creado, y no necesita recorrer ningún elemento del mismo por ende es O(1).


"""
Funcion hash_mod
"""


def hash_mod(key, m):
    return int(key % m)


def hash_mult(key, m, A):
    cuenta = int((m * ((key * A) % 1)))
    return cuenta


"""
insert(D,key, value)
Descripción: Inserta un key en una posición determinada por la función de hash (1)  en el diccionario (dictionary). Resolver colisiones por encadenamiento. En caso de keys duplicados se anexan a la lista.
Entrada: el diccionario sobre el cual se quiere realizar la inserción  y el valor del key a insertar 
Salida: Devuelve D
"""

# D = np.empty(m, dtype=object) Crear un array, e indicar que le voy a ingresar una lista.


def insert(D, key, value):
    ind = hash_mod(key, len(D))
    if D[ind] == None:
        D[ind] = []
        D[ind].append((key, value))
    else:
        D[ind].append((key, value))


"""
search(D,key)
Descripción: Busca un key en el diccionario
Entrada: El diccionario sobre el cual se quiere realizar la búsqueda (dictionary) y el valor del key a buscar.
Salida: Devuelve el value de la key.  Devuelve None si el key no se encuentra.
"""


def searchD(D, key):
    ind = hash_mod(key, len(D))
    if D[ind] == None:
        return None
    else:
        L = D[ind]
        i = 0
        while L[i] != None:
            tupla = L[i]
            if tupla[0] == key:
                return [i, tupla[1]]
            else:
                i += 1
    return None


def search(D, key):
    L = searchD(D, key)
    if L != None:
        return L[1]
    else:
        return None


"""
delete(D,key)
Descripción: Elimina un key en la posición determinada por la función de hash (1) del diccionario (dictionary) 
Poscondición: Se debe marcar como nulo  el key  a eliminar.  
Entrada: El diccionario sobre el se quiere realizar la eliminación  y el valor del key que se va a eliminar.
Salida: Devuelve D
"""


def delete(D, key):
    L = searchD(D, key)
    if L != None:
        ind = int(hash_mod(key, len(D)))
        i = L[0]
        D[ind][i] = None
        return D
    else:
        return None


