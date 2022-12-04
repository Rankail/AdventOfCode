import re
data = open("i.txt").read().split("\n")

n = 0
for l in data:
    m = re.search(r"(\d*)-(\d*),(\d*)-(\d*)", l)
    a, b, c, d = m.groups()
    if len(set(range(int(a),int(b)+1)).intersection(range(int(c),int(d)+1)))!=0:
        n+=1
print(n)