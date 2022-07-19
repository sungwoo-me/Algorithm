from collections import deque

def bfs(x,y):
    que = deque()
    que.append([x,y])
    visited[x][y] = False
    if graph[x][y] == 1 :
        return "NO"
    while(que):

        x,y = que.popleft()

        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            if nx == M-1 :
                return "YES"  

            if 0<=nx<M and 0<=ny<N and visited[nx][ny] and graph[nx][ny]== 0:
                que.append([nx,ny])
                visited[nx][ny] =False



    return "NO"


dx = [1,-1,0,0]
dy = [0,0,1,-1]

M, N  = map(int,input().split())

graph = [list(map(int,input())) for _ in range(M)]


result = False
visited = [[True]*N for _ in range(M)]  

for i in range(N):  
    if bfs(0,i) == "YES" :
        result = True
        break

if result :
    print("YES")
else : 
    print("NO")


