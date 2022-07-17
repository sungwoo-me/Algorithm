from collections import deque

def bfs(x,y,count,finish):    
    que = deque()
    que.append([x,y,count])
    if x == finish[0] and y == finish[1]:
        return 0

    while(que):
        x,y,count= que.popleft()
        count+=1
        
        for i in range(8):
            nx = x +dx[i]
            ny = y +dy[i]  

            if 0<=nx<l and 0<=ny<l and visited[nx][ny]:
                if nx == finish[0] and ny== finish[1]:
                    return count
                que.append([nx,ny,count])   
                visited[nx][ny] = False 


    return count


dx = [1,2,2,1,-1,-2,-2,-1]
dy = [-2,-1,1,2,2,1,-1,-2]


T = int(input())


for i in range(T):
    l = int(input())
    visited = [[True]*l for _ in range(l)]
    start = list(map(int,input().split()))
    finish = list(map(int,input().split()))
    count = 0
    print(bfs(start[0],start[1],count,finish))