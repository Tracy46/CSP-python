# def zhishu(num):
#     if num == 1:
#         return False
#     for i in range(2, int(num/2)):
#         if num%i == 0:
#             return False
#     return True
#
# #输入
# n = int(input())
# nums = [list(map(int, input().split())) for _ in range(n)]
# # print(nums)
# my_dict = {}
#
# #找出质数，若该质数是其因子，则除到不能除为止，之后再接着找
# for i in range(n):
#     for j in range(1, nums[i][0]+1):
#         value = 0
#         if zhishu(j) and nums[i][0]%j == 0:
#             while nums[i][0]%j == 0:
#                 nums[i][0] = nums[i][0]/j
#                 value += 1
#             my_dict[j] = value
#     filtered_dict = {key: value for key, value in my_dict.items() if value >= nums[i][1]}
#     print(sum(key ^ value for key, value in my_dict.items()))
# # 假设我们要筛选值为2的键值对
# #同时记录除的次数（设置一个字典？）

'''不用判断是否是素数，从2 开始，第一个因子，一定是素数因子'''
q = int(input())
inq = [[i for i in map(int, input().split())]for j in range(q)]

for i in range(q):
    zhengshu = inq[i][0]
    temp = []
    while zhengshu != 1:
        for j in range(2, zhengshu+1):
            if zhengshu % j == 0:
                temp.append(j)
                zhengshu = zhengshu//j
                break
    P = list(set(temp))
    X = list(set(temp))
    T = []
    Length = len(P)
    for m in range(Length):
        t = temp.count(X[m])
        if t< inq[i][1]:
            P.remove(X[m])
        elif t>=inq[i][1]:
            T.append(t)
        if P == [ ]:
            P.append(1)
            T.append(1)
    out = 1
    for l in range(len(T)):
        out *= P[l]**T[l]
    print(out)
