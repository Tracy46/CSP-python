n, m = map(int, input().strip().split())
nums = list(map(int, input().split()))
c_list = list()
c0 = 1
# c_list.append(c0)
for i in range(n):
    c_list.append(c0)
    c0 = c0*nums[i]
c0 = 1
temp = 0
test = 0
ans = list()
for i in range(n):
    if i != n-1:
        test = temp
        temp = m % c_list[i+1]
        ans.append((temp - test)/c_list[i])
    else:
        temp = m % c_list[n-1]
        ans.append((m - temp)/c_list[n-1])
for item in ans:
    print(int(item), end=" ")  # 使用 end=" " 来避免在每个元素之间添加换行符
