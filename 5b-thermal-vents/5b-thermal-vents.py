import numpy as np
import re

X_MAX = 1000
Y_MAX = 1000

class Line:
    def __init__(self, x1, y1, x2, y2):
        self.start = (int(x1), int(y1))
        self.end = (int(x2), int(y2))

    def __repr__(self) -> str:
        return f"Line({self.start} -> {self.end})"

    @property
    def is_vertical(self):
        return self.start[0] == self.end[0]

    @property
    def is_horizontal(self):
        return self.start[1] == self.end[1]

    @property
    def is_diagonal(self):
        return abs(self.end[1] - self.start[1]) == abs(self.end[0] - self.start[0])

lines: list[Line] = []
with open('input.txt') as file:
    text = file.read()

raw_lines = re.findall('^(\d+),(\d+) -> (\d+),(\d+)', text, re.MULTILINE)
lines = [Line(*raw) for raw in raw_lines]

coordinates = np.zeros((X_MAX, Y_MAX), dtype=int)
for line in lines:
    if line.is_horizontal:
        x1 = line.start[0]
        x2 = line.end[0]
        y = line.start[1]
        step = 1 if x1 < x2 else -1
        for x in range(x1, x2 + step, step):
            coordinates[y][x] += 1
    elif line.is_vertical:
        y1 = line.start[1]
        y2 = line.end[1]
        x = line.start[0]
        step = 1 if y1 < y2 else -1
        for y in range(y1, y2 + step, step):
            coordinates[y][x] += 1
    elif line.is_diagonal:
        x1 = line.start[0]
        x2 = line.end[0]
        y1 = line.start[1]
        y2 = line.end[1]
        x_step = 1 if x1 < x2 else -1
        y_step = 1 if y1 < y2 else -1
        for x, y in zip(range(x1, x2 + x_step, x_step), range(y1, y2 + y_step, y_step)):
            coordinates[y][x] += 1
    else:
        continue

num_points = len([c for c in coordinates.flatten() if c > 1])
print(num_points)
