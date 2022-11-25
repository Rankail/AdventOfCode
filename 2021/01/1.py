with open("input.txt") as f:
    count = 0
    lastV = int(f.readline())
    for line in f:
        if int(line) > lastV:
            count+=1
        lastV = int(line)
print(count)
        