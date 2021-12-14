from typing import Dict
from collections import Counter

STEPS = 40
rules: Dict[str, str] = {}

def split(chunk: str, counts: Dict[str, int], step: int = 0) -> Dict[str, int]:
    print(counts)
    if chunk in rules:
        insert = rules[chunk]
        counts[insert] += 1
    else:
        return counts

    if step < (STEPS - 1):
        counts = split(chunk[0] + insert, counts, step + 1)
        counts = split(insert + chunk[1], counts, step + 1)
    else:
        return counts

    return counts

with open('test.txt') as file:
    template = file.readline().strip()
    file.readline()
    for line in file.readlines():
        pair, element = line.strip().split(' -> ')
        rules[pair] = element

counts = Counter(template)
for i in range(len(template) - 1):
    chunk = template[i : i + 2]
    counts = split(chunk, counts)

print(counts)
