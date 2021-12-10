CLOSED = {"(": ")", "[": "]", "{": "}", "<": ">"}

POINTS = {
    ")": 3,
    "]": 57,
    "}": 1197,
    ">": 25137,
}

score = 0
queue = []

with open("input.txt") as file:
    for line in file.readlines():
        for char in line.strip():
            if char in CLOSED:
                queue.append(char)
            else:
                if CLOSED[queue.pop()] != char:
                    score += POINTS[char]
                    break

print(score)
