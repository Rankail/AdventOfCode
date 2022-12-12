import math
import sys
import threading

sys.setrecursionlimit(100000)
threading.stack_size(10**8)

data = open("i.txt").read().split("\n")

board: list[list[int]] = []
costs: list[list[int]] = []

start = [0, 0]

end = [0, 0]

for i, l in enumerate(data):
    board.append(list())
    costs.append(list())
    for j, e in enumerate(l):
        if e == "S":
            start[0] = i
            start[1] = j
            board[i].append(0)
        elif e == "E":
            end[0] = i
            end[1] = j
            board[i].append(26)
        else:
            board[i].append(ord(e)-97)
        costs[i].append(math.inf)

def check(x, y, c, prevH):
    if not (0<=x<len(board) and 0<=y<len(board[x])): return
    h = board[x][y]
    if prevH+1 < h: return
    if costs[x][y] <= c or c > costs[end[0]][end[1]]: return
    costs[x][y] = c
    check(x-1, y, c+1, h)
    check(x+1, y, c+1, h)
    check(x, y-1, c+1, h)
    check(x, y+1, c+1, h)

check(start[0], start[1], 0, 0)

print("\n".join(["".join(["#" if e!=math.inf else "." for e in l]) for l in costs]))