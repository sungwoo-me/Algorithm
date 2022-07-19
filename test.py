from collections import deque

def bfs(start):
    que = deque()
    que.append(start)
    visited[0] == False
    while(que) :
        x,y = que.popleft()
        if [x,y] == graph[-1] :
            return "happy"
        for i in range(len(graph)) :
            dx,dy = graph[i]
            nx = abs(x-dx)    
            ny = abs(y-dy)
            if nx + ny <=1000 and visited[i]:
                que.append([dx,dy])
                visited[i] = False

    return "sad"



T = int(input())
for i in range(T):
    dx = [1,-1,0,0]
    dy = [0,0,1,-1]
    N = int(input())
    graph=[]
    graph.append(list(map(int,input().split())))
    for i in range(N):
        graph.append(list(map(int,input().split())))
    graph.append(list(map(int,input().split())))
    
    visited = [True] * (N+2)
    print(bfs(graph[0]))
