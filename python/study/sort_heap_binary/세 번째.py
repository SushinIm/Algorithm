gaesu = int(input())
nums = []
data = []

for _ in range(gaesu):
    nums.append(int(input()))
    nums = sorted(nums)
    if len(nums) > 4:
        nums = nums[:4]

for _ in range(len(nums)):
    for __ in range(len(nums)):
        if _ != __:
            data.append(int(str(nums[_]) + str(nums[__])))

print(sorted(data)[2])