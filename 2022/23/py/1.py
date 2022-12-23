import time


blocks: set[tuple[int,int]] = set()

rounds = 0

def propose(bx, by):
    tests = [
        ((-1, -1), ( 0, -1), (+1, -1)),
        ((-1, +1), ( 0, +1), (+1, +1)),
        ((-1, -1), (-1,  0), (-1, +1)),
        ((+1, -1), (+1,  0), (+1, +1))
    ]
    results = [(bx, by-1), (bx, by+1), (bx-1, by), (bx+1, by)]

    foundOne = False
    for dx in range(-1, 2):
        for dy in range(-1, 2):
            if dx == 0 and dy == 0:
                continue
            if (bx+dx, by+dy) in blocks:
                foundOne = True
                break
        if foundOne: break

    if not foundOne:
        return None

    for i in range(4):
        for dx, dy in tests[(i+rounds) % 4]:
            if (bx+dx, by+dy) in blocks: break
        else:
            return results[(i+rounds) % 4]
    
    return None    

def step():
    global blocks, rounds
    con: dict = dict()
    proposed: set[tuple[int, int]] = set()
    doubles: set[tuple[int, int]] = set()

    for bx, by in blocks:
        p = propose(bx, by)
        if not p: continue
        con[(bx, by)] = p
        if p in proposed: doubles.add(p)
        else: proposed.add(p)

    moved = False
    newBlocks: set[tuple[int,int]] = set()
    for bx, by in blocks:
        if (bx, by) in con and con[(bx, by)] not in doubles:
            newBlocks.add(con[(bx, by)])
            moved = True
        else:
            newBlocks.add((bx, by))
    blocks = newBlocks
    rounds += 1
    return moved

def getEmptyInRect():
    count = 0
    xma = max(b[0] for b in blocks)
    xmi = min(b[0] for b in blocks)
    yma = max(b[1] for b in blocks)
    ymi = min(b[1] for b in blocks)
    for x in range(xmi, xma+1):
        for y in range(ymi, yma+1):
            if (x,y) not in blocks:
                count += 1
    return count

data = open("i.txt").read().split("\n")
for y, line in enumerate(data):
    for x, e in enumerate(line):
        if e == "#":
            blocks.add((x,y))

startTime = time.perf_counter()
for i in range(10):
    step()
result = getEmptyInRect()
endTime = time.perf_counter()
print(f"result: {result}")
print(f"finished after {endTime-startTime}s")