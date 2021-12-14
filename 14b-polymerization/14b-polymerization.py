from collections import defaultdict, Counter

STEPS = 40
rules: dict[str, str] = {}

with open("input.txt") as file:
    template = file.readline().strip()
    file.readline()
    for line in file.readlines():
        pair, element = line.strip().split(" -> ")
        rules[pair] = (pair[0] + element, element + pair[1])

pairs = [template[i : i + 2] for i in range(len(template) - 1)]
counts = defaultdict(lambda: 0)
counts.update(Counter(pairs))

for i in range(STEPS):
    offspring = defaultdict(lambda: 0)
    for pair, count in counts.items():
        if pair in rules:
            for each in rules[pair]:
                offspring[each] += count
        else:
            offspring[pair] += count
    counts = offspring

char_counts = defaultdict(lambda: 0)
for pair, count in counts.items():
    for char in pair:
        char_counts[char] += count

for char in char_counts:
    char_counts[char] = int(char_counts[char] / 2)

char_counts[template[0]] += 1
char_counts[template[-1]] += 1

print(max(char_counts.values()) - min(char_counts.values()))
