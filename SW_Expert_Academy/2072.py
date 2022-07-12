N = int(input())

for j in range(N):
    sum = 0 
    nums=map(int, input().split())
    for i in nums :
        if i%2 != 0 :
            sum +=i 
    
    print("#"+str(j+1),sum)