import math


def p1(f):
    arr = [list(l) for l in f.read().splitlines()]

    rows = []
    cols = []
    for i, l in enumerate(arr):
        if l.count("#") == 0:
            rows.append(i)

    for j in range(len(arr[0])):
        ls = [l[j] for l in arr]
        if ls.count("#") == 0:
            cols.append(j)

    galaxies = []

    for i, l in enumerate(arr):
        for j, char in enumerate(l):
            if char == "#":
                rows_before = sum(1 for r in rows if r < i)
                cols_before = sum(1 for c in cols if c < j)
                galaxies.append((i + rows_before, j + cols_before))
    s = 0
    for g1 in galaxies:
        for g2 in galaxies:
            if g1 == g2:
                continue

            g10, g11 = g1
            g20, g21 = g2
            s += abs(g20 - g10) + abs(g21 - g11)
    return s // 2


def p2(f):
    arr = [list(l) for l in f.read().splitlines()]

    rows = []
    cols = []
    for i, l in enumerate(arr):
        if l.count("#") == 0:
            rows.append(i)

    for j in range(len(arr[0])):
        ls = [l[j] for l in arr]
        if ls.count("#") == 0:
            cols.append(j)

    galaxies = []

    for i, l in enumerate(arr):
        for j, char in enumerate(l):
            if char == "#":
                rows_before = sum(1 for r in rows if r < i)
                cols_before = sum(1 for c in cols if c < j)
                galaxies.append((i + rows_before * 999999, j + cols_before * 999999))
    s = 0
    for g1 in galaxies:
        for g2 in galaxies:
            if g1 == g2:
                continue

            g10, g11 = g1
            g20, g21 = g2
            s += abs(g20 - g10) + abs(g21 - g11)
    return s // 2
