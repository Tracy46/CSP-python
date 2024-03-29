n, m = map(int, input().strip().split())
nums = list(map(int, input().split()))
nums.insert(0, 0)
nums.append(m)
temp = 0
ans = 0
for i in range(1, n+2):
    ans = ans + temp*(nums[i]-nums[i-1])
    temp += 1
print(ans)