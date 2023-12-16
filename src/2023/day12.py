from functools import cache


def p1(f):
    s = 0
    for l in f.read().splitlines():
        springs, numbers = l.split()
        numbers = [int(n) for n in numbers.split(",")]

        s += solve(springs, *numbers)

    return s


def p2(f):
    s = 0
    for l in f.read().splitlines():
        springs, numbers = l.split()
        numbers = [int(n) for n in numbers.split(",")]

        springs = X.join([springs] * 5)
        numbers = numbers * 5

        s += solve(springs, *numbers)

    return s


ZERO = "."
ONE = "#"
X = "?"


def solve(springs, *numbers: int) -> int:
    return _solve(springs + ".", *numbers)


@cache
def _solve(springs: str, *numbers: int) -> int:
    springs = springs.lstrip(ZERO)

    if len(numbers) == 0:
        return int(springs.count(ONE) == 0)

    if len(springs) == 0:
        return int(len(numbers) == 0)

    # springs starts with one or x now.
    if springs.startswith(ONE):
        first_block = numbers[0]
        numbers = numbers[1:]

        # springs has to have at least first_block chars left
        # the first first_block chars have to not be zero
        # if the springs have more chars:
        # the (first_block + 1)-th cannot be a one
        if (
            len(springs) < first_block
            or springs[0:first_block].count(ZERO) > 0
            or springs[first_block] == ONE
        ):
            return 0

        return solve(springs[first_block + 1 :], *numbers)

    # springs.startswith(X):
    return solve(ZERO + springs[1:], *numbers) + solve(ONE + springs[1:], *numbers)
