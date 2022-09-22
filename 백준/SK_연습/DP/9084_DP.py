import sys 
input = sys.stdin.readline

T = int(input())
for i in range(T):
    N = int(input())
    nums = list(map(int,input().split()))
    M = int(input())
    dp = [0 for i in range(M+1)]
    dp[0] = 1 
    for num in nums :
        for k in range(1,M+1):
            if k >= num :
                dp[k] = dp[k] + dp[k-num]
    
    print(dp[M])
