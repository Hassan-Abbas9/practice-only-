# Priority queues

# enque

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class Queue:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def display_nodes(self):
        current = self.head
        while current:
            print(current.value, end='---->')
            current = current.next

    def enqueue(self, value):
        node = Node(value)
        if self.length == 0:
            self.head = node
            self.tail = node
            self.length += 1

        else:
            self.tail.next = node
            self.tail = node
            self.length += 1

    def dequeue(self):

        if self.length == 0:
            print("The Queue is Empty!!")
        elif self.length == 1:
            self.head = None
            self.tail = None
            self.length -= 1
        else:
            current = self.head
            self.head = self.head.next
            self.length -= 1


queue_instance = Queue()
queue_instance.enqueue(10)
queue_instance.enqueue(20)
queue_instance.enqueue(30)
queue_instance.enqueue(40)
queue_instance.dequeue()
queue_instance.display_nodes()
