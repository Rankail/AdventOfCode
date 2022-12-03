with open("i.txt") as f:
    lines = [l.removesuffix("\n") for l in f]

def getFirstError(line: str)-> str:
    stack = []
    for c in line:
        if c=="(" or c=="{" or c=="[" or c=="<":
            stack.append(c)
        else:
            if c==")" and stack[-1]!="(":
                return 3
            elif c=="]" and stack[-1]!="[":
                return 57
            elif c=="}" and stack[-1]!="{":
                return 1197
            elif c==">" and stack[-1]!="<":
                return 25137
            stack.pop()
    return 0

n = 0
for l in lines:
    n += getFirstError(l)

print(n)