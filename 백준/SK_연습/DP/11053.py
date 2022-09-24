n = int(input())
nums = list(map(int,input().split()))

max= 0 
count = 0 
for i in nums :
    if max <i :
        count +=1 
        max=i
        print(i,count)

print(count)