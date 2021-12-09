import numpy as np


def check_neighbors(grid, x: int, y: int) -> bool:
    height = grid[y][x]
    neighbors = ((x, y + 1), (x + 1, y), (x - 1, y), (x, y - 1))
    for x_neighbor, y_neighbor in neighbors:
        if x_neighbor < 0 or y_neighbor < 0:
            continue
        try:
            neighbor_height = grid[y_neighbor][x_neighbor]
        except IndexError:
            continue
        else:
            if neighbor_height is not None and neighbor_height <= height:
                return False
    return True


x = 0
y = 0
grid = np.empty((100, 100), dtype=object)
candidates = []

with open("input.txt") as file:
    for line in file.readlines():
        x = 0
        for n in line.strip():
            grid[y][x] = int(n)
            if check_neighbors(grid, x, y):
                candidates.append((x, y))
            x += 1
        y += 1

low_points = []
risk_level = 0
for x, y in candidates:
    if check_neighbors(grid, x, y):
        low_points.append((x, y))
        risk_level += grid[y][x] + 1

print(risk_level)
