from __future__ import annotations

# node for double linked list
class Node:
    pre: Node = None
    nex: Node = None
    value: int = None

    def __init__(self, v: int):
        self.value = v

    # remove node from list
    def unlink(self):
        self.pre.nex = self.nex
        self.nex.pre = self.pre

    # unlink node, traverse by value of node and insert
    def move(self):
        if self.value % (len(nums)-1) == 0: return
        self.unlink()
        if self.value > 0:
            cur = self
            for _ in range(self.value):
                cur = cur.nex
            self.pre = cur
            self.nex = cur.nex
            self.pre.nex = self
            self.nex.pre = self
        elif self.value < 0:
            cur = self
            for _ in range(-self.value):
                cur = cur.pre
            self.nex = cur
            self.pre = cur.pre
            self.nex.pre = self
            self.pre.nex = self            

nodes: list[Node] = []
zero: Node = None

nums = [int(n) for n in open("i.txt").read().split("\n")]
for n in nums:
    nodes.append(Node(n))
    if n == 0:
        zero = nodes[-1]

# connect nodes
for p, n in zip(nodes, nodes[1:] + [nodes[0]]):
    p.nex = n
    n.pre = p

# 'mix' nodes
for n in nodes:
    n.move()

# traverse from zero
res = 0
cur = zero
for _ in range(3):
    for _ in range(1000 % len(nums)):
        cur = cur.nex
    res += cur.value
print("result:", res)


# wrong solutions:
# -16658
# 4936
# -12409
# -8561
# 16569
# 2967
# 14626
# 3721
# 9626

#correct 7153