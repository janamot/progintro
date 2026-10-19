import math
v0 = 20
uhel = math.radians(45)
g = 9.81
dt = [0.1, 0.01, 0.001]
x_presny = 40.77
y_max_presny = 10.19
t_presny = 2.88

for i in range(len(dt)):
    x = 0
    y = 0
    t = 0
    vx = v0 * math.cos(uhel)
    vy = v0 * math.sin(uhel)
    y_max = 0
    while y >= 0:
        t += dt[i]
        x += vx * dt[i]
        y += vy * dt[i]
        vy = vy - g * dt[i]
        if y_max < y:
            y_max = y
    
    print("-" * 10, dt[i], "-" * 10)
    print("dolet:", round(x, 2))
    print("odchylka:", round(x-x_presny, 2))
    print("max výška:", round(y_max, 2))
    print("odchylka:", round(y_max-y_max_presny, 2))
    print("doba:", round(t, 2))
    print("odchylka:", round(t-t_presny, 2))
    print()


