import networkx as nx
import matplotlib.pyplot as plt

from DFS_iterative import dfs_iterative
from BFS_iterative import bfs_iterative

from graph import create_graph, visualize_graph


def compare_alg(graph, start):
    print("DFS traversal:")
    dfs_iterative(graph, start)

    print("\nBFS traversal:")
    bfs_iterative(graph, start)

    
if __name__ == '__main__': 
    G = create_graph()
    compare_alg(G, 'WHitehall')
    visualize_graph(G)
    
