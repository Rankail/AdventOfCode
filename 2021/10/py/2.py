with open("i.txt") as f:
    lines = [l.removesuffix("\n") for l in f]

def hasError(line: str)-> bool:
    stack = []
    for c in line:
        if c=="(" or c=="{" or c=="[" or c=="<":
            stack.append(c)
        else:
            if c==")" and stack[-1]!="(":
                return True
            elif c=="]" and stack[-1]!="[":
                return True
            elif c=="}" and stack[-1]!="{":
                return True
            elif c==">" and stack[-1]!="<":
                return True
            stack.pop()
    return False

def getMissingScore(line: str) -> int:
    stack = []
    for c in line:
        if c in ("(", "{", "[", "<"):
            stack.append(c)
        elif c in (")","]","}",">"):
            stack.pop()
    n = 0
    points = ("(", "[", "{", "<")
    for c in reversed(stack):
        n *= 5
        n += points.index(c)+1
    return n
        

scores = [getMissingScore(l) for l in lines if not hasError(l)]
scores.sort()
print(scores[len(scores)//2])
