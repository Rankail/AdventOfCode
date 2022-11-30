def print2dArr(arr: list[list[bool]]):
    print('\n'.join([''.join(['{:1}'.format("#" if item else ".") for item in row]) for row in arr]))

board: list[list[bool]] = []
folds: list[tuple[bool, int]] = []
with open("i.txt") as f:
    points = []
    lines = [l for l in f]
    b = lines.index("\n")
    for l in lines[:b]:
        points.append(tuple(int(n) for n in l.removesuffix("\n").split(",")))
    for l in lines[b+1:]:
        folds.append((l[11]=="x", int(l[13:])))

maxX = max(p[0] for p in points)
maxY = max(p[1] for p in points)

for i in range(maxY+1):
    board.append([])
    for j in range(maxX+1):
        board[i].append(0)

for p in points:
    board[p[1]][p[0]] = True

# print(points)
# print(folds)

# print2dArr(board)
# print("********************")

for fold in folds:
    if not fold[0]:
        for i in range(len(board)):
            y = i if i < fold[1] else 2*fold[1]-i
            for j in range(len(board[0])):
                board[y][j] = board[y][j] or board[i][j]
        board = board[:fold[1]]
    else:
        for i in range(len(board)):
            for j in range(len(board[0])):
                x = j if j < fold[1] else 2*fold[1]-j
                board[i][x] = board[i][x] or board[i][j]
        board = [row[:fold[1]] for row in board]

print("********************")
print2dArr(board)
print(sum(r.count(True) for r in board))