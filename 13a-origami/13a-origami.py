import re

folds = []
points = []

with open("input.txt") as file:
    for line in file.readlines():
        if line == "\n":
            continue
        elif line.strip().startswith("fold along"):
            dim, fold = re.findall("(x|y)=(\d+)", line)[0]
            folds.append((dim, int(fold)))
        else:
            points.append(tuple(int(n) for n in line.strip().split(",")))

print(folds)
print(points)

points_xf = set()
for dim, fold in folds[:1]:
    if dim == "y":
        for x, y in points:
            if y > fold:
                points_xf.add((x, fold - (y - fold)))
            else:
                points_xf.add((x, y))
    elif dim == "x":
        for x, y in points:
            if x > fold:
                points_xf.add((fold - (x - fold), y))
            else:
                points_xf.add((x, y))

print(points_xf)
print(len(points_xf))
