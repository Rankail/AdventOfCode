with open("i.txt") as f:
    pairs = [s.removesuffix("\n").split("-") for s in f]
m: dict[str, set[str]] = {}
for a,b in pairs:
    if a!="end" and b!="start":
        if not a in m:
            m[a] = set()
            m[a].add(b)
        else:
            m[a].add(b)
    if b!="end" and a!="start":
        if not b in m:
            m[b] = set()
            m[b].add(a)
        else:
            m[b].add(a)

def findPaths(paths: list[list[str]], path: list[str], repeat: bool) -> list[list[str]]:
    if path[-1]=="end": return path
    for node in m[path[-1]]:
        if node.isupper() or (not node in path or repeat):
            if node == "end":
                paths.append(path + [node])
                continue
            findPaths(paths, path + [node], repeat and (node.isupper() or not node in path))

allPaths = []
findPaths(allPaths, ["start"], True)
for p in allPaths:
    print(p)
print(len(allPaths))

