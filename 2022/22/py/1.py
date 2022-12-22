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

# given a point and a direction pointing into a map end calculates the position if you wrap around.
# returns the current position if there is a wall
def wrapAround(board: list[list[int]], px: int, py: int, dx: int, dy: int):
    if dx == 1:
        for x in range(px):
            if board[py][x] != 2:
                if board[py][x] == 0: return (x, py)
                return (px, py)
    elif dx == -1:
        for x in range(len(board[py])-1, px, -1):
            if board[py][x] != 2:
                if board[py][x] == 0: return (x, py)
                return (px, py)
    elif dy == 1:
        for y in range(py):
            if board[y][px] != 2:
                if board[y][px] == 0: return (px, y)
                return (px, py)
    elif dy == -1:
        for y in range(len(board)-1, py, -1):
            if board[y][px] != 2:
                if board[y][px] == 0: return (px, y)
                return (px, py)

    raise IndexError("Failed to wrap")

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
            # next to map end -> wrap
            if nx < 0 or nx >= len(board[0]) or ny < 0 or ny >= len(board) or board[ny][nx] == 2:
                nx, ny = wrapAround(board, px, py, dx, dy)
                if nx == px and ny == py: break # found wall after wrap
            elif board[ny][nx]==1:
                break
            px, py = nx, ny

    print(px+1, py+1)
    print(1000*(py+1)+4*(px+1)+facing)

processWay()

# 164014