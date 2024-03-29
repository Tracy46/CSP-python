import math
n, m = map(float, input().strip().split())
nums = list(map(float, input().split()))
ans = 0
for i in range(int(n),-1,-1):
    ans += nums[i]/((1+m)**i)
print(ans)