x=0
y=0
with open("input.txt") as f:
    for l in f:
        if l[0]=="f":x+=int(l[-2])
        elif l[0]=="d":y+=int(l[-2])
        else:y-=int(l[-2])
print(x*y)