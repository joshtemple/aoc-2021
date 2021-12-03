import numpy as np

N_BITS = 12
total = np.empty((0, N_BITS), dtype=int)

def bin_arr_to_int(arr) -> int:
    return int(''.join(map(str, arr)), 2)

def calculate_gamma(arr) -> str:
    gamma = ((arr.sum(axis=0) / len(arr)) >= 0.5).astype(int)
    return gamma

def calculate_rating(numbers, rating_type: str, index = 0) -> int:
    if len(numbers) == 1:
        return bin_arr_to_int(numbers[0])
    else:
        gamma = calculate_gamma(numbers)
        if rating_type == 'oxygen':
            mode_bits = gamma
        elif rating_type == 'co2':
            mode_bits = (gamma == 0).astype(int) # Flip bits, this is epsilon
        else:
            raise ValueError(f'Unexpected rating type {rating_type}')
        matched = np.empty((0, N_BITS), dtype=int)
        for arr in numbers:
            if arr[index] == mode_bits[index]:
                matched = np.vstack((matched, arr))
        return calculate_rating(matched, rating_type, index + 1)

with open("input.txt") as file:
    for line in file.readlines():
        arr = np.array(list(line.strip()), dtype=int)
        total = np.vstack((total, arr))

oxygen = calculate_rating(total, 'oxygen')
print('Oxygen:', oxygen)
co2 = calculate_rating(total, 'co2')
print('CO2:', co2)
print(oxygen * co2)
