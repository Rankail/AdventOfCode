import sys
sys.setrecursionlimit(2000)

board = []
with open("i.txt") as f:
    board = list(list(int(n) for n in l if n!='\n') for l in f)

risk = 0
for i, row in enumerate(board):
    for j, e in enumerate(row):

        if (i>0 and board[i-1][j]<=e) or (i<len(board)-1 and board[i+1][j]<=e) or (j>0 and board[i][j-1]<=e) or (j<len(row)-1 and board[i][j+1]<=e):
            continue
        
        risk += 1+e

print(risk)
