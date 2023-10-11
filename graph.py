# graph.py

import numpy as np
import networkx as nx
import matplotlib.pyplot as plt
import cv2

def generate_and_display_graph(matrix):
    matrix = np.array(matrix)
    G = nx.Graph(matrix)
    layout = nx.spring_layout(G)

    plt.figure(figsize=(10, 10))
    nx.draw(G, pos=layout, with_labels=True, node_color='lightblue', node_size=500, font_size=12, font_color='black', font_weight='bold', width=2)

    plt.savefig("graph.png")
    image = cv2.imread("graph.png")

    cv2.imshow("Graph Image", image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == "__main__":
    matrix = [
        # Your adjacency matrix here
    ]

    generate_and_display_graph(matrix)
