from collections import defaultdict


def work(f):
    d = f.read()
    mm = {}
    for i, row in enumerate(d.splitlines()):
        for j, char in enumerate(row):
            if char not in [".", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]:
                mm[(i - 1, j - 1)] = (i, j)
                mm[(i - 1, j)] = (i, j)
                mm[(i - 1, j + 1)] = (i, j)

                mm[(i, j - 1)] = (i, j)
                mm[(i, j + 1)] = (i, j)

                mm[(i + 1, j - 1)] = (i, j)
                mm[(i + 1, j)] = (i, j)
                mm[(i + 1, j + 1)] = (i, j)
    rr = []
    gm = defaultdict(list)
    for i, row in enumerate(d.splitlines()):
        row = row + "."
        num = []
        isp = False
        for j, char in enumerate(row):
            if char not in ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]:
                if isp:
                    rr.append("".join(num))
                    gm[isp].append("".join(num))

                isp = False
                num = []
                continue
            num.append(char)

            if (i, j) in mm:
                isp = mm[(i, j)]
    return sum(int(j) for j in rr), sum(
        int(a[0]) * int(a[1]) for a in gm.values() if len(a) == 2
    )


def p1(f):
    return work(f)[0]


def p2(f):
    return work(f)[1]
