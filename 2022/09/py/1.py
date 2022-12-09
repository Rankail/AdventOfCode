data = open("i.txt").read().split("\n")

visited: list[list[int]] = [[0,0]]
ts = []
for i in range(2):
    ts.append([0,0][:])

def getNext(h, t):
    if abs(h[0]-t[0])<=1 and abs(h[1]-t[1])<=1:
        return t
    if not h[0] == t[0]:
        t[0] += -1 if h[0] < t[0] else 1
    if not h[1] == t[1]:
        t[1] += -1 if h[1] < t[1] else 1
    return t


for l in data:
    for c in range(int(l[2:])):
        if l[0] == "L":
            ts[0][0] -= 1
        elif l[0] == "R":
            ts[0][0] += 1
        elif l[0] == "D":
            ts[0][1] -= 1
        elif l[0] == "U":
            ts[0][1] += 1

        for i in range(1,len(ts)):
            ts[i] = getNext(ts[i-1],ts[i])

        if not (ts[-1] in visited):
            visited.append(ts[-1][:])

print(len(visited))
    