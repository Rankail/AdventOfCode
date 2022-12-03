with open("i.txt") as f:
    data = [l.removesuffix("\n") for l in f]

c = []
s = 0
for l in data:
    if l == "":
        c.append(s)
        s = 0
    else:
        s += int(l)
    print(l, s, "\n")

c.sort(reverse=True)

print(c[0]+c[1]+c[2])