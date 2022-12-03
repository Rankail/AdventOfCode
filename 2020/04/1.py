import re
data = [l for l in open("i.txt").read().split("\n\n")]

k = ("byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid")
c = 0
for d in data:
    m = re.findall(r"(\S{3}):([#\da-z]*)", d)
    print(m)
    n = [a[0] for a in m]
    
    if not all(j in n for j in k):
        continue
    for j in n:
        if j == "byr" and :
            
print(c)
    
