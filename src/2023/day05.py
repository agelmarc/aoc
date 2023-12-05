def p1(f):
    d = iter(f.read().splitlines())
    seeds = [int(s) for s in next(d).split(": ")[1].split()]
    maps = []
    next(d)
    for l in d:
        if "map" in l:
            continue
        if len(l) == 0:
            new_seeds = []
            for seed in seeds:
                new_seed = None
                found = False
                for mm in maps:
                    if mm[1] < seed <= mm[1] + mm[2] and not found:
                        found = True
                        new_seed = mm[0] + seed - mm[1]
                new_seeds.append(new_seed if found else seed)

            seeds = new_seeds
            maps = []
            continue
        maps.append([int(s) for s in l.split(" ")])
    return min(seeds)


def p2(f):
    d = iter(f.read().splitlines())
    seeds = [int(s) for s in next(d).split(": ")[1].split()]
    ranges = [[seeds[i], seeds[i] + seeds[i + 1]] for i in range(0, len(seeds), 2)]

    map_stages = []

    next(d)
    next(d)

    stage = []
    for l in d:
        if len(l) == 0:
            map_stages.append(stage)
            stage = []
            continue
        if "map" in l:
            continue
        m = [int(s) for s in l.split(" ")]
        m = [m[1], m[1] + m[2], m[0] - m[1]]
        stage.append(m)

    for stage in map_stages:
        stage = sorted(stage, key=lambda s: s[0])
        new_ranges = []

        for start, end in ranges:
            pushforward = start

            for left, right, delta in stage:
                if right < start or left >= end:
                    continue
                if left > pushforward:
                    new_ranges.append([pushforward, left])

                new_ranges.append(
                    [max(pushforward, left) + delta, min(end, right) + delta]
                )
                pushforward = min(end, right)
            if pushforward < end:
                new_ranges.append([pushforward, end])

        ranges = new_ranges

    return min(r[0] for r in ranges)


# mm: dst_s,
