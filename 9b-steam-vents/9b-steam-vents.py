from dataclasses import dataclass
import networkx as nx
import itertools


@dataclass
class Slice:
    xmin: int
    y: int

    def __post_init__(self):
        self.xmax = self.xmin
        self.size = 1

    def expand(self):
        self.xmax += 1
        self.size += 1

    def touches(self, other) -> bool:
        return (
            abs(self.y - other.y) == 1
            and (self.xmin <= other.xmax)
            and (self.xmax >= other.xmin)
        )

    def __hash__(self):
        return hash((self.y, self.xmin, self.xmax))


slices = []
with open("input.txt") as file:
    for y, line in enumerate(file.readlines()):
        s = None
        for x, n in enumerate(line.strip()):
            n = int(n)
            if n < 9:
                if s:
                    s.expand()
                else:
                    s = Slice(x, y)
            elif s:
                slices.append(s)
                s = None
        if s:
            slices.append(s)

G = nx.Graph()
G.add_nodes_from(slices)
for a, b in itertools.combinations(slices, 2):
    if a.touches(b):
        G.add_edge(a, b)

basins = nx.connected_components(G)
sizes = sorted([sum(s.size for s in basin) for basin in basins], reverse=True)
print(sizes[0] * sizes[1] * sizes[2])
