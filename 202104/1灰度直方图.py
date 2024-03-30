a, b, c = map(int, input().strip().split())
nums = [list(map(int, input().split())) for _ in range(a)]
# print(nums)
ans = [0 for _ in range(16)]
for i in range(a):
    for j in range(b):
        ans[nums[i][j]] += 1
for i in range(c):
    print(ans[i], end=' ')