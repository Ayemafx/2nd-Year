adj_list = {
    'A': ['B', 'E', 'D'],
    'B': ['A', 'C'],
    'C': ['B', 'F', 'E'],
    'D': ['A', 'E'],
    'E': ['A', 'C', 'D', 'F'],
    'F': ['C', 'E']
}

visited = set()

def dfs(visited, adj_list, node):
    if node not in visited:
        print(node)
        visited.add(node)
        for neighbour in adj_list[node]:
            dfs(visited, adj_list, neighbour)

print("Following is the Depth-First Search")
dfs(visited, adj_list, 'A')

