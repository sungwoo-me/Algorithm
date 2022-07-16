import math 
num = input()
now = num[0]
count =0 

for i in num :
    
    if i != now :
        count +=1 
        now = i

print(math.ceil(count/2))