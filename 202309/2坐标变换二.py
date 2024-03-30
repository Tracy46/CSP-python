from math import cos,sin

n, m = map(int, input().strip().split())
ki = [1]*10010
xita = [0]*10010
for i in range(1, n+1):
    in_type = 0
    in_value = 0
    in_type, in_value = map(float, input().strip().split())
    if in_type == 1:
        ki[i] = ki[i-1] * in_value
        xita[i] = xita[i-1]
    else:
        ki[i] = ki[i-1]
        xita[i] = xita[i-1] + in_value
for j in range(m):
    l, r, x, y = map(float, input().strip().split())
    ki_pro = ki[int(r)] / ki[int(l-1)]
    Sita_pro = xita[int(r)] - xita[int(l-1)]
    print((x*cos(Sita_pro)-y*sin(Sita_pro))*ki_pro, (x*sin(Sita_pro)+y*cos(Sita_pro))*ki_pro)
