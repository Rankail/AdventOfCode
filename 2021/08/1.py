with open("i.txt") as f:
    data = list(list(d.split() for d in l.split("|")) for l in f)
print(data[0])

count = 0

for ds, out in data:
    z = ["" for i in range(10)]
    z[1] = next(d for d in ds if len(d) == 2)
    ds.remove(z[1])
    z[4] = next(d for d in ds if len(d) == 4)
    ds.remove(z[4])
    z[7] = next(d for d in ds if len(d) == 3)
    ds.remove(z[7])
    z[8] = next(d for d in ds if len(d) == 7)
    ds.remove(z[8])
    # z[3] = next(d for d in ds if len(d) == 5 and len(set(z[1]).intersection(d)) == 2)
    # ds.remove(z[3])
    # z[0] = next(d for d in ds if len(d) == 6 and len(set(z[1]).intersection(d)) == 2)
    # ds.remove(z[0])
    # z[6] = next(d for d in ds if len(d) == 6 and len(set(z[1]).intersection(d)) == 1)
    # ds.remove(z[6])
    # z[9] = next(d for d in ds if len(d) == 6)
    # ds.remove(z[9])
    # z[5] = next(d for d in ds if len(set(z[9]).intersection(d)) == 5)
    # ds.remove(z[5])
    # z[2] = ds[0]

    z = ["".join(sorted(n)) for n in z]

    for o in out:
        if "".join(sorted(o)) in z:
            count += 1

print(count)
        