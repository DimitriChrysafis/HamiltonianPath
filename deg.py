# deg.py

import networkx as nx
import numpy
import numpy as np


def find_vertex_degrees(matrix):
    matrix = np.array(matrix)
    G = nx.Graph(matrix)
    degrees = dict(G.degree)

    for node, degree in degrees.items():
        print(f"Vertex {node}: Degree {degree}")

if __name__ == "__main__":
    matrix = [
        # Your adjacency matrix here
    ]

    find_vertex_degrees(matrix)
