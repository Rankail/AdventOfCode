data = open("i.txt").read().split("\n")

class Node:
    parent = None
    files: list
    dirs: list
    name: str = ""
    size: int = 0

    def __init__(self):
        self.parent = None
        self.files = []
        self.dirs = []
        self.size = 0

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
            n = Node()
            n.name = d[1]
            n.size = int(d[0])
            n.parent = curdir
            curdir.files.append(n)
        else:
            n = Node()
            n.name = d[1]
            n.parent = curdir
            curdir.dirs.append(n)


def traverse(n: Node) -> int:
    if n.size != 0:
        return n.size

    for c in n.files:
        n.size += c.size
    for d in n.dirs:
        n.size += traverse(d)
    return n.size

traverse(root)

m = []
need = root.size - 40000000

def travMax(n: Node):
    if n.size < need:
        return
    m.append(n.size)
    for d in n.dirs:
        travMax(d)

travMax(root)

m.sort()
print(root)

print(m[0])