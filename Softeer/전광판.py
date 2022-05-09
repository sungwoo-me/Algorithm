from collections import deque
T = int(input())
zero = [1,2,3,4,5,6]
one = [1,2]
two = [1,3,4,6,7]
three = [1,2,3,6,7]
four = [1,2,5,7]
five = [2,3,5,6,7]
six = [2,3,4,5,6,7]
seven = [1,2,5,6]
eight = [1,2,3,4,5,6,7]
nine = [1,2,3,5,6,7]

nums =[zero,one,two,three,four,five,six,seven,eight,nine]

for i in range(T) :
    que1 ,que2 = map(deque,list(input().split()))
    sum = 0
    while que1 or que2 :
        num1=[]
        num2=[]
        if que1 :
            num1 = [i for i in nums[int(que1.pop())]]
            
        if que2 :
            num2 =[i for i in nums[int(que2.pop())]]

        delnums = [i for i in num1 if i in num2]
        
        num1.extend(num2)

        result = list(set(num1))

        result = [i for i in result if i not in delnums]
        sum += len(result)

    print(sum)