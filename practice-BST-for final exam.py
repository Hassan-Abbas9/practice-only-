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
            while current != None:
                if data < current.data:
                    if current.left is None:  # we directly add the value, since left is EMPTY
                        current.left = new_node
                        current = None  # we added the left node, so we can terminate the insert.
                    else:
                        current = current.left  # We point the current to the LEFT NODE, if left node is not empty...

                elif data >= current.data:
                    if current.right is None:  # we directly add the value, since right is EMPTY
                        current.right = new_node
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
            elif data > current.data:
                current = current.right

        return False

    def delete(self, data):
        parent = None
        current = self.root

        # Search for the node to delete
        while current is not None and current.data != data:
            parent = current
            if data < current.data:
                current = current.left
            else:
                current = current.right

        # If the node with the given data is not found
        if current is None:
            print(f"Node with value {data} not found.")
            return

        # Node with data is found, now handle deletion cases
        if current.left is None and current.right is None:
            # Case 1: Node to be deleted has no children
            if parent is None:
                # If it's the root, set the root to None
                self.root = None
            elif parent.left == current:
                parent.left = None
            else:
                parent.right = None
        elif current.left is not None and current.right is not None:
            # Case 3: Node to be deleted has two children
            successor_parent = current
            successor = current.right

            while successor.left is not None:
                successor_parent = successor
                successor = successor.left

            # Copy the successor's data to the current node
            current.data = successor.data

            # Remove the successor (which is guaranteed to have at most one child)
            if successor_parent.left == successor:
                successor_parent.left = successor.right
            else:
                successor_parent.right = successor.right
        else:
            # Case 2: Node to be deleted has one child
            child = current.left if current.left is not None else current.right

            if parent is None:
                # If it's the root, update the root
                self.root = child
            elif parent.left == current:
                parent.left = child
            else:
                parent.right = child

        print(f"Deleted node with value {data}")


def main():
    bst = BinarySearchTree()
    print(bst.root)
    bst.insert(10)
    bst.insert(5)
    bst.insert(13)
    bst.insert(4)
    bst.insert(7)
    bst.insert(2)
    bst.insert(9)
    bst.insert(11)
    bst.insert(6)
    bst.insert(4)
    bst.delete(5)

    print(bst.search(5))
    print(f"root is {bst.root.data}")
    print(bst.root.left.right.data)



if __name__ == '__main__':
    main()

