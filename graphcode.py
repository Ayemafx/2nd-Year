all_edges = [
    ('A', 'B'), ('A', 'E'), ('A', 'D'), ('B', 'C'), ('C', 'F'), ('C', 'E'), ('D', 'E'), ('E', 'F')
]


class Graph:
    def __init__(self, nodes):
        self.nodes = nodes
        self.adj_list = {}

        for node in self.nodes:
            self.adj_list[node] = []

    def add_edge(self, u, v):
        self.adj_list[u].append(v)
        self.adj_list[v].append(u)

    def print_adj_list(self):
        print("Adjacency List")
        for node in self.nodes:
            print(f"{node} -> {self.adj_list[node]}")

    def to_adj_matrix(self):
        matrix = [[0] * len(self.nodes) for _ in range(len(self.nodes))]
        for i in range(len(self.nodes)):
            for j in range(len(self.nodes)):
                if i == j:
                    matrix[i][j] = 0
                elif self.nodes[i] in self.adj_list[self.nodes[j]]:
                    matrix[i][j] = 1
        return matrix


def print_matrix(matrix):
    print("Adjacency Matrix")
    for i in range(len(nodes)):
        for j in range(len(nodes)):
            print(matrix[i][j], end=" ")
        print()


nodes = ["A", "B", "C", "D", "E", "F"]
graph = Graph(nodes)

for u, v in all_edges:
    graph.add_edge(u, v)

graph.print_adj_list()
matrix = graph.to_adj_matrix()
print()
print_matrix(matrix)