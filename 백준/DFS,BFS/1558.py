from collections import deque 


def bfs(x,y,goal):
    que = deque()
    que.append([x,y])
    visited[x][y] = False
    while(que):
        x,y = que.popleft()
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            if 0<=nx<N and 0<=ny<N and visited[nx][ny] and graph[nx][ny]>goal:
                que.append([nx,ny])
                visited[nx][ny] = False


dx = [0,0,1,-1]
dy = [1,-1,0,0]

N = int(input())
graph = [list(map(int,input().split())) for _ in range(N)]

max_num = 0 
for i in graph :
    max_num = max(max_num,max(i))

count_list = []

for g in range(max_num+1):
    visited = [[True]*N for _ in range(N)]
    count = 0 
    for i in range(N):
        for j in range(N):
            if visited[i][j] and graph[i][j]>g :
                count+=1
                bfs(i,j,g)
    count_list.append(count)


result =max(count_list)

print(result)