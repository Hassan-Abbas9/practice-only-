##########################
#####Adjacency Martix#####
##########################


class Graph:

    def __init__(self, num_vertices):
        self.num_vertices = num_vertices
        self.adj_matrix = [[0] * num_vertices for _ in range(num_vertices)]

    def add_vertex(self):
        self.num_vertices += 1
        for row in self.adj_matrix:
            row.append(0)
        self.adj_matrix.append([0] * self.num_vertices)
        print("Added vetrex", self.num_vertices - 1)

    def add_edge(self, v1, v2):
        if 0 <= v1 < self.num_vertices and 0 <= v2 < self.num_vertices:
            self.adj_matrix[v1][v2] = 1
            self.adj_matrix[v2][v1] = 1
            print(f"Added an edge between vertices {v1} and {v2}")
        else:
            print(f"Invalid vertices {v1} and {v2}")

    def display_graph(self):
        if len(self.adj_matrix) == 0:
            print("Graph is empty!\n")
            return
        for row in self.adj_matrix:
            print(row)
            # print(" ".join(map(str,row)))
            # the gap is that we r saying keep gaps

def main():
    print("\n#######################")
    print("          AM           ")
    print("#######################\n")

    graph = Graph(4)
    graph.display_graph()
    graph.add_vertex()
    graph.display_graph()

    graph.add_edge(0, 1)
    graph.add_edge(0, 2)
    graph.add_edge(1, 3)
    graph.add_edge(2, 3)
    graph.add_edge(3, 4)
    graph.add_edge(5, 1)

    graph.display_graph()


# if __name__ == '__main__':
#     main()

#####################
#        AL
#####################

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.length = 0

    def add_node(self, node):
        new_node = Node(node)
        self.head = new_node
        self.length += 1

    def display_node(self):
        temp = self.head
        while temp:
            print(temp.value, end='-->')
            temp = temp.next
        print("None")

class Graph2:
    def __init__(self):
        self.adj_list = {}

    def add_vertex(self, vertex):
        if vertex not in self.adj_list:
            self.adj_list[vertex] = LinkedList()
            return
        print(f'vertex {vertex} already exists')

    def add_edge(self, v1, v2):
        if v1 in self.adj_list and v2 in self.adj_list:
            self.adj_list[v1].add_node(v1)
            self.adj_list[v2].add_node(v2)
        else:
            print(f"Invalid vertices {v1} and {v2}")

    def display_graph(self):
        if self.adj_list == {}:
            print("Graph is empty!\n")
            return
        for vertex in self.adj_list:
            print(vertex + ":", end=" ")
            self.adj_list[vertex].display_node()


if __name__ == '__main__':
    print("\n#######################")
    print("          AM           ")
    print("#######################\n")

    graph = Graph2()
    graph.display_graph()
    graph.add_vertex("A")
    graph.add_vertex("B")
    graph.add_vertex("C")
    graph.add_vertex("D")
    graph.add_vertex("E")
    graph.add_vertex("C")
    graph.add_vertex("Z")
    graph.display_graph()
    graph.add_edge("A", "B")
    graph.add_edge("B", "C")
    graph.add_edge("C", "A")
    graph.display_graph()