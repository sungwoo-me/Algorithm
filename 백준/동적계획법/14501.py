N = int(input())
time = [list(map(int,input().split())) for _ in range(N)]

print(time)
dp = [0]*N
for i in range(N):
    if i+time[i][0]<=N:
        dp[i] = time[i][1]
        for j in range(i):
            print(i,j,dp)
            if i>=j+time[j][0]:
                dp[i] = max(dp[i],dp[j]+time[i][1])
print(max(dp))
