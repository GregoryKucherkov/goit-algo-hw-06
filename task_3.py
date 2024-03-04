import networkx as nx
import matplotlib.pyplot as plt

from dijkstra import dijkstra
from graph import create_graph


def main():
    G = create_graph()
    distances = dijkstra(G, 'WHitehall') 
    for key, value in distances.items():
        print(f'To station: {key} | Closest distance: {value} ')

   
if __name__ == '__main__': 
    main()

