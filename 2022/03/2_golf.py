print([sum(ord(c)-38 if ord(c)<97 else ord(c)-96 for c in[set(d).intersection(f[i+1]).intersection(f[i+2]).pop()for i,d in range(0,len(f),3)])for f in [open("i.txt").read().split("\n")]][0])