N,M = map(int,input().split())

nums = list(map(int, input().split()))

result = []
for i in range(N):
    for j in range(i+1,N):
        for k in range(j+1,N):
            sum =nums[i]+nums[j]+nums[k] 
            if sum <= M:
                result.append(sum)

print(max(result))