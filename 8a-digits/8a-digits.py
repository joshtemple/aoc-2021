DIGIT_SEGMENTS = {
    0: 'abcefg',
    1: 'cf',
    2: 'acdeg',
    3: 'acdfg',
    4: 'bcdf',
    5: 'abdfg',
    6: 'abdefg',
    7: 'acf',
    8: 'abcdefg',
    9: 'abcdfg'
}

unique_segment_digits = 0
with open('input.txt') as file:
    for line in file.readlines():
        for segment in line.strip().split(' | ')[1].split(' '):
            if len(segment) in (2, 3, 4, 7):
                unique_segment_digits += 1

print(unique_segment_digits)