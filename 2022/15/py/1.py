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


row = y=2000000
c = 0
blocked = set()
for s, d in zip(sen, ds):
    dif = abs(row-s[1])
    if dif > d: continue
    blocked.update(range(s[0]-(d-dif), s[0]+(d-dif)))
print(len(blocked))