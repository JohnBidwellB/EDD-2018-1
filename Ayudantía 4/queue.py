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


    def __str__(self):
        if self.empty():
            return "Queue is empty"
        else:
            to_print = ""
            temp = self.head
            while temp != None:
                to_print += str(temp)+" "
                temp = temp.next
            return to_print

if __name__=="__main__":
    pq = Queue()
    pq.enqueue(7)
    pq.enqueue(9)
    pq.enqueue(10)
    pq.enqueue(6)
    print(pq)
    pq.dequeue()
    print(pq)
