# main.py

import ham
import graph
import numpy as np
import deg

if __name__ == "__main__":
    adjacency_matrix = ham.adjacency_matrix

    print("Hamiltonian Paths and Cycles:")
    all_paths = ham.all_paths
    for start_node, path, hamiltonian_status in all_paths:
        print(f"Starting from {start_node}: {path} - {hamiltonian_status}")

    print("\nGraph and Degrees:")
    deg.find_vertex_degrees(adjacency_matrix)
    graph.generate_and_display_graph(adjacency_matrix)



