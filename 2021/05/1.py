import re
lines = []
with open("input.txt") as f:
    lines = list(l for l in f)

size = 1000
m = [[0]*size for i in range(size)]

for l in lines:
    cs = list(int(n) for n in re.split(r",| -> ", l))
    if cs[1] == cs[3]:
        for i in range(min(cs[0], cs[2]), max(cs[0], cs[2])+1):
            m[i][cs[1]]+=1
    elif cs[0] == cs[2]:
        for i in range(min(cs[1], cs[3]), max(cs[1], cs[3])+1):
            m[cs[0]][i]+=1

count = 0
for r in m:
    for e in r:
        if e>=2:
            count+=1
print(count)