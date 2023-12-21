from dataclasses import dataclass
from io import TextIOWrapper
from math import prod

from numpy import MAY_SHARE_BOUNDS


@dataclass
class Pulse:
    sender: str
    high: bool
    recipient: str


@dataclass
class FlipFlop:
    name: str
    recv: list[str]
    state: bool

    def recv_pulse(self, pulse: Pulse) -> list[Pulse]:
        if pulse.high:
            return []

        self.state = not self.state
        return [
            Pulse(sender=self.name, high=self.state, recipient=recv)
            for recv in self.recv
        ]


@dataclass
class Conjunction:
    name: str
    recv: list[str]
    state: dict[str, bool]

    def recv_pulse(self, pulse: Pulse) -> list[Pulse]:
        self.state[pulse.sender] = pulse.high

        return [
            Pulse(sender=self.name, high=not all(self.state.values()), recipient=recv)
            for recv in self.recv
        ]


@dataclass
class Broadcast:
    name = "broadcaster"
    recv: list[str]

    def recv_pulse(self, pulse: Pulse) -> list[Pulse]:
        return [
            Pulse(sender="broadcaster", high=pulse.high, recipient=recv)
            for recv in self.recv
        ]


def p1(f: TextIOWrapper):
    modules: dict[str, Broadcast | Conjunction | FlipFlop] = {"rx": Broadcast(recv=[])}
    for l in f.read().splitlines():
        if l.startswith("%"):
            name, recv = l[1:].split(" -> ")
            recv = recv.split(", ")
            modules[name] = FlipFlop(name=name, state=False, recv=recv)
        elif l.startswith("&"):
            name, recv = l[1:].split(" -> ")
            recv = recv.split(", ")
            modules[name] = Conjunction(name=name, recv=recv, state={})
        else:
            recv = l.split(" -> ")[1].split(", ")
            modules["broadcaster"] = Broadcast(recv=recv)

    # poulate state dict for conjunctions

    for name, module in modules.items():
        for recv in module.recv:
            recv_module = modules[recv]
            if isinstance(recv_module, Conjunction):
                recv_module.state[name] = False

    count_low = 0
    count_high = 0
    for _ in range(1000):
        pulses = [Pulse(sender="button", high=False, recipient="broadcaster")]
        while pulses:
            # print(pulses)
            new_pulses = []
            for pulse in pulses:
                if pulse.high:
                    count_high += 1
                else:
                    count_low += 1
                new_pulses.extend(modules[pulse.recipient].recv_pulse(pulse))

            pulses = new_pulses
    return count_low * count_high


def p2(f: TextIOWrapper):
    modules: dict[str, Broadcast | Conjunction | FlipFlop] = {"rx": Broadcast(recv=[])}
    for l in f.read().splitlines():
        if l.startswith("%"):
            name, recv = l[1:].split(" -> ")
            recv = recv.split(", ")
            modules[name] = FlipFlop(name=name, state=False, recv=recv)
        elif l.startswith("&"):
            name, recv = l[1:].split(" -> ")
            recv = recv.split(", ")
            modules[name] = Conjunction(name=name, recv=recv, state={})
        else:
            recv = l.split(" -> ")[1].split(", ")
            modules["broadcaster"] = Broadcast(recv=recv)

    output_module = [mod for mod in modules.values() if "rx" in mod.recv][0]
    if not isinstance(output_module, Conjunction):
        raise Exception("fuck")

    for name, module in modules.items():
        for recv in module.recv:
            recv_module = modules[recv]
            if isinstance(recv_module, Conjunction):
                recv_module.state[name] = False
    button_presses = 0
    values = {}
    while True:
        button_presses += 1
        pulses = [Pulse(sender="button", high=False, recipient="broadcaster")]
        while pulses:
            new_pulses = []
            for pulse in pulses:
                if pulse.recipient == output_module.name and pulse.high:
                    values[pulse.sender] = button_presses
                new_pulses.extend(modules[pulse.recipient].recv_pulse(pulse))
            pulses = new_pulses

        if len(values) == 4:
            break

    return prod(values.values())
