N_DAYS = 256
calendar = [0] * (N_DAYS + 10)

with open("input.txt") as file:
    start = [int(n) for n in file.read().strip().split(",")]

n = 0
for birthday in start:
    calendar[birthday + 1] += 1

for t in range(N_DAYS + 1):
    n_born_today = calendar[t]
    calendar[t + 7] += n_born_today
    calendar[t + 9] += n_born_today

print(sum(calendar[: N_DAYS + 1]) + len(start))
