## Contenidos

* Algoritmos de ordenamiento
* Listas

## Algoritmos de ordenamiento

* Bubble sort

```python
def bubble_sort(list):
    for i in range(len(list)-1, 0, -1):
        for j in range(0, i):
            if list[j] > list[j+1]:
                list[j], list[j+1] = list[j+1], list[j]


if __name__=="__main__":
    list = [49, 91, 11, 39, 98, 66, 24, 70, 3, 16]
    bubble_sort(list)
    print(list)
```

* Selection sort

```python
def selection_sort(list):
    for i in range(len(list)-1, 0, -1):
        max_number_position = 0
        for j in range(1, i+1):
            if list[j] > list[max_number_position]:
                max_number_position = j
        list[max_number_position], list[i] = list[i], list[max_number_position]


if __name__=="__main__":
    list = [49, 91, 11, 39, 98, 66, 24, 70, 3, 16]
    selection_sort(list)
    print(list)
```

* Merge sort

```python

```

* Insertion sort

```python
def insertion_sort(list):
    for i in range(1, len(list)):
        key = list[i]
        j = i-1
        while j >= 0 and key < list[j]:
            list[j+1] = list[j]
            j -= 1
        list[j+1] = key

if __name__=="__main__":
    list = [49, 91, 11, 39, 98, 66, 24, 70, 3, 16]
    insertion_sort(list)
    print(list)
```

## Listas

* Colección lineal de elementos
* Cada elemento recibe el nombre de nodo
* Cada nodo almacena la información del elemento y un puntero al elemento siguiente
* TDA lista:
  * Crear
  * Agregar
  * Quitar
  * Vacio

* Lista simple

```python
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class List:
    def __init__(self):
        self.head = None
        self.tail = None

    def empty(self):
        return self.head == None

    def insert_last(self, element):
        if self.empty():
            self.head = Node(element)
            self.tail = self.head
        else:
            node = Node(element)
            self.tail.next_node = node
            self.tail = node

    def insert_first(self, element):
        if self.empty():
            self.head = Node(element)
            self.tail = self.head
        else:
            node = Node(element)
            node.next_node = self.head
            self.head = node

    def print_list(self):
        if self.empty():
             print("Lista vacia")
        else:
            temp = self.head
            i = 1
            seguir = True
            while seguir:
                print("Nodo {} contiene el número {}".format(i, temp.data))
                temp = temp.next_node
                i += 1
                if temp == None:
                    break

if __name__=="__main__":
    lista = List()
    lista.insert_last(4)
    lista.insert_last(2)
    lista.insert_last(6)
    lista.insert_first(1)
    lista.print_list()
    print(lista.head.data)
    print(lista.tail.data)

```

## Ejercicios

#### Ejercicio 1

Se requiere implementar la clase Lista que almacene números enteros y soporte las operaciones:

* **ordenar(A)**: que ordene de forma descendente el conjunto A.
* **select(A, i)**: obtiene el i-ésimo elemento del conjunto ordenado A.
* **posicion(A, x)**: Obtiene la posición que ocupa el elemento x dentro del conjunto A.
* **pertetencia(A, x)**: responde `True` si x pertenece a A. `False` en caso contrario.
* **sucesor(A, x)**: dado un número entero cualquiera x, obtiene el menor elemento y perteneciente a A tal que x < y.
* **antecesor(A, x)**: dado un número entero cualquiera x, obtiene el mayor elemento y perteneciente a A tal que y < x.
* **vacio(A)**: responde `True` si el conjunto está vacio. `False` en caso contrario.
* **minimo(A)**: devuelve el menor elemento de A.
* **insertar(A, x)**:  Inserta el elemento x en el conjunto A. La lista debe permanecer ordenada al insertar un nuevo elemento
* **eliminar(A, x)**: Elimina el elemento x del conjunto A.


#### Ejercicio 2

Tres de las funcionalidades básicas de un Web Browser son la de poder avanzar o retroceder en el
historia de páginas y la de volver a visitar un sitio anteriormente recorrido. En este aspecto, el
trazado de páginas:

`Nueva pestaña -> Home -> Facebook -> Twitter`

Asuma que un sitio web, para nuestro caso, tiene solo dos datos relevantes: URL y Nombre
(ejemplo: www.google.cl y Google respectivamente). En base a lo anterior se pide que programe
la clase “PaginaWeb” con todo lo necesario y la clase “Browser” con lo siguiente:

* Un método llamado “paginaActual( )” que imprima el nombre y URL de página en que
actualmente está el Web Browser.

* Un método llamado “visitarPaginaNueva( )” que reciba una URL y un nombre de página y la
agregue a la lista de páginas. Esta sería nuestra página actual.
* Un método llamado “volverPaginaN(posiciones, adelante o atrás) ” que permita volver a un
sitio ya visitado basándose en que sea N posiciones (de 1 a muchas) más adelante o más
atrás (1 es adelante, 2 es atrás). En caso de que N sobrepase el total de opciones hacia atrás
o adelante deberá enviar el mensaje: “Imposible visitar la página”. En caso contrario, deberá
imprimir la URL y el nombre de la página y dejar dicha página como la actual. Esto no genera
una nueva página ni afecta el historial.

* Un método llamado “historial( )” que imprima el Historial completo de páginas visitadas en el
Web Browser desde el último hasta el primero.

#### Ejercicio 3

Suponga que necesita almacenar un conjunto de datos sobre una lista enlazada. Se desea soportar búsqueda sobre dicho conjunto de datos. Se sabe también que ciertos elementos del conjunto son buscados más frecuentemente que otros, y que la tendencia de búsqueda cambia con el tiempo, en el sentido que los elementos más frecuentemente consultados no necesariamente son los mismos en todo momento. Modifique la implementación de listas enlazadas para permitir la búsqueda eficiente de los elementos más consultados en un momento dado. También se desea soportar la inserción de nuevos elementos.
