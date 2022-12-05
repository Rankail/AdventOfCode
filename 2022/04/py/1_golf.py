import re
print([(a<=c and b>=d) or (a>=c and b<=d)for a,b,c,d in ((int(a) for a in re.search(r"(\d*)-(\d*),(\d*)-(\d*)",l).groups()) for l in open("i.txt").read().split("\n"))].count(True))