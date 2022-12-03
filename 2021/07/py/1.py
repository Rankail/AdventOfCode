with open("i.txt") as f:
    data = [int(n) for n in f.read().split(",")]

m = max(data)*len(data)
for i in range(max(data)):
    m = min(m, sum(abs(i-x) for x in data))
print(m)


