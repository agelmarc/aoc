from functools import cache


def p2(f):
    arr = tuple(f.read().splitlines())
    for _ in range(3):
        arr = rotate(arr)

    seen = []

    while True:
        for _ in range(4):
            arr = roll(arr)
            arr = rotate(arr)

        if arr in seen:
            break
        seen.append(arr)

    first = seen.index(arr)

    arr = seen[(1_000_000_000 - 1 - first) % (len(seen) - first) + first]

    w = 0

    for l in arr:
        for i, c in enumerate(l):
            if c == "O":
                w += len(l) - i

    return w


def p1(f):
    arr = tuple(f.read().splitlines())
    for _ in range(3):
        arr = rotate(arr)

    arr = roll(arr)

    w = 0

    for l in arr:
        for i, c in enumerate(l):
            if c == "O":
                w += len(l) - i

    return w


def roll(arr: tuple[str, ...]):
    return tuple(sort(line) for line in arr)


@cache
def sort(s: str) -> str:
    return "#".join(
        [part.count("O") * "O" + part.count(".") * "." for part in s.split("#")]
    )


def rotate(arr: tuple[str, ...]):
    x = ["".join(list(c)) for c in zip(*arr)]
    return tuple(l[::-1] for l in x)
