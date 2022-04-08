n = list(input())


result = 0 

for i in n :
    i = int(i)
    if result == 0 :
        result = i 
    else :
        sum = result + i
        mul = result * i 
        result = max(sum,mul)

print(result)
