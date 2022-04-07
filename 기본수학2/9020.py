from __future__ import barry_as_FLUFL


def func1(num):
    
    nums = [True]*num
    for i in range(2,int((num**0.5))+1):
        if nums[i]==True:
            for j in range(i+i,num,i):
                nums[j]=False
    return [i for i in range(2,num) if nums[i] == True]


num = int(input())

for i in range(num):
    test = int(input())
    list1= func1(test)
    idx = max([i for i in range(len(list1)) if list1[i]<=test/2])
    breakpoint=False
    for j in range(idx,-1,-1):
        for k in range(idx,len(list1)):
            if list1[j]+list1[k]==test:
                print(list1[j],list1[k])
                breakpoint=True
                break
        if breakpoint==True :
            break