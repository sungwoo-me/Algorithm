from collections import deque 


def bfs(start):
    que = deque()
    que.append([start,0])
    visited[start] =False
    while(que) :
        now,count = que.popleft()

        if now == 100 :
            return count
        count+=1
        for i in range(1,7):
            few = graph[now]+i
            if  0<few<=100 and visited[few] :
                que.append([few,count])
                visited[few]=False

N, M = map(int,input().split())
graph = [i for i in range(101)]
visited= [True]*101
for i in range(N+M):
    a,b = map(int,input().split())
    graph[a]=b

print(bfs(1))

