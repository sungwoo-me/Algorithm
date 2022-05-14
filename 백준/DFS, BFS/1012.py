import sys
sys.setrecursionlimit(10**9)
dx = [1,-1,0,0]
dy = [0,0,1,-1]

def dfs(x,y) :

    for k in range(4):
        nx = x+dx[k] 
        ny = y+dy[k]
        if 0<=nx<N and 0<=ny<M and visited[nx][ny] and graph[nx][ny]==1 :
            visited[nx][ny]=False 
            dfs(nx,ny)       

    return 

T = int(input())
for _ in range(T):
    M,N,K = map(int,input().split())
    graph = [[0]*M for _ in range(N)]
    visited = [[True]*M for _ in range(N)]

    for i in range(K) :
        x,y = map(int,input().split())
        graph[y][x] = 1 
    

    count = 0
    for i in range(N):
        for j in range(M):
            if graph[i][j] == 1 and visited[i][j]:

                dfs(i,j)

                count+=1 
    
    print(count)

