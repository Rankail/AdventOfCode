data = open("i.txt").read().split("\n")

line = 0

def reduce(a: str):
    red = True
    while red:
        if len(a) >200:
            break
        red = False
        depth = 0
        token = ""
        for i, c in enumerate(a):
            if c == "[":
                depth += 1
                if depth == 5:
                    #explode
                    j = a.find("]", i)
                    s = a[i+1:j].split(",")
                    for k in range(j+1, len(a)):
                        if a[k].isdigit():
                            l = k
                            while a[l+1].isdigit(): l+=1
                            a = f"{a[:k]}{int(a[k:l+1])+int(s[1])}{a[l+1:]}"
                            break
                    a = a[:i]+"0"+a[j+1:]
                    for k in range(i-1, 0, -1):
                        if a[k].isdigit():
                            l = k
                            while a[k-1].isdigit(): k-=1
                            a = f"{a[:k]}{int(a[k:l+1])+int(s[0])}{a[l+1:]}"
                            break
                    red = True
                    break
            elif c == "]":
                depth-=1

        if red: continue
        token = ""
        for i, c in enumerate(a):
            if c == "]" or c == ",":
                if token:
                    if int(token)>9:
                        #split
                        n = int(token)
                        a = f"{a[:i-2]}[{n//2},{(n+1)//2}]{a[i:]}"
                        red = True
                        token = ""
                        break
                token = ""
            elif not c =="[":
                token += c

    return a

def add (a, b):
    return reduce(f"[{a},{b}]")  

def magnitude(a):
    if type(a) == list:
        return 3*magnitude(a[0])+2*magnitude(a[1])
    return a

a1 = data[0]
for l in data:
    a1 = add(a1, l)
    
print(magnitude(eval(a1)))
