from  __future__ import annotations
from collections import defaultdict
import math
import re
import time

# Nodes of flowrate 0 can be ignored

AVAILABLE_TIME = 30

rates: dict[str, int] = {}
conns: dict[str, dict[str, int]] = {}
dists: dict[str, dict[str, int]] = {}

def readInput():
    connStrs: dict[str, list[str]] = {}
    data = open("i.txt").read().split("\n")
    for l in data:
        m = re.match(r"Valve (.*) has flow rate=(.*); tunnels? leads? to valves? (.*)", l)
        name, flowrate, others = m.group(1), int(m.group(2)), m.group(3).split(", ")
        connStrs[name] = others
        rates[name] = flowrate
    for n, ns in connStrs.items():
        conns[n] = defaultdict(lambda: math.inf)
        for c in ns:
            conns[n][c] = 1

# remove valves with flowrate 0 and connect their neigbors (sets distances too)
def reduceNodes():
    while True:
        for name, rate in rates.items():
            if rate != 0 or name == "AA": continue
            # connect neighbor-nodes with each other
            for cs, cd in conns[name].items():
                for ds, dd in conns[name].items():
                    if cs == ds: continue
                    conns[cs][ds] = min(conns[cs][ds], cd+dd)
                    conns[ds][cs] = min(conns[ds][cs], cd+dd)
            # remove 0-node
            for cs in conns[name]:
                conns[cs].pop(name)
            conns.pop(name)
            rates.pop(name)
            break
        else:
            break

# calculates all distances between all nodes with FWI
def calcDistances():
    for n in rates:
        dists[n] = defaultdict(lambda: math.inf)
        dists[n][n] = 0
    for n1, cs in conns.items():
        for n2, w in cs.items():
            dists[n1][n2] = w
    
    for k in rates:
        for i in rates:
            for j in rates:
                dists[i][j] = min(dists[i][j], dists[i][k] + dists[k][j])

# generates all paths through nodes within the timelimit
def allPaths(node: str, unvisited: set[str], opened: list[str], time_left: int):
    for n in unvisited:
        d = dists[node][n]+1
        if d < time_left:
            yield from allPaths(n, unvisited - {n}, opened+[n], time_left-d)
    yield opened

# calculates the released pressure of a path
def getPathReleased(path: list[str]):
    release = 0
    t = AVAILABLE_TIME
    cur = "AA"
    for n in path:
        d = dists[cur][n]+1
        t -= d
        release += t * rates[n]
        cur = n
    return release

# gets the maximal pressure released by the best path
def getMax():
    m = 0
    for o in allPaths("AA", set(rates.keys()), [], AVAILABLE_TIME):
        m = max(m, getPathReleased(o))
    return m

readInput()
startTime = time.perf_counter_ns()
reduceNodes()
t1 = time.perf_counter_ns()
print(f"reduced nodes in {(t1-startTime)/1000000000}s")
calcDistances()
t2 = time.perf_counter_ns()
print(f"calculated distances in {(t2-t1)/1000000000}s")
result = getMax()
endTime = time.perf_counter_ns()
print(f"found max path in {(endTime-t2)/1000000000}s")
print(f"finished after a total of {(endTime-startTime)/1000000000}s")
print(f"final result: {result}")

