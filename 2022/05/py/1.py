import re
data = open("i.txt").read().split("\n")[10:]
stacks = ["RPCDBG", "HVG", "NSQDJPM", "PSLGDCNM", "JBNCPFLS", "QBDZVGTS", "BZMHFTQ", "CMDBF", "FCQG"]

# data = open("i2.txt").read().split("\n")[5:]
# stacks = ["ZN", "MCD", "P"]

stacks = [list(s) for s in stacks]

for l in data:
    m = re.search(r"move (\d*) from (\d*) to (\d*)", l)
    for i in range(int(m.group(1))):
        stacks[int(m.group(3))-1].extend(stacks[int(m.group(2))-1][-1:])
        stacks[int(m.group(2))-1] = stacks[int(m.group(2))-1][:-1]

print("".join(list(s[-1] for s in stacks)))
