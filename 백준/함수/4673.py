def func1(n):
    sum = n
    nums=list(str(n))
    for i in range(len(nums)):
        sum+=int(nums[i])
    return sum

self=[i for i in range(1,10001)]

remove_num=[]

for i in range(1,10001):
    a = func1(i)
    if a<=10000:
        remove_num.append(func1(i))

remove_num=list(set(remove_num))

for i in range(len(remove_num)):
    self.remove(remove_num[i])
    


[print(self[i]) for i in range(len(self))]