def func1(num):
    for i in range(2,num):
        if num%i==0:

            return False
    return True 


a = int(input())
b = int(input())

sum = 0
min = 10000
for i in range(a,b+1):
    if i==1 :
        pass
    elif i==2:
        sum+=2
        if min>i:
            min =i
    
    else:
        if func1(i):
            sum+=i
            if min>i:
                min =i

if sum == 0:
    print("-1")
else:
    print(sum)
    print(min)