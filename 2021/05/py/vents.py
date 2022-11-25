import re
lines = []
with open("input.txt") as f:
    lines = list(l for l in f)

m = [[0]*1000]*1000
for l in lines:
    cs = list(int(n) for n in re.split(r"( *\, *)|( *-> *)", l))
    print(cs)
