import numpy as np
import itertools

boards = []

with open("input.txt") as file:
    j = -1
    for i, line in enumerate(file.readlines()):
        if i == 0:
            draw_seq = tuple(int(n) for n in line.strip().split(','))
            print(f'Draw sequence [{len(draw_seq)}]:', draw_seq)
        else:
            if line == '\n':
                j += 1
                boards.append(np.empty((0, 5), dtype=int))
            else:
                row = np.array(line.strip().split(), dtype=int)
                boards[j] = np.vstack((boards[j], row))

winners = []
last_winner = None

for i in range(len(draw_seq)):
    d = set(draw_seq[:i + 1])

    for j, board in enumerate(boards):
        if j not in winners:
            for row in itertools.chain(board, board.transpose()):
                if set(row.flatten()) <= d:
                    last_winner = board
                    last_winning_round = i
                    winners.append(j)

unmarked = set(last_winner.flatten()) - set(draw_seq[:last_winning_round + 1])
last_called = draw_seq[last_winning_round]
score = sum(unmarked) * last_called

print(last_winner)
print(sum(unmarked), '*', last_called, '=', score)