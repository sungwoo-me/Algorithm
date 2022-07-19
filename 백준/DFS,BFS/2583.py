from collections import deque 
def bfs(x,y,result) :
    que = deque()
    que.append([x,y])
    visited[x][y] = False
    while(que):
        x,y = que.popleft()
        result +=1 
        for i in range(4):
            nx = x+ dx[i]
            ny = y +dy[i]
            if 0<= nx <N and 0 <= ny < M and visited[nx][ny] and graph[nx][ny] :
                que.append([nx,ny])
                visited[nx][ny] = False
    
    return result

M,N,K = map(int,input().split())
graph = [[True]*M for _ in range(N)]
visited = [[True]*M for _ in range(N)]
dx  = [1,-1,0,0]
dy = [0,0,1,-1]

for i in range(K):
    x,y,fx,fy = map(int,input().split())
    for i in range(x,fx) : 
        for j in range(y,fy):
            graph[i][j] = False

count = 0
count1 = []
for i in range(N):
    for j in range(M):
        if visited[i][j] and graph[i][j]:
            count1.append(bfs(i,j,0))
            count +=1 

count1.sort()
print(count)
print(*count1)
