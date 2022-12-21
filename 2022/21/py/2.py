from __future__ import annotations
import re
import time

# multiple usages of variables directly or indirectly depending on 'humn' could lead to an expression
# with two unknown operands which can not be resolved as easily
# 
# circular expressions are not detected and could lead to an infinite loop

class Monkey:
    name: str = None
    value: int = None
    left: Monkey = None
    right: Monkey = None
    operator: str = None

    def __init__(self, name: str):
        self.name = name

    # traverse tree and resolve all calculations that are possible
    def calc(self):
        if self.name == "humn": return None
        if self.value != None:
            return self.value

        a = self.left.calc()
        b = self.right.calc()

        assert a is not None or b is not None, "Error: Found expression with two unknwon operands"
        if a is None or b is None: return None

        if self.operator == "+":
            self.value = a + b
        elif self.operator == "-":
            self.value = a - b
        elif self.operator == "*":
            self.value = a * b
        elif self.operator == "/":
            self.value = a / b

        return self.value

    # given a target result calculates the missing input of incomplete expressions. Exits after reaching the human-node
    def decalc(self, v: int):
        if self.name == "humn":
            endTime = time.perf_counter()
            print("result: ",v)
            print(f"finished after {endTime - startTime}s")
            exit()

        r = 0
        if self.right.value == None:
            if self.operator == "+":
                r = v - self.left.value   # a+b=c -> b=c-a
            elif self.operator == "-":
                r = self.left.value - v   # a-b=c -> b=a-c
            elif self.operator == "*":
                r = v / self.left.value   # a*b=c -> b=c/a
            elif self.operator == "/":
                r = self.left.value / v   # a/b=c -> b=a/c
            self.right.decalc(r)

        elif self.left.value == None:
            if self.operator == "+":
                r = v - self.right.value  # a+b=c -> a=c-b
            elif self.operator == "-":
                r = v + self.right.value  # a-b=c -> a=b+c
            elif self.operator == "*":
                r = v / self.right.value  # a*b=c -> a=c/b
            elif self.operator == "/":
                r = v * self.right.value  # a/b=c -> a=b*c
            self.left.decalc(r)

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
            mk.operator = m[2]
            mk.right = m[3]
        
        if mk.name == "root":
            root = mk
        if mk.name == "humn":
            mk.value = None

        monkeys[m[0]] = mk

    for m in monkeys.values():
        if m.left:
            m.left = monkeys[m.left]
        if m.right:
            m.right = monkeys[m.right]

    return root

startTime = time.perf_counter()

root = readInput()

a = root.left.calc()
b = root.right.calc()

if a == None:
    root.left.decalc(b)
else:
    root.right.decalc(a)