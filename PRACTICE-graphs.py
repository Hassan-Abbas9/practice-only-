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


if __name__ == '__main__':
    main()

#####################
#        AL
#####################


