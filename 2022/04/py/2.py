import re
data = open("i.txt").read().split("\n")

n = 0
for l in data:
    m = re.search(r"(\d*)-(\d*),(\d*)-(\d*)", l)
    a, b, c, d = [int(n) for n in m.groups()]
    if (a<=c and b>=d) or (a>=c and b<=d) or a<=c<=b or a<=d<=b or c<=a<=d or c<=b<=d:
        n+=1
print(n)