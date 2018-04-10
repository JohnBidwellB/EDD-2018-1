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
