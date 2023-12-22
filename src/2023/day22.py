from collections import defaultdict, deque
from io import TextIOWrapper


def p1(f: TextIOWrapper):
    bricks = []
    for i, l in enumerate(f.read().splitlines()):
        first, second = l.split("~")
        x1, y1, z1 = first.split(",")
        x2, y2, z2 = second.split(",")
        bricks.append(
            [
                [
                    min(int(x1), int(x2)),
                    min(int(y1), int(y2)),
                    min(int(z1), int(z2)),
                ],
                [
                    max(int(x1), int(x2)),
                    max(int(y1), int(y2)),
                    max(int(z1), int(z2)),
                ],
            ]
        )

    grid: dict[tuple[int, int], tuple[int, int]] = {}
    bricks_down = defaultdict(set)
    bricks_up = defaultdict(set)

    for id, brick in enumerate(sorted(bricks, key=lambda b: b[0][2])):
        points = []
        for x in range(brick[0][0], brick[1][0] + 1):
            for y in range(brick[0][1], brick[1][1] + 1):
                points.append((x, y))

        max_height = max(grid.get((i, j), (0, None))[0] for i, j in points)

        brick_height = brick[1][2] - brick[0][2] + 1
        for x, y in points:
            down_height, down = grid.get((x, y), (0, None))
            if down is not None and down_height == max_height:
                bricks_up[down].add(id)
                bricks_down[id].add(down)
            grid[(x, y)] = (max_height + brick_height, id)
    count = 0
    for brick in range(len(bricks)):
        if all(len(bricks_down[b]) > 1 for b in bricks_up[brick]):
            count += 1
    return count


def p2(f: TextIOWrapper):
    bricks = []
    for i, l in enumerate(f.read().splitlines()):
        first, second = l.split("~")
        x1, y1, z1 = first.split(",")
        x2, y2, z2 = second.split(",")
        bricks.append(
            [
                [
                    min(int(x1), int(x2)),
                    min(int(y1), int(y2)),
                    min(int(z1), int(z2)),
                ],
                [
                    max(int(x1), int(x2)),
                    max(int(y1), int(y2)),
                    max(int(z1), int(z2)),
                ],
            ]
        )

    grid: dict[tuple[int, int], tuple[int, int]] = {}
    bricks_down = defaultdict(set)
    bricks_up = defaultdict(set)

    for id, brick in enumerate(sorted(bricks, key=lambda b: b[0][2])):
        points = []
        for x in range(brick[0][0], brick[1][0] + 1):
            for y in range(brick[0][1], brick[1][1] + 1):
                points.append((x, y))

        max_height = max(grid.get((i, j), (0, None))[0] for i, j in points)

        brick_height = brick[1][2] - brick[0][2] + 1
        for x, y in points:
            down_height, down = grid.get((x, y), (0, None))
            if down is not None and down_height == max_height:
                bricks_up[down].add(id)
                bricks_down[id].add(down)
            grid[(x, y)] = (max_height + brick_height, id)
    count = 0
    for brick in range(len(bricks)):
        visited = deque([brick])
        removed = {brick}
        while visited:
            brick = visited.popleft()
            for b in bricks_up[brick]:
                if len(bricks_down[b] - removed) == 0:
                    removed.add(b)
                    visited.append(b)

        count += len(removed) - 1

    return count
