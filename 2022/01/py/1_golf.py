print(max(sum(int(r) for r in p.split("\n")) for p in open("../i.txt").read().split("\n\n")))