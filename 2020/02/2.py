import re

data = [l for l in open("i.txt").read().split("\n")]

v = 0
for d in data:
    m = re.search(r"(\d+)-(\d+) (\S): (.*)", d)
    if (m.group(4)[int(m.group(1))-1] == m.group(3)) != (m.group(4)[int(m.group(2))-1] == m.group(3)):
        v+=1

print(v)