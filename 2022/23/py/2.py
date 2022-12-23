import time


blocks: set[tuple[int,int]] = set()

rounds = 0

def propose(bx, by):
    elves = [False]*9
    for dx in range(-1, 2):
        for dy in range(-1, 2):
            if dx == 0 and dy == 0: continue
            elves[dx+1+dy*3+3] = (bx+dx, by+dy) in blocks

    # checks if there is any elf next to it
    if not any(elves):
        return None
    
    tests = (
        (0, 1, 2),
        (6, 7, 8),
        (0, 3, 6),
        (2, 5, 8)
    )
    results = [(bx, by-1), (bx, by+1), (bx-1, by), (bx+1, by)]

    # checks for empty sides starts with offset of rounds
    for i in range(4):
        for ei in tests[(i+rounds) % 4]:
            if elves[ei] : break
        else:
            return results[(i+rounds) % 4]
    
    return None

def step():
    global blocks, rounds
   
    con: dict = dict()
    proposed: set[tuple[int, int]] = set()
    doubles: set[tuple[int, int]] = set()

    # gets all proposed moves and doubles
    for bx, by in blocks:
        p = propose(bx, by)
        if not p: continue
        con[(bx, by)] = p
        if p in proposed: doubles.add(p)
        else: proposed.add(p)

    # creates new state
    moved = False
    newBlocks: set[tuple[int,int]] = set()
    for bx, by in proposed - doubles:
        if (bx, by) in con and con[(bx, by)] not in doubles:
            newBlocks.add(con[(bx, by)])
            moved = True
        else:
            newBlocks.add((bx, by))
    blocks = newBlocks
    rounds += 1
    return moved

# gets rect and counts empty positions
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
while step():
    pass
endTime = time.perf_counter()
print(f"result: {rounds}")
print(f"finished after {endTime-startTime}s")