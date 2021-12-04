import numpy as np
import itertools

boards = []

with open("input.txt") as file:
    j = -1
    for i, line in enumerate(file.readlines()):
        if i == 0:
            draw_seq = tuple(int(n) for n in line.strip().split(','))
            print('Draw sequence:', draw_seq)
        else:
            if line == '\n':
                j += 1
                boards.append(np.empty((0, 5), dtype=int))
            else:
                row = np.array(line.strip().split(), dtype=int)
                boards[j] = np.vstack((boards[j], row))

winner = None

for i in range(len(draw_seq)):
    if winner is None:
        d = set(draw_seq[:i + 1])
    else:
        break

    for board in boards:
        for row in itertools.chain(board, board.transpose()):
            if set(row.flatten()) <= d:
                if winner is not None:
                    raise RuntimeError('Aready a winner in this round')
                else:
                    winner = board
                    last_called = draw_seq[i]

unmarked = set(winner.flatten()) - d
score = sum(unmarked) * last_called

print(winner)
print(sum(unmarked), '*', last_called, '=', score)