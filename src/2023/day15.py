from collections import OrderedDict


def p1(f):
    return sum(_hash(s) for s in f.read().split(","))


def _hash(str):
    val = 0
    for c in str:
        val += ord(c)
        val *= 17
        val %= 256
    return val


def p2(f):
    hm = [OrderedDict() for _ in range(256)]
    for step in f.read().strip().split(","):
        if "-" in step:
            label = step[:-1]
            box = hm[_hash(label)]
            if label in box:
                del box[label]

        if "=" in step:
            label, f = step.split("=")
            box = hm[_hash(label)]

            box[label] = int(f)

    s = 0
    for i, box in enumerate(hm):
        for j, f in enumerate(box.values()):
            s += (i + 1) * (j + 1) * f
    return s
