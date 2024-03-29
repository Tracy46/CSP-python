import math
def guiyhua(x, average, fangcha) -> float:
    x = (x - average) / math.sqrt(fangcha)
    return x


n = int(input())
nums = list(map(int, input().split()))
#print(n, nums)
nums_average = sum(nums) / len(nums)
nums_fangcha = 0
for i in range(n):
    nums_fangcha += ((nums[i] - nums_average) ** 2)
nums_fangcha = nums_fangcha / n
for i in range(n):
    nums[i] = guiyhua(nums[i],nums_average,nums_fangcha)
    print(nums[i])
