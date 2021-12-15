import numpy as np
import networkx as nx


def is_valid(x: int, y: int) -> bool:
    return x >= 0 and x < dim and y >= 0 and y < dim


with open("input.txt") as file:
    template = np.genfromtxt(file, delimiter=1, dtype=int)

row = template

for i in range(1, 5):
    new = np.vectorize(lambda x: x + i if (x + i) <= 9 else (x + i) - 9)(
        template
    )
    row = np.concatenate((row, new), axis=1)
grid = row
for i in range(1, 5):
    new = np.vectorize(lambda x: x + i if (x + i) <= 9 else (x + i) - 9)(row)
    grid = np.concatenate((grid, new))

dim = len(grid)

G = nx.DiGraph()
for i, row in enumerate(grid):
    for j, col in enumerate(row):
        for y_n, x_n in ((i, j + 1), (i + 1, j), (i, j - 1), (i - 1, j)):
            if is_valid(x_n, y_n):
                weight = grid[y_n][x_n]
                print(f"({j}, {i}) -> ({x_n}, {y_n}) [{weight}]")
                G.add_edge((j, i), (x_n, y_n), weight=weight)

path = nx.shortest_path(G, (0, 0), (dim - 1, dim - 1), "weight")
risk = sum([grid[y][x] for x, y in path])
print(risk - grid[0][0])
