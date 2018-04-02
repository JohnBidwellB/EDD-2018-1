# -*- coding: utf-8 -*-
# import node

class Node:
    def __init__(self, data):
        self.data = data
        self.next_node = None

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

lista = List()
lista.insert_last(4)
lista.insert_last(2)
lista.insert_last(6)
lista.insert_first(1)
lista.print_list()
print(lista.head.data)
print(lista.tail.data)
