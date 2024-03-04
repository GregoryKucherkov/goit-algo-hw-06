def dijkstra(graph, start):
    distances = {vertex: float('infinity') for vertex in graph}
    distances[start] = 0
    #changed for networkx 
    unvisited = list(graph.nodes())
    

    while unvisited:
        current_vertex = min(unvisited, key=lambda vertex: distances[vertex])
       
        if distances[current_vertex] ==float('infinity'):
            break

        for neighbor, weight in graph[current_vertex].items():
            #changed for networkx to get access to weight
            distance = distances[current_vertex] + weight['weight']

            if distance < distances[neighbor]:
                distances[neighbor] = distance

        unvisited.remove(current_vertex)
    
    return distances


if __name__ == '__main__': 
    dijkstra()

