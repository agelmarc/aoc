from collections import defaultdict


def matches(line):
    line = line.split(":")[1]
    win, have = line.split("|")
    win = win.split()
    have = have.split()
    win = set(win)
    have = set(have)

    matches = sum([1 for h in have if h in win])
    return matches


def p1(f):
    s = 0
    for line in f.read().splitlines():
        m = matches(line)
        s += 2 ** (m - 1) if m > 0 else 0
    return s
    ...


def p2(f):
    d = f.read().splitlines()
    ls = defaultdict(lambda: 1)
    ls[1] = 1
    for i, l in enumerate(d, start=1):
        m = matches(l)
        for j in range(i + 1, i + m + 1):
            ls[j] += ls[i]

    return sum(ls[i] for i in range(1, len(d) + 1))
