N, M = map(int,input().split())

nums = list(map(int,input().split()))
sum = 0 

for i in range(N+1) :
    for j in nums :
        if i%j == 0 :
            sum += i 
            break

print(sum)

