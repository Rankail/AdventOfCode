import re

text = open("stats.txt").read().splitlines()
data = text[2:-1:2]

s1, s2 = 0, 0
avg1 = []
avg2 = []

for l in data:
    m = re.match(r" +\d+ +\|\| +([\d:]+|\-) +\| +([\d]+|\-) +\|\| +([\d:]+|\-) +\| +([\d]+|\-) +", l)
    if m.group(1) == "-": continue
    s1 += sum(60**(2-i)*int(n) for i, n in enumerate(m.group(1).split(":")))
    avg1.append(int(m.group(2)))
    s2 += sum(60**(2-i)*int(n) for i, n in enumerate(m.group(3).split(":")))
    avg2.append(int(m.group(4)))

a1 = sum(avg1)//len(avg1)
a2 = sum(avg2)//len(avg2)
t1 = f"{s1//3600:02}:{(s1%3600)//60:02}:{s1%60:02}"
t2 = f"{s2//3600:02}:{(s2%3600)//60:02}:{s2%60:02}"

text = [l+"\n" for l in text]
text[52] = f" total || {t1} | {a1} || {t2} | {a2} "
open("stats.txt", "w").writelines(text)