from collections import deque 

dx = [0,0,1,-1]
dy = [1,-1,0,0]

def bfs(x,y) :
    count = 0
    que = deque()
    que.append([x,y,count])
    visited[x][y] = False 
    while(que):

        x,y,count = que.popleft()
        count += 1 
        graph[x][y] = count
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<=nx< N and 0<=ny <M and visited[nx][ny] and graph[nx][ny]==1 :
                visited[nx][ny] = False
                que.append([nx,ny,count])

N,M = map(int,input().split())
count = 0 
graph = [list(map(int,list(input()))) for _ in range(N)]
visited = [ [True] *M  for _ in range(N)]

bfs(0,0)

print(graph[N-1][M-1])

