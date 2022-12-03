data = [l for l in open("i.txt").read().split("\n")]

def slope(dx):
    c = 0
    for i, r in enumerate(data):
        if r[(i*dx)%len(r)] == "#":
            c+=1
    return c

cs = 0
for i in range(0, len(data), 2):
    r = data[i]
    if r[(i//2)%len(r)] == "#":
        cs+=1
print(cs)
print(slope(1)*slope(3)*slope(5)*slope(7)*cs)
