# Control 2

Dada la siguiente implementación de la clase Stack, usted deberá implementar los métodos **push()** y **pop()** siguiendo las propiedades de los Stacks y la implementación dada:

```python
class Node:
    def __init__(self, value):
        self.prev = None
        self.value = value

class Stack:
    def __init__(self):
        self.head = None
        self.count = 0

    def empty(self):
        return self.head == None

    def push(self, element):
        pass

    def pop(self):
        pass

    def top(self):
        if self.empty():
            return False
        return self.head
```

Ademas, escriba el algoritmo **intercambio**, el cual toma dos pilas A y B como parámetro y como resultado hace que el contenido de ambas pilas se intercambie, quedando la pila A tal como era la pila B en un principio, y viceversa. Como variable auxiliar sólo puede emplear una única pila.

```python
def intercambio(...):
  pass
```


## Pauta

Distribución de puntajes:
  - Método push():
    - 0.5pts por crear nodo
    - 0.5pts por comprobar que está vacía  y asignar el nuevo nodo en el tope
    - 1pto por asignar el nuevo nodo al tope de la pila
  - Método pop():
    - 1pto por comprobar que está vacía
    - 1pto por asignar el nuevo nodo al tope de la pila


```python
class Stack:

  def push(self, element):
        node = Node(element)
        self.count += 1
        if self.empty():
            self.head = node
        else:
            node.prev = self.head
            self.head = node

  def pop(self):
      if self.empty():
          return False
      else:
          self.head = self.head.prev
          self.count -= 1

def intercambio(stack1, stack2):
  aux = Stack()
  while(stack1.empty() == False and stack2.empty() == False):
      aux.push(stack1.top)
      aux.push(stack2.top)
      stack1.pop()
      stack2.pop()
  while(aux.empty() == False):
      stack1.push(aux.top())
      aux.pop()
      stack2.push(aux.top())
      aux.pop()
```
