# Control 1

Dada la siguiente implementación de una lista doblemente enlazada, escriba el método `sort()` el cual haciendo uso del algoritmo de ordenamiento BubbleSort ordene todos los elementos de la lista en orden ascendente.

```python
class Node:
    def __init__(self, data):
        self.data = data
        self.next_node = None
        self.prev_node = None
```

```python
class ListaDoblementeEnlazada:
    def __init__(self):
        self.head = None
        self.tail = None

    def swap(self, node1, node2):
          node1.next_node = node2.next_node
          node2.next_node = node1
          node2.prev_node = node1.prev_node
          node1.prev_node = node2

          if node2.prev_node != None:
              node2.prev_node.next_node = node2
          else:
              self.head = node2
          if node1.next_node != None:
              node1.next_node.prev_node = node1
          else:
              self.tail = node1
              
    def sort(self):
          if self.empty():
              print("No hay elementos que ordenar")
          else:
              temp = self.head
              length = self.length()
              for i in range(length+1, 0, -1):
                  for j in range(0, i+1):
                      if temp.next_node != None:
                          if temp.data > temp.next_node.data:
                              self.swap(temp, temp.next_node)
                          else:
                              temp = temp.next_node
                      else:
                          temp = self.head
                          break

```
