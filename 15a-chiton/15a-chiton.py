import matplotlib.pyplot as plt
import numpy as np
import networkx as nx

with open("input.txt") as file:
    grid = np.genfromtxt(file, delimiter=1, dtype=int)

DIM = len(grid)


def is_valid(x: int, y: int) -> bool:
    return x >= 0 and x < DIM and y >= 0 and y < DIM


G = nx.DiGraph()
for i, row in enumerate(grid):
    for j, col in enumerate(row):
        for y_n, x_n in ((i, j + 1), (i + 1, j), (i, j - 1), (i - 1, j)):
            if is_valid(x_n, y_n):
                weight = grid[y_n][x_n]
                print(f"({j}, {i}) -> ({x_n}, {y_n}) [{weight}]")
                G.add_edge((j, i), (x_n, y_n), weight=weight)

path = nx.shortest_path(G, (0, 0), (DIM - 1, DIM - 1), "weight")
risk = sum([grid[y][x] for x, y in path])
print(risk - grid[0][0])
