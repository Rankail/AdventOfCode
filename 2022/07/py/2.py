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

        for f in self.files:
            self.size += f.size
        for d in n.dirs:
            self.size += d.getSize()
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
            return f"> {self.name} {self.size}"
        return f"{self.name} {self.size}"

root = Node()
root.name = "/"
curdir = root

for l in data:
    if l.startswith("$"):
        if l == "$ cd /":
            curdir = root
        elif l == "$ cd ..":
            curdir = curdir.parent
        elif l.startswith("$ cd"):
            d = l[5:]
            curdir = next(f for f in curdir.dirs if f.name == d)
    else:
        d = l.split(" ")
        if d[0] != "dir":
            n = Node(curdir, d[1], int(d[0]))
            curdir.files.append(n)
        else:
            n = Node(curdir, d[1])
            curdir.dirs.append(n)

m = []
need = root.getSize() - 40000000

def travMax(n: Node):
    if n.size < need:
        return
    m.append(n.size)
    for d in n.dirs:
        travMax(d)

travMax(root)
m.sort()
print(m[0])