from dataclasses import dataclass
from io import TextIOWrapper
from math import prod
from typing import Literal

from utils.graph import all_paths


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


def p2(f: TextIOWrapper):
    @dataclass
    class Rule:
        target: str
        condition: str

    input = f.read()
    rules_str, parts = (a.splitlines() for a in input.split("\n\n"))
    rulesets: dict[str, list[Rule]] = {}

    rulesets["A"] = []
    rulesets["R"] = []

    for rule in rules_str:
        name, ruleset = rule.split("{")
        ruleset = ruleset[:-1].split(",")
        rs: list[Rule] = []
        for r in ruleset:
            if ":" in r:
                rs.append(Rule(target=r.split(":")[1], condition=r.split(":")[0]))
            else:
                rs.append(Rule(target=r, condition=""))
        rulesets[name] = rs

    def next_nodes(node: str) -> list[tuple[str, int]]:
        n: list[tuple[str, int]] = []
        for i, r in enumerate(rulesets[node]):
            n.append((r.target, i))
            if not r.condition:
                break
        return n

    paths = all_paths(("in", 0), "A", next_nodes)
    s = 0
    for path in paths:
        values = {
            "x": list(range(1, 4001)),
            "m": list(range(1, 4001)),
            "a": list(range(1, 4001)),
            "s": list(range(1, 4001)),
        }

        for i in range(len(path) - 1):
            curr_node, _ = path[i]
            _, info = path[i + 1]
            for rule in rulesets[curr_node][:info]:
                if "<" in rule.condition:
                    char, threshold = rule.condition.split("<")
                    values[char] = [v for v in values[char] if v >= int(threshold)]
                if ">" in rule.condition:
                    char, threshold = rule.condition.split(">")
                    values[char] = [v for v in values[char] if v <= int(threshold)]

            rule = rulesets[curr_node][info]

            if "<" in rule.condition:
                char, threshold = rule.condition.split("<")
                values[char] = [v for v in values[char] if v < int(threshold)]
            if ">" in rule.condition:
                char, threshold = rule.condition.split(">")
                values[char] = [v for v in values[char] if v > int(threshold)]

        s += prod(len(v) for v in values.values())

    return s
