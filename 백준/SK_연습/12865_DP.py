N ,K = map(int,input().split())
graph = [[]]
for i in range(N):
    graph.append(list(map(int,input().split())))



dp = [[0 for _ in range(K+1)] for _ in range(N+1)]


for i in range(1,N+1) :
    for j in range(1,K+1) :
        w = graph[i][0]
        v = graph[i][1]
        if w<=j :
            dp[i][j]=max(dp[i-1][j],v+dp[i-1][j-w])
        else :
            dp[i][j]=dp[i-1][j]

print(graph)

for i in dp :
    print(i)

print(dp[N][K])