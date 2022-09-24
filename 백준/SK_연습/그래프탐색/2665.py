from collections import deque 
import heapq

def bfs() :
    que = []
    heapq.heappush(que,[0,0,0])
    while que : 
        count,x,y = heapq.heappop(que)
        go = False
        result = []

        if x == N-1 and y == N-1 :
            return count

        for i in range(4):
            nx =x+dx[i]    
            ny =y+dy[i]
            temp = count +1
            if 0<=nx<N and 0<=ny<N and visited[nx][ny] :
                if graph[nx][ny] == 1 :
                    heapq.heappush(que,[count,nx,ny])
                    visited[nx][ny] = False
                else :
                    heapq.heappush(que,[temp,nx,ny])
                    visited[nx][ny] = False



N = int(input())

graph =[list(map(int,input())) for _ in range(N)]

visited =[[True]* N for _ in range(N)]


dx = [0,0,1,-1]
dy = [1,-1,0,0]

print(bfs())