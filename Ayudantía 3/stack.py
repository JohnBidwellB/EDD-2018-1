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

    def __str__(self):
        if self.empty():
            return "Stack empty"
        else:
            aux = Stack()
            to_print = ""
            while self.empty() != True:
                to_print += "{} ".format(self.top().value)
                aux.push(self.top())
                self.pop()
            while aux.empty() != True:
                self.push(aux.top())
                aux.pop()
            return to_print


if __name__=="__main__":
    stack = Stack()
    print(stack.empty())
    stack.push(5)
    stack.push(2)
    stack.push(8)
    print("=== stack ===")
    print(stack)
    print(stack.top().value)
    stack.pop()
    print(stack.top().value)
    stack.pop()
    print(stack.top().value)
    stack.pop()
    print(stack.count)
