import re

data = open("i.txt").read().split("\n")
row = 2000000
rngs = []
for l in data:
    m = list(int(n) for n in re.findall(r"-?\d+", l))
    sx, dif, d = m[0], abs(row-m[1]), abs(m[2]-m[0])+abs(m[3]-m[1])
    if dif < d:
        rngs.append((sx-d+dif, sx+d-dif))

print(max(r[1] for r in rngs)-min(r[0] for r in rngs))