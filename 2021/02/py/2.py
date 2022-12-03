a=0
x=0
y=0
with open("input.txt") as f:
    for l in f:
        if l[0]=="f":
            x+=int(l[-2])
            y+=int(l[-2])*a
        elif l[0]=="d":a+=int(l[-2])
        else:a-=int(l[-2])
print(x*y)