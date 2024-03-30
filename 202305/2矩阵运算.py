# n, m = map(int,input().strip().split())
# Q = [list(map(int,input().split())) for _ in range(n)]
# K = [list(map(int,input().split())) for _ in range(n)]
# V = [list(map(int,input().split())) for _ in range(n)]
# W = list(input().strip().split())
# #先计算Q X K
# temp = list()
# #num = 0
# for i in range(n):
#     for j in range(m):
#         temp.append([i][j]*K[i][m-j-1])
# WQK = [a * b for a, b in zip(W,temp)]
# #list1 = list()
# ans = list()
# num = 0
# for m in range(m):   #列
#     ans = list()
#     num = 0
#     for n in range(n):  #行
#         num += WQK[n]*V[n][m]
#     ans.append(num)
#     print(ans)
#
n, d = map(int, input().split())
Q = [[i for i in map(int, input().split())] for j in range(n)]
K = [[i for i in map(int, input().split())] for j in range(n)]
V = [[i for i in map(int, input().split())] for j in range(n)]
W = [i for i in map(int, input().split())]
tmp = []
ans = []

# 计算 K的转置 * V = tmp
for i in range(d):
    tmp.append([])
    for j in range(d):
        tmp[i].append(0)
        for k in range(n):
            tmp[i][j] += K[k][i] * V[k][j]

# 计算 Q * tmp = ans
for i in range(n):
    ans.append([])
    for j in range(d):
        ans[i].append(0)
        for k in range(d):
            ans[i][j] += Q[i][k] * tmp[k][j]
        ans[i][j] *= W[i]

for i in range(n):
    a = []
    for j in range(d):
        a.append(ans[i][j])
    print(*a)   #可变参数解包运算符;将列表 a 中的元素解包并作为单独的参数传递给 print() 函数
