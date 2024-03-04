from collections import deque

def bfs_iterative(graph, start):
    visited = set()
    queue = deque([start])

    while queue:    
        vertex = queue.popleft()
        if vertex not in visited:
            print(f'|{vertex}|', end=' ', flush=True)

            visited.add(vertex)
            queue.extend(set(graph[vertex]) - visited)
    
