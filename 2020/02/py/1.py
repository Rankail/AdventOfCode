import re

data = [l for l in open("i.txt").read().split("\n")]

v = 0
for d in data:
    m = re.search(r"(\d+)-(\d+) (\S): (.*)", d)
    c = m.group(4).count(m.group(3))
    if int(m.group(1)) <= c <= int(m.group(2)):
        v+=1

print(v)