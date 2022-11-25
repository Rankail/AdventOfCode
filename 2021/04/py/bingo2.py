lines: list[str] = []
with open("input.txt") as f:
    lines = [l for l in f]

drawn: list[int] = list(int(n) for n in lines[0].split(","))
print(len(drawn))

boards: list[list[list[int]]] = []
for i in range(len(lines) // 6):
    boards.append(list(list(drawn.index(int(n)) for n in lines[i*6+j+2].split()) for j in range(5)))

maxBoard: list[list[int]] = None
maxI: int = 4

for board in boards:
    minCols = [0, 0, 0, 0, 0]
    minD = len(drawn)+1
    for i, row in enumerate(board):
        minRow = 0
        for j, e in enumerate(row):
            minRow = max(minRow, e)
            minCols[j] = max(minCols[j], e)
        minD = min(minD, minRow)
    minD = min(minD, min(minCols))
    if minD > maxI:
        maxI = minD
        maxBoard = board

sum = 0
for row in maxBoard:
    for e in row:
        if (e > maxI):
            sum += drawn[e]

print(maxI, maxBoard)
print(sum * drawn[maxI])

