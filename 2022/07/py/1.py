from __future__ import annotations

data = open("i.txt").read().split("\n")

class Node:
    parent = None
    files: list[Node] = None
    dirs: list[Node] = None
    name: str = None
    size: int = None

    def __init__(self, parent: Node = None, name: str = "", size: int = 0):
        self.parent = parent
        self.name = name
        self.size = size
        self.dirs = []
        self.files = []

    def getSize(self):
        if self.size != 0:
            return self.size

        x = 0
        for f in self.files:
            x += f.size
        for d in self.dirs:
            x += d.getSize()
        self.size = x
        return self.size

    def __str__(self, level=0):
        ret = "\t"*level+repr(self)+"\n"
        for d in self.dirs:
            ret += d.__str__(level+1)
        for f in self.files:
            ret += f.__str__(level+1)
        return ret

    def __repr__(self):
        if not (len(self.dirs) == 0 and len(self.files) == 0):
            return f"  {self.name} {self.size}"
        return f"- {self.name} {self.size}"

root = Node(None, "/")
curDir = root

for l in data:
    if l.startswith("$"):
        if l == "$ cd /":
            curDir = root
        elif l == "$ cd ..":
            curDir = curDir.parent
        elif l.startswith("$ cd"):
            d = l[5:]
            curDir = next(f for f in curDir.dirs if f.name == d)
    else:
        d = l.split(" ")
        if d[0] != "dir":
            n = Node(curDir, d[1], int(d[0]))
            curDir.files.append(n)
        else:
            n = Node(curDir, d[1])
            curDir.dirs.append(n)

root.getSize()

m = []
def traverseMax100k(n: Node):
    for d in n.dirs:
        traverseMax100k(d)
    if n.size <= 100000:
        m.append(n)

traverseMax100k(root)
print(sum(n.size for n in m))