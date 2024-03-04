import networkx

def dfs_iterative(graph, start_vertex):
    visited = set()

    stack = [start_vertex]

    while stack:
        vertex = stack.pop()

        if vertex not in visited:
            print(f'|{vertex}|', end=' ', flush=True)

            visited.add(vertex)

            # Changed for networkx
            stack.extend(reversed(list(graph.neighbors(vertex))))

