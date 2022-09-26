n = int(input())
dp = [[0,0] for _ in range(n+1)]

nums=[0]
[nums.append(int(input())) for _ in range(n)]


if n ==1 :
    print(nums[1])
elif n==2 :
    print(nums[1]+nums[2])
else:
    dp[1]=[nums[1],1]
    dp[2]=[nums[1]+nums[2],2]




    for i in range(3,n+1):
        if dp[i-1][1]==2 :
            dp[i]=max([dp[i-3][0]+nums[i]+nums[i-1],2],[dp[i-2][0]+nums[i],1])

        else :
            dp[i]=max([dp[i-1][0]+nums[i],2],[dp[i-2][0]+nums[i],1])

    print(dp[i][0])