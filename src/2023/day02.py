def work(f):
    d = f.read()
    s = 0
    s1 = 0
    for row in d.splitlines():
        game_id, l = row[5:].split(":")
        game_id = int(game_id)
        l = l.split("; ")
        added = True

        blues = []
        reds = []
        greens = []

        for l in l:
            l = l.split(", ")

            for l in l:
                if "red" in l:
                    red = l[:-4]
                    reds.append(int(red))
                    if int(red) > 12:
                        added = False
                elif "blue" in l:
                    blue = l[:-5]
                    blues.append(int(blue))
                    if int(blue) > 14:
                        added = False
                elif "green" in l:
                    green = l[:-6]
                    greens.append(int(green))
                    if int(green) > 13:
                        added = False
        min_blue = max(blues)
        min_red = max(reds)
        min_green = max(greens)
        power = min_blue * min_red * min_green
        s1 += power
        if added:
            s += game_id

    return s, s1


def p1(f):
    return work(f)[0]


def p2(f):
    return work(f)[1]
