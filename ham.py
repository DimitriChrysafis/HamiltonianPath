# ham.py

import networkx as nx
import numpy as np

adjacency_matrix = [
    [0, 1, 1, 0, 0, 0, 0, 1, 0, 0],
    [1, 0, 1, 1, 0, 0, 0, 0, 0, 0],
    [1, 1, 0, 0, 1, 0, 1, 0, 0, 1],
    [0, 1, 0, 0, 1, 0, 0, 0, 0, 0],
    [0, 0, 1, 1, 0, 1, 1, 0, 0, 0],
    [0, 0, 0, 0, 1, 0, 1, 0, 0, 0],
    [0, 0, 0, 0, 1, 1, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 1, 1],
    [0, 0, 0, 0, 0, 0, 0, 1, 0, 1],
    [0, 0, 1, 0, 0, 0, 1, 1, 1, 0]
]

def is_hamiltonian_path_or_cycle(path, graph):
    if len(path) != len(set(path)):
        return "Not a Hamiltonian (Repeated vertices)"
    if len(path) == len(graph.nodes()):
        if graph.has_edge(path[-1], path[0]):
            return "Hamiltonian Cycle"
        else:
            return "Hamiltonian Path"
    elif len(path) == len(graph.nodes()) - 1:
        return "Hamiltonian Path"
    else:
        return "Not a Hamiltonian (Incomplete path)"

matrix = np.array(adjacency_matrix)
G = nx.Graph(matrix)

def enumerate_paths(graph, start, path=[]):
    path = path + [start]
    if len(path) == len(graph.nodes()):
        yield path
    for neighbor in graph.neighbors(start):
        if neighbor not in path:
            for new_path in enumerate_paths(graph, neighbor, path):
                yield new_path

all_paths = []
for start_node in G.nodes():
    paths = list(enumerate_paths(G, start=start_node))
    all_paths.extend([(start_node, path, is_hamiltonian_path_or_cycle(path, G)) for path in paths])

for start_node, path, hamiltonian_status in all_paths:
    print(f"Starting from {start_node}: {path} - {hamiltonian_status}")
