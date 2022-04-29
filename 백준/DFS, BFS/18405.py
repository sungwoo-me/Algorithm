from collections import deque 
import sys

N,K = map(int,sys.stdin.readline().split())
graph = []
data = []

dx = [-1,1,0,0]
dy = [0,0,-1,1]

for i in range(N):
    # 보드 정보를 한 줄 단위로 입력 
    graph.append(list(map(int,sys.stdin.readline().split())))
    for j in range(N):
        # 해당 위치 바이러스 존재 하는 경우 
        if graph[i][j] != 0 :
            # 바이러스 종류 시간 위치 x 위치 y 삽입 
            data.append((graph[i][j], 0 , i, j))


S,X,Y = map(int,sys.stdin.readline().split())

data.sort()



q= deque(data)

while q :
    v,s,x,y = q.popleft()
    if s == S:
        break
    for i in range(4):
        nx = x+dx[i]
        ny = y+dy[i]

        if 0<= nx and nx <N and 0 <=ny and ny <N :
            if graph[nx][ny] == 0 :
                graph[nx][ny] = v 
                q.append([v,s+1,nx,ny])

print(graph[X-1][Y-1])