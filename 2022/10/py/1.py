data = open("i.txt").read().split("\n")

reg = 1
clock = 1
res = 0

for l in data:
    if clock > 220:
        break
    if l.startswith("addx"):
        clock+=1
        if (clock-20)%40 == 0:
            res += clock*reg
        reg += int(l[5:])
    clock+=1
    if (clock-20)%40 == 0:
        res += clock*reg

print(res)