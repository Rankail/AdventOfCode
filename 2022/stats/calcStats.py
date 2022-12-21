import re

class Day:
    num: int = None
    time1: int = None
    time2: int = None
    rank1: int = None
    rank2: int = None
    fullCount1: int = None
    fullCount2: int = None
    topPer1: float = None
    topPer2: float = None

    def __init__(self, num: int):
        self.num = num


days: list[Day] = []


for stat, count in zip(open("stats.txt").read().split("\n")[2:-1:2], reversed(open("fullCount.txt").read().split("\n"))):
    m = re.match(r" +(\d+) +\|\| +([\d:]+|\-) +\| +(\d+|\-) +\| +([\d\.%]+|\-) +\|\| +([\d:]+|\-) +\| +(\d+|\-) +\| +([\d\.%]+|\-) +", stat)
    d = Day(int(m.group(1)))
    if m.group(2) == "-": continue
    d.time1 = sum(60**(2-i)*int(n) for i, n in enumerate(m.group(2).split(":")))
    d.rank1 = int(m.group(3))
    if m.group(5) != "-":
        d.time2 = sum(60**(2-i)*int(n) for i, n in enumerate(m.group(5).split(":")))
        d.rank2 = int(m.group(6))

    m = re.match(r" ?\d+ +(\d+) +(\d+).*", count)
    d.fullCount2 = int(m.group(1))
    d.fullCount1 = d.fullCount2+int(m.group(2))

    d.topPer1 = d.rank1/d.fullCount1
    if d.rank2:
        d.topPer2 = d.rank2/d.fullCount2

    days.append(d)

avg1 = sum(d.rank1 for d in days) // len(days)
timeSum1 = sum(d.time1 for d in days)
t1 = f"{timeSum1//3600:02}:{(timeSum1%3600)//60:02}:{timeSum1%60:02}"
per1 = sum(d.topPer1 for d in days) / len(days)

avg2 = sum(d.rank2 for d in days if d.rank2) // len(list(1 for d in days if d.rank2))
timeSum2 = sum(d.time2 for d in days if d.time2)
t2 = f"{timeSum2//3600:02}:{(timeSum2%3600)//60:02}:{timeSum2%60:02}"
per2 = sum(d.topPer2 for d in days if d.time2) / len(list(1 for d in days if d.rank2))

text = open("stats.txt").read().split("\n")

for i, line in enumerate(text[2:-1:2]):
    if i >= len(days): break
    d = days[i]
    line = f"{line[:28]}{d.topPer1:6.2%}{line[34:56]}{d.topPer2:6.2%} "
    text[2+i*2] = line


text = [l+"\n" for l in text]
text[52] = f" total || {t1} | {avg1:4} | {per1:6.2%} || {t2} | {avg2:4} | {per2:6.2%}"
open("stats.txt", "w").writelines(text)


