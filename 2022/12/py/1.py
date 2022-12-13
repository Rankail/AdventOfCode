from collections import deque

data = open("i.txt").read().split("\n")

board: list[list[int]] = []

start: tuple[int, int]

end: tuple[int, int]

for i, l in enumerate(data):
    board.append(list())
    for j, e in enumerate(l):
        if e == "S":
            start = (i,j)
            board[i].append(0)
        elif e == "E":
            end = (i, j)
            board[i].append(26)
        else:
            board[i].append(ord(e)-97)

def bfs():
    visited = {(start[0], start[1])}
    q: deque[tuple[int, int, int]] = deque()
    q.append((0, start[0], start[1]))
    while len(q) > 0:
        kost, cx, cy = q.popleft()
        for rx, ry in ((cx-1, cy), (cx+1, cy), (cx, cy-1), (cx, cy+1)):
            if not (0<=rx<len(board) and 0<=ry<len(board[0])): continue
            if (rx, ry) in visited: continue
            if board[rx][ry]-board[cx][cy]>1: continue
            if rx == end[0] and ry == end[1]:
                print(kost +1)
                exit(0)
            visited.add((rx, ry))
            q.append((kost+1, rx, ry))
                

bfs()
print("failed")