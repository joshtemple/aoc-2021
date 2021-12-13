from collections import defaultdict
from pprint import pprint

graph = defaultdict(list)

with open("input.txt") as file:
    for line in file.readlines():
        start, end = line.strip().split("-")
        graph[start].append(end)
        graph[end].append(start)

pprint(graph)


def dfs(visited, graph, node, path=None, paths=None):
    if path is None:
        path = []
    if paths is None:
        paths = []

    path.append(node)
    if node.islower():
        visited.add(node)

    if node == "end":
        paths.append(path)
        print(path)
    else:
        for child in graph[node]:
            if child in visited:
                continue
            else:
                paths = dfs(visited, graph, child, path, paths)

    path.pop()
    if node.islower():
        visited.remove(node)

    return paths


visited = set()
paths = dfs(visited, graph, "start")
print(len(paths))
