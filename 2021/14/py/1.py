from collections import Counter

data = open("i.txt").read().split("\n")

m: dict[str,str] = dict()
for l in data[2:]:
    pat, a = l.split(" -> ")
    m[pat] = a

counter = Counter()

pairs: dict[str, int] = {pat: 0 for pat in m.keys()}
for i, c in enumerate(data[0][:-1]):
    pairs[c+data[0][i+1]] += 1
    counter[c] += 1
counter[data[0][-1]] += 1

def step():
    global pairs
    newPairs = {pat: 0 for pat in m.keys()}
    for p, c in pairs.items():
        newPairs[p[0]+m[p]] += c
        newPairs[m[p]+p[1]] += c
        counter[m[p]] += c
    pairs = newPairs

for i in range(40):
    step()

print(max(counter.values()) - min(c for c in counter.values() if c > 0))