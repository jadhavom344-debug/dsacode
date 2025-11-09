# ------------------------------------------
# BFS using Adjacency List
# DFS using Adjacency Matrix
# ------------------------------------------

# Graph nodes
nodes = ['A', 'B', 'C', 'D', 'E']

# Adjacency List for BFS
adj_list = {
    'A': ['B', 'C'],
    'B': ['D'],
    'C': ['E'],
    'D': ['E'],
    'E': []
}

# Adjacency Matrix for DFS (A, B, C, D, E)
adj_matrix = [
    [0, 1, 1, 0, 0],  # A
    [0, 0, 0, 1, 0],  # B
    [0, 0, 0, 0, 1],  # C
    [0, 0, 0, 0, 1],  # D
    [0, 0, 0, 0, 0]   # E
]

# ------------------------------------------
# BFS Implementation
# ------------------------------------------
from collections import deque

def bfs(start):
    visited = set()
    queue = deque([start])
    result = []

    while queue:
        node = queue.popleft()
        if node not in visited:
            result.append(node)
            visited.add(node)
            for neighbor in adj_list[node]:
                if neighbor not in visited:
                    queue.append(neighbor)
    return result

# ------------------------------------------
# DFS Implementation (Adjacency Matrix)
# ------------------------------------------
def dfs(start_index, visited=None):
    if visited is None:
        visited = set()
    visited.add(start_index)

    node = nodes[start_index]
    result = [node]

    for neighbor_index in range(len(nodes)):
        if adj_matrix[start_index][neighbor_index] == 1 and neighbor_index not in visited:
            result.extend(dfs(neighbor_index, visited))

    return result

# ------------------------------------------
# Running both algorithms
# ------------------------------------------
print("BFS starting from A:", bfs("A"))
print("DFS starting from A:", dfs(0))
