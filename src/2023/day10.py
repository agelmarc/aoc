import itertools

index_jmp = {
    "|": [(-1, 0), (1, 0)],
    "-": [(0, -1), (0, 1)],
    "L": [(-1, 0), (0, 1)],
    "J": [(-1, 0), (0, -1)],
    "7": [(1, 0), (0, -1)],
    "F": [(1, 0), (0, 1)],
}


def get_next_indices(i, j, arr):
    if arr[i][j] in index_jmp.keys():
        (di1, dj1), (di2, dj2) = index_jmp[arr[i][j]]
        return [(i + di1, j + dj1), (i + di2, j + dj2)]

    return []


def get_loop(arr):
    idxs = []
    for i, l in enumerate(arr):
        if "S" in l:
            j = l.index("S")
            idxs.append((i, j))
    si, sj = idxs[0]

    for i in [-1, 1]:
        if (si, sj) in get_next_indices(si + i, sj, arr):
            idxs.append((si + i, sj))
            break
    else:
        for j in [-1, 1]:
            if (si, sj) in get_next_indices(si, sj + j, arr):
                idxs.append((si, sj + j))
                break

    while idxs[-1] != idxs[0]:
        ni, nj = idxs[-1]
        oi, oj = idxs[-2]
        possibilities = get_next_indices(ni, nj, arr)
        if (oi, oj) == possibilities[0]:
            next = possibilities[1]
        else:
            next = possibilities[0]
        idxs.append(next)
    return idxs


def p1(f):
    arr = f.read().splitlines()
    arr = [list(l) for l in arr]

    idxs = get_loop(arr)

    return (len(idxs) - 1) // 2


def p2(f):
    arr = f.read().splitlines()
    arr = [list(l) for l in arr]

    loop = get_loop(arr)
    tilecount = len(loop)
    loop = [(loop[i], loop[i + 1]) for i in range(len(loop) - 1)]
    all_gridpoints = set()
    gridpoints = {(0, 0)}
    ak = 0
    print(len(arr) * len(arr[0]))
    while True:
        new_gridpoints = set()
        for i, j in gridpoints:
            for di, dj in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                if (i + di, j + dj) in gridpoints:
                    continue
                if not (0 <= i + di <= len(arr)) or not (0 <= j + dj <= len(arr[0])):
                    continue

                a, b = tuple(
                    set(
                        [
                            (i - 1, j - 1),
                            (i - 1, j),
                            (i, j - 1),
                            (i, j),
                        ]
                    )
                    & set(
                        [
                            (i + di - 1, j + dj - 1),
                            (i + di - 1, j + dj),
                            (i + di, j + dj - 1),
                            (i + di, j + dj),
                        ]
                    )
                )

                if (a, b) in loop or (b, a) in loop:
                    continue

                # print(idx)
                new_gridpoints.add((i + di, j + dj))

        new_gridpoints = new_gridpoints - gridpoints - all_gridpoints
        ak += len(new_gridpoints)
        print(ak)
        all_gridpoints &= gridpoints
        gridpoints = new_gridpoints
        if len(new_gridpoints) == 0:
            break

    s = 0
    for i in range(len(arr)):
        for j in range(len(arr[0])):
            if (
                (i, j) in gridpoints
                and (i + 1, j) in gridpoints
                and (i, j + 1) in gridpoints
                and (i + 1, j + 1) in gridpoints
            ):
                s += 1

    return len(arr) * len(arr[0]) - tilecount - s + 1
