import re

def getInput(path: str):
    data = open(path).read().split("\n")
    way = data[-1]
    data = data[:-2]
    maxW = max(len(l) for l in data)
    board = []
    for l in data:
        row = []
        for c in list(l):
            if c == " ":
                row.append(2)
            elif c == "#":
                row.append(1)
            else:
                row.append(0)
        for _ in range(len(l), maxW):
            row.append(2)
        board.append(row)

    return (board, way)

# gets first empty spot in first row of board
def getStartPoint(board: list[list[int]]):
    for x in range(len(board[0])):
        if board[0][x] == 0:
            return (x, 0)

    raise IndexError("No possible starting spot")

def getDir(facing: int):
    return ((1,0), (0,1), (-1,0), (0,-1))[facing]

# given a position and a direction pointing into a map end calculates transforms the coordinates acoording the map of my input as a cube
# returns the current position if there is a wall
def transformCube(board: list[list[int]], x, y, dx, dy):
    # dx -1
    # x50 y<50 => y=149-(y-50) x=0 f0
    # x50 y>=50 => y=100 x=y-50 f1
    # x0 y<150 => y=49-(y-100) x=50 f0
    # x0 y>=150 => y=0 x=y-150+50 f1

    # dx 1
    # x149 => y=149-(y) x=99 f2
    # x99 y<100 => y=49 x=y-50+100 f3
    # x99 y>=100 => y=49-(y-100) f2
    # x49 => y=149 x=y-150+50 f3

    # dy -1
    # y100 => y=x+50 x=50 f0
    # y0 x<100 => y=x-50+150 x=0 f0
    # y0 x>=100 => y=199 x=x-100 f3

    # dy 1
    # y49 => y=x-100+50 x=99 f2
    # y149 => y=x-50+150 x=49 f2
    # y199 => y=0 x=x+100 f1

    f = -1
    nx, ny = x, y
    if dx == -1:
        if x == 50:
            if y < 50:
                nx = 0
                ny = 149-y
                f = 0
            elif y >= 50:
                nx = y-50
                ny = 100
                f = 1
        elif x == 0:
            if y < 150:
                nx = 50
                ny = 149-y
                f = 0
            elif y >= 150:
                nx = y-100
                ny = 0
                f = 1

    elif dx == 1:
        if x == 149:
            nx = 99
            ny = 149-y
            f = 2
        elif x == 99:
            if y < 100:
                nx = y+50
                ny = 49
                f = 3
            elif y >= 100:
                nx = 149
                ny = 149-y
                f = 2
        elif x == 49:
            nx = y-100
            ny = 149
            f = 3

    elif dy == -1:
        if y == 100:
            nx = 50
            ny = x+50
            f = 0
        elif y == 0:
            if x < 100:
                nx = 0
                ny = x+100
                f = 0
            elif x >= 100:
                nx = x-100
                ny = 199
                f = 3

    elif dy == 1:
        if y == 49:
            nx = 99
            ny = x-50
            f = 2
        elif y == 149:
            nx = 49
            ny = x+100
            f = 2
        elif y == 199:
            nx = x+100
            ny = 0
            f = 1

    if f == -1:
        raise IndexError(f"No matching case for: {x} {y} {dx} {dy}")

    if board[ny][nx] != 0:
        return (x,y, f)
    return (nx,ny, f)


def processWay():
    board, way = getInput("i.txt")
    px, py = getStartPoint(board)
    facing = 0
    m = re.findall(r"(\d+|R|L)", way)
    for op in m:
        if op == "R":
            facing = (facing+1) % 4
            continue
        elif op == "L":
            facing = (facing-1) % 4
            continue
        
        n = int(op)
        dx, dy = getDir(facing)
        for _ in range(n):
            nx, ny = px+dx, py+dy
            if nx < 0 or nx >= len(board[0]) or ny < 0 or ny >= len(board) or board[ny][nx] == 2:
                nx, ny, f = transformCube(board, px, py, dx, dy)
                if nx == px and ny == py: break
                facing = f
                dx, dy = getDir(facing)
            elif board[ny][nx]==1:
                break

            px, py = nx, ny

    print(px+1, py+1)
    print(1000*(py+1)+4*(px+1)+facing)

processWay()

# 69279 high
# 26236 low

# 47525

