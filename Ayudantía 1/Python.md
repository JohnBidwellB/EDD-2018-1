# Ayudantía 1
---

Temas a tratar:
* Python

***

### Resumen de Python

**Nombres**

* Variables, funciones, métodos, paquetes y módulos
  - lower_case_with_underscores
* Clases y excepciones
  - CapWords
* Métodos protegidos y funciones internas
  - _single_leading_underscore(self, ...)
* Métodos privados
  - __double_leading_underscore(sefl, ...)
* Constantes
  - ALL_CAPS_WITH_UNDERSCORES

**Comentarios**

* Inline
  `# Comentario`
* Multiline
  ```Python
  """
  Comentario
  """
  ```

**Input/Output**

```python
nombre = input("Nombre: ")
print(nombre)
```

**Condiciones**

```python
if condicion:
  # Código
elif condicion:
  # Código
else:
  # Código
```

**Ciclos**

* Ciclo `for`

```python
for i in range(10):
  if i == 2:
    continue
  print(i) # 0, 1, 3, ..., 9
for i in range(1, 11):
  print(i) # 1, 2, 3, ..., 10
for i in range(10, 1, -2):
  print(i) # 10, 8, 6, 4, 2
```

* Ciclo `while`

```python
while True:
  if False:
    break
  print("Hola mundo")
```

**Funciones**

```python
def mi_funcion(param1, param2):
  ### Código
  print(param1, param2)
  return algo
```

```python
def hartos_parametros(*args):
  for param in args:
    print(param)
```

```python
def diccionario_de_parametros(**kwargs):
  print("Nombre: ", kwargs.get("nombre"))
  print("Edad: ", kwargs.get("edad"))
  print("Carrera: ", kwargs.get("carrera", "No está estudiando"))

diccionario_de_parametros(nombre="John", edad=23, carrera="ICIT")
```

**Clases**

```python
class Persona:
  def __init__(self, nombre, edad):
    self.nombre = nombre
    self.edad = edad

  def __info(self):
    print(self.nombre + str(self.edad))

a = Persona("John", 23)
a.info()
```

* Herencia

```python
class Alumno(Persona):
    def __init__(self, nombre, edad, carrera):
        Persona.__init__(self, nombre, edad)
        self.carrera = carrera


    def info_completa(self):
        self.imprimir_info()
        print(self.carrera)

a = Alumno("John", 23, "ICIT")
a.info_completa()
```

**Módulos**

**Listas**

```Python
lista = [1,2,3,4,....]
lista = list("Hola")

len(lista) # Cantidad de elementos
lista[2] # Retorna el elemento en la posición 2
lista.append(10) # Agrega al final
lista.count(elemento) # Cantidad de veces que está elemento en la lista
del lista[posicion] # Elimina el elemento en posicion
lista.remove(x) # Elimina todas las ocurrencias de x en la lista
lista[1:3] # Entrega los elementos 1 y 2 de la lista

if 5 in lista: # Para saber si la lista posee el elemento
  # Do something

for elemento in lista:
  print(elemento)
```

**Diccionarios**

```python
diccionario = { 'nombre': "John", 'edad': 23, 'carrera': "ICIT" }
print(diccionario.nombre)
