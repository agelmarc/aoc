from heapq import heappop, heappush
from io import TextIOWrapper


def p1(f: TextIOWrapper):
    arr = [list(l) for l in f.read().splitlines()]

    si, sj = 0, 0
    for i, sub in enumerate(arr):
        if "S" in sub:
            si, sj = i, sub.index("S")

    visited = get_visited(arr, (si, sj))
    steps = 64
    return sum(1 for k, v in visited.items() if v <= steps and v % 2 == steps % 2)


def p2(f: TextIOWrapper):
    arr = [list(l) for l in f.read().splitlines()]

    si, sj = 0, 0
    for i, sub in enumerate(arr):
        if "S" in sub:
            si, sj = i, sub.index("S")

    visited = get_visited(arr, (si, sj))
    n = 26501365 // 131

    even_full = sum(1 for v in visited.values() if v % 2 == 0)
    odd_full = sum(1 for v in visited.values() if v % 2 == 1)

    even_corner = sum(1 for v in visited.values() if v > 65 and v % 2 == 0)
    odd_corner = sum(1 for v in visited.values() if v > 65 and v % 2 == 1)

    return (
        even_full * n**2
        + odd_full * (n + 1) ** 2
        + even_corner * n
        - odd_corner * (n + 1)
    )


def get_visited(arr: list[list[str]], start: tuple[int, int]):
    queue: list[tuple[int, tuple[int, int]]] = [(0, start)]
    visited: dict[tuple[int, int], int] = {}
    while queue:
        dist, curr_node = heappop(queue)
        if curr_node in visited:
            continue
        visited[curr_node] = dist
        for di, dj in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            i, j = curr_node[0] + di, curr_node[1] + dj
            if (
                0 <= i <= len(arr) - 1
                and 0 <= j <= len(arr[0]) - 1
                and arr[i][j] == "."
            ):
                heappush(queue, (dist + 1, (i, j)))
    return visited
