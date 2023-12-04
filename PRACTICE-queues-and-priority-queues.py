# Queues (Using LINKEDLISTS)

# enqueue

# class Node:
#     def __init__(self, value):
#         self.value = value
#         self.next = None
#
#
# class Queue:
#     def __init__(self):
#         self.head = None
#         self.tail = None
#         self.length = 0
#
#     def display_nodes(self):
#         current = self.head
#         while current:
#             print(current.value, end='---->')
#             current = current.next
#
#     def enqueue(self, value):
#         node = Node(value)
#         if self.length == 0:
#             self.head = node
#             self.tail = node
#             self.length += 1
#
#         else:
#             self.tail.next = node
#             self.tail = node
#             self.length += 1
#
#     def dequeue(self):
#
#         if self.length == 0:
#             print("The Queue is Empty!!")
#         elif self.length == 1:
#             self.head = None
#             self.tail = None
#             self.length -= 1
#         else:
#             current = self.head
#             self.head = self.head.next
#             self.length -= 1
#
#
# queue_instance = Queue()
# queue_instance.enqueue(10)
# queue_instance.enqueue(20)
# queue_instance.enqueue(30)
# queue_instance.enqueue(40)
# queue_instance.dequeue()
# queue_instance.display_nodes()


# Priority Queues (Using LINKEDLISTS)


# class Node:
#     def __init__(self, value):
#         self.value = value
#         self.next = None
#
#
# class PriorityQueue:
#     def __init__(self):
#         self.head = None
#         self.tail = None
#         self.length = 0
#
#     def enqueue(self, value):
#         new_node = Node(value)
#
#         if self.length == 0:
#             self.head = new_node
#             self.tail = new_node
#             self.length += 1
#
#         else:
#             if new_node.value < self.head.value:
#                 new_node.next = self.head
#                 self.head = new_node
#                 self.length += 1
#             else:
#                 current = self.head
#                 prev = current
#                 while current and current.value <= new_node.value:
#                     prev = current
#                     current = current.next
#                 prev.next = new_node
#                 new_node.next = current
#                 self.length += 1
#
#     def dequeue(self):
#         if self.length == 0:
#             print("The Queue is Empty!!")
#         elif self.length == 1:
#             self.head = None
#             self.tail = None
#             self.length -= 1
#         else:
#             current = self.head
#             self.head = self.head.next
#             self.length -= 1
#
#             if self.head is None:
#                 self.tail = None
#
#     def display_nodes(self):
#         current = self.head
#         while current:
#             print(current.value, end='---->')
#             current = current.next
#
#
# priority_queue_instance = PriorityQueue()
# priority_queue_instance.enqueue(10)
# priority_queue_instance.enqueue(20)
# priority_queue_instance.enqueue(50)
# priority_queue_instance.enqueue(30)
# priority_queue_instance.dequeue()
# priority_queue_instance.display_nodes()


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class Stack:
    def __init__(self, value):
        new_node = Node(value)
        self.top = new_node
        self.height = 1

    def print_stack(self):
        temp = self.top
        while temp != None:
            print(temp.value)
            temp = temp.next

    def push(self, value):
        new_node = Node(value)
        if self.top == None:
            self.top = new_node
        else:
            temp = self.top
            self.top = new_node
            new_node.next = temp
        self.height += 1

    def pop(self):
        if self.height == 0:
            return "your stack is empty"
        else:
            next_value = self.top.next
            self.top = next_value
        self.height -= 1


stack_instance = Stack(5)
stack_instance.push(10)
stack_instance.push(15)
stack_instance.push(20)
stack_instance.push(25)
stack_instance.print_stack()
stack_instance.pop()
stack_instance.pop()
stack_instance.pop()
print("Your stack after popping is: ")
stack_instance.print_stack()
