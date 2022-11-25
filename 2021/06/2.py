with open("input.txt") as f:
    data = [int(n) for n in f.read().split(",")]

timers = [0 for i in range(9)]
for d in data:
    timers[d] += 1

for _ in range(256):
    new = timers[0]
    timers[7] += timers[0]
    for j in range(8):
        timers[j] = timers[j+1]
    timers[8] = new
print(sum(timers))
        