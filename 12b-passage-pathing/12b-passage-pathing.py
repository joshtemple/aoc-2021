from collections import defaultdict
from pprint import pprint

graph = defaultdict(list)

with open("input.txt") as file:
    for line in file.readlines():
        start, end = line.strip().split("-")
        graph[start].append(end)
        graph[end].append(start)

pprint(graph)


def dfs(visited, graph, node, repeat_available=True, path=None, paths=None):
    if path is None:
        path = []
    if paths is None:
        paths = []

    path.append(node)
    if node.islower():
        visited[node] += 1

    if node == "end":
        paths.append(path)
        print(path)
    else:
        for child in graph[node]:
            if child == "start":
                continue
            elif visited.get(child, 0) > 0:  # If already visited
                if repeat_available:  # Check if repeat is available
                    paths = dfs(
                        visited,
                        graph,
                        child,
                        repeat_available=False,
                        path=path,
                        paths=paths,
                    )
            else:
                paths = dfs(
                    visited, graph, child, repeat_available, path=path, paths=paths
                )

    path.pop()
    if node.islower():
        visited[node] -= 1

    return paths


visited = defaultdict(lambda: 0)
paths = dfs(visited, graph, "start")
print(len(paths))
