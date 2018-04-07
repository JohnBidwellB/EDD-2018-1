# -*- coding: utf-8 -*-

class Node:
    def __init__(self, data):
        self.data = data
        self.next_node = None
        self.prev_node = None

class ListaDoblementeEnlazada:
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
            node  = Node(element)
            self.tail.next_node = node
            node.prev_node = self.tail
            self.tail = node

    def insert_first(self, element):
        if self.empty():
            self.head = Node(element)
            self.tail = self.head
        else:
            node = Node(element)
            node.next_node = self.head
            self.head.prev_node = node
            self.head = node

    def print_list(self):
        if self.empty():
             print("Lista vacia")
        else:
            temp = self.head
            i = 1
            while True:
                if temp.prev_node == None:
                    print("None", temp.data, temp.next_node.data)
                elif temp.next_node == None:
                    print(temp.prev_node.data, temp.data, "None")
                else:
                    print(temp.prev_node.data, temp.data, temp.next_node.data)
                temp = temp.next_node
                i += 1
                if temp == None:
                    break

    def length(self):
        elements = 0
        temp = self.head
        while True:
            elements += 1
            if temp.next_node == None:
                break
            temp = temp.next_node
        return elements

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

if __name__=="__main__":
    lista = ListaDoblementeEnlazada()
    lista.insert_last(5)
    lista.insert_last(2)
    lista.insert_last(-2)
    lista.insert_last(6)
    lista.insert_last(3)
    lista.insert_last(1)
    lista.insert_last(-1)
    lista.sort()
    lista.print_list()
