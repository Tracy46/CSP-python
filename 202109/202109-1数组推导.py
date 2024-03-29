n = int(input())
nums = list(map(int, input().split()))
max, min = nums[0], nums[0]
for i in range(n-1):
    if nums[i+1] > nums[i]:
        max += nums[i+1]
        min += nums[i+1]
    else:
        max += nums[i+1]
        min += 0
print(max)
print(min)