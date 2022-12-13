from typing import Any

data = open("i.txt").read().split("\n\n")
        
def parse(d: str) -> tuple[list[Any], int]:
    obj = []
    token = ""
    i = 0
    while i < len(d):
        e = d[i]
        if e == ",":
            if token:
                obj.append(int(token))
            token = ""
        elif e == "]":
            if token:
                obj.append(int(token))
            return (obj, i+1)
        elif e == "[":
            n, j = parse(d[i+1:])
            i += j
            obj.append(n)
        else:
            token += e
        i += 1
    if token:
        obj.append(int(token))
    return (obj, i)

def compare(l1, l2):
    for l, r in zip(l1, l2):
        if isinstance(l, list):
            if isinstance(r, list):
                c = compare(l, r)
                if c!=0:
                    return c
            else:
                c = compare(l, [r])
                if c!=0:
                    return c
        elif isinstance(r, list):
            c = compare([l], r)
            if not c==0:
                return c
        else:
            if l > r:
                return 1
            elif r > l:
                return -1
    return len(l1)-len(l2)

inds = []
for i, ps in enumerate(data):
    p1, p2 = ps.split("\n")
    l1 = parse(p1[1:-1])[0]
    l2 = parse(p2[1:-1])[0]

    if compare(l1, l2) < 0:
        inds.append(i+1)

print(sum(inds))