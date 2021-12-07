import numpy as np

with open("input.txt") as file:
    start = np.array(file.read().strip().split(","), dtype=int)

median = np.median(start)
total_fuel = sum([abs(crab - median) for crab in start])

print(start)
print(median)
print(total_fuel)
