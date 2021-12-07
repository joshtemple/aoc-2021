import numpy as np


def fuel_cost(distance: int) -> int:
    return sum(range(distance + 1))


with open("input.txt") as file:
    start = np.array(file.read().strip().split(","), dtype=int)

costs = []
for position in range(min(start), max(start)):
    costs.append(
        (position, sum(fuel_cost(abs(crab - position)) for crab in start))
    )

print(min(costs, key=lambda x: x[1]))
