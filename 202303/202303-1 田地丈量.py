# n, x, y = map(int,input().strip().split())
# position = [list(map(int,input().split())) for _ in range(n)]
# # print(position)
# for i in range(n):
#     if position[i][0] >= x:
#         continue
#     elif position[i][1] >= y:
#         continue
#     elif position[i][2] <= 0:
#         continue
#     elif position[i][3] <= 0:
#         continue
#     else:
#
n, a, b = map(int, input().split())

location = [[i for i in map(int, input().split())]for j in range(n)]
sum = 0

for i in range(n):
    x = min(a, location[i][2]) - max(0, location[i][0])
    y = min(b, location[i][3]) - max(0, location[i][1])
    if x >= 0 and y >= 0:
        sum += x * y

print(sum)