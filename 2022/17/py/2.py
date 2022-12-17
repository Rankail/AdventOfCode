jets = open("i.txt").read()

def getPiece(t, y):
    if t == 0:
        return set([(2,y),(3,y),(4,y),(5,y)])
    elif t == 1:
        return set([(2,y+1),(3,y),(4,y+1),(3,y+1),(3,y+2)])
    elif t == 2:
        return set([(2,y),(3,y),(4,y),(4,y+1),(4,y+2)])
    elif t == 3:
        return set([(2,y),(2,y+1),(2,y+2),(2,y+3)])
    elif t == 4:
        return set([(2,y), (3,y), (2,y+1), (3,y+1)])
    return None

def moveLeft(p):
    if any(x==0 for x,_ in p): return p
    return set([(x-1,y) for x,y in p])

def moveRight(p):
    if any(x==6 for x,_ in p): return p
    return set([(x+1,y) for x,y in p])

def moveDown(p):
    return set([(x,y-1) for x,y in p])

board: set[tuple[int, int]] = set([(x,0) for x in range(7)])

def lastRows():
    maxY = max(y for _,y in board)
    return frozenset((x,maxY-y) for (x,y) in board if maxY-y < 40)

TARGET = 1000000000000
SEEN: dict[set[tuple[int,int]], tuple[int, int]] = {}
top = 0
ji = 0
ti = 0
added = 0
while ti<TARGET:
    piece = getPiece(ti%5, top+4)
    while True:
        # move x
        if jets[ji]=="<":
            p = moveLeft(piece)
            if not (p & board):
                piece = p
        elif jets[ji]==">":
            p = moveRight(piece)
            if not (p & board):
                piece = p

        ji = (ji+1)%len(jets)
        # move y
        p = moveDown(piece)
        if p & board:
            board.update(piece)
            top = max([y for _,y in board])

            # last 40 lines occured before in exact same situation?
            N = (ji, ti%5, lastRows())
            if N in SEEN:
                ot, oy = SEEN[N]
                dy = top-oy # y-distance to last occurence
                dt = ti-ot # piece-distance to last occurence
                amt = (TARGET-ti)//dt # times the sequence can be repeated before overshooting  the target
                added += amt*dy # additional lines found by sequence
                ti += amt*dt
            SEEN[N] = (ti, top)
            break
        piece = p

    ti += 1

print(top+added)