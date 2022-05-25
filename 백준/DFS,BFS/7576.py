from collections import deque
import sys 

input = sys.stdin.readline


dx = [0,0,1,-1]
dy = [1,-1,0,0]

def bfs(count) :
    que = deque(tmt)
    while que :
        x, y,count = que.popleft()
        if graph[x][y] == 0 : 
            graph[x][y] = count
        else:
            if graph[x][y] > count :
                graph[x][y] = count

        count +=1 


        for i in range(4) :
            nx = x+dx[i]
            ny = y+dy[i]
            if 0<=nx<N and 0<=ny<M and visited[nx][ny] and (graph[nx][ny] == 0 or graph[nx][ny]>count) :
                visited[nx][ny]=False 
                que.append([nx,ny,count])


    return count


def result():
    max = 0
    for i in graph :
        for j in i :
            if j == 0 :
                print(-1)
                return
            elif max < j :
                max = j                        
    if max == 1 :
        print(0)
    else :
        print(max-1)

def tomato():
    for i in range(N):
        for j in range(M):
            if graph[i][j]==1 :
                tmt.append([i,j,1])


M , N = map(int,input().split())
graph = [list(map(int,input().split())) for _ in range(N)]
visited = [[True]*M for _ in range(N)]

tmt =[]
count = 0

tomato()
bfs(count)
result()