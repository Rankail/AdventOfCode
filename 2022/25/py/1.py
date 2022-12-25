def snafuToInt(num: str):
    n = 0
    for c in num:
        n *= 5
        if c == "-":
            n -= 1
        elif c == "=":
            n -= 2
        else:
            n += int(c)
    return n

def intToSnafu(num: int):
    n = ""
    while num != 0:
        m = num%5
        if m == 4:
            n = "-"+n
        elif m == 3:
            n = "="+n
        else:
            n = str(m)+n
        num //= 5
        if m > 2:
            num += 1

    return n
            


sum1 = 0
data = open("i.txt").read().split("\n")
for y, line in enumerate(data):
    sum1 += snafuToInt(line)

print(intToSnafu(sum1))