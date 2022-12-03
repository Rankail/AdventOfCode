import sys
sys.setrecursionlimit(2000)

board = []
with open("i.txt") as f:
    board = list(list(int(n) for n in l if n!='\n') for l in f)

def getBasinSize(x, y):
    if board[x][y]==-1 or board[x][y]==9:
        return 0
    s = 1
    board[x][y] = -1
    if x>0:
        s += getBasinSize(x-1, y)
    if x<len(board)-1:
        s += getBasinSize(x+1, y)
    if y>0:
        s += getBasinSize(x, y-1)
    if y<len(board[x])-1:
        s += getBasinSize(x, y+1)
    return s

sizes = []
for i, row in enumerate(board):
    for j, e in enumerate(row):

        if (i>0 and board[i-1][j]<=e) or (i<len(board)-1 and board[i+1][j]<=e) or (j>0 and board[i][j-1]<=e) or (j<len(row)-1 and board[i][j+1]<=e):
            continue
        
        sizes.append(getBasinSize(i, j))

sizes.sort(reverse=True)
print(sizes[0]*sizes[1]*sizes[2])
