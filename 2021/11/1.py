board = []
with open("i.txt") as f:
    board = list(list(int(c) for c in l.removesuffix("\n")) for l in f)
print(board)

flashes = 0

def emitEnergy(x: int, y: int) -> bool:
    board[x][y] = -1
    for i in range(max(0, x-1), min(x+2, len(board))):
        for j in range(max(0, y-1), min(y+2, len(board))):
            if board[i][j]<0: continue
            board[i][j] += 1

def oneRound():
    global board, flashes
    board = [[n+1 for n in r] for r in board]
    
    emitted = True
    while emitted:
        emitted = False
        for i in range(len(board)):
            for j in range(len(board[i])):
                if board[i][j]>9:
                    emitted=True
                    flashes += 1
                    emitEnergy(i, j)
    board = [[0 if n==-1 else n for n in r] for r in board]

for i in range(100):
    oneRound()
print(board)
print(flashes)
    
