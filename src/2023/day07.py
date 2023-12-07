from dataclasses import dataclass

ord = {k: i for i, k in enumerate("23456789TJQKA", start=1)}


@dataclass
class Card:
    s: str

    def rank2(self):
        d = dict.fromkeys("AKQJT98765432", 0)
        for char in self.s:
            if char in "AKQJT98765432":
                d[char] += 1
        count_jokers = self.s.count("J")
        b = sorted([a for a in d.values() if a > 0], reverse=True)
        b[0] += count_jokers

        if b == [1, 1, 1, 1, 1]:
            return 0
        elif b == [2, 1, 1, 1]:
            return 1
        elif b == [2, 2, 1]:
            return 2
        elif b == [3, 1, 1]:
            return 3
        elif b == [3, 2]:
            return 4
        elif b == [4, 1]:
            return 5
        elif b == [5]:
            return 6
        raise Exception("fuck")

    def rank(self):
        d = dict.fromkeys("AKQJT98765432", 0)
        for char in self.s:
            d[char] += 1
        b = sorted([a for a in d.values() if a > 0], reverse=True)

        if b == [1, 1, 1, 1, 1]:
            return 0
        elif b == [2, 1, 1, 1]:
            return 1
        elif b == [2, 2, 1]:
            return 2
        elif b == [3, 1, 1]:
            return 3
        elif b == [3, 2]:
            return 4
        elif b == [4, 1]:
            return 5
        elif b == [5]:
            return 6
        raise Exception("fuck")

    def __lt__(self, other):
        if self.rank() == other.rank():
            for i, j in zip(self.s, other.s):
                if ord[i] != ord[j]:
                    return ord[i] < ord[j]
            return False
        return self.rank() < other.rank()


def p1(f):
    d = f.read().splitlines()

    cards = []
    for l in d:
        card, bid = l.split(" ")
        card = Card(card)
        cards.append((card, int(bid)))
    cards = sorted(cards, key=lambda c: c[0])

    return sum(i * b for i, (_, b) in enumerate(cards, start=1))


ord2 = {k: i for i, k in enumerate("J23456789TQKA", start=1)}


@dataclass
class Card2:
    s: str

    def rank(self):
        d = dict.fromkeys("AKQT98765432", 0)
        for char in self.s:
            if char in "AKQT98765432":
                d[char] += 1
        count_jokers = self.s.count("J")
        b = sorted([a for a in d.values() if a > 0], reverse=True)
        if len(b) == 0:
            b = [5]
        else:
            b[0] += count_jokers

        if b == [1, 1, 1, 1, 1]:
            return 0
        elif b == [2, 1, 1, 1]:
            return 1
        elif b == [2, 2, 1]:
            return 2
        elif b == [3, 1, 1]:
            return 3
        elif b == [3, 2]:
            return 4
        elif b == [4, 1]:
            return 5
        elif b == [5]:
            return 6
        raise Exception("fuck")

    def __lt__(self, other):
        if self.rank() == other.rank():
            for i, j in zip(self.s, other.s):
                if ord2[i] != ord2[j]:
                    return ord2[i] < ord2[j]
            return False
        return self.rank() < other.rank()


def p2(f):
    d = f.read().splitlines()

    cards = []
    for l in d:
        card, bid = l.split(" ")
        card = Card2(card)
        cards.append((card, int(bid)))
    cards = sorted(cards, key=lambda c: c[0])

    return sum(i * b for i, (_, b) in enumerate(cards, start=1))
