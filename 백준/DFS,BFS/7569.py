from collections import deque
import sys


def bfs():
    global max 
    que = deque(graph2)
    while(que):
        x,y,z,count = que.popleft()
        visited[z][y][x] = False
        graph[z][y][x] = 1
        count +=1
        for i in range(6):
            nx = x+ dx[i]
            ny = y + dy[i]
            nz = z + dz[i]
            if 0<=nx<M and 0<=ny<N and 0<=nz<H and graph[nz][ny][nx]== 0 and visited[nz][ny][nx] :
                que.append([nx,ny,nz,count])
                visited[nz][ny][nx] = False
                if max < count :
                    max = count


def check():
    for i in range(H):
        for j in range(N):
            for k in range(M):
               if graph[i][j][k] == 1:
                    graph2.append([k,j,i,0])          

def check2():
    for i in range(H):
        for j in range(N):
            for k in range(M):
               if graph[i][j][k] == 0:
                    return -1

input = sys.stdin.readline
M,N,H =map(int,input().split())
visited = [list([True]*M for _ in range(N)) for _ in range(H)]
graph = [list(list(map(int,input().split())) for _ in range(N)) for _ in range(H)]
graph2 = []
max = 0 
dx = [1,-1,0,0,0,0]
dy = [0, 0,1,-1,0,0]
dz = [0,0,0,0,1,-1]

check()
bfs()

if check2()== -1 :
    print(-1)
else :
    print(max)
