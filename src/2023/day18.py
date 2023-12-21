dirs = {"R": (1, 0), "L": (-1, 0), "U": (0, 1), "D": (0, -1)}


def p1(f):
    area = 0
    prev_i, prev_j = 0, 0
    for l in f.read().splitlines():
        dir, num, _ = l.split()
        num = int(num)

        i = prev_i + dirs[dir][0] * num
        j = prev_j + dirs[dir][1] * num

        area += (prev_i + i) * (prev_j - j)
        area += num
        prev_i, prev_j = i, j

    return int(area / 2 + 1)


def p2(f):
    area = 0
    prev_i, prev_j = 0, 0
    for l in f.read().splitlines():
        _, _, hex = l.split()

        num = int(hex[2:7], 16)

        if hex[7] == "0":
            dir = "R"
        elif hex[7] == "1":
            dir = "D"
        elif hex[7] == "2":
            dir = "L"
        elif hex[7] == "3":
            dir = "U"
        else:
            raise Exception("fuck")

        i = prev_i + dirs[dir][0] * num
        j = prev_j + dirs[dir][1] * num

        area += (prev_i + i) * (prev_j - j)
        area += num
        prev_i, prev_j = i, j

    return int(area / 2 + 1)
