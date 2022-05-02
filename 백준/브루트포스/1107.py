target = int(input())
N = int(input())
if N != 0 :
    nums = list(input().split())

else:
    nums=[]

a =True
for i in range(0,500001):
    num1 = target +i 
    num2 = target -i 
    if num2<=0 :
        num2 = 0
    num1_true =True
    num2_true =True
    for j in str(num1):
        if j in nums:
            num1_true =False
            break
    for j in str(num2):
        if j in nums:
            num2_true =False
            break


    if num2_true:
        result =num2
        a =False
        break
    
    

    if num1_true :
        result =num1
        a =False
        break

   


if a == False :
    print(min(len(str(result))+abs(result-target),abs(100-target)))
else :
    print(abs(100-target))






