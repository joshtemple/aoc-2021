from typing import Optional
from dataclasses import dataclass
from functools import reduce


@dataclass
class Packet:
    version: int
    type_id: int


@dataclass
class Operator(Packet):
    length_type_id: Optional[int]
    children: list[Packet]

    @property
    def values(self) -> tuple[int]:
        return tuple(child.evaluate() for child in self.children)

    def evaluate(self) -> int:
        if self.type_id == 0:
            return reduce(lambda x, y: x + y, self.values)
        elif self.type_id == 1:
            return reduce(lambda x, y: x * y, self.values)
        elif self.type_id == 2:
            return min(self.values)
        elif self.type_id == 3:
            return max(self.values)
        elif self.type_id == 5:
            return int(self.values[0] > self.values[1])
        elif self.type_id == 6:
            return int(self.values[0] < self.values[1])
        elif self.type_id == 7:
            return int(self.values[0] == self.values[1])
        else:
            raise ValueError(f"Invalid operator type ID: {self.type_id}")


@dataclass
class Literal(Packet):
    value: int

    def evaluate(self) -> int:
        return self.value


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


def parse_packet(s: str, i: int = 0) -> Packet:
    version = int(s[i : i + 3], 2)
    i += 3
    type_id = int(s[i : i + 3], 2)
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
        packet = Literal(version, type_id, value=literal)
        i += 5
    else:
        length_type_id = s[i]
        subs = []
        i += 1
        if length_type_id == "1":
            count_sub = int(s[i : i + 11], 2)
            i += 11
            for _ in range(count_sub):
                i, sub = parse_packet(s, i)
                subs.append(sub)
        elif length_type_id == "0":
            len_sub = int(s[i : i + 15], 2)
            i += 15
            sub_start = i
            while i < (sub_start + len_sub):
                i, sub = parse_packet(s, i)
                subs.append(sub)
        packet = Operator(version, type_id, length_type_id, children=subs)

    return i, packet


with open("input.txt") as file:
    transmission = file.read().strip()

_, packet = parse_packet(hex_to_bin(transmission))
print(packet.evaluate())
