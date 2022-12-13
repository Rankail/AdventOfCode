from typing import Any
from functools import cmp_to_key
import re

data = [d for d in open("i.txt").read().split("\n") if d != ""]
        
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

ls = [parse(p[1:-1])[0] for p in data]
ls.append([[2]])
ls.append([[6]])
ls = sorted(ls, key=cmp_to_key(compare))

ls = [i+1 for i, l in enumerate(ls) if l == [[2]] or l == [[6]]]
print(ls[0]*ls[1])
