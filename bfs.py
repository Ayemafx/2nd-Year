adj_list = {
    'A': ['B', 'E', 'D'],
    'B': ['A', 'C'],
    'C': ['B', 'F', 'E'],
    'D': ['A', 'E'],
    'E': ['A', 'C', 'D', 'F'],
    'F': ['C', 'E']
}

visited = []
queue = []


def bfs(visited, adj_list, node):
    visited.append(node)
    queue.append(node)

    while queue:  # Creating loop to visit each node
        m = queue.pop(0)
        print(m, end=" ")

        for neighbour in adj_list[m]:
            if neighbour not in visited:
                visited.append(neighbour)
                queue.append(neighbour)


# Driver Code
print("Following is the Breadth-First Search")
bfs(visited, adj_list, 'B')  # function calling