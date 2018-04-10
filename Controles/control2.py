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

    def top(self):
        if self.empty():
            return False
        return self.head

    def print_stack(self):
        if self.empty():
            print("Stack empty")
        else:
            aux = Stack()
            while self.empty() != True:
                print("valor: "+ str(self.top().value))
                aux.push(self.top())
                self.pop()
            while aux.empty() != True:
                self.push(aux.top())
                aux.pop()


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

if __name__=="__main__":
    stack1 = Stack()
    stack1.push(5)
    stack1.push(2)
    stack1.push(8)

    stack2 = Stack()
    stack2.push(1)
    stack2.push(3)
    stack2.push(7)

    intercambio(stack1, stack2)

    print("=== stack 1 ===")
    stack1.print_stack()
    print("=== stack 2 ===")
    stack2.print_stack()
