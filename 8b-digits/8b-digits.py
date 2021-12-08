from collections import Counter
from itertools import chain

DIGIT_SEGMENTS = {
    "abcefg": 0,
    "cf": 1,
    "acdeg": 2,
    "acdfg": 3,
    "bcdf": 4,
    "abdfg": 5,
    "abdefg": 6,
    "acf": 7,
    "abcdefg": 8,
    "abcdfg": 9,
}

# Known values based on unique occurrences across all digits
SEGMENT_COUNTS = {
    4: "e",
    6: "b",
    9: "f",
}

# Known digits based on number of signals
SEGMENT_LEN_TO_DIGIT = {
    2: 1,
    3: 7,
    4: 4,
    7: 8,
}


def subtract(d1: str, *d) -> str:
    return "".join(c for c in d1 if c not in chain(*d))


def translate(signal: str, key: dict) -> str:
    decoded = "".join(sorted(key[c] for c in signal))
    return str(DIGIT_SEGMENTS[decoded])


numbers = []
with open("input.txt") as file:
    for line in file.readlines():
        signals, output = line.strip().split(" | ")
        signals = signals.split(" ")

        digits = [None] * 10
        for signal in signals:
            i = SEGMENT_LEN_TO_DIGIT.get(len(signal))
            if i:
                digits[i] = signal
        c = Counter(chain.from_iterable(signals))
        # Calculate known values based on how many times they appear across all digits
        key = {SEGMENT_COUNTS[v]: k for k, v in c.items() if SEGMENT_COUNTS.get(v)}
        # a is the difference between 7 and 1
        key["a"] = subtract(digits[7], digits[1])
        # d is the difference between 4 and 1, with the known value of b removed
        key["d"] = subtract(digits[4], digits[1]).replace(key["b"], "")
        # g is the difference between 8 and 4 and 7, with the known value of e removed
        key["g"] = subtract(digits[8], digits[4], digits[7]).replace(key["e"], "")
        # Now we know enough to recreate 6
        digits[6] = "".join(key.values())
        # c is the difference between 8 and 6
        key["c"] = subtract(digits[8], digits[6])

        # Need to flip our dictionary to translate
        inverted_key = {v: k for k, v in key.items()}

        # Combine solved numbers together and recast to an int
        numbers.append(
            int("".join(translate(digit, inverted_key) for digit in output.split(" ")))
        )

print(sum(numbers))
