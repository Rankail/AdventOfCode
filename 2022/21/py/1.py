from __future__ import annotations
import re
import time

# circular expressions are not detected and could lead to an infinite loop

class Monkey:
    name: str = None
    value: int = None
    left: Monkey = None
    right: Monkey = None
    operand: str = None

    def __init__(self, name: str):
        self.name = name

    # traverse tree and resolve all calculations
    def calc(self):
        if self.value != None:
            return self.value

        a = self.left.calc()
        b = self.right.calc()

        if self.operand == "+":
            self.value = a + b
        elif self.operand == "-":
            self.value = a - b
        elif self.operand == "*":
            self.value = a * b
        elif self.operand == "/":
            self.value = a / b

        return self.value

# reads input and builds expression tree. returns root-node
def readInput():
    root: Monkey = None
    monkeys: dict[str, Monkey] = {}

    for line in open("i.txt").read().split("\n"):
        m = re.split(r"\:? ", line)

        if len(m) == 2:
            mk = Monkey(m[0])
            mk.value = int(m[1])
        else:
            mk = Monkey(m[0])
            mk.left = m[1]
            mk.operand = m[2]
            mk.right = m[3]

        if mk.name == "root":
            root = mk
        monkeys[m[0]] = mk

    for m in monkeys.values():
        if m.left and m.right:
            m.left = monkeys[m.left]
            m.right = monkeys[m.right]

    return root

startTime = time.perf_counter()

root = readInput()

result = root.calc()

endTime = time.perf_counter()

print("result: ", result)
print(f"finished after {endTime - startTime}s")

