import re

data = open("i.txt").read().split("\n")
data2 = (list(int(n) for n in re.split(r" -> |,", l)) for l in  data)

# convert input to poly-lines and get min/max x-/y-values to minimize board
lines = []
ma = 0
mi = 9999999
ya = 0
for l in data2:
    poly = []
    for i in range(0, len(l), 2):
        poly.append((l[i],l[i+1]))
        ma = max(ma, l[i])
        mi = min(mi, l[i])
        ya = max(ya, l[i+1])
    lines.append(poly)

lines = [[(p[0]-mi+1,p[1]) for p in l] for l in lines]

board = [[0]*(ma-mi+3) for i in range(ya+1)]

# draw lines on board
for l in lines:
    for i, p1 in enumerate(l[:-1]):
        p2 = l[i+1]
        if p1[0] == p2[0]:
            for i in range(min(p1[1], p2[1]), max(p1[1], p2[1])+1):
                board[i][p1[0]] = 1
        else:
            for i in range(min(p1[0], p2[0]), max(p1[0], p2[0])+1):
                board[p1[1]][i] = 1

# simulate sand until y of one gets greater than the y of the lowest line
fellOut = False
c = 0
while not fellOut:
    x = 500-mi+1
    y = 0
    c+= 1
    while True:
        if y+1>= len(board):
            fellOut = True
            break
        if board[y+1][x] == 0:
            y+=1
        elif board[y+1][x-1] == 0:
            x -= 1
            y+=1
        elif board[y+1][x+1] == 0:
            x += 1
            y += 1
        else:
            board[y][x] = 2
            break

def printArr(arr: list[list[int]]):
    print("\n".join("".join(" " if e == 0 else ("\u2588" if e == 1 else "\u2591") for e in l) for l in arr))

printArr(board)

print(c-1)
