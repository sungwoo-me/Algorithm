from collections import deque

n = int(input())

# dp =[]
# for i in range(n):
#     dp.append(list(map(int,input().split())))

# for i in range(1,n):
#     for j in range(len(dp[i])):
#         if j == 0 :
#             dp[i][j]=dp[i][j]+dp[i-1][j]
#         elif j == len(dp[i])-1 :
#             dp[i][j]=dp[i][j]+dp[i-1][j-1]
#         else :
#             dp[i][j] = max(dp[i-1][j-1],dp[i-1][j]) +dp[i][j]

# print(dp)
# print(max(dp[n-1]))

def bfs():
    max= 0
    que = deque()
    que.append([0,0,nums[0][0]])
    while que :        
        x,y,sum = que.popleft()
        if sum > max :
            max = sum
        for i in dxy: 
            nx = x+i[0]
            ny = y+i[1]
            if 0<=nx<n and 0<=ny<len(nums[nx])  :
                que.append([nx,ny,sum+nums[nx][ny]])

    print(max)

dxy = [[1,0],[1,1]]

nums=[]

for i in range(n):
    nums.append(list(map(int,input().split())))

bfs()

# print(nums)