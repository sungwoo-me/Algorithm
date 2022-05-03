N = int(input())
sum = 0 
for i in range(1,N+1):
    sum +=i 
    if sum == N :
        print(i)
        break
    elif sum > N :
        print(i-1)
        break
