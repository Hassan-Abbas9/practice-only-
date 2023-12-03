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

    def add_node_at_beginning(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
            self.head.next = None
        elif self.length == 1:
            self.head = new_node
            self.head.next = self.tail
        else:
            temp = self.head
            self.head = new_node
            self.head.next = temp

        self.length += 1
        return True

    def delete_node_at_beginning(self):
        delete = self.head
        if self.length == 0:
            print("You have no nodes in your linked list")
        elif self.length == 1:
            self.head = None
            self.tail = None
        else:
            self.head = self.head.next

        self.length -= 1
        return True

    def pop(self):
        if self.length == 0:
            return None
        temp = self.head
        pre = self.head
        while(temp.next):
            pre = temp
            temp = temp.next
        self.tail = pre
        self.tail.next = None
        self.length -= 1
        if self.length == 0:
            self.head = None
            self.tail = None


LL_instance = LinkedList()
LL_instance.append(30)
LL_instance.append(20)
LL_instance.append(10)
LL_instance.add_node_at_beginning(40)
LL_instance.add_node_at_beginning(50)
LL_instance.add_node_at_beginning(60)
LL_instance.delete_node_at_beginning()
LL_instance.delete_node_at_beginning()
LL_instance.pop()
LL_instance.display_nodes()

