from itertools import permutations

def func1(num) :

    if num <= 1 :
        return False 
    if num<2:
        return True
    for i in range(2,num):
        if num%i==0:
            return False
    return True

def solution(numbers):
    result = []
    count =0
    for i in range(len(numbers)):
        result+=list(permutations(numbers,i+1))

    result = set(result)

    result2 =[]

    for i in result :
        nums = ""
        for j in i :
            nums+=j
        
        if func1(int(nums)):
            result2.append(int(nums))

    result2 = set(result2)

    return print(len(result2))


solution("011")