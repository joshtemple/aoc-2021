import numpy as np

N_BITS = 12

total = np.array((0, ) * N_BITS, dtype=int)
num_lines = 0

def bit_not(n: int, numbits: int) -> int:
    """Bitwise complement for n bits, unsigned. From S/O"""
    return (1 << numbits) - 1 - n

with open("input.txt") as file:
    for line in file.readlines():
        num_lines += 1
        total += np.array(list(line.strip()), dtype=int)

gamma_binary_ndarray = ((total / num_lines) >= 0.5).astype(int)
gamma_string = ''.join(map(str, gamma_binary_ndarray))
gamma = int(gamma_string, 2)

print('gamma:', gamma)

epsilon = bit_not(gamma, N_BITS)
print('epsilon:', epsilon)

print(gamma * epsilon)