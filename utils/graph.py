from collections import deque
from heapq import heappop, heappush
from typing import Any, Callable


def dijkstra[
    N
](
    initial_node: N,
    next_nodes: Callable[[N], list[N]],
    edge_weight: Callable[[N, N], float],
):
    queue: list[tuple[float, N]] = [(0, initial_node)]
    visited: dict[N, float] = {}

    while queue:
        weight, curr_node = heappop(queue)

        if curr_node in visited:
            continue

        visited[curr_node] = weight

        for node in next_nodes(curr_node):
            added_weight = edge_weight(curr_node, node)
            heappush(queue, ((weight + added_weight), node))

    return visited


def all_paths[
    N, I
](
    initial_node: tuple[N, I], end_node: N, next_nodes: Callable[[N], list[tuple[N, I]]]
) -> list[list[tuple[N, I]]]:
    queue = deque[list[tuple[N, I]]]()
    queue.append([initial_node])
    paths: list[list[tuple[N, I]]] = []
    while queue:
        path = queue.popleft()
        node, _ = path[-1]
        if node == end_node:
            paths.append(path)

        for next_node, info in next_nodes(node):
            if next_node not in path:
                queue.append(path + [(next_node, info)])

    return paths
