from heapq import heappop, heappush
from typing import Callable


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
