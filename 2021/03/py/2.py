lines: list[str] = []
with open("input.txt") as f:
    lines = [l for l in f]

def getMostLeastCommonNumber(lines: list[str], most: bool) -> int:
    linesC = lines.copy()
    for i in range(len(linesC[0])):
        if ([l[i] for l in linesC].count("1") >= len(linesC)/2) == most:
            linesC = [l for l in linesC if l[i]=="1"]
        else: linesC = [l for l in linesC if l[i]=="0"]
        if len(linesC)==1: break
    return int(linesC[0],2)

ogr = getMostLeastCommonNumber(lines, True)
csr = getMostLeastCommonNumber(lines, False)

print(ogr*csr)
