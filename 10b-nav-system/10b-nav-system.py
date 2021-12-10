CLOSED = {"(": ")", "[": "]", "{": "}", "<": ">"}

POINTS = {
    ")": 1,
    "]": 2,
    "}": 3,
    ">": 4,
}

score = 0


def score_string(s) -> int:
    score = 0
    for char in s:
        score *= 5
        score += POINTS[CLOSED[char]]
    return score


scores = []
with open("input.txt") as file:
    for line in file.readlines():
        queue = []
        for char in line:
            if char in CLOSED:
                queue.append(char)
            elif char == "\n":
                scores.append(score_string(reversed(queue)))
            elif CLOSED[queue.pop()] != char:
                break

middle = int((len(scores) - 1) / 2)
print(sorted(scores)[middle])
