from dataclasses import dataclass

from utils.graph import dijkstra


class Dir:
    DOWN = (1, 0)
    UP = (-1, 0)
    LEFT = (0, -1)
    RIGHT = (0, 1)


@dataclass(frozen=True)
class Node:
    pos: tuple[int, int]
    dir: tuple[int, int]
    acc: int

    def __lt__(self, other):
        return True


def p1(f):
    arr = [list(l) for l in f.read().splitlines()]

    max_i = len(arr) - 1
    max_j = len(arr[0]) - 1

    def next_nodes(node: Node) -> list[Node]:
        nodes: list[Node] = []
        new_dirs = []
        match node.dir:
            case Dir.DOWN | Dir.UP:
                new_dirs = [Dir.LEFT, Dir.RIGHT]
            case Dir.LEFT | Dir.RIGHT:
                new_dirs = [Dir.UP, Dir.DOWN]

        for new_dir in new_dirs:
            new_i, new_j = (sum(x) for x in zip(node.pos, new_dir))
            if 0 <= new_i <= max_i and 0 <= new_j <= max_j:
                nodes.append(Node((new_i, new_j), new_dir, 0))

        new_i, new_j = (sum(x) for x in zip(node.pos, node.dir))
        if 0 <= new_i <= max_i and 0 <= new_j <= max_j and node.acc < 2:
            nodes.append(Node((new_i, new_j), node.dir, node.acc + 1))

        return nodes

    def edge_weight(out: Node, inc: Node) -> float:
        return float(arr[inc.pos[0]][inc.pos[1]])

    done = dijkstra(Node((0, 0), Dir.DOWN, -1), next_nodes, edge_weight)

    return min(v for k, v in done.items() if k.pos == (max_i, max_j))


def p2(f):
    arr = [list(l) for l in f.read().splitlines()]

    max_i = len(arr) - 1
    max_j = len(arr[0]) - 1

    def next_nodes(node: Node) -> list[Node]:
        nodes: list[Node] = []
        new_dirs = []
        match node.dir:
            case Dir.DOWN | Dir.UP:
                new_dirs = [Dir.LEFT, Dir.RIGHT]
            case Dir.LEFT | Dir.RIGHT:
                new_dirs = [Dir.UP, Dir.DOWN]

        for new_dir in new_dirs:
            new_i, new_j = (sum(x) for x in zip(node.pos, new_dir))
            if 0 <= new_i <= max_i and 0 <= new_j <= max_j and node.acc >= 4:
                nodes.append(Node((new_i, new_j), new_dir, 1))

        new_i, new_j = (sum(x) for x in zip(node.pos, node.dir))
        if 0 <= new_i <= max_i and 0 <= new_j <= max_j and node.acc < 10:
            nodes.append(Node((new_i, new_j), node.dir, node.acc + 1))
        return nodes

    def edge_weight(out: Node, inc: Node) -> float:
        return float(arr[inc.pos[0]][inc.pos[1]])

    done = dijkstra(Node((0, 0), Dir.DOWN, 5), next_nodes, edge_weight)
    return min(v for k, v in done.items() if k.pos == (max_i, max_j) and k.acc >= 4)
