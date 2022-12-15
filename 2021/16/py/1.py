data = open("i.txt").read()

# Testcases
# data = "8A004A801A8002F478" # 16
# data = "620080001611562C8802118E34" # 12
# data = "C0015000016115A2E0802F182340" # 23
# data = "A0016C880162017C3686B18A3D4780" # 31

def binToInt(b: str):
    n = 0
    for c in b:
        n *= 2
        if c == "1": n += 1
    return n

vsum = 0

def packet(s: str, cnt: int = -1):
    global vsum
    i = 0
    c = 0
    while i < len(s)-1 and (cnt == -1 or cnt > c):
        if len(s)-i < 11: return i
        version = s[i:i+3]
        vsum += binToInt(version)
        typeId = s[i+3:i+6]
        i += 6
        if typeId == "100":
            num = ""
            while s[i] == "1":
                i += 5
            i += 5
        elif s[i] == "0":
            i += 1
            num = s[i:i+15]
            i += 15
            i += packet(s[i:i+binToInt(num)])
        elif s[i] == "1":
            i += 1
            num = s[i:i+11]
            i += 11
            i += packet(s[i:], binToInt(num))
        
        c+=1
    return i

d = ""
for c in data:
    n = ord(c)-55 if ord(c)>=65 else int(c)
    p = ""
    while n > 0:
        p = str(n%2) + p
        n //= 2
    d +=  "0"*(4-len(p))+p

packet(d)
print(vsum)
# 875