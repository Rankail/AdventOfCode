import sys

sys.setrecursionlimit(10000) # :)

data = open("i.txt").read().split("\n")

drops = set()
air = dict()
c = 0 # sides

for d in data:
    drops.add(tuple(int(n) for n in d.split(",")))

# get air neigbors of drops and count all sidess connected to those
for x, y, z in drops:
    for ox, oy, oz in [(-1,0,0),(1,0,0),(0,-1,0),(0,1,0),(0,0,-1),(0,0,1)]:
        p = (x+ox,y+oy,z+oz)
        if p not in drops:
            air[p] = 0
            c += 1

print(c)

# 2006