data = [[int(d) for d in list(row)] for row in open("i.txt").read().split("\n")]
print(data)
w = len(data[0])
h = len(data)
m = 0

def checkDir(x, y, dx, dy):
    i = 1
    while 0<=x+i*dx<w and 0<=y+i*dy<h:
        if data[y+i*dy][x+i*dx]>=data[y][x]:
            return i
        i+=1
    return i-1

def checkNode(x, y):
    if (x == 0 or y == 0 or x == w-1 or y == h-1):
        return 0
    n = checkDir(x, y, -1, 0)
    n *= checkDir(x, y, 1, 0)
    n *= checkDir(x, y, 0, -1)
    n *= checkDir(x, y, 0, 1)
    return n

for i in range(len(data)):
    for j in range(len(data[i])):
        m = max(m, checkNode(j, i))
        
print(m)