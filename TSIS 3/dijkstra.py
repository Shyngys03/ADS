from math import inf
from typing import Any, Generator

def get_link_v(v: int, adjacency_matrix: list[list[int]]) -> Generator[Any, Any, Any]:
    for i, weight in enumerate(adjacency_matrix[v]):
        if weight > 0:
            yield i

def get_min(T: list[int], visited: set[int]) -> int:
    mini = -1
    m = inf

    for i, t in enumerate(T):
        if t < m and i not in visited:
            m = t
            mini = i

    return mini

def dijkstra(adjacency_matrix: list[list[int]], start: int) -> list[int]:
    n = len(adjacency_matrix)
    T = [inf] * n
    v = start
    visited = {v}
    T[v] = 0

    while v != -1:
        for i in get_link_v(v, adjacency_matrix):
            if i not in visited:
                w = T[v] + adjacency_matrix[v][i]
                if w < T[i]:
                    T[i] = w

        v = get_min(T, visited)
        if v != -1:
            visited.add(v)

    return T

adjacency_matrix = [
    [0, 3, 1, 3, 0, 0],
    [3, 0, 4, 0, 0, 0],
    [1, 4, 0, 0, 7, 5],
    [3, 0, 0, 0, 0, 2],
    [0, 0, 7, 0, 0, 4],
    [0, 0, 5, 2, 4, 0]
]

start_node = 1
shortest_distances = dijkstra(adjacency_matrix, start_node)
print(shortest_distances)