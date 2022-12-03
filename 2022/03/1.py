import re

data = open("i.txt").read().split("\n")

n = 0
for d in data:
    s1 = d[:len(d)//2]
    s2 = d[len(d)//2:]
    i = list(set(s1).intersection(s2))[0]

    if ord(i) < 97:
        n+= ord(i)-65+27
    else:
        n+= ord(i)-96

print(n)