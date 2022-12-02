with open("i.txt") as f:
    data = [l.removesuffix("\n") for l in f]

n = 0
for l in data:
    if not l:
        continue
    a=0
    b = 0
    if l[0] == "A":
        a = 0
    elif l[0] == "B":
        a = 1
    elif l[0] == "C":
        a = 2
    if l[2] == "X":
        b = 0
    elif l[2] == "Y":
        b = 1
    elif l[2] == "Z":
        b = 2

    if b-a == 1 or b-a == -2:
        n += 6
    elif b-a == 0:
        n += 3
    n+= b+1

print( n )