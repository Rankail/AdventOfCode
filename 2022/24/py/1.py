from collections import deque
from heapq import heappop, heappush
import time

w, h = 0, 0

blizzards: set[tuple[int, int]] = set()
states: list[list[list[int]]] = []

# generate next blizzard state
def updateBlizzards():
    global blizzards
    newBlizzards = set()
    for b in blizzards:
        if b[2] == 0:
            if b[0] != w-2:
                newBlizzards.add((b[0]+1, b[1], 0))
            else:
                newBlizzards.add((1, b[1], 0))
        elif b[2] == 1:
            if b[1] != h-2:
                newBlizzards.add((b[0], b[1]+1, 1))
            else:
                newBlizzards.add((b[0], 1, 1))
        elif b[2] == 2:
            if b[0] != 1:
                newBlizzards.add((b[0]-1, b[1], 2))
            else:
                newBlizzards.add((w-2, b[1], 2))
        elif b[2] == 3:
            if b[1] != 1:
                newBlizzards.add((b[0], b[1]-1, 3))
            else:
                newBlizzards.add((b[0], h-2, 3))
    blizzards = newBlizzards
    m = [r[:] for r in mTemplate]
    for bx, by, _ in blizzards:
        m[by][bx] = 1
    return m

# search for shortets path from 1,0 to w-2, h-1. returns required time
def search():
    found: set[tuple[int, int, int]] = set()
    q: deque[tuple[int, int, int, int]] = deque() # time, t-dist, x, y
    q.append((0, 1, 0))
    while q:
        t, px, py = q.popleft()
        while t > len(states)-1:
            states.append(updateBlizzards())
            found = set()
        for dx, dy in [(1,0), (0,1), (-1,0), (0,-1), (0,0)]:
            if (t+1, px+dx, py+dy) in found: continue
            if (px,py)==(1,0) and dy == -1: continue
            if states[t][py+dy][px+dx] == 1: continue
            if (px+dx, py+dy) == (w-2, h-2):
                return t+2
            
            found.add((t+1, px+dx, py+dy))
            q.append((t+1, px+dx, py+dy)) #w-px-dx+h-py-dy,
    print("failed")
    return None

sTime = time.perf_counter()
data = open("i.txt").read().split("\n")        
h = len(data)
w = len(data[0])
for y, line in enumerate(data):
    for x, c in enumerate(line):
        if c == ">":
            blizzards.add((x, y, 0))
        elif c == "v":
            blizzards.add((x, y, 1))
        elif c == "<":
            blizzards.add((x, y, 2))
        elif c == "^":
            blizzards.add((x, y, 3))

# generate empty map template
mTemplate = [[0]*w for _ in range(h)]
for i in range(w):
    mTemplate[0][i] = 1
    mTemplate[h-1][i] = 1
for i in range(h):
    mTemplate[i][0] = 1
    mTemplate[i][w-1] = 1
mTemplate[0][1] = 0

result = search()
eTime = time.perf_counter()
print(f"result: {result}")
print(f"finished after {eTime-sTime}s")

#232