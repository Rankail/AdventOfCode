data = open("i.txt").read().split("\n")

reg = 1
clock = 0
res = 0

screen=["."]*240

def draw():
    if reg-1<=clock%40<=reg+1:
        print(reg, clock%40)
        screen[clock] = "#"

for l in data:
    draw()
    if clock > 240:
        break
    if l == "noop":
        clock += 1
    if l.startswith("addx"):
        clock+=1
        draw()
        clock+=1
        reg += int(l[5:])

for i in range(6):
    print("".join(screen[i*40:(i+1)*40]))