# Hamiltonian Path Finder
![Sample image](/sample.jpg)


This Python project is designed to find Hamiltonian paths and cycles in a given graph. The initial adjacency matrix for the graph is provided below:

```python
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
```
## ham.py

The `ham.py` file contains the initial adjacency matrix of the graph.  It uses NetworkX to work with graphs.

## graph.py

The `graph.py` file generates a graphical representation of the given graph and displays it. 

## deg.py

The `deg.py` file calculates the degrees of vertices in the graph.
