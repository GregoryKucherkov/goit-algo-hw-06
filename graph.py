import networkx as nx
import matplotlib.pyplot as plt

def create_graph():
    G = nx.Graph()

    # Відображення частини модифікованого метро New York
    edges_with_weights = [
        ("WHitehall", "Rector", {'weight': 2}),
        ("WHitehall", "Bowling", {'weight': 1}),
        ("WHitehall", "Cortland", {'weight': 2}),
        ("WHitehall", "City_hall", {'weight': 2}),
        ("Rector", "Rector_green", {'weight': 1}),
        ("Rector", "Cortland", {'weight': 2}),
        ("Cortland", "Cortland_green", {'weight': 1}),
        ("Bowling", "Rector_green", {'weight': 1}),
        ("Rector_green", "Wall_st", {'weight': 1}),
        ("Wall_st", "Cortland_green", {'weight': 1}),
        ("Cortland", "City_hall", {'weight': 2}),
        ("Cortland_green", "Chambers", {'weight': 2}),
        ("City_hall", "Canal", {'weight': 2}),
        ("Canal", "Canal_green", {'weight': 1}),
        ("Canal", "Prince", {'weight': 3}),
        ("Chambers", "Canal_green", {'weight': 3}),
        ("Canal_green", "Spring", {'weight': 3}),
        ("Spring", "Bleecker", {'weight': 3}),
        ("Prince", "8th_street", {'weight': 3}),
        ("8th_street", "14_union", {'weight': 3}),
        ("14_union", "14_union_green", {'weight': 1}),
        ("14_union_green", "3-av", {'weight': 4}),
        ("Bowling", "Borough", {'weight': 4})
    ]
    
    G.add_edges_from(edges_with_weights)
    return G

def visualize_graph(G):
    pos = nx.spring_layout(G)

    nx.draw(G, pos, with_labels=True, node_size=200, node_color="skyblue", font_size=8, font_color="black", font_weight="bold", edge_color="gray")
    plt.show()
    
