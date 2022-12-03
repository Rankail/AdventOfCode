data = open("i.txt").read().split("\n")

n = 0
for j in range(0, len(data), 3):
    i = set(data[j]).intersection(data[j+1])
    i2 = list(i.intersection(data[j+2]))[0]

    if ord(i2)< 97:
        n+= ord(i2)-65+27
    else:
        n+= ord(i2)-96

print(n)