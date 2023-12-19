from math import prod


def p1(f):
    rules, parts = (a.splitlines() for a in f.read().split("\n\n"))
    rules_p = {}

    for rule in rules:
        name, ruleset = rule.split("{")
        ruleset = ruleset[:-1].split(",")

        rules_p[name] = ruleset

    def next_rule(name, p):
        if name == "R":
            return False
        if name == "A":
            return True

        ruleset = rules_p[name]

        for rule in ruleset:
            if ">" in rule:
                condition, next_rule = rule.split(":")
                lhs, rhs = condition.split(">")
                if p[lhs] > int(rhs):
                    return next_rule
            elif "<" in rule:
                condition, next_rule = rule.split(":")
                lhs, rhs = condition.split("<")
                if p[lhs] < int(rhs):
                    return next_rule
            else:
                return rule
        raise Exception("fuck")

    c = 0
    for part in parts:
        part = part[1:-1].split(",")
        part = {p.split("=")[0]: int(p.split("=")[1]) for p in part}

        rule = "in"
        while True:
            rule = next_rule(rule, part)
            # print(rule)
            if isinstance(rule, bool):
                if rule:
                    c += sum(part.values())
                break

    return c
