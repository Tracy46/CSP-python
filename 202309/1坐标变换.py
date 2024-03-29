n, m = map(int,input().strip().split())
action = [list(map(int, input().split())) for _ in range(n)]
position = [list(map(int, input().split())) for _ in range(m)]
# print(action)
# print(position)
for i in range(m):
    for j in range(n):
        position[i][0] += action[j][0]
        position[i][1] += action[j][1]
    print(position[i][0],position[i][1])