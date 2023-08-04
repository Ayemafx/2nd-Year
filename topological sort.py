from collections import deque

def topological_sort_dfs(adj_list):
    sorted_nodes = deque()
    visited = set()

    def dfs(node):
        visited.add(node)
        for neighbor in adj_list[node]:
            if neighbor not in visited:
                dfs(neighbor)
        sorted_nodes.appendleft(node)

    for node in adj_list:
        if node not in visited:
            dfs(node)

    return list(sorted_nodes)


adj_list = {
    'A': ['B', 'E', 'D'],
    'B': ['A', 'C'],
    'C': ['B', 'F', 'E'],
    'D': ['A', 'E'],
    'E': ['A', 'C', 'D', 'F'],
    'F': ['C', 'E']
}


print("Topological Sorted Array")
print(topological_sort_dfs(adj_list))