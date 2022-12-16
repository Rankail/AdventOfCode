from __future__ import annotations
from heapq import heappop, heappush
import re
from collections import deque, defaultdict

data = open("i.txt").read().split("\n")

nodes: dict[str, Node] = {}
dists = {}

ma = 0

def printNodes(suffix: str = ""):
    print("###########")
    for n in nodes.values():
        print(n.name+suffix)
    for n in nodes.values():
        for c in n.conns.keys():
            if ord(n.name[0]) < ord(c.name[0]):
                print(n.name+suffix+" "+c.name+suffix)
    print("###########")



class Node:
    conns: dict[Node, int] = None
    rate: int = None
    opened: list[str] = None
    name: str = None

    def __init__(self, name, rate):
        self.name = name
        self.rate = rate
        self.conns = dict()

    def check(self: Node, time_left: int, released: int, opened: list[str], path: list[str]):
        global ma
        # print(unopened)
        for uo in nodes:
            if uo in opened: continue
            dist = dists[self.name][uo]
            if time_left-dist <= 0:
                r = released+nodes[uo].rate*time_left
                # if path[0] == "DD 0 1": print(path) # D 0, B 20, J 33, H 54, E 79, C 81
                if r > ma:
                    # print(uol, time_left, dist, released, r, path)
                    print(ma)
                    ma = max(ma, r)
                continue
            
            nodes[uo].check(time_left-dist-1, released + (time_left-dist-1)*nodes[uo].rate, uol, path + [uo + " " + str(time_left)])

    def __repr__(self, depth=0):
        return f"<Node '{self.name}' {self.rate} {[f'({n.__repr__(1)}: {nd})' for n, nd in self.conns.items()] if depth==0 else ''}>"

    def __lt__(self, o: Node):
        return self.name < o.name

    # def getConnStr(self):
    #     return f"{self.name}: {','.join(n.name for n in self.conns.keys())}"

def bfs(a: Node, b: Node):
    unvisited = set(nodes.values())
    unvisited.remove(a)
    q: list[tuple[int, Node]] = []
    heappush(q, (0, a))
    while b in unvisited:
        d, n = heappop(q)
        for c, cd in n.conns.items():
            if c not in unvisited: continue
            if c == b: return d+cd
            heappush(q, (d+cd, c))
    print("error")
    return None

# def generatePaths(pos, open, time_left):
#     for c in nodes:
#         if 

def getDistNodes(a: Node, b: Node):
    if b in a.conns.keys():
        return a.conns[b]
    return bfs(a, b)

conns: dict[str, list[str]] = {}
for l in data:
    m = re.match(r"Valve (.*) has flow rate=(.*); tunnels? leads? to valves? (.*)", l)
    name, flowrate, others = m.group(1), int(m.group(2)), m.group(3).split(", ")
    conns[name] = others
    nodes[name] = Node(name, flowrate)

for name, connected in conns.items():
    for c in connected:
        nodes[name].conns[nodes[c]] = 1

# for n in nodes.values():
#     print(n.getConnStr())
# print("-----")

# printNodes()
printNodes()

foundZero = True
while foundZero:
    foundZero = False
    for n in nodes.values():
        if n.rate == 0:
            # print(n.name, n.conns.keys())
            for c, cd in n.conns.items():
                for d, dd in n.conns.items():
                    if c == d: continue
                    # print(c)
                    # print(d)
                    # print(c.name, d.name)
                    nodes[c.name].conns[d] = cd+dd
                    nodes[d.name].conns[c] = cd+dd
                # print(c)
                c.conns.pop(n)
            if n.name != "AA":
                n.conns = dict()
                nodes.pop(n.name)
                foundZero = True
            # print(nodes["AA"])
            break

nodes = {n.name: n for n in nodes.values() if len(n.conns) != 0}
for n in nodes.values():
    n.conns = {n: d for n, d in n.conns.items() if len(n.conns) != 0}
printNodes("1")
exit()
for n in nodes.values():
    dists[n.name] = {}
    for n2 in nodes.values():
        # print(n.name, n2.name)
        if n2.name == "AA": continue
        if n == n2:
            dists[n.name][n2.name] = 0
        else:
            dists[n.name][n2.name] = getDistNodes(n, n2)

# for nn, ds in dists.items():
#     print(nn, ds)
# print(nodes["AA"])


# unopenedStart = list(nodes.keys())
# unopenedStart.remove("AA")
# # print(unopenedStart)
# print("searching path")
# nodes["AA"].check(30, 0, unopenedStart, [])
# print(ma)

# 6228 high
# 5077 high
#2663 high
