def func(num):
    if num<100:
        return True
    else:
        str_nums=[int(i) for i in str(num)]
        str_nums2 = [str_nums[i]-str_nums[i-1] for i in range(len(str_nums)-1,0,-1)]
        str_nums2 = list(set(str_nums2))
        if len(str_nums2)==1:
            return True
        else :
            return False

num = int(input())

count = 0
for i in range(1,num+1):
    if func(i):
        count+=1

print(count)
