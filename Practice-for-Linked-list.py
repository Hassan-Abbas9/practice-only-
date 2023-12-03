class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def display_nodes(self):
        current = self.head
        while current:
            print(current.value, end="--->")
            current = current.next

    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node

        self.length += 1
        return True


LL_instance = LinkedList()
LL_instance.append(30)
LL_instance.append(20)
LL_instance.append(10)
LL_instance.display_nodes()








