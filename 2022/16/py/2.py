from __future__ import annotations
import re
import sys
from collections import deque, defaultdict
from heapq import heappush, heappop

data = open("i2.txt").read().split("\n")

nodes: dict[str, Node] = {}
conns: dict[str, list[str]] = {}

ma = 0

# class Connection:
#     node: Node = None
#     dist: int = None

#     def __init__(self, node: Node, dist: int=1):
#         self.node = node
#         self.dist = dist

#     def __repr__(self):
#         return f"<Conn {self.node.__repr__()} {self.dist}>"

#     def __eq__(self, o: Connection):


class Node:
    conns: dict[Node, int] = None
    flow_rate: int = None
    opened: int = None
    highest: dict[int, (int,int)] = None
    name: str = None

    def __init__(self, name, rate):
        self.name = name
        self.rate = rate
        self.conns = dict()
        self.highest = defaultdict(lambda: (0,0))

    def check(self: Node, time: int, released: int, speed: int, opened: list[name]):
        global ma
        if time == 30:
            if released+speed > ma:
                ma = released+speed
                print(ma)
            return
        # if self.highest[time][0] < released and self.highest[time][1] < speed: return
        # if self.highest[time][0] >= released and self.highest[time][1] >= speed:
        #     self.highest[time] = (released, speed)
        if (name not in opened) and self.rate > 0:
            self.check(time+1, released+speed, speed+self.rate, opened + [self.name])
        for c in self.conns:
            c.check(time+1, released+speed, speed, opened)

    def __repr__(self, depth=0):
        return f"<Node '{self.name}' {self.rate} {[f'({n.__repr__(1)}: {nd})' for n, nd in self.conns.items()] if depth==0 else ''}>"


for l in data:
    m = re.match(r"Valve (.*) has flow rate=(.*); tunnels? leads? to valves? (.*)", l)
    name, flowrate, others = m.group(1), int(m.group(2)), m.group(3).split(", ")
    conns[name] = others
    nodes[name] = Node(name, flowrate)
        
for name, connected in conns.items():
    if nodes[name].rate == 0:
        for c in connected:
            for d in connected:
                if c == d: continue
                nodes[c].conns[nodes[d]] = 2
                nodes[d].conns[nodes[c]] = 2
    else:
        for c in connected:
            nodes[name].conns[nodes[c]] = 1

foundZero = True
while foundZero:
    foundZero = False
    for n in nodes.values():
        print(n.rate, len(n.conns))
        if n.rate == 0 and len(n.conns) != 0:
            # print(n)
            foundZero = True
            for c, cd in n.conns.items():
                for d, dd in n.conns.items():
                    if c == d: continue
                    nodes[c.name].conns[d] = cd+dd
                    nodes[d.name].conns[c] = cd+dd
            n.conns = dict()

starts = []


nodes = {n.name: n for n in nodes.values() if n.rate != 0}
for n in nodes.values():
    n.conns = {n: d for n, d in n.conns.items() if n.rate != 0}

print(nodes)

# nodes["AA"].check(0, 0, 0, [])

# print(check("AA", [], 0, 1))

# 6228 high
# 5077 high
#2663 high
