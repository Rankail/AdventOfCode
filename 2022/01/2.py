with open("i.txt") as f:
    data = [l.removesuffix("\n") for l in f]

c = []
m = 0
s = 0
for l in data:
    if l == "":
        c.append(s)
        s = 0
    else:
        s += int(l)
        m = max(s, m)

c.sort(reverse=True)

print(c[0]+c[1]+c[2])