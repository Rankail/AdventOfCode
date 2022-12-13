from functools import cmp_to_key

data = [d for d in open("i.txt").read().split("\n") if d != ""]

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

ls = [eval(p) for p in data]
ls.append([[2]])
ls.append([[6]])
ls = sorted(ls, key=cmp_to_key(compare))

ls = [i+1 for i, l in enumerate(ls) if l == [[2]] or l == [[6]]]

print(ls[0]*ls[1])
# 24948