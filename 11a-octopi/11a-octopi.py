import numpy as np

DIM = 10
STEPS = 100


def is_valid(x, y):
    return x >= 0 and x < DIM and y >= 0 and y < DIM


def iter_neighbors(x, y):
    for x_n in range(x - 1, x + 2):
        for y_n in range(y - 1, y + 2):
            if is_valid(x_n, y_n) and (x_n, y_n) != (x, y):
                yield x_n, y_n


def get_lit(grid: np.array, x: int, y: int, flashes: int) -> np.array:
    energy = grid[y][x]
    if energy > 9:
        flashes += 1
        grid[y][x] = 0
        for x_n, y_n in iter_neighbors(x, y):
            if grid[y_n][x_n] > 0:
                grid[y_n][x_n] += 1
                grid, flashes = get_lit(grid, x_n, y_n, flashes)
    elif energy == 0:
        pass
    return grid, flashes


with open("input.txt") as file:
    grid = np.genfromtxt(file, delimiter=1, dtype=int)

flashes = 0
for i in range(STEPS):
    for x in range(DIM):
        for y in range(DIM):
            grid[y][x] += 1
    for x in range(DIM):
        for y in range(DIM):
            grid, flashes = get_lit(grid, x, y, flashes)

print(flashes)
