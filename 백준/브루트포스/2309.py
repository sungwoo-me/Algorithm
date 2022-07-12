import sys
input = sys.stdin.readline
nums = [int(input().strip()) for i in range(9)]


for i in range(len(nums)) :
    for j in range(i+1,len(nums)) :
        if nums[i] + nums[j] == sum(nums) - 100 :# 직접 입력
            a = nums[i]
            b = nums[j]
            nums.remove(a)
            nums.remove(b)
            break
nums.sort()
for i in nums :
    print(i)
