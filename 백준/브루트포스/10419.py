T = int(input())


nums = [int(input()) for _ in range(T)]

max_num = max(nums)

dp = [0] * (max_num+1)

for i in range(1,max_num+1):
    now = dp[i-1]
    if i-(now+1) >= (now+1)**2: 
        dp[i] = dp[i-1] +1
    else :
        dp[i] = now


for i in nums :
    print(dp[i])