from collections import deque
import re
import time

data = open("i.txt").read().split("\n")

class Blueprint:
    id: int = None
    oC: int = None
    cC: int = None
    obC: tuple[int, int] = None
    gC: tuple[int, int] = None

def solve(b: Blueprint, time):
    q = deque()
    q.append((1,0,0,0, 0,0,0,0, time))

    SEEN = set()

    best = 0

    while q:
        orR, clR, obR, geR, ore, cla, obs, geo, t = q.popleft()

        best = max(best, geo)
        if t == 0:
            continue

        # check if we can even get higher than the current best
        if geo + t*geR + t * (t-1) / 2 <= best:
            continue

        # state was visited before
        if (orR, clR, obR, geR, ore, cla, obs, geo) in SEEN:
            continue
        SEEN.add((orR, clR, obR, geR, ore, cla, obs, geo))

        if len(SEEN) % 1000000 == 0:
            print(t, best, len(SEEN))

        # check if we will ever need more of a robot than we already have (only one can be build per minute)
        q.append((orR, clR, obR, geR, ore+orR, cla+clR, obs+obR, geo+geR, t-1))
        if obs >= b.gC[1] and ore >= b.gC[0]:
            q.append((orR, clR, obR, geR+1, ore+orR-b.gC[0], cla+clR, obs+obR-b.gC[1], geo+geR, t-1))
        if cla >= b.obC[1] and ore >= b.obC[0] and obR < b.gC[1]:
            q.append((orR, clR, obR+1, geR, ore+orR-b.obC[0], cla+clR-b.obC[1], obs+obR, geo+geR, t-1))
        if ore >= b.cC and clR < b.obC[1]:
            q.append((orR, clR+1, obR, geR, ore+orR-b.cC, cla+clR, obs+obR, geo+geR, t-1))
        if ore >= b.oC and orR < max(b.cC, b.obC[0], b.gC[0]):
            q.append((orR+1, clR, obR, geR, ore+orR-b.oC, cla+clR, obs+obR, geo+geR, t-1))
    
    return best

startTime = time.perf_counter()
res = 1
for line in data[:3]:
    m = re.match(r"Blueprint (\d+): Each ore robot costs (\d+) ore\. Each clay robot costs (\d+) ore\. Each obsidian robot costs (\d+) ore and (\d+) clay\. Each geode robot costs (\d+) ore and (\d+) obsidian\.", line)
    
    b = Blueprint()
    b.id = int(m.group(1))
    b.oC = int(m.group(2))
    b.cC = int(m.group(3))
    b.obC = (int(m.group(4)), int(m.group(5)))
    b.gC = (int(m.group(6)), int(m.group(7)))

    r = solve(b, 32)
    res *= r
    print("result:", r)

print("final:", res)
dt = time.perf_counter() - startTime
m = dt // 60
s = dt % 60
if m != 0:
    print(f"finished after {m}min {s}s")
else:
    print(f"finished after {s}s")