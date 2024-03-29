n, m = map(int,input().strip().split())
Q = [list(map(int,input().split())) for _ in range(n)]
K = [list(map(int,input().split())) for _ in range(n)]
V = [list(map(int,input().split())) for _ in range(n)]
W = list(input().strip().split())
#先计算Q X K
temp = list()
#num = 0
for i in range(n):
    for j in range(m):
        temp.append([i][j]*K[i][m-j-1])
WQK = [a * b for a, b in zip(W,temp)]
#list1 = list()
ans = list()
num = 0
for m in range(m):   #列
    ans = list()
    num = 0
    for n in range(n):  #行
        num += WQK[n]*V[n][m]
    ans.append(num)
    print(ans)


