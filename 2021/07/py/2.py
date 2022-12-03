import math
with open("i.txt") as f:
    data = [int(n) for n in f.read().split(",")]

m = math.inf
for i in range(max(data)+1):
    m = min(m, sum((abs(i-x)*(abs(i-x)+1)//2) for x in data))
print(m)