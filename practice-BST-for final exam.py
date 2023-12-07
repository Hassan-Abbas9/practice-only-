class Node:

    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data


class BinarySearchTree:
    def __init__(self):
        self.root = None  # initially the Root is empty

    def insert(self, data):
        new_node = Node(data)
        if self.root is None:
            self.root = new_node
        else:
            current = self.root  # the actual root should stay with us
            while current:
                if data < current.data:
                    if current.left is None:  # we directly add the value, since left is EMPTY
                        current.left = data
                        current = None  # we added the left node, so we can terminate the insert.
                    else:
                        current = current.left  # We point the current to the LEFT NODE, if left node is not empty...

                elif data >= current.data:
                    if current.right is None:  # we directly add the value, since right is EMPTY
                        current.right = data
                        current = None  # we added the right node, so we can terminate the insert.
                    else:
                        current = current.right
        print(f"Added the node with value {data}")

    def search(self, data):
        if self.root is None:
            print("Your BST is empty!")
            return
        current = self.root
        while current is not None:
            if data == current.data:
                return True
            elif data < current.data:
                current = current.left
            elif data < current.data:
                current = current.right

        return False
