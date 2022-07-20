from collections import deque 

def bfs(x,y):
    que = deque()
    que.append([x,y,0])
    visited[x][y] = False
    while(que):
        x,y,count =que.popleft()
        count +=1 
        for i in range(4):
            nx = x+dx[i]
            ny = y +dy[i]
            if 0<=nx<N and 0<=ny<M and visited[nx][ny] and graph[nx][ny]== "L" :
                que.append([nx,ny,count])
                visited[nx][ny] = False

    return count

N,M = map(int,input().split())
dx = [1,-1,0,0]
dy = [0,0,1,-1]
max = 0 
graph=[list(input()) for _ in range(N)]

for i in range(N):
    for j in range(M):
        if graph[i][j] == "L":
            visited = [[True]*M for _ in range(N)]
            count_now = bfs(i,j)
            if max < count_now :
                max = count_now

print(max)