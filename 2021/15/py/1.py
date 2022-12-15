from collections import deque

board = [[int(n) for n in l] for l in open("i.txt").read().split("\n")]

w, h = len(board[0]), len(board)

ex, ey = len(board[0])-1, len(board)-1

def getRisk(x, y):
    return board[x][y]

def path():
    visited: list[tuple[int, int]] = list((0,0))
    no: list[tuple[int, int, int]] = list()
    no.append((0,0,0))
    while no:
        nx, ny, c = 0, 0, (len(board)**2)*10
        for n in no:
            if n[2] < c:
                nx, ny, c = n
        no.remove((nx, ny, c))
        for rx, ry in (nx+1, ny), (nx-1, ny), (nx, ny+1), (nx, ny-1):
            if not(0<=rx<=ex and 0<=ry<=ey): continue
            if (rx, ry) in visited: continue
            if rx == ex and ry == ey:
                print(c+getRisk(rx, ry))
                exit(0)
            no.append((rx, ry, c+getRisk(rx, ry)))
            visited.append((rx, ry))

path()
print("failed")



