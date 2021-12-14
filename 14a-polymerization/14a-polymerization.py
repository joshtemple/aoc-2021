from collections import Counter

STEPS = 10
rules = {}

with open('input.txt') as file:
    template = file.readline().strip()
    file.readline()
    for line in file.readlines():
        pair, element = line.strip().split(' -> ')
        rules[pair] = element

for i in range(STEPS):
    polymer = ''
    for i in range(len(template) - 1):
        chunk = template[i : i + 2]
        polymer += chunk[0] + rules.get(chunk, "")

    polymer += template[-1]
    template = polymer

c = Counter(polymer)
print(max(c.values()) - min(c.values()))
