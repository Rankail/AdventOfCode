import sys

sys.setrecursionlimit(10000) # :)

data = open("i.txt").read().split("\n")

drops = set()
air = dict()
c = 0 # sides

for d in data:
    drops.add(tuple(int(n) for n in d.split(",")))

# gets bounds of all droplets
mi = (min(x for x,_,_ in drops), min(y for _,y,_ in drops), min(z for _,_,z in drops))
ma = (max(x for x,_,_ in drops), max(y for _,y,_ in drops), max(z for _,_,z in drops))

# get air neigbors of drops and count all sidess connected to those
for x, y, z in drops:
    for ox, oy, oz in [(-1,0,0),(1,0,0),(0,-1,0),(0,1,0),(0,0,-1),(0,0,1)]:
        p = (x+ox,y+oy,z+oz)
        if p not in drops:
            air[p] = 0
            c += 1

# count how many droplets the air neigbors are connnected too
for x, y, z in air:
    for ox, oy, oz in [(-1,0,0),(1,0,0),(0,-1,0),(0,1,0),(0,0,-1),(0,0,1)]:
        p = (x+ox,y+oy,z+oz)
        if p in drops:
            air[(x,y,z)] += 1

# find connected air; returns false if it goes out of the drop-bounds before reaching a dead-end
connectedCur = set()
def findConnected(x:int, y:int, z:int):
    global connectedCur
    p = (x,y,z)
    connectedCur.add(p)
    if x<=mi[0] or y<=mi[1] or z<=mi[2] or x>=ma[0] or y>=ma[1] or z>=ma[2]:
        return False
    for ox, oy, oz in [(-1,0,0),(1,0,0),(0,-1,0),(0,1,0),(0,0,-1),(0,0,1)]:
        p = (x+ox,y+oy,z+oz)
        if p not in drops and p not in connectedCur:
            if not findConnected(x+ox,y+oy,z+oz):
                return False

    return True

# find all trapped air
oldConns = set()
for x, y, z in air:
    if (x,y,z) in oldConns:
        continue
    connectedCur = set()
    if findConnected(x, y, z):
        oldConns.update(connectedCur)

# subtract all sides of drops connected to trapped air
for p in oldConns:
    if p in air:
        c -= air[p]

print(c)

# 2006