with open("i.txt") as f:
    data = [l.removesuffix("\n") for l in f]

m = 0
s = 0
for l in data:
    if l == "":
        s = 0
    else:
        s += int(l)
        m = max(s, m)

print(m)