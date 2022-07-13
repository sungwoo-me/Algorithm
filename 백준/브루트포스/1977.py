M = int(input())
N = int(input())

nums = []
for i in range(0,N+1):
    if M<=i*i<=N :
        nums.append(i*i)


if nums :
    print(sum(nums))
    print(min(nums)) 

else :
    print(-1)