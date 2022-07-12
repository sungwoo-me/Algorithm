import sys
sys.setrecursionlimit(10**9)
input = sys.stdin.readline

dx = [1, -1, 0, 0,1,1,-1,-1]
dy = [0, 0 ,1, -1,1,-1,1,-1]


def dfs(x,y):
    visited[x][y] = False
    
    for k in range(8):
        nx = x + dx[k]
        ny = y + dy[k]
        if 0<=nx<h and 0<=ny<w and visited[nx][ny]and graph[nx][ny] ==1 :
            dfs(nx,ny)

while(True):
    w,h = map(int,input().split())
    if w==0 and h ==0 :
        break
    graph=[list(map(int,input().split())) for i in range(h)]
    visited = [[True]*w for _ in range(h)]
    result = 0
    for i in range(h):
        for j in range(w):
            if graph[i][j] == 1 and visited[i][j]:
                result+=1  
                dfs(i,j)
    print(result)

