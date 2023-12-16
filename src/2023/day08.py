import functools
import math
from itertools import cycle

# def p1(f):
#     d = f.read().splitlines()

#     inst = cycle([1 if a == "R" else 0 for a in d[0]])

#     m = {}
#     for l in d[2:]:
#         k, v = l.split(" = (")
#         v = v[:-1].split(", ")
#         m[k] = v

#     steps = 0
#     r = "AAA"

#     for i in inst:
#         steps += 1
#         r = m[r][i]
#         if r == "ZZZ":
#             return steps


def p2(f):
    d = f.read().splitlines()

    inst = cycle([1 if a == "R" else 0 for a in d[0]])

    m = {}
    for l in d[2:]:
        k, v = l.split(" = (")
        v = v[:-1].split(", ")
        m[k] = v

    steps = 0
    ll = []
    r = [a for a in m.keys() if a.endswith("A")]
    for i in inst:
        if len(r) == 0:
            return functools.reduce(math.lcm, ll)

        steps += 1
        new_r = []
        for r in r:
            nr = m[r][i]
            if not nr.endswith("Z"):
                new_r.append(nr)
            else:
                ll.append(steps)
        r = new_r
