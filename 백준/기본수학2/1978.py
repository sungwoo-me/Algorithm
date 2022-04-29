
def func1(num) :
    if num == 1 :
        return False 
    if num<2:
        return True
    for i in range(2,num):
        if num%i==0:
            return False
    return True


num = int(input())

sum=0 

nums = list(map(int,input().split()))

for i in nums:
    if func1(i):
        sum+=1

print(sum)