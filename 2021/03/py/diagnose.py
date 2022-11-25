cbits = [0,0,0,0,0,0,0,0,0,0,0,0]
with open("input.txt") as f:
    for l in f:
        for i in range(len(cbits)):
            cbits[i] += int(l[i])*2-1
g=0
for i in range(len(cbits)):
    g*=2
    if cbits[i] > 0:
        g+=1
print(g*(pow(2,len(cbits))-g-1))
