from collections import defaultdict, deque
from heapq import heappop, heappush
import math

board = [[int(n) for n in l] for l in open("i.txt").read().split("\n")]

w, h = len(board[0]), len(board)

ex, ey = 5*w-1, 5*h-1

def getRisk(x, y):
    return (board[x%w][y%h]+x//w+y//h-1)%9+1

def path():
    risks = defaultdict(lambda: math.inf)
    risks[(0,0)] = 0
    unvisited: list[tuple[int, int]] = set()
    for y in range(w*5):
        for x in range(h*5):
            unvisited.add((x, y))
    
    no: list[tuple[int, int, int]] = []
    heappush(no, (0,(0,0)))
    while (ex, ey) in unvisited:
        risk, cur = heappop(no)
        if not cur in unvisited: continue
        cx, cy = cur
        for rx, ry in (cx+1, cy), (cx-1, cy), (cx, cy+1), (cx, cy-1):
            if not (rx, ry) in unvisited: continue
            if rx == ex and ry == ey:
                print(risk+getRisk(rx, ry))
                exit(0)
            neigrisk = min(risks[(rx, ry)], risk+getRisk(rx, ry))
            risks[(rx,ry)] = neigrisk
            heappush(no, (neigrisk, (rx, ry)))
        unvisited.remove(cur)

path()
print("failed")

