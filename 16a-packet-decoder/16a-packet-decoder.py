def hex_to_bin(s: str) -> str:
    return bin(int(s, 16))[2:].zfill(len(s) * 4)


def show_index(s: str, i: int):
    print(s)
    print(" " * i, "^", f" i = {i}", sep="")


def parse_literal(s: str) -> int:
    parsed = ""
    for i in range(0, len(s) - (len(s) % 5), 5):
        parsed += s[i + 1 : i + 5]
    return int(parsed, 2)


def parse_packet(s: str, i: int = 0, version_sum=0):
    version = int(s[i : i + 3], 2)
    version_sum += version
    print(f"v{version},", end=" ")
    i += 3
    type_id = int(s[i : i + 3], 2)
    print(f"{'literal' if type_id == 4 else 'operator'}:", end=" ")
    i += 3

    length_type_id = None
    count_sub = None
    len_sub = None

    if type_id == 4:
        sentinel = "0"
        literal = ""
        while s[i] != sentinel:
            literal += s[i + 1 : i + 5]
            i += 5
        literal += s[i + 1 : i + 5]
        literal = int(literal, 2)
        i += 5
        print(literal)
    else:
        length_type_id = s[i]
        print(f"[{length_type_id}]")
        i += 1
        if length_type_id == "1":
            count_sub = int(s[i : i + 11], 2)
            print(f"Using number of subpackets, {count_sub}")
            i += 11
            for _ in range(count_sub):
                i, version_sum = parse_packet(s, i, version_sum)
        elif length_type_id == "0":
            len_sub = int(s[i : i + 15], 2)
            print(f"Using number of bits, {len_sub}")
            i += 15
            sub_start = i
            while i < (sub_start + len_sub):
                i, version_sum = parse_packet(s, i, version_sum)

    return i, version_sum


with open("input.txt") as file:
    transmission = file.read().strip()

_, version_sum = parse_packet(hex_to_bin(transmission))
print(version_sum)
