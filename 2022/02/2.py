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
        n += ((a-1+3)%3)+1
    elif l[2] == "Y":
        n += a+1+3
    elif l[2] == "Z":
        n += 6 + ((a+1)%3)+1

print( n )