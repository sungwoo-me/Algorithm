
def func1(num):
    
    nums = [True]*num
    for i in range(2,int((num**0.5))+1):
        if nums[i]==True:
            for j in range(i+i,num,i):
                nums[j]=False
    return [i for i in range(2,num) if nums[i] == True]


num=1

while True:
    num = int(input())
    if num ==0:
        break
    sosu1 = func1(num+1)
    sosu2 = func1(num*2+1)

    print(len(sosu2)-len(sosu1))



