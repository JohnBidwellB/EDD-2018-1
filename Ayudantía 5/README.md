

# Contenidos

* Árboles.
* Árbol binario.
* Recorrido in-order, post-order, pre-order.

## Árboles

Está compuesto por 0 o más nodos.

Cada nodo tiene:
  - Dos punteros a los hijos: Uno para el hijo izquierdo, otro para el hijo derecho.
  - Información.

Así como en listas teníamos el nodo Head para acceder a la lista, en árboles tenemos el nodo root(raiz), desde este nodo se construye el árbol.

Un nodo que no tiene hijos se considera como un nodo hoja.

#### Atributos

* Tamaño: Cantidad de nodos que componen el árbol.
* Profundidad: Hay de 2 tipos
  - De nodo: Distancia entre el nodo y la raiz.
  - De árbol: Distancia entre la raiz y el nodo de mayor profundidad.
* Árbol balanceado: Árbol que tiene todos los niveles completos.

## Árbol binario de búsqueda

Árbol en que cada los hijos izquierdo de cada nodo sean menores que el y los hijos derechos sean mayores. Útil para encontrar información.

![Binary Search Tree](images/bst.png)

![Binary Search Tree construction](images/BSTConstruction.png)

#### Recorrido de un árbol binario

Se comienza con la raiz del árbol y luego se realizan 3 acciones.

* In-order: Se recorre primero el lado izquierdo del árbol, luego la raiz y finalmente el lado derecho del árbol, o dicho de otra manera, de menor a mayor.
  - Atraviese el sub-árbol izquierdo
  - Visite la raíz
  - Atraviese el sub-árbol derecho
* Pre-order: Se recorre primero la raiz y luego los sub-árboles
  - Visite la raíz
  - Atraviese el sub-árbol izquierdo
  - Atraviese el sub-árbol derecho
* Post-order: Se recorre primero cada sub-árbol y finalmente la raiz
  - Atraviese el sub-árbol izquierdo
  - Atraviese el sub-árbol derecho
  - Visite la raíz

#### Visualización

Pueden comprobar visualmente todas las operaciones y recorrido en el siguiente [link](http://www.cs.armstrong.edu/liang/animation/web/BST.html).

#### Implementación


```python
# -*- coding: utf-8 -*-

class Node:
    def __init__(self, value):
        self.left = None
        self.right = None
        self.value = value

class BST:
    def __init__(self):
        self.root = None

    def empty(self):
        return self.root == None

    def __add(self, value, node):
        if value < node.value:
            if node.left == None:
                node.left = Node(value)
                return
            self.__add(value, node.left)
        elif value > node.value:
            if node.right == None:
                node.right = Node(value)
                return
            self.__add(value, node.right)

    def add(self, value):
        if self.empty():
            node = Node(value)
            self.root = node
        else:
            self.__add(value, self.root)

    def __search(self, value, node):
        if node == None:
            return False
        elif value == node.value:
            return True
        elif value < node.value:
            self.__search(self, value, node.left)
        else:
            self.__search(self, value, node.right)

    def search(self, value):
        if self.empty():
            return False
        else:
            self.__search(self, value, self.root)

    def delete(self): #Implementar
        pass

    def in_order(self, node = None):


    def post_order(self): #Implementar
        pass

    def pre_order(self): #Implementar
        pass

    def leaf_number(self): #Implementar
        pass

    def tree_height(self): #Implementar
        pass

    def node_height(self): #Implementar
        aux = self.root
        height = 0
        if

    def find_minimum(self): #Implementar
        pass

    def find_maximum(self, node): #Implementar
        pass


if __name__=="__main__":
    bst = BST()
    bst.add(10)
    bst.add(12)
    bst.add(5)
    bst.add(4)
    bst.add(20)
    bst.add(8)
    bst.add(7)
    bst.add(15)
    bst.add(13)
```
