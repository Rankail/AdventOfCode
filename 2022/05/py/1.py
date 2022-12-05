import re
data = open("i.txt").read()
stackInput, moveInput = data.split("\n\n")

c = len(stackInput.split("\n")[0])//4+1
stacks: list[str] = [""]*c

for s in reversed(stackInput.split("\n")[:-1]):
    i = 0
    print(s)
    for i in range(c):
        if s[i*4+1] != " ":
            stacks[i] += s[i*4+1]

for l in moveInput.split("\n"):
    m = re.search(r"move (\d*) from (\d*) to (\d*)", l)
    for i in range(int(m.group(1))):
        stacks[int(m.group(3))-1] += stacks[int(m.group(2))-1][-1:]
        stacks[int(m.group(2))-1] = stacks[int(m.group(2))-1][:-1]

print("".join(s[-1] for s in stacks))
