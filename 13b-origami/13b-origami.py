import re

folds = []
points = set()

with open("input.txt") as file:
    for line in file.readlines():
        if line == "\n":
            continue
        elif line.strip().startswith("fold along"):
            dim, line = re.findall("(x|y)=(\d+)", line)[0]
            folds.append((dim, int(line)))
        else:
            points.add(tuple(int(n) for n in line.strip().split(",")))


def fold(points: set, dim: str, line: int) -> set:
    points_xf = set()
    if dim == "y":
        for x, y in points:
            if y > line:
                points_xf.add((x, line - (y - line)))
            else:
                points_xf.add((x, y))
    elif dim == "x":
        for x, y in points:
            if x > line:
                points_xf.add((line - (x - line), y))
            else:
                points_xf.add((x, y))

    return points_xf


def plot(points):
    max_x = max(p[0] for p in points)
    max_y = max(p[1] for p in points)
    grid = [[" " for i in range(max_x + 1)] for j in range(max_y + 1)]

    for x, y in sorted(points):
        grid[y][x] = "#"

    for row in grid:
        for col in row:
            print(col, end=" ")
        print()


for dim, line in folds:
    points = fold(points, dim, line)

plot(points)
