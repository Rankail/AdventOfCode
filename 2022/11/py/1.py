import re

data = open("i.txt").read().split("\n")

class Monkey:
    num: int = None
    items: list[int] = None
    op: str = None
    incN: str = None
    test = None
    trueMonk = None
    falsMonk = None
    count = 0

    def __repr__(self) -> str:
        return f"{self.num}: {self.items} {self.op} {self.incN}; {self.test}->{self.trueMonk} {self.falsMonk}"

ms: list[Monkey] = []

for i in range((len(data)+1)//7):
    m = Monkey()
    d = data[i*7:(i+1)*7]
    m.num = int(d[0][7:-1])
    m.items = [int(n) for n in d[1][18:].split(", ")]
    r = re.match(r"  Operation: new = old (.) (.*)", d[2])
    m.op = r.group(1)
    m.incN = r.group(2)
    m.test = int(d[3][20:])
    m.trueMonk = int(d[4][29:])
    m.falsMonk = int(d[5][30:])
    ms.append(m)

cDiv = 1
for m in ms:
    cDiv *= m.test
print(cDiv)

for i in range(10000):
    print(i)
    for m in ms:
        #print("------------------")
        for j, s in enumerate(m.items):
            if m.op == "+":
                if m.incN == "old":
                    m.items[j] += s
                else:
                    m.items[j] += int(m.incN)
            else:
                if m.incN == "old":
                    m.items[j] *= s
                else:
                    m.items[j] *= int(m.incN)
            m.items[j] %= cDiv
            # print(s, m.op, m.incN, "=", m.items[j])
            m.count += 1
            if m.items[j] % m.test == 0:
                # print(m.items[j],"->",m.trueMonk)
                ms[m.trueMonk].items.append(m.items[j])
            else:
                # print(m.items[j],"->",m.falsMonk)
                ms[m.falsMonk].items.append(m.items[j])
        m.items.clear()



o = [m.count for m in ms]
o.sort(reverse=True)
print(o)
print(o[0]*o[1])