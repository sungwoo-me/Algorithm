from collections import deque

def bfs(x,y,graph,visited):
    que = deque()
    que.append([x,y])
    visited[x][y] = False 
    while que :
        x,y = que.popleft()
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            if 0<=nx<N and 0<=ny<N and visited[nx][ny] and graph[nx][ny] == graph[x][y] :
                 visited[nx][ny] = False 
                 que.append([nx,ny])

dx = [1,-1,0,0]
dy = [0,0,1,-1]

N = int(input())

graph1 =[list(input()) for _ in range(N)]
visited1 = [[True]*N for _ in range(N)]

graph2 = [[] for _ in range(N)]
visited2 =[[True]*N for _ in range(N)]

for i in range(N):
    for j in range(N):
        if graph1[i][j] == "R" :
            graph2[i].append("G")
        else :
            graph2[i].append(graph1[i][j])

result1 = 0 
result2 = 0
for i in range(N):
    for j in range(N):
        if visited1[i][j] :
           result1 +=1 
           bfs(i,j,graph1,visited1)

        if visited2[i][j]:
            result2  +=1 
            bfs(i,j,graph2,visited2)

print(result1, result2) 



# R,B 가 하나 