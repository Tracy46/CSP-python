from math import cos, sin

n, m = map(int,input().strip().split())
action = [list(map(float, input().split())) for _ in range(n)]
position = [list(map(float, input().split())) for _ in range(m)]
# print(action)
# print(position)
for i in range(m):   #遍历输入的坐标
    for j in range(int(position[i][0]-1), int(position[i][1])):
        temp = 0
        if action[j][0] == 1:                            #1表示拉伸
            position[i][2] *= action[j][1]
            position[i][3] *= action[j][1]
        if action[j][1] == 2:
            temp = position[i][2]
            position[i][2] = position[i][2]*cos(action[j][1]) - position[i][3]*sin(action[j][1])
            position[i][3] = temp*sin(action[j][1]) + position[i][3]*cos(action[j][1])
    print(round(position[i][2],3),round(position[i][3],3))

