sx, sy, ex, ey = 253, -73, 280, -46
# sx, sy, ex, ey = 20, -10, 30, -5 # 112

vs = set()
for vx_ in range(0, ex+1):
    for vy_ in range(-abs(sy)-1, abs(sy)+1):
        vx = vx_
        vy = vy_
        px, py = 0, 0
        while px < ex and py > sy:
            px += vx
            py += vy
            if sx<=px<=ex and sy<=py<=ey:
                vs.add((vx_, vy_))
                break
            vx = max(0, vx-1)
            vy -= 1

print(len(vs))  
# 1334