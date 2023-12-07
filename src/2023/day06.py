from math import prod


def p1(f):
    ll = [l.split() for l in f.read().splitlines()]
    a = iter(zip(*ll))
    next(a)
    rs = []
    for t, r in a:
        t = int(t)
        r = int(r)
        res = 0
        for i in range(t):
            d = (t - i) * i
            if d > r:
                res += 1
        rs.append(res)
    return prod(rs)


def p2(f):
    ll = f.read().splitlines()
    ll = [l.replace(" ", "").split(":")[1] for l in ll]

    t = int(ll[0])
    r = int(ll[1])
    res = 0
    for i in range(t):
        d = (t - i) * i
        if d > r:
            res += 1

    return res
