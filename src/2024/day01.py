PART = "both"
# PART = 1
# PART = 2

# SAMPLE = None
SAMPLE = """3   4
4   3
2   5
1   3
3   9
3   3
"""


def p1(input: str):
    a = []
    b = []

    for line in input.splitlines():
        n1, n2 = line.split()
        a.append(int(n1))
        b.append(int(n2))

    ans = sum(abs(n1 - n2) for n1, n2 in zip(sorted(a), sorted(b)))

    return ans


def p2(input):
    a = []
    cnt = {}

    for line in input.splitlines():
        n1, n2 = line.split()
        a.append(int(n1))
        if int(n2) in cnt:
            cnt[int(n2)] += 1
        else:
            cnt[int(n2)] = 1
    ans = sum(n1 * cnt.get(n1, 0) for n1 in a)
    return ans
