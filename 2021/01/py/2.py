with open("input.txt") as f:
    count = 0
    lastVs = [int(f.readline()) for i in range(3)]
    idx = 0
    for line in f:
        if int(line) > lastVs[idx]:
            count+=1
        lastVs[idx] = int(line)
        idx = (idx+1) % 3
print(count)
        