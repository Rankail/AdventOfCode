import re, sys, time

data = open("i.txt").read().split("\n")

def man(x1, y1, x2, y2):
    return abs(x2-x1)+abs(y2-y1)

sen = []
for l in data:
    m = list(int(n) for n in re.findall(r"-?\d+", l))
    sen.append((m[0], m[1], man(m[0], m[1], m[2], m[3])))


m = 4000000
barLen = 100
printStep = max(1, m//barLen)
startT = time.perf_counter_ns()
for i in range(m+1):
    if (i%printStep==0):
        p = i/m
        sys.stdout.write(f"\r[{'='*int(barLen*p)}{' '*(barLen-int((barLen*p)))}] {i/40000:02}%")
    rngs = []
    for sx, sy, d in sen:
        rd = abs(sy-i)
        if d >= rd:
            rngs.append((max(0, sx-(d-rd)), min(sx+(d-rd), m)))
    rngs.sort(key=lambda x: x[0])
    j = 0
    for r in rngs:
        if r[0] > j+1:
            sys.stdout.write(f"\rfound possible solution: ({j+1}, {i}) => {(j+1)*m+i}{' '*barLen}\n")
            found_solution = True
        j = max(j, r[1])

sys.stdout.write(f"\r[{'='*barLen}] 100.0% {' '*barLen}\n")
print(f"finished after {(time.perf_counter_ns()-startT)/1000000000}s")
if not found_solution: print("no solution was found")
# (3103499, 3391794) => 12413999391794