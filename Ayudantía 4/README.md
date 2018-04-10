## Contenidos

* Colas
* Colas de prioridad


## Colas

#### Implementación

```python

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __str__(self):
        return ("{}".format(str(self.value)))

class Queue:
    def __init__(self):
        self.head = None
        self.tail = None
        self.count = 0

    def empty(self):
        return self.head == None

    def enqueue(self, value):
        node = Node(value)
        if self.empty():
            self.head = node
            self.tail = node
            self.count += 1
        else:
            self.tail.next = node
            self.tail = node
            self.count += 1

    def dequeue(self):
        temp  = self.head
        if self.empty():
            print("Queue is empty")
        else:
            temp = self.head
            self.head = temp.next
            temp.next = None
            self.count -= 1


if __name__=="__main__":
    pq = Queue()
    pq.enqueue(7)
    pq.enqueue(9)
    pq.enqueue(10)
    pq.enqueue(6)
    pq.dequeue()
```


## Colas de prioridad

Es una EDD similar a las colas en la que los elementos además tienen asignada una prioridad.
En una cola de prioridad un elemento con mayor prioridad será desencolada antes que un elemento con mayor prioridad.

#### Operaciones

Debe soportar al menos las siguientes operaciones:

* Encolar: Que añada un elemento a la cola con su correspondiente prioridad.
* Desencolar: Que desencole el elemento con mayor prioridad.

## Ejercicios

#### Ejercicio 1

Implemente la clase Cola con los métodos:
* Push
* Pop
* Front
* Back
* Empty

#### Ejercicio 2

Sea Q una cola de enteros no vacía, y S una pila de enteros inicialmente vacía. Use sólo las operaciones de las clases `Pila` y `Cola` y una única variable auxiliar `x` para invertir el orden de los elementos en Q.

#### Ejercicio 3

Implementar Cola de prioridad

#### Ejercicio 4

Modifique la implementación de Cola de prioridad para que al insertar un elemento este sea ubicado en la cola de acuerdo a su prioridad.
