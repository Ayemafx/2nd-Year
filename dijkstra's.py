import sys
from heapq import heapify, heappush, heappop

def dijkstra_algorithm(adj_list, src, dest):
    inf = sys.maxsize
    node_data = {
        'A': {'cost': inf, 'pred': []},
        'B': {'cost': inf, 'pred': []},
        'C': {'cost': inf, 'pred': []},
        'D': {'cost': inf, 'pred': []},
        'E': {'cost': inf, 'pred': []},
        'F': {'cost': inf, 'pred': []}
    }

    node_data[src]['cost'] = 0
    visited = []
    temp = src #node that is currently being visited
    for i in range(5): #total vertices - 1 range
        if temp not in visited:
            visited.append(temp)
            min_heap = []
            for j in adj_list[temp]:
                cost = node_data[temp]['cost'] + adj_list[temp][j]
                if cost < node_data[j]['cost']:
                    node_data[j]['cost'] = cost
                    node_data[j]['pred'] = node_data[temp]['pred'] + list(temp)
                heappush(min_heap, (node_data[j]['cost'], j))
        heapify(min_heap)
        temp = min_heap[0][1]
    print("Shortest Distance: " + str(node_data[dest]['cost']))
    print("Shortest Path: " + str(node_data[dest]['pred'] + list(dest)))

if __name__ == "__main__":
    adj_list = {
        'A': {'B': 3, 'E': 6, 'D': 5},
        'B': {'A': 3, 'C': 7},
        'C': {'B': 7, 'F': 5, 'E': 4},
        'D': {'A': 5, 'E': 10},
        'E': {'A': 6, 'C': 4, 'D': 10, 'F': 10},
        'F': {'C': 5, 'E': 10}
    }

dijkstra_algorithm(adj_list, 'F', 'A')

