nums = [int(input()) for _ in range(9)]

sum_nums = sum(nums)
br = False

for i in range(9):
    for j in range(9):
        if i == j :
            continue
        
        if sum_nums - nums[i] - nums[j] == 100 :
            a = nums[i]
            b = nums[j]
            nums.remove(a)
            nums.remove(b)
            br = True
            break
    if br :
        break



for i in nums :
    print(i)
