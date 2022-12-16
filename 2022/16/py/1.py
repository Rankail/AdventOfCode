from __future__ import annotations
import re
import sys
from collections import deque, defaultdict

data = open("i.txt").read().split("\n")

rate = {}
nodes = {}


class Node:
    childs: list[Node]
    flow_rate: int = None
    opened: int = None

    def __init__(self, childs, flow_rate):
        self.childs = []
        self.flow_rate = flow_rate
        self.opened = False

for l in data:
    m = re.match(r"Valve (.*) has flow rate=(.*); tunnels? leads? to valves? (.*)", l)
    name, flowrate, others = m.group(1), int(m.group(2)), m.group(3).split(", ")
    print(name, flowrate, others)
    nodes[name] = others
    rate[name] = flowrate


def check(pos: str, opened: list[str], released: int, time: int):
    for e in opened:
        released += rate[e]
    if time == 30: return released
    ma = released
    if not pos in opened and rate[pos] > 0:
        ma = max(ma, check(pos, opened +[pos], released, time+1))
    
    for c in nodes[pos]:
        ma = max(ma, check(c, opened, released, time+1))
    return ma


highest = defaultdict(lambda:0)

def bfs():
    ma = 0
    q = deque()
    q.append(("AA", [], 0, 0, 1))
    while q:
        print(len(q))
        name, opened, speed, released, time = q.popleft()
        if (highest[name] > released+speed*(30-time+1)): continue
        highest[name] = max(highest[name], released+speed*(30-time))
        if time == 30:
            ma = max(ma, released+speed)
            continue
        if not name in opened and rate[name] > 0:
            q.append((name, opened + [name], speed+rate[name], released+speed, time+1))
        for c in nodes[name]:
            q.append((c, opened, speed, released+speed, time+1))
    print(ma)

bfs()

# print(check("AA", [], 0, 1))

# 2119
