num =int(input())
num2 = 2
num3= int(num ** 0.5)
while num2<=num3  :
    if num%num2==0:
        num=int(num/num2)
        print(num2)
    else:
        num2+=1

if num >1 :
    print(num)