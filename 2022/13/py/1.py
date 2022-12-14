data = open("i.txt").read().split("\n\n")

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
    l1 = eval(p1)
    l2 = eval(p2)

    if compare(l1, l2) < 0:
        inds.append(i+1)

print(sum(inds))
# 5882