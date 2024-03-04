import networkx as nx
import matplotlib.pyplot as plt

from graph import create_graph, visualize_graph
    
def main():
    G = create_graph()

    #Аналіз графа:
    #Граф має 19 вершин
    print(G.number_of_nodes())

    # Граф має 23 ребра
    print(G.number_of_edges())

    # цей принт показує кількість звязків вузлів, найбільше Cortland:4, WHitehall: 4
    print(G.degree())

    # Чим більше з'єднань має вузол, тим більш центральним він є
    print(nx.degree_centrality(G))

    visualize_graph(G)


if __name__ == '__main__': 
    main()
    
