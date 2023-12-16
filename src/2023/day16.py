def p1(f):
    field = f.read().splitlines()
    return get_energized((0, -1, 0, 1), field)


def p2(f):
    field = f.read().splitlines()
    arr = []
    for i in range(len(field)):
        arr.append(get_energized((i, -1, 0, 1), field))
        arr.append(get_energized((i, len(field) + 1, 0, -1), field))

    for j in range(len(field[0])):
        arr.append(get_energized((-1, j, 1, 0), field))
        arr.append(get_energized((len(field[0]) + 1, j, -1, 0), field))

    return max(arr)


def get_energized(start_pos: tuple[int, int, int, int], field):
    laser_ends: set[tuple[int, int, int, int]] = {start_pos}
    seen_laser_states = set()
    while len(laser_ends) > 0:
        new_laser_ends = progress_lasers(laser_ends, field)
        laser_ends = set()
        for laser_end in new_laser_ends:
            if laser_end not in seen_laser_states:
                seen_laser_states.add(laser_end)
                laser_ends.add(laser_end)

    energized = {(i, j) for i, j, _, _ in seen_laser_states}

    return len(energized)


def progress_lasers(laser_ends: set[tuple[int, int, int, int]], field):
    new_laser_ends: set[tuple[int, int, int, int]] = set()
    for i, j, di, dj in laser_ends:
        new_i, new_j = (i + di, j + dj)
        if not (0 <= new_i < len(field)):
            continue
        if not (0 <= new_j < len(field[0])):
            continue
        match field[new_i][new_j]:
            case ".":
                new_laser_ends.add((new_i, new_j, di, dj))
            case "|":
                if di == 0:
                    new_laser_ends.add((new_i, new_j, 1, 0))
                    new_laser_ends.add((new_i, new_j, -1, 0))
                else:
                    new_laser_ends.add((new_i, new_j, di, dj))
            case "-":
                if dj == 0:
                    new_laser_ends.add((new_i, new_j, 0, 1))
                    new_laser_ends.add((new_i, new_j, 0, -1))
                else:
                    new_laser_ends.add((new_i, new_j, di, dj))
            case "\\":
                new_laser_ends.add((new_i, new_j, dj, di))
            case "/":
                new_laser_ends.add((new_i, new_j, -dj, -di))
    return new_laser_ends
