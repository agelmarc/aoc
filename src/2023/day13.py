def p1(f):
    cols = 0
    rows = 0

    for block in f.read().split("\n\n"):
        arr = block.splitlines()

        rows += get_mirror1([list(l) for l in arr])
        cols += get_mirror1(list(zip(*arr)))
    return 100 * rows + cols


def p2(f):
    cols = 0
    rows = 0

    for block in f.read().split("\n\n"):
        arr = block.splitlines()

        rows += get_mirror2([list(l) for l in arr])
        cols += get_mirror2(list(zip(*arr)))
    return 100 * rows + cols


def get_mirror1(arr):
    for i in range(1, len(arr)):
        left_side = arr[:i]
        right_side = arr[i:]
        if all(lhs == rhs for lhs, rhs in zip(reversed(left_side), right_side)):
            return i
    return 0


def get_mirror2(arr):
    for i in range(1, len(arr)):
        left_side = arr[:i]
        right_side = arr[i:]
        differences = 0
        for lhs, rhs in zip(reversed(left_side), right_side):
            differences += sum(1 for c1, c2 in zip(lhs, rhs) if c1 != c2)
        if differences == 1:
            return i
    return 0
