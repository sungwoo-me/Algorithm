from collections import deque

queue = deque()



queue.append(1)
queue.append(2)
queue.append(3)
queue.append(4)
queue.append(5)

queue.popleft()

print(queue)

queue.reverse()

print(queue)

from collections import deque 
import sys 
input = sys.stdin.readline

def bfs(x,y) :
    que = deque()
    que.append([x,y,0,True])

    visited[x][y]= False

    while(que):
        x,y,count,visited2= que.popleft()
        if x== Ex-1 and y == Ey-1 :
            return count
        count +=1
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<= nx < N and  0 <= ny< M and visited[nx][ny]  :
                if graph[nx][ny] == 0 :
                    que.append([nx,ny,count,visited2])
                elif  graph[nx][ny]==1 and visited2 :
                    que.append([nx,ny,count,False])
                visited[nx][ny] == False 

                


    return -1

N, M = map(int,input().split())
Hx,Hy = map(int,input().split())
Ex,Ey = map(int,input().split())

dx = [1,-1,0,0]
dy = [0,0,1,-1]



graph = [list(map(int,input().split())) for i in range(N)]
visited = [[True]*M for _ in range(N)]

visited2= True



print(bfs(Hx-1,Hy-1))
