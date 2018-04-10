class Node:
    def __init__(self, value, priority):
        self.value = value
        self.priority = priority
        self.next = None

    def __str__(self):
        return ("{}({})".format(str(self.value), str(self.priority)))

class PriorityQueue:
    def __init__(self):
        self.head = None
        self.tail = None
        self.count = 0

    def empty(self):
        return self.head == None

    def enqueue(self, value, priority):
        node = Node(value, priority)
        if self.empty():
            self.head = node
            self.tail = node
            self.count += 1
        else:
            self.tail.next = node
            self.tail = node
            self.count += 1

    def find(self):
        if self.empty():
            return None
        else:
            temp = self.head
            prev_high_node = temp
            high_node = temp
            high_priority = temp.priority
            while temp.next != None:
                if temp.next.priority > high_priority:
                    prev_high_node = temp
                    high_node = temp.next
                    high_priority = temp.next.priority
                temp = temp.next
            return prev_high_node, high_node

    def dequeue(self):
        if self.empty():
            print("PriorityQueue is empty")
        else:
            prev_to_dequeue, to_dequeue = self.find()
            #print(prev_to_dequeue.next)

            if prev_to_dequeue == to_dequeue and self.count > 1:
                self.head = to_dequeue.next
            elif prev_to_dequeue == to_dequeue and self.count == 1:
                self.head = None
                self.tail = None
            else:
                next = prev_to_dequeue.next.next
                prev_to_dequeue.next.next = None # Elimina la referencia next del nodo a eliminar
                prev_to_dequeue.next = next
            self.count -= 1

    def __str__(self):
        if self.empty():
            return "PriorityQueue is empty"
        else:
            to_print = ""
            temp = self.head
            while temp != None:
                to_print += str(temp)+" "
                temp = temp.next
            return to_print

if __name__=="__main__":
    pq = PriorityQueue()
    pq.enqueue(7, 3)
    pq.enqueue(9, 1)
    pq.enqueue(10, 8)
    pq.enqueue(6, 5)
    print(pq)
    pq.dequeue()
    print(pq)
    pq.dequeue()
    print(pq)
    pq.dequeue()
    print(pq)
    pq.dequeue()
    print(pq)
