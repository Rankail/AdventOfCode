import re, math

data = open("i.txt").read().split("\n")

mi = math.inf
ma = 0
bs = []
sen = []
ds = []
for l in data:
    m = re.match(r"Sensor at x\=(-?\d+)\, y\=(-?\d+)\: closest beacon is at x\=(-?\d+)\, y\=(-?\d+)", l)
    bs.append((int(m.group(3)), int(m.group(4))))
    sen.append((int(m.group(1)), int(m.group(2))))
    ds.append(abs(int(m.group(3))-int(m.group(1)))+abs(int(m.group(2))-int(m.group(4))))
    ma = max(ma, int(m.group(3)))
    ma = max(ma, int(m.group(1)))
    mi = min(mi, int(m.group(3)))
    mi = min(mi, int(m.group(1)))

def getPossibles(row):
    blocked = set()
    for s, d in zip(sen, ds):
        dif = abs(row-s[1])
        if dif >= d: continue
        blocked.update(range(max(0, s[0]-(d-dif)), min(s[0]+(d-dif)+1, 4000000)))
    return blocked

m = 4000000
r = set(range(0, m))
for i in range(0, m):
    if (i%10000 == 0): print(i)
    p = getPossibles(i)
    diff = r.difference(p)
    if diff:
        diff = list(diff)
        print(diff, diff[0]*m+i)