sx, sy, ex, ey = 253, -73, 280, -46
# sx, sy, ex, ey = 20, -10, 30, -5 # 45

my = 0
for vx_ in range(0, ex+1):
    for vy_ in range(-abs(sy)-1, abs(sy)+1):
        vx = vx_
        vy = vy_
        px, py = 0, 0
        my_ = 0
        while px < ex and py > sy:
            px += vx
            py += vy
            my_ = max(py, my_)
            if sx<=px<=ex and sy<=py<=ey:
                my = max(my, my_)
                break
            vx = max(0, vx-1)
            vy -= 1

print(my)

# 2628
