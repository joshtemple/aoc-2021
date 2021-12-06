from itertools import chain
from multiprocessing import Pool

N_DAYS = 256


def reproduce(fish):
    if fish == 0:
        return (6, 8)
    else:
        return (fish - 1,)


with open("input.txt") as file:
    fish = [int(n) for n in file.read().strip().split(",")]

pool = Pool()
t = 0
while t < N_DAYS:
    fish = list(chain(*pool.map(reproduce, fish)))
    print(f"{t}: {len(fish)}")
    t += 1

print(len(fish))
