n, m = map(int, input().strip().split())
nums = [list(map(int, input().split())) for _ in range(m)]
flag = list(0 for _ in range(n+1))
flag[0] = 1
# print(flag)
# print(nums)
ans = 0
for i in range(m):
    if flag[nums[i][1]] != 1:
        ans += 1
    flag[nums[i][0]] = 1
print(ans)