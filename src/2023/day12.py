def p1(f):
    s = 0
    for l in f.read().splitlines():
        springs, numbers = l.split()
        numbers = [int(n) for n in numbers.split(",")]

        s += solve(springs, numbers)
    return s


ZERO = "."
ONE = "#"
X = "?"


def solve(
    springs: str,
    numbers: list[int],
) -> int:
    springs = springs.lstrip(ZERO)
    if len(numbers) == 0:
        return 1
    if len(springs) == 0:
        return 0
    # springs starts with one or x now.
    if springs.startswith(ONE):
        first_block, *numbers = numbers
        if springs[0:first_block].count(ZERO) == 0 and (
            len(springs) <= first_block or springs[first_block] in [ZERO, X]
        ):
            return solve(springs[first_block + 1 :], numbers)

        return 0

    # springs.startswith(X):
    return solve(ZERO + springs[1:], numbers) + solve(ONE + springs[1:], numbers)
