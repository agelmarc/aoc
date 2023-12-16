def p1(f):
    s = 0
    for l in f.read().splitlines():
        b = [[int(a) for a in l.split()]]
        seq = [int(a) for a in l.split()]
        while sum(seq) != 0:
            seq = [seq[i + 1] - seq[i] for i in range(len(seq) - 1)]
            b.append(seq)

        s += sum(a[-1] for a in b)
    return s


def p2(f):
    s = 0
    for l in f.read().splitlines():
        b = [[int(a) for a in l.split()]]
        seq = [int(a) for a in l.split()]
        while sum(seq) != 0:
            seq = [seq[i + 1] - seq[i] for i in range(len(seq) - 1)]
            b.append(seq)

        a = 0
        for ls in reversed(b):
            first = ls[0]
            a = first - a

        s += a
    return s
